#include <Python.h>
#include <unicap/unicap.h>

#define MAX_PROPERTIES 64

unsigned char *buf = NULL;
int nrOfPixel = 0;

unicap_handle_t 
getHandle (void)
{
  unicap_device_t imaging_source_dev;
  int dev_count = 0;
  unicap_enumerate_devices(NULL, &imaging_source_dev, dev_count);
  unicap_handle_t handle;
  if(!SUCCESS(unicap_open (&handle, &imaging_source_dev)))
    {
      fprintf(stderr, "could not open device");
      return NULL;
    }
  return handle;
}

static void	
new_frame_cb(unicap_event_t event, 
	     unicap_handle_t handle,
	     unicap_data_buffer_t *buffer, 
	     void *user_data) 
{
  volatile int * framecounter = (volatile int *)user_data;
  if(buf == NULL)
    {
      buf = malloc(nrOfPixel);
      unsigned char *unicapmem = buffer->data;
      memcpy(buf, unicapmem, nrOfPixel);
      *framecounter = *framecounter - 1;
    }
}

unicap_format_t
getformat(unicap_handle_t handle)
{
  unicap_format_t format;
  if (!SUCCESS(unicap_get_format(handle, &format))) 
    {
      fprintf(stderr, "cannot get format\n");
      return format;
    }
  return format;
}

void 
setformat(unicap_handle_t handle, unicap_format_t format)
{
  format.buffer_type = UNICAP_BUFFER_TYPE_SYSTEM;
  if (!SUCCESS(unicap_set_format(handle, &format))) 
    {
      fprintf(stderr, "cannot set format\n");
    }
}

void
setformat_fromstr(unicap_handle_t handle, const char *formatstr)
{
  unicap_format_t format;
  int i;
  for(i=0;SUCCESS(unicap_enumerate_formats(handle, NULL, &format, i)); i++)
    {
      if(strcmp(formatstr, format.identifier) == 0)
	{
	  break;
	}
    }
  setformat(handle, format);
}

void
getproperty(unicap_handle_t handle, unicap_property_t *prop, char *propid)
{
  int i;
  for(i = 0; SUCCESS(unicap_enumerate_properties(handle, NULL, prop,i)); i++)
    {
      unicap_property_t p = *prop;
      if(strcmp(propid, p.identifier) == 0)
	{
	  unicap_get_property(handle, prop);
	  break;
	}
    }
}

void 
setshutter(unicap_handle_t handle, double shutter)
{
  unicap_property_t exautoprop;
  getproperty(handle, &exautoprop, "Exposure, Auto");
  exautoprop.value = 1;
  unicap_set_property(handle, &exautoprop);
  unicap_property_t shutterprop;
  getproperty(handle, &shutterprop, "shutter");
  shutterprop.value = shutter;
  unicap_set_property_manual(handle, "shutter");
  unicap_set_property(handle, &shutterprop);
}

double
getduration(unicap_handle_t handle)
{
  unicap_property_t prop;
  getproperty(handle, &prop, "shutter");
  return prop.value;
}

int	
capture(unicap_handle_t handle) 
{
  unicap_format_t format = getformat(handle);
  volatile int framecounter = 1;

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

static PyObject *
unicap_getadjustments(PyObject *self, PyObject *args)
{
  unicap_handle_t handle = getHandle();
  unicap_format_t format = getformat(handle);
  const char * formatstr = format.identifier;
  char adjstr[1024];
  double duration = getduration(handle);
  snprintf(adjstr, 1024, "Format:%s;Shutter:%f",formatstr, duration );
  PyObject * pystr = PyUnicode_FromString(adjstr);
  return pystr;
}

static PyObject *
unicap_setformat(PyObject *self, PyObject *args)
{
  const char *formatstr;
  if(!PyArg_ParseTuple(args, "s", &formatstr))
    {
      return NULL;
    }
  setformat_fromstr(getHandle(),formatstr);
  return PyLong_FromLong(1);
}

static PyObject *
unicap_setshutter(PyObject *self, PyObject *args)
{
  unicap_handle_t handle = getHandle();
  double shutter;
  if(!PyArg_ParseTuple(args, "d", &shutter))
    {
      return NULL;
    }
  printf("arg was: %f\n", shutter);
  setshutter(handle, shutter);
  unicap_close(handle);
  return PyLong_FromLong(1);
}

static PyObject *
unicap_getshutter(PyObject *self, PyObject *args)
{
  unicap_handle_t handle = getHandle();
  double dur = getduration(handle);
  unicap_close(handle);
  return  PyFloat_FromDouble(dur);
}

static PyMethodDef UnicapMethods[] = {
  {"capture", unicap_capture, METH_VARARGS, "capture a image with defined gain and shutter. Return a list with intensity values"},
  {"getadjustments", unicap_getadjustments, METH_VARARGS, "get current adjuments(formats, duration) of the connected camera as a string" },
  {"setformat", unicap_setformat, METH_VARARGS, "sets the format (e.g RAW Bayer, YUV) of camera"},
  {"setshutter", unicap_setshutter, METH_VARARGS, "sets the exposure time of a single shot"},
  {"getshutter", unicap_getshutter, METH_VARARGS, "get the exposure time"},
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

