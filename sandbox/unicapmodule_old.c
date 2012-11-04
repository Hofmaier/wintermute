
//#include <string.h>
#include <Python.h>
#include <unicap/unicap.h>
#include <fitsio.h>
//#include <stdio.h>
//#include <stdlib.h>
//#include <unistd.h>
//#include <fcntl.h>

#define MAX_DEVICES 10
#define	MAX_PROPERTIES	64


#define	MAX_FORMATS	10
static unicap_format_t	formats[MAX_FORMATS];
static int	nformats = 0, nsizes = 0;
static int	selected_format = -1;

static unicap_device_t devices[MAX_DEVICES];
static int ndevices = 0;
static unicap_handle_t handle = NULL;
static int selected_device = -1;

static unicap_property_t properties[MAX_PROPERTIES];
static int nproperties = 0;

int opendevice(int i) {
  if ((i < 0) || (i > ndevices)) 
    {
      fprintf(stderr, "not a valid device: %d\n", i);
      return -1;
    }
  if (selected_device >= 0) 
    {
      unicap_close(handle);
      handle = NULL;
      selected_device = -1;
    }
  selected_device = i;
  if (!SUCCESS(unicap_open(&handle, &devices[selected_device]))) 
    {
      return -1;
    }
  
  fprintf(stderr, "%s:%d: device %s selected\n",
	  __FILE__, __LINE__,
	  devices[selected_device].identifier);

  return 0;
}

static unicap_property_t *
ui_get_pt(int i) 
{
  if ((i < 0) || (i >= nproperties)) 
    {
      fprintf(stderr, "not a valid property: %d\n", i);
      return NULL;
    }
  unicap_property_t * pt = &properties[i];
  unicap_get_property(handle, pt);
  return pt;
}

int	
ui_set_property_double(int i, double v) 
{
  int rc = -1, j;
  unicap_property_t * pt = ui_get_pt(i);
  if (NULL == pt) { return rc; }

  switch (pt->type) 
    {
    case UNICAP_PROPERTY_TYPE_RANGE:
      if ((v < pt->range.min) || (v > pt->range.max)) 
	{
	  goto out;
	}
      rc = 0;
      pt->value = v;
      break;
    case UNICAP_PROPERTY_TYPE_VALUE_LIST:
      for (j = 0; j < pt->value_list.value_count; j++) 
	{
	  if (pt->value_list.values[j] == v) 
	    {
	      pt->value = v;
	    rc = 0;
	    break;
	  }
      }
    break;
  }
out:
  if (!rc) {
    unicap_set_property(handle, pt);
  }
}

int	ui_set_property_int(int i, int j) {
	int	rc = -1;
	unicap_property_t	*pt = ui_get_pt(i);
	if (NULL == pt) { return rc; }

	switch (pt->type) 
	  {
	  case UNICAP_PROPERTY_TYPE_RANGE:
	  case UNICAP_PROPERTY_TYPE_VALUE_LIST:
	    return ui_set_property_double(i, j);
	    return ui_set_property_double(i, j);
	  case UNICAP_PROPERTY_TYPE_FLAGS:
	    if ((pt->flags_mask & j) == j) {
			pt->flags = j;
			rc = 0;
	    }
	    break;
	  case UNICAP_PROPERTY_TYPE_MENU:
	    if ((j < 0) || (j >= pt->menu.menu_item_count)) {
	      rc = -1;
	    }
	    strcpy(pt->menu_item, pt->menu.menu_items[j]);
	    break;
	  }
	if (!rc) 
	  {
	    unicap_set_property(handle, pt);
	  }
}

int
set_property(int i, const char *value) {
  unicap_property_t * pt = ui_get_pt(i);
  if (NULL == pt) { return -1; }

  double value_double = atof(value);
  int value_int = atof(value);
 
  switch (pt->type) 
    {
    case UNICAP_PROPERTY_TYPE_RANGE:
    case UNICAP_PROPERTY_TYPE_VALUE_LIST:
      return ui_set_property_double(i, value_double);
    case UNICAP_PROPERTY_TYPE_MENU:
		// XXX try value in menu list
    case UNICAP_PROPERTY_TYPE_FLAGS:
      return ui_set_property_int(i, value_int);
    case UNICAP_PROPERTY_TYPE_DATA:
      break;
    case UNICAP_PROPERTY_TYPE_UNKNOWN:
      break;
    }
  return -1;
}

