from django.db import models

class Tag(models.Model):
    # id = uuid
    name = models.CharField(max_length=128)

    def str(self):
        return f'{name}'

    def repr(self):
        return f'<Tag({self.name})>'

class Happening(models.Model):
    # id = models uuid
    title = models.CharField(max_length=128)
    image = models.ImageField()
    text = models.TextField(max_length=1024)
    tags = models.ForeignKey(Tag, on_delete='NULL')
    start_date = models.DateField()
    end_date = models.DateField()

    def str(self):
        return '{} ({})'.format(self.title, self.start_date)

    def repr(self):
        return '<Happening({}, {})>'.format(self.title, self.start_date)


class Registration(models.Model):
    # id uuid
    name = models.CharField(max_length=320)
    mobile = models.CharField(max_length=20)
    email = models.CharField(max_length=320)
    happening = models.ForeignKey(Happening, on_delete='CASCADE')

    def str(self):
        return f'{self.name} - {self.happening.title}'

    def repr(self):
        return f'<Registration({self.name}, {self.mobile}, {self.email}, {self.happening})>'