from django.shortcuts import render
from django.http import Http404

from .models import Notes
from .forms import NotesForm
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)


class NotesCreateView(CreateView):
    model = Notes
    success_url = "/smart/notes"
    form_class = NotesForm


class NotesUpdateView(UpdateView):
    model = Notes
    success_url = "/smart/notes"
    form_class = NotesForm


class NotesDeleteView(DeleteView):
    model = Notes
    success_url = "/smart/notes"
    template_name = "notes/notes_delete.html"


class NotesListView(ListView):
    model = Notes
    context_object_name = "notes"
    template_name = "notes/notes_list.html"


class NotesDetailView(DetailView):
    model = Notes
    context_object_name = "note"
    template_name = "notes/notes_detail.html"
