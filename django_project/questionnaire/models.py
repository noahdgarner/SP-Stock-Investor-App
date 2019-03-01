# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.core.validators import MinValueValidator

# Create your models here.

class user(models.Model):
    date_of_birth = models.DateField()

    name = models.CharField(max_length = 40)

    #do you need to be 18?
    Age = models.PositiveIntegerField(validators=[MinValueValidator(18)])

    Financial_Situation = models.PositiveIntegerField(validators=[MinValueValidator(1)])

    Income = models.PositiveDecimalField()

    investing_knowledge = models.PositiveIntegerField(validators=[MinValueValidator(1)])

    investing_amount = models.PositiveDecimalField(validators=[MinValueValidator(1)])

    risk_tolerance = models.PositiveIntegerField(validators=[MinValueValidator(1)])

    #TODO
    #areas of interest