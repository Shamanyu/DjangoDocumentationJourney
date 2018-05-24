# Write test cases

import datetime

from django.test import TestCase
from django.utils import timezone

from .models import Question

# Create your tests here.

"""
python manage.py test polls creates a special database for testing. It then
looks for test methods whose name begin with 'test'.
"""
class QuestionModelTests(TestCase):

    def test_was_published_recently_with_future_question(self):

        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)
        self.assertIs(future_question.was_published_recently(), False)
