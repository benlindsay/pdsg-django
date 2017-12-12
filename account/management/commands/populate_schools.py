from django.core.management.base import BaseCommand
from account.models import School

class Command(BaseCommand):
    args = ''
    help = 'Fills School model with 12 UPenn schools + other'

    def _create_schools(self):
        asc = School(name='Annenberg School for Communication', abbrev='ASC')
        asc.save()

        gse = School(name='Graduate School of Education', abbrev='GSE')
        gse.save()

        law = School(name='Law School', abbrev='Law')
        law.save()

        sas = School(name='School of Arts and Sciences', abbrev='SAS')
        sas.save()

        dental = School(name='School of Dental Medicine', abbrev='Dental')
        dental.save()

        seas = School(name='School of Engineering and Applied Science',
                      abbrev='SEAS')
        seas.save()

        psom = School(name='Perelman School of Medicine', abbrev='PSoM')
        psom.save()

        nursing = School(name='School of Nursing', abbrev='Nursing')
        nursing.save()

        sp2 = School(name='School of Social Policy and Practice', abbrev='SP2')
        sp2.save()

        vet = School(name='School of Veterinary Medicine', abbrev='Vet')
        vet.save()

        wharton = School(name='Wharton School', abbrev='Wharton')
        wharton.save()

        other = School(name='Other', abbrev='Other')
        other.save()

    def handle(self, *args, **options):
        self._create_schools()
