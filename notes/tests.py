from django.test import TestCase
from .models import Note


class NoteModelTest(TestCase):

    def test_note_creation(self):
        note = Note.objects.create(
            title="Test Note",
            content="This is a test note"
        )

        self.assertEqual(note.title, "Test Note")
        self.assertEqual(note.content, "This is a test note")


class NoteViewTest(TestCase):

    def test_note_list_view(self):
        response = self.client.get('/')

        self.assertEqual(response.status_code, 200)

    def test_create_note(self):
        response = self.client.post('/create/', {
            'title': 'Shopping',
            'content': 'Buy milk'
        })

        self.assertEqual(response.status_code, 302)
        self.assertEqual(Note.objects.count(), 1)