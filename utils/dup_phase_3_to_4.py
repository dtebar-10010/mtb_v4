import os
import sys
import django

# Set up Django environment
os.environ.setdefault( 'DJANGO_SETTINGS_MODULE', 'mtb_v4_settings.settings' )  # Replace with your project name
PROJECT_ROOT = os.path.dirname( os.path.abspath( '../manage.py' ) )
sys.path.append( PROJECT_ROOT )

django.setup( )

from mtb_v4_app.models import Media  # Replace 'your_app' with your app name

def duplicate_media_phase_3_to_4( ):
   original_records = Media.objects.filter( phase = 3 )
   new_records = [ ]

   for record in original_records:
      new_record_data = record.__dict__.copy( )
      new_record_data.pop( '_state', None )
      new_record_data[ 'id' ] = None  # Remove the existing id to generate a new one
      new_record_data[ 'phase' ] = 4  # Set the new phase to 4

      # Update the path to reflect phase 4
      new_record_data[ 'path' ] = new_record_data[ 'path' ].replace( '/03/', '/04/' ).replace( 'third_era', 'fourth_era' )

      new_record = Media( **new_record_data )
      new_records.append( new_record )

   Media.objects.bulk_create( new_records )

if __name__ == '__main__':
   duplicate_media_phase_3_to_4( )
   print( "Media records with phase 3 duplicated to phase 4 successfully!" )
