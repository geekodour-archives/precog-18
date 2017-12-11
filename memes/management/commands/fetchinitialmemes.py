from django.core.management.base import BaseCommand, CommandError

from memes.tasks.fetchmemes import RedditMemeFetcher, GiphyMemeFetcher

class Command(BaseCommand):
    help = 'Fetch 500 Memes from each reddit,instagram,giphy,facebook'

    redditmeme = RedditMemeFetcher()
    giphymeme = GiphyMemeFetcher()
    #redditmeme.getInitialMemes()
    giphymeme.getInitialMemes()

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Successfully fetched everything'))