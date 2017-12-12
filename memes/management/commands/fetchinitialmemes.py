from django.core.management.base import BaseCommand, CommandError

from memes.tasks.fetchmemes import RedditMemeFetcher, GiphyMemeFetcher

class Command(BaseCommand):
    help = 'Fetch Memes from each reddit,instagram,giphy,facebook'
    ''' now only reddit and giphy '''
    redditmeme = RedditMemeFetcher()
    giphymeme = GiphyMemeFetcher()

    redditmeme.getInitialMemes()
    giphymeme.getInitialMemes()
    giphymeme.getTheOfficeMemes()

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Successfully fetched everything'))