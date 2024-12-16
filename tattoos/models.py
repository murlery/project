from django.db import models 

# Create your models here.
class Style(models.Model):
    name = models.TextField("Название стиля")
    class Meta:
        verbose_name = "Стиль"
        verbose_name_plural = "Стили"
    def __str__(self) -> str:
        return self.name
    
class Price(models.Model):
    name = models.TextField("Цена")
    class Meta:
        verbose_name = "Цена"
        verbose_name_plural = "Цены"
    def __str__(self) -> str:
        return self.name

class TattooStudio(models.Model):
    name = models.TextField("Тату студия")
    class Meta:
        verbose_name = "Тату студия"
        verbose_name_plural = "Тату студии"
    def __str__(self) -> str:
        return self.name

class TattooArtist(models.Model):
    name = models.TextField("Тату мастер")
    tattooStudio = models.ForeignKey("TattooStudio",on_delete=models.CASCADE,null=True )
    picture = models.ImageField("Изображение", null=True, upload_to="tattooArtists")
    class Meta:
        verbose_name = "Тату мастер"
        verbose_name_plural = "Тату мастера"
    def __str__(self) -> str:
        return self.name
    
class Tattoo(models.Model):
    name = models.TextField("Название")
    style = models.ForeignKey("Style", on_delete=models.CASCADE,null=True)
    price = models.ForeignKey("Price", on_delete=models.CASCADE,null=True)
    # добавим ImageField, в upload_to указываем папку куда загружать файл
    picture = models.ImageField("Изображение", null=True, upload_to="tattoos")
    tattooArtist = models.ForeignKey("TattooArtist", on_delete=models.CASCADE,null=True)
    user = models.ForeignKey("auth.User", verbose_name="Пользователь",on_delete=models.CASCADE,null = True)
    class Meta:
        verbose_name = "Татуировка"
        verbose_name_plural = "Татуировки"

