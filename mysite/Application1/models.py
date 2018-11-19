#!/usr/bin/env python
from django.db import models
import uuid

# Create your models here.


def f():
    d = uuid.uuid4()
    return d[0:19]


class Schools(models.Model):
    name = models.CharField(max_length=20)
    maxstudents = models.PositiveIntegerField()

    def add_student(self, student):
        if self.students_set.count() >= self.maxstudents:
            raise Exception("This school is already full.")
        self.students_set.add(student)


class Students(models.Model):
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    identification = models.CharField(
        max_length=20, unique=True, default=f, editable=False)
    school = models.ForeignKey(
        'Schools', on_delete=models.CASCADE, related_name='students')

    class Meta:
        unique_together = ('firstname', 'lastname', 'school')

    def __unicode__(self):
        return "%s %s" % (
            self.identification, self.firstname, self.lastname, self.school)
