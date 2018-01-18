# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# TODO: You might decide to change around the model structure and might want
# more (or fewer) models, depending on your design. We've included these models
# as a resonable default to get you started.

class Post(models.Model):
    """TODO: What is a `Document`?"""

    text = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    # TODO: Add additional fields here

class Comment(models.Model):
    """TODO: What is a `Comment`?"""

    # TODO: Add your fields here
