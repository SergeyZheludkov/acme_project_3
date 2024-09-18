from django.db import models

from .validators import real_age


class Birthday(models.Model):
    first_name = models.CharField('Name', max_length=20)
    last_name = models.CharField(
        'Surname', blank=True, help_text='Optional field', max_length=20
    )
    birthday = models.DateField('Birthday', validators=(real_age, ))
    image = models.ImageField(
        'Photo', upload_to='birthdays_images', blank=True
    )

    class Meta:
        ordering = ('birthday', )
        constraints = (
            models.UniqueConstraint(
                fields=('first_name', 'last_name', 'birthday'),
                name='Unique person constraint',
            ),
        )
