from django.core.management.base import BaseCommand, CommandError

from shortener.models import stored_url

class Command(BaseCommand):
    help = "refreshes short url with manage.py command"

    def add_arguments(self, parser):
        parser.add_argument("--items", type=int)

    def handle(self, *args, **options):
        return stored_url.objects.refresh_short_urls(itm=options['items'])
        