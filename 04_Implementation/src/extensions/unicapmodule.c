#include <Python.h>
#include <unicap/unicap.h>

unsigned char *buf = NULL;
int nrOfPixel = 0;

unicap_handle_t 
getHandle (void)
{
  unicap_device_t imaging_source_dev;
  int dev_count = 0;
  unicap_enumerate_devices(NULL, &imaging_source_dev, dev_count);
  printf("Open %s\n", imaging_source_dev.identifier); 
  unicap_handle_t handle;
  unicap_open (&handle, &imaging_source_dev);
  return handle;
}

static void	
new_frame_cb(unicap_event_t event, 
	     unicap_handle_t handle,
	     unicap_data_buffer_t *buffer, 
	     void *user_data) 
{

  volatile int * framecounter = (volatile int *)user_data;
  *framecounter = *framecounter - 1;
  printf("framecounter is now %d \n", *framecounter);
  int datasize = buffer->buffer_size;
  printf("buffersize: %d malloc \n", datasize);
  
  buf = malloc(nrOfPixel);
  unsigned char *unicapmem = buffer->data;
  memcpy(buf, unicapmem, nrOfPixel);
  printf("copied %d pixels\n", nrOfPixel);
}

int	
capture(unicap_handle_t handle) {
  printf("capture \n");
  unicap_format_t format;
  volatile int framecounter = 1;

  if (!SUCCESS(unicap_get_format(handle, &format))) 
    {
      fprintf(stderr, "cannot get format\n");
      return -1;
    }

  printf("format is %s \n", format.identifier);
  format.buffer_type = UNICAP_BUFFER_TYPE_SYSTEM;

  if (!SUCCESS(unicap_set_format(handle, &format))) 
    {
      fprintf(stderr, "cannot set format\n");
      return -1;
    }

  int imagewidth;
  int imageheight;
  imagewidth = format.size.width;
  imageheight = format.size.height;
  nrOfPixel = imagewidth * imageheight;
  
  unicap_register_callback(handle, UNICAP_EVENT_NEW_FRAME,
		(unicap_callback_t)new_frame_cb, (void*)&framecounter);
  unicap_start_capture(handle);
  while (framecounter > 0) 
    {
      usleep(100000);
    }

  unicap_stop_capture(handle);
  
  printf("capture exit\n");
  return 0;
}

static PyObject *
unicap_capture(PyObject *self, PyObject *args)
{
  unicap_handle_t handle = getHandle();
  
  capture(handle);
  unicap_close(handle);

  PyObject* imgarray = PyList_New(nrOfPixel);
  int i;
  for(i = 0; i < nrOfPixel; i++)
    {
      long l = buf[i];
      PyObject* intensity = PyLong_FromLong(l);
      PyList_SetItem(imgarray, i, intensity);
    }
  free(buf);
  buf = NULL;
  return imgarray;
}

static PyMethodDef UnicapMethods[] = {
  {"capture", unicap_capture, METH_VARARGS, "capture a image with defined gain and shutter"},
  {NULL, NULL, 0, NULL}
};

static struct PyModuleDef unicapmodule = {
  PyModuleDef_HEAD_INIT,
  "unicap",
  NULL,
  -1,
  UnicapMethods
};

PyMODINIT_FUNC
PyInit_unicap(void)
{
  return PyModule_Create(&unicapmodule);
}

