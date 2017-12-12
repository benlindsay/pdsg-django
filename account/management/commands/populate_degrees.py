from django.core.management.base import BaseCommand
from account.models import Degree

class Command(BaseCommand):
    args = ''
    help = 'Fills Degree model with degree options + other'

    def _create_degrees(self):
        bachelors = Degree(name='Bachelors')
        bachelors.save()

        masters = Degree(name='Masters')
        masters.save()

        phd = Degree(name='PhD')
        phd.save()

        postdoc = Degree(name='Postdoc')
        postdoc.save()

        md = Degree(name='MD')
        md.save()

        other = Degree(name='Other')
        other.save()

    def handle(self, *args, **options):
        self._create_degrees()
