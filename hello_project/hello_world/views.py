from django.shortcuts import render

from .models import Table1


def hello_world(request):
    tables_contents = Table1.objects.prefetch_related('related_items').last()
    return render(request, 'hello_world.html', {'table': tables_contents})
