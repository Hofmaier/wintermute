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

void isAvailable(const char name)
{

  unicap_device_t tis_dev;
  while(SUCCESS(status))
    {
      status = unicap_enumerate_devices(NULL, &tis_dev, dev_count);
      if(!SUCCESS(status)) break;
    }
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
      if(!SUCCESS(status)) break;

      unicap_property_t currentproperty = properties[propertycount];
      char * propertyType;
      if(currentproperty.type == UNICAP_PROPERTY_TYPE_RANGE)
	{
	  propertyType = "Range";
	}
      else
	{
	  propertyType = "";
	}
      printf("%d: %s RelationsCount: %d ", propertycount, currentproperty.identifier, currentproperty.relations_count);
      printf("Type: %s \n", propertyType);
propertycount++;
    }

}

/*
void display_video_stream(int argc, char **argv){
  GtkWidget * window;
  GtkWidget * ugtk_display;

  gtk_init(&argc, &argv);

  window = gtk_window_new(GTK_WINDOW_TOPLEVEL);
  g_signal_connect (G_OBJECT (window), "destroy", G_CALLBACK(gtk_main_quit), NULL);
  
  ugtk_display = unicapgtk_video_display_new_by_device(NULL);
  gtk_container_add(GTK_CONTAINER (window), ugtk_display);
  unicapgtk_video_display_start (UNICAPGTK_VIDEO_DISPLAY(ugtk_display));

  gtk_widget_show_all(window);
  gtk_main();
}
*/

int main (int argc, char **argv)
{
  //display_video_stream(argc, argv);
  unicap_handle_t handle;
  handle = open_imagingsource_camera();
  //print_formats(handle);
  //print_properties(handle);
  //unicap_close (handle);
  return 0;
}