void 
initproperties(void) {
  int i;
  unicap_status_t status = STATUS_SUCCESS;
  for (i = 0; SUCCESS(status) && (i < MAX_PROPERTIES); i++) 
    {
      status = unicap_enumerate_properties(handle, NULL,
					   &properties[i], i);
      if (SUCCESS(status)) 
	{
	  unicap_get_property(handle, &properties[i]);
	}
      else 
	{
	  break;
	}
    }
  nproperties = i;
}


void  
retrieve_formats() {
	unicap_status_t	status = STATUS_SUCCESS;
	int	i;

		fprintf(stderr, "%s:%d: listing formats\n", __FILE__, __LINE__);

	for (i = 0; SUCCESS(status) && (i < MAX_FORMATS); i++) {
		status = unicap_enumerate_formats(handle, NULL, &formats[i], i);
		if (SUCCESS(status)) {
			printf("%d: %s\n", i, formats[i].identifier);
		} else {
			break;
		}
	}
	nformats = i;
}


int 
ui_select_size(int i) {
  
  if (selected_format < 0) 
    {
      fprintf(stderr, "no format selected\n");
      return -1;
    }
  if ((i < 0) || (i >= formats[selected_format].size_count)) 
    {
      return -1;
    }
  formats[selected_format].size.width =
    formats[selected_format].sizes[i].width,
    formats[selected_format].size.height =
    formats[selected_format].sizes[i].height;
  if (!SUCCESS(unicap_set_format(handle, &formats[selected_format]))) 
    {
      fprintf(stderr, "cannot set format %s\n",
	      formats[selected_format].identifier);
      return -1;
    }

  fprintf(stderr, "%s:%d: selected %d x %d\n",
	  __FILE__, __LINE__,
	  formats[selected_format].size.width,
	  formats[selected_format].size.height);
  return 0;
}


void	
list_formats() {
	if (!handle) {
		fprintf(stderr, "no camera selected\n");
		return;
	}
	retrieve_formats();
	int	i;
	for (i = 0; i < nformats; i++) {
		printf("%d: %s\n", i, formats[i].identifier);
	}

		fprintf(stderr, "%s:%d: end of format list: %d found\n",
			__FILE__, __LINE__, nformats);

}

int	
getFormatIndex(const char *name) {
	int	i, l = strlen(name);
	for (i = 0; i < nformats; i++) {
		if (0 == strncmp(formats[i].identifier, name, l)) {
			return i;
		}
	}
	return -1;
}

int
select_format(int i) {
	if (!handle) {
		fprintf(stderr, "no camera selected\n");
		return;
	}
	if ((i < 0) || (i >= nformats)) {
		return -1;
	}
	selected_format = i;
	/* at this point we should always select size 0 */
	return ui_select_size(0);
}



void 
closedevice(void) 
{
  if (handle) 
    {
      unicap_close(handle);
    }
}

static void	
retrieve_devices(void) {
  unicap_status_t  status = STATUS_SUCCESS;
  int i;
  for (i = 0; SUCCESS(status) && (i < MAX_DEVICES); i++) {
    status = unicap_enumerate_devices(NULL, &devices[i], i);
    if (!SUCCESS(status)) break;
  }
  ndevices = i;
  if (i == 0) 
    {
      printf("no devices found");
    }
}

int 
getPropertyIndex(const char *name)
{
  int i, l;
  l = strlen(name);

  fprintf(stderr, "%s:%d: looking for property %s\n",
			__FILE__, __LINE__, name);

  for (i = 0; i < nproperties; i++) 
    {
         
    if (0 == strncmp(properties[i].identifier, name, l)) 
      {
	fprintf(stderr, "%s:%d: property %s has number %d\n", __FILE__, __LINE__, name, i);
	unicap_property_t prop = properties[i];
	printf("Property %s has value %f\n", prop.identifier, prop.value);
	return i;
      }
    }
  return -1;
}

void 
printallpropertyvalues()
{
  printf("nr of properties %d\n", nproperties);
  int i = 0;
  for( i = 0; i<nproperties; i++)
    {
      unicap_property_t prop = properties[i];
      const char *name = prop.identifier;
      double value = prop.value;
      printf("%s : %f\n", name, value);
      
    }
}


