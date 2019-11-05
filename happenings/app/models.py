from django.db import models
from django.utils import timezone

class Tag(models.Model):
    # id = uuid
    name = models.CharField(max_length=128)

    def __str__(self):
        return f'{self.name}'

    def __repr__(self):
        return f'<Tag({self.name})>'

class HappeningQuerySet(models.QuerySet):
    def active(self):
        return self.filter(start_date__lte=timezone.now(), end_date__gte=timezone.now())

    def upcoming(self):
        return self.filter(start_date__gte=timezone.now())

    def finished(self):
        return self.filter(end_date__lte=timezone.now())

class Happening(models.Model):

    # id = models uuid
    title = models.CharField(max_length=128)
    image = models.ImageField()
    text = models.TextField(max_length=1024, null=True, blank=True)
    tags = models.ManyToManyField(Tag)
    start_date = models.DateField()
    end_date = models.DateField()

    happenings = HappeningQuerySet.as_manager()

    def get_status(self):
        if self.end_date < timezone.localdate(timezone.now()):
            return 'FINISHED'
        elif self.start_date > timezone.localdate(timezone.now()):
            return 'UPCOMING'
        elif self.start_date < timezone.localdate(timezone.now()) and self.end_date > timezone.localdate(timezone.now()):
            return 'ACTIVE'
        else:
            return 'N/A'

    def __str__(self):
        return '{} ({})'.format(self.title, self.start_date)

    def __repr__(self):
        return '<Happening({}, {})>'.format(self.title, self.start_date)


class Registration(models.Model):
    # id uuid
    name = models.CharField(max_length=320)
    mobile = models.CharField(max_length=20)
    email = models.CharField(max_length=320)
    happening = models.ForeignKey(Happening, on_delete='CASCADE')

    def __str__(self):
        return f'{self.name} - {self.happening.title}'

    def __repr__(self):
        return f'<Registration({self.name}, {self.mobile}, {self.email}, {self.happening})>'