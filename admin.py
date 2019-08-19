from django.contrib import admin
from .models import Style, Malt, MaltWeight, HopAcid, Hop, HopAddition, Yeast, Recipe

@admin.register(Style)
class StyleAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    list_filter = ('name', )
    search_fields = ('name', )
    prepopulated_fields = {'slug': ('name', )}
    ordering = ('name', )

@admin.register(Malt)
class MaltAdmin(admin.ModelAdmin):
    list_display = ('name', 'lovibond', 'slug')
    list_filter = ('name', )
    search_fields = ('name', )
    prepopulated_fields = {'slug': ('name', 'lovibond', )}
    ordering = ('name', 'lovibond', )

admin.site.register(MaltWeight)
admin.site.register(HopAcid)

@admin.register(Hop)
class HopAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    list_filter = ('name', )
    search_fields = ('name', )
    prepopulated_fields = {'slug': ('name', )}
    ordering = ('name', '-alpha_acid', )

admin.site.register(HopAddition)

@admin.register(Yeast)
class YeastAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    list_filter = ('name', )
    search_fields = ('name', )
    prepopulated_fields = {'slug': ('name', )}
    ordering = ('name', )

@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ('style', 'name', 'slug')
    list_filter = ('style', 'name', )
    search_fields = ('name', )
    prepopulated_fields = {'slug': ('name', 'style', )}
    ordering = ('style', 'name', )