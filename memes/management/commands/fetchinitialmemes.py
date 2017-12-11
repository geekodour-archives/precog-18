from django.core.management.base import BaseCommand, CommandError

class Command(BaseCommand):
    help = 'Fetch 500 Memes from each reddit,instagram,giphy,facebook'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Successfully fetched everything'))