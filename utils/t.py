import os
import sys
import django

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mtb_v4_settings.settings')
PROJECT_ROOT = os.path.dirname( os.path.abspath( '../manage.py' ) )
sys.path.append(PROJECT_ROOT)

django.setup()

from mtb_v4_app.models import Media, Page  # Import both models

def add_posters_phase_3():
    # Find all videos in phase 3
    videos = Media.objects.filter(phase=3, type='video')

    new_records = []
    for video in videos:
        poster_record = Media(
            title=f'Poster for {video.title}',
            phase=3,
            path=video.path.replace('.mp4', '.jpg'),  # Assuming poster path is similar to video path
            type='image',
            page=video.page
        )
        new_records.append(poster_record)

    Media.objects.bulk_create(new_records)
    print(f"Added {len(new_records)} poster records for phase 3 videos.")

if __name__ == '__main__':
    add_posters_phase_3()
