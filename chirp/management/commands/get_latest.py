from django.core.management import BaseCommand
from chirp.models import Chirp


class Command(BaseCommand):
    def add_arguments(self, parser):
        """
        Creates an optional argument of --limit to specify how many to return
        :param parser:
        :return:
        """
        parser.add_argument('--limit', type=int, help='Limit the results',
                            default=1)

    def handle(self, *args, **options):
        """
        This method is required to be overridden. It is the main source of code
        :param args:
        :param options:
        :return:
        """
        chirp = Chirp.objects.order_by('-posted_at')[:options['limit']]

        self.stdout.write("Got chirp len of {}".format(len(chirp)))
