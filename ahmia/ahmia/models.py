"""Models for the database of ahmia."""
import re

from django.core.exceptions import ValidationError
from django.core.validators import MaxLengthValidator, MinLengthValidator
from django.db import models

def validate_onion_url(url):
    """ Test is url correct onion URL."""
    #Must be like http://3g2upl4pq6kufc4m.onion/
    if len(url) != 30:
        raise ValidationError(u'%s length is not 30' % url)
    if url[0:7] != 'http://':
        raise ValidationError(u'%s is not beginning with http://' % url)
    if url[-7:] != '.onion/':
        raise ValidationError(u'%s is not ending with .onion/' % url)
    if not re.match("[a-z2-7]{16}", url[7:-7]):
        raise ValidationError(u'%s is not valid onion domain' % url)

class HiddenWebsite(models.Model):
    """Hidden service website."""
    #for instance: http://3g2upl4pq6kufc4m.onion/
    onion = models.URLField(validators=[validate_onion_url], unique=True)