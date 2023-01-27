from django.test import TestCase
from .forms import ThreadForm, CommentForm


class TestThreadForm(TestCase):
    '''
    Testing for Create Thread Form
    '''

    # Tests to check required fields are not blank

    def test_thread_year_is_required(self):
        '''
        Test to ensure year is present
        '''
        form = ThreadForm({'year': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('year', form.errors.keys())
        self.assertEqual(form.errors['year'][0], 'This field is required.')

    def test_thread_make_is_required(self):
        '''
        Test to ensure make is present
        '''
        form = ThreadForm({'make': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('make', form.errors.keys())
        self.assertEqual(
            form.errors['make'][0], 'This field is required.'
            )

    def test_thread_model_is_required(self):
        '''
        Test to ensure make is present
        '''
        form = ThreadForm({'model': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('model', form.errors.keys())
        self.assertEqual(
            form.errors['model'][0], 'This field is required.'
            )

    def test_thread_story_is_required(self):
        '''
        Test to ensure make is present
        '''
        form = ThreadForm({'story': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('story', form.errors.keys())
        self.assertEqual(
            form.errors['story'][0], 'This field is required.'
            )

    def test_thread_modifications_is_required(self):
        '''
        Test to ensure make is present
        '''
        form = ThreadForm({'modifications': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('modifications', form.errors.keys())
        self.assertEqual(
            form.errors['modifications'][0], 'This field is required.'
            )

    def test_fields_are_explicit_in_form_metaclass(self):
        form = ThreadForm()
        self.assertEqual(form.Meta.fields,
                         ('year', 'make', 'model', 'thread_image', 'story',
                          'modifications'))


class TestCommentForm(TestCase):

    def test_comment_body_is_required(self):
        form = CommentForm({'body': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('body', form.errors.keys())
        self.assertEqual(form.errors['body'][0], 'This field is required.')

    def test_fields_are_explicit_in_form_metaclass(self):
        form = CommentForm()
        self.assertEqual(form.Meta.fields,
                         ('body',))
