from django.test import TestCase
from .models import Notes

class NotesModelTest():
    def __init__(self):
        """Create 20 Notes instances for testing"""
        for i in range(20):
            Notes.objects.create(
                name=f'Note {i}',
                note=f'This is the content of note {i}.',
            )

NotesModelTest()
