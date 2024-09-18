from django.db import models


class Birthday(models.Model):
    first_name = models.CharField('Name', max_length=20)
    last_name = models.CharField(
        'Surname', blank=True, help_text='Optional field', max_length=20
    )
    birthday = models.DateField('Birthday')
