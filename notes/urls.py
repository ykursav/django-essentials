from django.urls import path

from . import views


# Can be...
urlpatterns = [
    path("notes", views.NotesListView.as_view(), name="notes.list"),
    path("notes/<int:pk>", views.NotesDetailView.as_view(), name="note.detail"),
]
