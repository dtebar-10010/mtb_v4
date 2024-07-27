from django.shortcuts import render
from .models import Media, History

def home( request ):
   # Get the current phase from the request, default to 1 if not provided
   current_phase = int( request.GET.get( 'phase', 1 ) )

   # Fetch media items that match the current phase
   media_list = Media.objects.filter( phase = current_phase )

   # Fetch history items that match the current phase
   history_list = History.objects.filter( phase = current_phase )

   # Define phases with Roman numerals
   phases = [ (1, '1959 - 1962'), (2, '1962 - 1966'), (3, '1966 - 1970'), (4, '1970 - 9999'), (5, 'Karaokes') ]

   context = {
      'current_phase': current_phase,
      'media_list'   : media_list,
      'history_list' : history_list,
      'phases'       : phases
   }
   return render( request, 'home.html', context )
