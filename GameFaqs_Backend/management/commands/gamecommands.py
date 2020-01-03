from django.core.management.base import BaseCommand
from GameFaqs_Backend.models import Platform


class Command(BaseCommand):
    help = 'Commands for games, etc'

    def handle(self, *args, **options):
        Platform.objects.create(consoles='PS4')
        Platform.objects.create(consoles='Xbox One')
        Platform.objects.create(consoles='Switch')
        Platform.objects.create(consoles='PS3')
        Platform.objects.create(consoles='Xbox 360')
        Platform.objects.create(consoles='Wii U')
        Platform.objects.create(consoles='VITA')
        Platform.objects.create(consoles='PC')
        Platform.objects.create(consoles='Android')
        Platform.objects.create(consoles='IOS')
        Platform.objects.create(consoles='3DS')
        Platform.objects.create(consoles='PSP')
        Platform.objects.create(consoles='Gamecube')
        Platform.objects.create(consoles='PS2')
        Platform.objects.create(consoles='PS1')
        Platform.objects.create(consoles='Xbox')
        Platform.objects.create(consoles='Nintendo 64')
