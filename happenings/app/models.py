from django.db import models

class Tag(models.Model):
    # id = uuid
    name = models.CharField(max_length=128)

    def __str__(self):
        return f'{self.name}'

    def __repr__(self):
        return f'<Tag({self.name})>'

class Happening(models.Model):
    # id = models uuid
    title = models.CharField(max_length=128)
    image = models.ImageField()
    text = models.TextField(max_length=1024)
    tags = models.ManyToManyField(Tag)
    start_date = models.DateField()
    end_date = models.DateField()

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