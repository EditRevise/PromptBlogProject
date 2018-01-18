# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

def index(request):
    """Render the homepage."""
    return render(request, 'blog/index.html')
