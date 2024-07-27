import os
import sys
import django

# Set up Django environment
os.environ.setdefault( 'DJANGO_SETTINGS_MODULE', 'mtb_v4_settings.settings' )  # Replace with your project name
PROJECT_ROOT = os.path.dirname( os.path.abspath( '../manage.py' ) )
sys.path.append( PROJECT_ROOT )

django.setup( )

from mtb_v4_app.models import Media

def duplicate_media_phase_1_to_2( ):
   original_records = Media.objects.filter( phase = 1 )
   new_records = [ ]

   for record in original_records:
      new_record_data = record.__dict__.copy( )
      new_record_data.pop( '_state', None )
      new_record_data[ 'id' ] = None  # Remove the existing id to generate a new one
      new_record_data[ 'phase' ] = 2
      new_record = Media( **new_record_data )
      new_records.append( new_record )

   Media.objects.bulk_create( new_records )

if __name__ == '__main__':
   duplicate_media_phase_1_to_2( )
   print( "Media records with phase 1 duplicated to phase 2 successfully!" )
