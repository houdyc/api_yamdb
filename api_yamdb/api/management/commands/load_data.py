import csv
import logging

from django.core.management.base import BaseCommand

from reviews.models import Category, Comments, Genre, Review, Title, TitleGenre
from users.models import User


class Command(BaseCommand):
    """Класс для инициализации БД из csv файла."""

    def handle(self, *args, **options):
        """Запись в базу данных."""

        logging.debug('Импортируется users.csv')
        with open('static/data/users.csv', 'r', encoding='utf-8') as file:
            users = csv.DictReader(file, delimiter=',')

        for user in users:
            logging.info(user)
            user = User(
                id=user['id'],
                username=user['username'],
                email=user['email'],
                role=user.get('role'),
                bio=user.get('bio'),
                first_name=user.get('first_name'),
                last_name=user.get('last_name'),
            )
            user.save()

        logging.debug('Импортируется genre.csv')
        with open('static/data/genre.csv', 'r', encoding='utf-8') as file:
            genres = csv.DictReader(file, delimiter=',')

        for genre in genres:
            logging.info(genre)
            genre_to_save = Genre(
                id=genre['id'],
                name=genre['name'],
                slug=genre.get('slug'),
            )
            genre_to_save.save()

        logging.debug('Импортируется category.csv')
        with open('static/data/category.csv', 'r', encoding='utf-8') as file:
            categories = csv.DictReader(file, delimiter=',')

        for category in categories:
            logging.info(category)
            category_to_save = Category(
                id=category['id'],
                name=category['name'],
                slug=category.get('slug'),
            )
            category_to_save.save()

        logging.debug('Импортируется titles.csv')
        with open('static/data/titles.csv', 'r', encoding='utf-8') as file:
            titles = csv.DictReader(file, delimiter=',')

        for title in titles:
            logging.info(title)
            title_to_save = Title(
                id=title['id'],
                name=title['name'],
                year=title.get('year'),
                description=title.get('description'),
                category_id=title.get('category'),
            )
            title_to_save.save()

        logging.debug('Импортируется review.csv')
        with open('static/data/review.csv', 'r', encoding='utf-8') as file:
            reviews = csv.DictReader(file, delimiter=',')

        for review in reviews:
            logging.info(review)
            review_to_save = Review(
                id=review['id'],
                title_id=review['title_id'],
                author_id=review.get('author'),
                text=review.get('text'),
                score=review.get('score'),
                pub_date=review.get('pub_date'),
            )
            review_to_save.save()

        logging.debug('Импортируется comments.csv')
        with open('static/data/comments.csv', 'r', encoding='utf-8') as file:
            comments = csv.DictReader(file, delimiter=',')

        for comment in comments:
            logging.info(comment)
            comment_to_save = Comments(
                id=comment['id'],
                review_id=comment['review_id'],
                text=comment.get('text'),
                author_id=comment.get('author'),
                pub_date=comment.get('pub_date'),
            )
            comment_to_save.save()

        logging.debug('Импортируется genre_title.csv')
        with open(
            'static/data/genre_title.csv', 'r', encoding='utf-8') as file:
            title_genres = csv.DictReader(file, delimiter=',')

        for title_genre in title_genres:
            logging.info(title_genre)
            title_genre_to_save = TitleGenre(
                id=title_genre['id'],
                title_id=title_genre['title_id'],
                genre_id=title_genre['genre_id'],
            )
            title_genre_to_save.save()
