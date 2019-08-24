from django.urls import path

from .views import MatchDetailsView

urlpatterns = [
    path('match-details', MatchDetailsView.as_view(), name='matchDetails')
]