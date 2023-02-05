from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

USER = 'user'
MODERATOR = 'moderator'
ADMIN = 'admin'

ROLES = [
    (USER, 'Пользователь'),
    (MODERATOR, 'Модератор'),
    (ADMIN, 'Администратор'),
]


class User(AbstractUser):
    """Модель пользователей."""

    username = models.CharField(
        max_length=150,
        unique=True,
        verbose_name='Имя пользователя',
    )

    email = models.EmailField(
        max_length=254,
        unique=True,
        verbose_name='Электронная почта',
    )

    first_name = models.CharField(
        max_length=150,
        blank=True,
        verbose_name='Имя',
    )

    last_name = models.CharField(
        max_length=150,
        blank=True,
        verbose_name='Фамилия',
    )

    bio = models.TextField(
        max_length=500,
        blank=True,
        verbose_name='Информация о себе',
    )

    role = models.CharField(
        max_length=15,
        choices=ROLES,
        default=USER,
        verbose_name='Роль пользователя',
    )

    @property
    def is_user(self):
        return self.role == USER

    @property
    def is_admin(self):
        return self.role == ADMIN

    @property
    def is_moderator(self):
        return self.role == MODERATOR

    class Meta:
        ordering = ('id',)
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.username


class Category(models.Model):
    """Модель категорий произведений."""

    name = models.CharField(
        max_length=200,
        verbose_name='Категория',
    )

    slug = models.SlugField(
        unique=True,
        verbose_name='URL категории'
    )


    class Meta:
        ordering = ('name',)
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Genre(models.Model):
    """Модель жанров произведений."""

    name = models.CharField(
        max_length=200,
        verbose_name='Жанр произведения',
    )

    slug = models.SlugField(
        unique=True,
        verbose_name='URL жанра',
    )

    class Meta:
        ordering = ('name',)
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'

    def __str__(self):
        return self.name


class Title(models.Model):
    """Модель произведений."""

    name = models.CharField(
        max_length=250,
        verbose_name='Название произведения',
    )

    year = models.PositiveIntegerField(
        verbose_name='Год издания',
    )

    description = models.TextField(
        blank=True,
        verbose_name='Описание произведения',
    )

    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        related_name='titles',
        null=True,
        blank=True,
        verbose_name='Категория',
    )

    genre = models.ManyToManyField(
        Genre,
        related_name='titles',
        blank=True,
        verbose_name='Жанр',
    )

    class Meta:
        ordering = ('name',)
        verbose_name = 'Произведение'
        verbose_name_plural = 'Произведения'

    def __str__(self):
        return self.name

class Review(models.Model):
    """Модель отзыва."""

    title = models.ForeignKey(
        Title,
        on_delete=models.CASCADE,
        verbose_name='Отзыв',
        related_name='reviews',
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Автор',
        related_name='reviews',
    )
    text = models.TextField(max_length=250)
    pub_date = models.DateTimeField(
        auto_now_add=True,
        db_index=True,
        verbose_name='Дата публикации'
    )
    score = models.IntegerField(
        validators=[
            MinValueValidator(1),
            MaxValueValidator(10)
        ],
        null=True,
        verbose_name='Оценка'
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['author', 'title'], name='unique')
        ]

    def __str__(self):
        return self.text


class Comments(models.Model):
    """Модель комментария."""

    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Автор',
        related_name='comments',
    )
    text = models.TextField(max_length=250, verbose_name='Текст отзыва')
    review = models.ForeignKey(
        Review,
        on_delete=models.CASCADE,
        verbose_name='Отзыв',
        related_name='comments',
    )
    pub_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата публикации',
        db_index=True
    )

    class Meta:
        verbose_name = ('Комментарий',)
        verbose_name_plural = 'Комментарии'

    def __str__(self):
        return self.text
