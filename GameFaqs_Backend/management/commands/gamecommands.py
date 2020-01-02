from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Commands for games, etc'

    def handle(self, *args, **options):
        pass
        # ShoeColor.objects.create(color='Black')
        # ShoeType.objects.create(style='Sneaker')
