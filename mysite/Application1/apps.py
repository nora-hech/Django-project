#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class Application1Config(AppConfig):
    name = 'Application1'
    verbose_name = "Application"
