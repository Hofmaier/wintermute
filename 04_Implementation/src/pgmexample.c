
/*
** tut_2_4.c
** 
** 
** Started on  Mon Nov 27 17:10:52 2006 Arne Caspari
** Last update Fri Dec  1 07:40:06 2006 Arne Caspari
*/


#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <unicap.h>
#include <fcntl.h>

#define MAX_DEVICES 64
#define MAX_FORMATS 64
#define MAX_PROPERTIES 64

int	outfile;

unicap_handle_t
open_device ()
{
  int dev_count;
  int status = STATUS_SUCCESS;
  unicap_device_t devices[MAX_DEVICES];
  unicap_handle_t handle;
  int d = -1;

  for (dev_count = 0; SUCCESS (status) && (dev_count < MAX_DEVICES);
       dev_count++)
    {
      // (1)
      status =
	unicap_enumerate_devices (NULL, &devices[dev_count], dev_count);
      if (SUCCESS (status))
	{
	  printf ("%d: %s\n", dev_count, devices[dev_count].identifier);
	}
      else
	{
	  break;
	}
    }

  if (dev_count == 0)
    {
      // no device selected
      return NULL;
    }


  while ((d < 0) || (d >= dev_count))
    {
      printf ("Open Device: ");
      scanf ("%d", &d);
    }

  unicap_open (&handle, &devices[d]);

  return handle;
}

void
set_format (unicap_handle_t handle)
{
  unicap_format_t formats[MAX_FORMATS];
  int format_count;
  unicap_status_t status = STATUS_SUCCESS;
  int f = -1;

  for (format_count = 0; SUCCESS (status) && (format_count < MAX_FORMATS);
       format_count++)
    {
      status = unicap_enumerate_formats (handle, NULL, &formats[format_count],	// (1)
					 format_count);
      if (SUCCESS (status))
	{
	  printf ("%d: %s\n", format_count, formats[format_count].identifier);
	}
      else
	{
	  break;
	}
    }

  if (format_count == 0)
    {
      // no video formats
      return;
    }

  while ((f < 0) || (f >= format_count))
    {
      printf ("Use Format: ");
      scanf ("%d", &f);
    }

  if (formats[f].size_count)
    {
      // (2)
      int i;
      int s = -1;

      for (i = 0; i < formats[f].size_count; i++)
	{
	  printf ("%d: %dx%d\n", i, formats[f].sizes[i].width,
		  formats[f].sizes[i].height);
	}

      while ((s < 0) || (s >= formats[f].size_count))
	{
	  printf ("Select Size: ");
	  scanf ("%d", &s);
	}

      formats[f].size.width = formats[f].sizes[s].width;
      formats[f].size.height = formats[f].sizes[s].height;
    }

  if (!SUCCESS (unicap_set_format (handle, &formats[f])))	// (3)
    {
      fprintf (stderr, "Failed to set the format!\n");
      exit (-1);
    }
}

static void new_frame_cb( unicap_event_t event, unicap_handle_t handle, unicap_data_buffer_t *buffer, void *usr_data )
{
   volatile int *frame_count = ( volatile int * )usr_data;
printf("frame: %d, size: %ld\n", *frame_count, buffer->buffer_size);
write(outfile, buffer->data, buffer->buffer_size);
   
   // (6)
   *frame_count = *frame_count -1;
}


void capture_frames( unicap_handle_t handle, int nframes )
{
   unicap_format_t format;
   volatile int frame_count;
   

   if( !SUCCESS( unicap_get_format( handle, &format ) ) )
   {
      fprintf( stderr, "Failed to get video format!\n" );
      exit( -1 );
   }
   
   format.buffer_type = UNICAP_BUFFER_TYPE_SYSTEM; // (1)
   
   if( !SUCCESS( unicap_set_format( handle, &format ) ) )
   {
      fprintf( stderr, "Failed to set video format!\n" );
      exit( -1 );
   }
   

   frame_count = nframes;
   unicap_register_callback( handle, UNICAP_EVENT_NEW_FRAME, (unicap_callback_t)new_frame_cb, (void*)&frame_count ); // (2)

   unicap_start_capture( handle ); // (3)
   
   while( frame_count > 0 ) // (4)
   {
      usleep( 100000 );
   }
   printf( "Captured %d frames!\n", nframes );

   unicap_stop_capture( handle ); // (5)
    
}

void set_range_property( unicap_handle_t handle )
{
   unicap_property_t properties[MAX_PROPERTIES];
   int property_count;
   int range_ppty_count;
   unicap_status_t status = STATUS_SUCCESS;
   int p = -1;
   double new_value = 0.0;

   for( property_count = range_ppty_count = 0; SUCCESS( status ) && ( property_count < MAX_PROPERTIES ); property_count++ )
   {
      status = unicap_enumerate_properties( handle, NULL, &properties[range_ppty_count], property_count );       // (1)
      if( SUCCESS( status ) )
      {
	 if( properties[range_ppty_count].type == UNICAP_PROPERTY_TYPE_RANGE ) // (2)
	 {
	    printf( "%d: %s\n", property_count, properties[range_ppty_count].identifier );
	    range_ppty_count++;
	 }
      }
      else
      {
	 break;
      }
   }

   if( range_ppty_count == 0 )
   {
      // no range properties
      return;
   }
   
   while( ( p < 0 ) || ( p > range_ppty_count ) )
   {
      printf( "Property: " );
      scanf( "%d", &p );
   }
   
   status = unicap_get_property( handle, &properties[p] ); // (3)
   if( !SUCCESS( status ) )
   {
      fprintf( stderr, "Failed to inquire property '%s'\n", properties[p].identifier );
      exit( -1 );
   }
   
   printf( "Property '%s': Current = %f, Range = [%f..%f]\n", properties[p].identifier,
	   properties[p].value, properties[p].range.min, properties[p].range.max );
   
   new_value = properties[p].range.min - 1.0f;
   while( ( new_value < properties[p].range.min ) || ( new_value > properties[p].range.max ) )
   {
      printf( "New value for property: " );
      scanf( "%lf", &new_value );
   }
   
   properties[p].value = new_value;
   
   if( !SUCCESS( unicap_set_property( handle, &properties[p] ) ) ) // (4)
   {
      fprintf( stderr, "Failed to set property!\n" );
      exit( -1 );
   }
}


int
main (int argc, char **argv)
{
	outfile = open("capture.dat", O_CREAT|O_TRUNC|O_WRONLY, 0777);
  unicap_handle_t handle;
  handle = open_device ();
  if (!handle)
    {
      return -1;
    }

  capture_frames( handle, 30 );

  unicap_close (handle);
  return 0;
}
