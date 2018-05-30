import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','budget.settings')

import django
django.setup()

from budgetApp.models import Stuff

def new_month():
    """Use this to clear the actual data back to 0 every month"""
    stuff = Stuff.objects.order_by('top_name')
    for i in stuff:
        i.actual = 0
        i.save()


"""print (stuff)
for i in stuff:
    print (i.actual)"""

if __name__ == "__main__":
    new_month()
