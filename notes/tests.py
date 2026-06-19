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

    def test_update_note(self):
        """Test that an existing note can be updated."""
        note = Note.objects.create(
            title="Old Title",
            content="Old content"
        )

        response = self.client.post(f'/update/{note.id}/', {
            'title': 'Updated Title',
            'content': 'Updated content'
        })

        note.refresh_from_db()

        self.assertEqual(response.status_code, 302)
        self.assertEqual(note.title, 'Updated Title')
        self.assertEqual(note.content, 'Updated content')

    def test_delete_note(self):
        """Test that an existing note can be deleted."""
        note = Note.objects.create(
            title="Delete Me",
            content="This note will be deleted"
        )

        response = self.client.post(f'/delete/{note.id}/')

        self.assertEqual(response.status_code, 302)
        self.assertEqual(Note.objects.count(), 0)