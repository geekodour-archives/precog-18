from django.core.management.base import BaseCommand, CommandError
from memes.customdb import db
import pymongo

class Command(BaseCommand):
    help = 'Create Indexes for search'

    db.meme.create_index([('title','text'),('extracted_text','text')])

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Successfully indexed title and extracted text'))