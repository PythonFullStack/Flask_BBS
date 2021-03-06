from flask import  Flask
from celery import Celery
from flask_mail import Message

from exts import mail
import config

app = Flask(__name__)

mail.init_app(app)


def make_celery(app):
    celery = Celery(
        app.import_name,
        backend=config.CELERY_RESULT_BACKEND,
        broker=config.CELERY_BROKER_URL
    )
    # celery.conf.update(app.config)

    class ContextTask(celery.Task):
        def __call__(self, *args, **kwargs):
            with app.app_context():
                return self.run(*args, **kwargs)

    celery.Task = ContextTask
    return celery


celery = make_celery(app)


@celery.task
def send_mail_celery(subject, recipients, body):
    message = Message(subject=subject, recipients=recipients, body=body)
    mail.send(message)
