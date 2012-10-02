#include <unicap.h>
#include <stdio.h>

#define MAX_FORMATS 64

unicap_handle_t open_imagingsource_camera ()
{
  unicap_device_t imaging_source_dev;
  int dev_count = 0;
  unicap_enumerate_devices(NULL, &imaging_source_dev, dev_count);
  printf("Open %s\n", imaging_source_dev.identifier);
  
  unicap_handle_t handle;
  unicap_open (&handle, &imaging_source_dev);
  return handle;
}

void print_formats(unicap_handle_t handle)
{
  unicap_format_t formats[MAX_FORMATS];
  int index = 0;
  int status = STATUS_SUCCESS;
  while(SUCCESS(status)){
    status =  unicap_enumerate_formats(handle, NULL, &formats[index], index);
    printf("%d: %s\n", index, formats[index].identifier);
    index++;
  }
  printf("End of Formatslist\n");
}

void print

int main (int argc, char **argv)
{
  unicap_handle_t handle;
  handle = open_imagingsource_camera();
  print_formats(handle);
  unicap_close (handle);
  return 0;
}
