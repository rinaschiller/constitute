# Create your tasks here
from __future__ import absolute_import, unicode_literals
from celery import shared_task, task

@shared_task
def test(arg):
    print(arg)

@shared_task
def fetchSexistTweets():
    from .fetchTweets import fetchTweets
    from .models import Politician
    politician_ids = Politician.objects.values_list('id', flat=True)
    fetchTweets(politician_ids, True)

@shared_task
def fetchAllTweets():
    from .fetchTweets import fetchTweets
    from .models import Politician
    politician_ids = Politician.objects.values_list('id', flat=True)
    fetchTweets(politician_ids, True)
