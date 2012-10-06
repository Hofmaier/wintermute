#include <unicap.h>
#include <stdio.h>

#define MAX_FORMATS 64
#define NR_OF_PROPERTIES 9

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
    if(!SUCCESS(status)) break;
    unicap_format_t currentFormat = formats[index];
    printf("%d: %s Size: %d x %d\n", index, currentFormat.identifier, currentFormat.size.width, currentFormat.size.height);
    index++;
  }
  printf("End of Formatslist\n");
}

void print_properties(unicap_handle_t handle){
  unicap_property_t properties[NR_OF_PROPERTIES];
  int status = STATUS_SUCCESS;
  int propertycount = 0;
  while(SUCCESS(status)){
      status = unicap_enumerate_properties(handle, NULL, &properties[propertycount], propertycount);
      unicap_property_t property = properties[propertycount];
      
      printf("%d: %s\n", propertycount, property.identifier);
propertycount++;
    }

}

int main (int argc, char **argv)
{
  unicap_handle_t handle;
  handle = open_imagingsource_camera();
  print_formats(handle);
  print_properties(handle);
  unicap_close (handle);
  return 0;
}
