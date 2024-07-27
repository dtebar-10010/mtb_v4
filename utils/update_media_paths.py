import os
import sys
import django

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mtb_v4_settings.settings')  # Replace 'mtb_v4_settings' with your project name
PROJECT_ROOT = os.path.dirname( os.path.abspath( '../manage.py' ) )
sys.path.append(PROJECT_ROOT)

django.setup()

from mtb_v4_app.models import Media  # Replace 'your_app' with your app name


def update_media_paths_phase_2():
    media_to_update = Media.objects.filter(phase=2)
    updated_count = 0

    for media in media_to_update:
        new_path = media.path.replace('/01/', '/02/').replace('first_era', 'second_era')
        if new_path != media.path:  # Only update if the path actually changed
            media.path = new_path
            media.save()
            updated_count += 1

    print(f"Updated {updated_count} Media records with phase 2 paths.")


if __name__ == '__main__':
    update_media_paths_phase_2()
