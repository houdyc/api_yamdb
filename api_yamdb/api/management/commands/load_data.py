import csv

from django.core.management import BaseCommand

from reviews.models import Category, Comments, Genre, Review, Title, TitleGenre
from users.models import User

TABLES = {
    User: 'users.csv',
    Genre: 'genre.csv',
    Category: 'category.csv',
    Title: 'titles.csv',
    Review: 'review.csv',
    Comments: 'comments.csv',
    TitleGenre: 'genre_title.csv',
}


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        for model, csv_f in TABLES.items():
            with open(
                f'static/data/{csv_f}',
                'r',
                encoding='utf-8'
            ) as csv_file:
                reader = csv.DictReader(csv_file)
                model.objects.bulk_create(
                    model(**data) for data in reader)
        self.stdout.write(self.style.SUCCESS('Загрузка данных завершена'))
