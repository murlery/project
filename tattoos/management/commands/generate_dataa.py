import os
from django.core.management.base import BaseCommand
from faker import Faker
import random
from django.db import transaction
from django.contrib.auth.models import User


# ... импортируйте ваши модели из файла models.py ...
from tattoos.models import Style, Price, TattooStudio, TattooArtist, Tattoo


class Command(BaseCommand):
    def handle(self, *args, **options):
        fake = Faker('ru_RU')
        self.generate_data(fake)

    @transaction.atomic
    def generate_data(self, fake):
        num_styles = 100
        num_prices = 100
        num_studios = 100
        num_artists = 1000
        num_tattoos = 1000
        num_users = 100

        # 1. Стили
        styles = [Style(name=fake.word()) for _ in range(num_styles)]
        Style.objects.bulk_create(styles)

        # 2. Цены
        prices = [Price(name=f"{fake.random_int(min=500, max=50000)} руб.") for _ in range(num_prices)]
        Price.objects.bulk_create(prices)

        # 3. Тату студии
        studios = [TattooStudio(name=fake.company()) for _ in range(num_studios)]
        TattooStudio.objects.bulk_create(studios)

        # 4. Тату мастера
        artists = []
        for i in range(num_artists):
            studio = random.choice(list(TattooStudio.objects.all()))
            artists.append(TattooArtist(name=fake.name(), tattooStudio=studio))

        TattooArtist.objects.bulk_create(artists)

        # 5. Пользователи
        users = [User.objects.create_user(username=f"user_{i}", password='password') for i in range(num_users)]


        # 6. Татуировки
        tattoos = []
        for i in range(num_tattoos):
            style = random.choice(list(Style.objects.all()))
            price = random.choice(list(Price.objects.all()))
            artist = random.choice(list(TattooArtist.objects.all()))
            user = random.choice(users)
            tattoos.append(Tattoo(name=fake.word(), style=style, price=price, tattooArtist=artist, user=user))

            # Заглушка для изображения (замените на реальную генерацию изображений)
            image_path = os.path.join("media", "tattoos", f"tattoo_{i}.txt")
            with open(image_path, 'w') as f:
                pass
            tattoos[-1].picture.name = image_path

        Tattoo.objects.bulk_create(tattoos)

