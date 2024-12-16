from django.contrib import admin

from tattoos.models import Style, Tattoo, Price, TattooArtist, TattooStudio

# Register your models here.


@admin.register(Tattoo)
class TattooAdmin(admin.ModelAdmin):
    list_display=['id','name', 'style','price','tattooArtist']

@admin.register(Style)
class StyleAdmin(admin.ModelAdmin):
    list_display = ["name"]

@admin.register(Price)
class StyleAdmin(admin.ModelAdmin):
    list_display = ["name"]

@admin.register(TattooArtist)
class TattooArtistAdmin(admin.ModelAdmin):
    list_display = ["name",'tattooStudio']

@admin.register(TattooStudio)
class TattooStudioAdmin(admin.ModelAdmin):
    list_display = ["name"]