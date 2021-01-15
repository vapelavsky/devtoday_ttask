from apscheduler.schedulers.background import BackgroundScheduler
from django.db.models import F
from django_apscheduler.jobstores import DjangoJobStore
from posts.models import Post


def reset_upvotes():
    Post.objects.update(upvotes_counter=F(0))


def start():
    scheduler = BackgroundScheduler()
    scheduler.add_jobstore(DjangoJobStore(), "default")
    scheduler.add_job(reset_upvotes(), 'interval', hours=24, name='reset_upvotes', jobstore='default')
    scheduler.start()
