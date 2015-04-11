# Validators are a way to provide reusable validation logic
# for different types of fields
# See: https://docs.djangoproject.com/en/1.7/ref/validators/

from django.core.exceptions import ValidationError
from django.utils import timezone
import datetime

def not_dead(value):
    """Raise a ValidationError if the value is over 200 years ago.
    """
    now = timezone.now()
    if value <= now - datetime.timedelta(weeks= (200 * 52)):
        msg=u'the value is over 200 years ago'
        raise ValidationError(msg)
        
def not_future(value):
    """Raise a ValidationError if the value is in the future.
    """
    now = timezone.now()
    if now <= value:
        msg=u'value is in the future'
        raise ValidationError(msg)

