from django.contrib import admin
from .models import Chocolate, Ingredient, Media, Quote

class IngredientInline(admin.TabularInline):
    model = Ingredient
    extra = 1

class MediaInline(admin.TabularInline):
    model = Media
    extra = 1

class ChocolateAdmin(admin.ModelAdmin):
    inlines = [IngredientInline, MediaInline]

admin.site.register(Chocolate, ChocolateAdmin)
admin.site.register(Quote)