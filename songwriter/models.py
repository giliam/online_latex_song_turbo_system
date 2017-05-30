# coding:utf-8

from datetime import timedelta

from django.db import models
from django.utils.translation import ugettext_lazy as _


class Author(models.Model):
    firstname = models.CharField(
        max_length=150, 
        default="",
        blank=True
    )
    lastname = models.CharField(
        max_length=150, 
        default="",
        blank=True
    )

    def __str__(self):
        return u"Author: {0} {1}".format(self.firstname, self.lastname.upper())


class Editor(models.Model):
    name = models.CharField(
        max_length=150, 
        default="",
        blank=True
    )

    def __str__(self):
        return u"Editor: {0}".format(self.name)


class Theme(models.Model):
    name = models.CharField(
        max_length=150,
        default="",
        blank=False
    )

    def __str__(self):
        return u"Theme: {0}".format(self.name)


class Chord(models.Model):
    note = models.CharField(
        max_length=15,
        blank=False,
        default=""
    )
    linked_word = models.CharField(
        max_length=50,
        blank=False,
        default=""
    )
    spot_in_verse = models.PositiveIntegerField()


class Verse(models.Model):
    order = models.PositiveIntegerField()
    content = models.TextField(blank=False)
    
    followed_by_new_paragraph = models.BooleanField(
        default=False,
        verbose_name=_("followed by a new paragraph?").capitalize()
    )

    is_refrain = models.BooleanField(
        default=False,
        verbose_name=_("is a refrain verse?").capitalize()
    )

    chords = models.ForeignKey(Chord, related_name='+')

    def __str__(self):
        return u"Verse: {0}".format(self.content)


class Song(models.Model):
    title = models.CharField(
        max_length=150,
        default="",
        blank=False
    )

    author = models.ForeignKey(Author, related_name="+")
    editor = models.ForeignKey(Editor, related_name="+")
    theme = models.ForeignKey(Theme, related_name="+")
    
    rights_paid = models.BooleanField(
        default=True,
        verbose_name=_("rights paid")
    )
    secli_number = models.CharField(
        max_length=150, 
        default="",
        blank=True
    )
    sacem_number = models.CharField(
        max_length=150, 
        default="",
        blank=True
    )

    comments = models.TextField(
        blank=False,
        verbose_name=_("comments").capitalize()
    )

    added_date = models.DateTimeField(
        _('date added to the database'),
        auto_now_add=True,
        blank=True
    )
    updated_date = models.DateTimeField(
        _('date updated to the database'),
        auto_now=True
    )

    def __str__(self):
        return u"Song: {0}".format(self.title)