int
getDeviceIndex(const char *name) {
  int i;
  fprintf(stderr, "%s:%d: looking for device named %s\n",
	  __FILE__, __LINE__, name);
 
  for (i = 0; i < ndevices; i++) 
    {
      int l = strlen(name);
      fprintf(stderr, "%s:%d: \"%s\" ?= \"%s\"\n", __FILE__, __LINE__, devices[i].identifier, name);
    
    if (0 == strncmp(devices[i].identifier, name, l)) 
      {
	return i;
      }
  }
  return -1;
}


static const char	*filenameformat = "output%02d.fits";

unsigned char *buf = NULL;
int datasize = 0;
int nrOfPixel = 0;

static void	
new_frame_cb(unicap_event_t event, 
	     unicap_handle_t handle,
	     unicap_data_buffer_t *buffer, 
	     void *user_data) 
{

  volatile int * framecounter = (volatile int *)user_data;
  *framecounter = *framecounter - 1;
  printf("framecounter is now %d \n", *framecounter);
  datasize = buffer->buffer_size;
  printf("buffersize: %d \n", datasize);
  buf = malloc(nrOfPixel);
  unsigned char *unicapmem = buffer->data;
  memcpy(buf, unicapmem, nrOfPixel);
  printf("copied %d pixels\n", nrOfPixel);
}

int	
capture(int nimages) {
  printf("capture \n");
  unicap_format_t format;
  volatile int framecounter = nimages;

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

  printf("captured %d frames\n", nimages);
  unicap_stop_capture(handle);
  
  printf("ui_captureexit\n");
  return 0;
}

int main (int argc, char **argv)
{
  const char *deviceidentifier = "DBK 21AU618.AS";
  const char *gain = "260";
  const char *shutter = "0.03";
  const char *format = "RGB Bayer ( BA81 )";
  retrieve_devices();
  int deviceindex = getDeviceIndex(deviceidentifier);
  opendevice(deviceindex);
  initproperties();
  int gainpropertyindex = getPropertyIndex("Gain");
  set_property(gainpropertyindex, gain);
  int shutterpropertyindex = getPropertyIndex("shutter");
  set_property(shutterpropertyindex, shutter);
 
  list_formats();
  int rgbindex = getFormatIndex(format);
  select_format(rgbindex);
  printallpropertyvalues();  
  capture(1);
  closedevice();
  
  
  int index = 0;
  
  for(index = 0; index < datasize; index++)
    {
     
    }
  return 0;
}

static PyObject *
unicap_isAvailable(PyObject *self, PyObject *args)
{
  const char * deviceidentifier;
  PyArg_ParseTuple(args, "s", &deviceidentifier);
  printf("deviceidentifier %s\n", deviceidentifier);
  retrieve_devices();
  printf("retrieve devices \n");
  int deviceindex = getDeviceIndex(deviceidentifier);
  printf("deviceindex: %d \n", deviceindex);
  long retVal = 0;
  if(deviceindex != -1)
    {
      retVal = 1;
    }
  return PyBool_FromLong(retVal);
}

static PyObject *
unicap_capture(PyObject *self, PyObject *args)
{
  const char *deviceidentifier = "DBK 21AU618.AS";
  const char *gain = "260";
  const char *shutter = "0.03";
 
  //  PyArg_ParseTuple(args, "sss", &deviceidentifier, &gain, &shutter);
  printf("capture image with %s  %s gain and %s shutter\n", deviceidentifier, gain, shutter);
  retrieve_devices();
  int deviceindex = getDeviceIndex(deviceidentifier);
  opendevice(deviceindex);
  initproperties();
  int propertyindex = getPropertyIndex("Gain");
  set_property(propertyindex, gain);
  capture(1);
  closedevice();

  PyObject* imgarray = PyList_New(nrOfPixel);
  int i;
  for(i = 0; i < nrOfPixel; i++)
    {
      long l = buf[i];
      PyObject* intensity = PyLong_FromLong(l);
      PyList_SetItem(imgarray, i, intensity);
    }
  free(buf);
  return imgarray;
}

static PyMethodDef UnicapMethods[] = {
  {"isAvailable", unicap_isAvailable, METH_VARARGS, "Check if camera is connected"},
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

