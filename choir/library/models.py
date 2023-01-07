from django.db import models
from django.core.validators import FileExtensionValidator

from account.models import Campus, CustomUser
from django.dispatch import receiver

# Create your models here.

class Sheet(models.Model):
    title = models.CharField(verbose_name='Title Of the Song', max_length=100000, unique=True)
    composer = models.CharField(verbose_name='Composer Of the Song', max_length=100000)
    n = (('Solfa', 'Solfa'),
         ('Staff', 'Staff'),
         ('Both', 'Both'),
         )
    notation = models.CharField(choices=n, max_length=100000)
    t = (('Liturgy', 'Liturgy'),
         ('Classical', 'Classical'),
         ('Cultural', 'Cultural'),
         ('Other', 'Other'),
         )
    type = models.CharField(choices=t, max_length=100000)
    p = (('None', 'None'),
         ('Ordinary', 'Ordinary'),
         ('Advent', 'Advent'),
         ('Christmas', 'Christmas'),
         ('Lent', 'Lent'),
         ('Easter', 'Easter'),
         ('Pentecost', 'Pentecost'),
         ('Christ The King', 'Christ The King'),
         )
    part_of_calender = models.CharField(choices=p, verbose_name='Part of calender', max_length=100000)
    p2 = (('None', 'None'),
          ('Entrance', 'Entrance'),
          ('Lord Have Mercy', 'Lord Have Mercy'),
          ('Glory be to God', 'Glory be to God'),
          ('Creed', 'Creed'),
          ('Prayer of the Faithful', 'Prayer of the Faithful'),
          ('Offertory/Thanksgiving', 'Offertory/Thanksgiving'),
          ('Consecration', 'Consecration'),
          ('Holy', 'Holy'),
          ('Our Father', 'Our Father'),
          ('Lord Have Mercy', 'Lord Have Mercy'),
          ('Communion', 'Communion'),
          ('Dismissal', 'Dismissal'),
          )
    part_of_mass = models.CharField(choices=p2, verbose_name='Part of mass', max_length=100000)
    uploader = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    uploaded_at = models.DateField(auto_now_add=True)
    file = models.FileField(upload_to='Documents/%Y/%m/%d/',
                            validators=[FileExtensionValidator(allowed_extensions=['pdf'])])

    def __str__(self):
        return f'{self.title} by {self.composer}'


    class Meta:
        ordering = ('-uploaded_at',)

class Audio(models.Model):
    title = models.CharField(verbose_name='Title Of the Song', max_length=100000, unique=True)
    composer = models.CharField(verbose_name='Composer Of the Song', max_length=100000)
    t = (('Liturgy', 'Liturgy'),
         ('Classical', 'Classical'),
         ('Cultural', 'Cultural'),
         ('Other', 'Other'),
         )
    type = models.CharField(choices=t, max_length=100000)
    p = (('None', 'None'),
         ('Ordinary', 'Ordinary'),
         ('Advent', 'Advent'),
         ('Christmas', 'Christmas'),
         ('Lent', 'Lent'),
         ('Easter', 'Easter'),
         ('Pentecost', 'Pentecost'),
         ('Christ The King', 'Christ The King'),
         )
    part_of_calender = models.CharField(choices=p, verbose_name='Part of calender', max_length=100000)
    p2 = (('None', 'None'),
          ('Entrance', 'Entrance'),
          ('Lord Have Mercy', 'Lord Have Mercy'),
          ('Glory be to God', 'Glory be to God'),
          ('Creed', 'Creed'),
          ('Prayer of the Faithful', 'Prayer of the Faithful'),
          ('Offertory/Thanksgiving', 'Offertory/Thanksgiving'),
          ('Consecration', 'Consecration'),
          ('Holy', 'Holy'),
          ('Our Father', 'Our Father'),
          ('Lord Have Mercy', 'Lord Have Mercy'),
          ('Communion', 'Communion'),
          ('Dismissal', 'Dismissal'),
          )
    part_of_mass = models.CharField(choices=p2, verbose_name='Part of mass', max_length=100000)
    uploader = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    uploaded_at = models.DateField(auto_now_add=True)
    file = models.FileField(upload_to='Audio/%Y/%m/%d/',
                            validators=[FileExtensionValidator(allowed_extensions=['mp3', 'ogg', 'wav'])])

    def __str__(self):
        return f'{self.title} by {self.composer}'

    class Meta:
        ordering = ('-uploaded_at',)

class Video(models.Model):
    title = models.CharField(verbose_name='Title Of the Song', max_length=100000, unique=True)
    composer = models.CharField(verbose_name='Composer Of the Song', max_length=100000)
    t = (('Liturgy', 'Liturgy'),
         ('Classical', 'Classical'),
         ('Cultural', 'Cultural'),
         ('Other', 'Other'),
         )
    type = models.CharField(choices=t, max_length=100000)
    p = (('None', 'None'),
         ('Ordinary', 'Ordinary'),
         ('Advent', 'Advent'),
         ('Christmas', 'Christmas'),
         ('Lent', 'Lent'),
         ('Easter', 'Easter'),
         ('Pentecost', 'Pentecost'),
         ('Christ The King', 'Christ The King'),
         )
    part_of_calender = models.CharField(choices=p, verbose_name='Part of calender', max_length=100000)
    p2 = (('None', 'None'),
          ('Entrance', 'Entrance'),
          ('Lord Have Mercy', 'Lord Have Mercy'),
          ('Glory be to God', 'Glory be to God'),
          ('Creed', 'Creed'),
          ('Prayer of the Faithful', 'Prayer of the Faithful'),
          ('Offertory/Thanksgiving', 'Offertory/Thanksgiving'),
          ('Consecration', 'Consecration'),
          ('Holy', 'Holy'),
          ('Our Father', 'Our Father'),
          ('Lord Have Mercy', 'Lord Have Mercy'),
          ('Communion', 'Communion'),
          ('Dismissal', 'Dismissal'),
          )
    part_of_mass = models.CharField(choices=p2, verbose_name='Part of mass', max_length=10000)
    uploader = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    uploaded_at = models.DateField(auto_now_add=True)
    file = models.FileField(upload_to='Videos/%Y/%m/%d/',
                            validators=[FileExtensionValidator(allowed_extensions=['mp4','mp4','mov', 'flv','avi'])])

    def __str__(self):
        return f'{self.title} by {self.composer}'

    class Meta:
        ordering = ('-uploaded_at',)

class Document(models.Model):
    title = models.CharField(verbose_name='Title', max_length=1000000, )
    details = models.TextField(verbose_name='Details of the Document',max_length=100000, )
    campus = models.ForeignKey(Campus, on_delete=models.CASCADE, related_name='campus_of_document', )
    uploader = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    uploaded_at = models.DateField(auto_now_add=True)
    file = models.FileField(upload_to='Official_Documents/%Y/%m/%d/',
                            validators=[FileExtensionValidator(allowed_extensions=['pdf'])])
    #file = models.FileField(upload_to='Official_Documents/%Y/%m/%d/',
                            #validators=[FileExtensionValidator(allowed_extensions=['pdf'])])

    def __str__(self):
        return f'{self.title} '

    class Meta:
        ordering = ('-uploaded_at',)
