from django.db import models
from django.urls import reverse


class Style(models.Model):
    name = models.CharField(max_length = 100)
    slug = models.SlugField(max_length = 100, unique = True)
    description = models.TextField(blank = True, null = True)

    class Meta:
        ordering = ('name', )

    def get_absolute_url(self):
        return reverse('brew:style', args = [self.slug, ])

    def __str__(self):
        return self.name

class Malt(models.Model):
    name = models.CharField(max_length = 100)
    slug = models.SlugField(max_length = 100,  unique = True)
    description = models.TextField(blank = True, null = True)
    lovibond = models.SmallIntegerField(blank = True, null = True)

    class Meta:
        ordering = ('name', '-lovibond', )

    def get_absolute_url(self):
        return reverse('brew:malt', args = [self.slug, ])

    def __str__(self):
        if self.lovibond:
            return self.name + ' ' + str(self.lovibond) + 'L'
        else:
            return self.name

class HopAcid(models.Model):
    alpha_acid = models.DecimalField(max_digits = 3, decimal_places = 1, blank = True, null = True)

    class Meta:
        ordering = ('-alpha_acid', )

    def __str__(self):
        return str(self.alpha_acid)

class Hop(models.Model):
    name = models.CharField(max_length = 100)
    slug = models.SlugField(max_length = 100, unique = True)
    description = models.TextField(blank = True, null = True)
    alpha_acid = models.ForeignKey(HopAcid, blank = True, null = True, on_delete = models.CASCADE)

    class Meta:
        ordering = ('name', '-alpha_acid', )

    def get_absolute_url(self):
        return reverse('brew:hop', args = [self.slug, ])

    def __str__(self):
        if self.alpha_acid:
            return str(self.alpha_acid) + '% ' + self.name
        else:
            return self.name

class Yeast(models.Model):
    name = models.CharField(max_length = 100)
    slug = models.SlugField(max_length = 100, unique = True)
    description = models.TextField(blank = True, null = True)

    class Meta:
        ordering = ('name', )

    def __str__(self):
        return self.name

class Recipe(models.Model):
    style = models.ForeignKey(Style, related_name = 'recipes', on_delete = models.CASCADE)
    name = models.CharField(max_length = 100, blank = True, null = True)
    slug = models.SlugField(max_length = 100, unique = True)
    description = models.TextField(blank = True, null = True)
    batch_size = models.DecimalField(max_digits = 6, decimal_places = 2)
    boil_size = models.DecimalField(max_digits = 6, decimal_places = 2)
    original_gravity = models.DecimalField(max_digits = 4, decimal_places = 3)
    final_gravity = models.DecimalField(max_digits = 4, decimal_places = 3)

    CELCIUS = 'C'
    FAHRENHEIT = 'F'
    KELVIN = 'K'
    UNIT_CHOICES = [(CELCIUS, 'celcius'), (FAHRENHEIT, 'fahrenheit'), (KELVIN, 'kelvin')]
    mash_temperature = models.SmallIntegerField(default = 152)
    unit = models.CharField(max_length = 1, choices = UNIT_CHOICES, default = FAHRENHEIT)

    special_instructions = models.TextField(blank = True, null = True)


    yeast = models.ForeignKey(Yeast, related_name = 'recipes', on_delete = models.CASCADE)

    class Meta:
        ordering = ('style', 'name', )

    def __str__(self):
        if self.name:
            return self.name + ' ' + self.style.name
        else:
            return self.style.name

class MaltWeight(models.Model):
    malt = models.ForeignKey(Malt, related_name = 'malt_weights', on_delete = models.CASCADE)
    weight = models.DecimalField(max_digits = 7, decimal_places = 3)

    POUNDS = 'lb'
    OUNCES = 'oz'
    UNIT_CHOICES = [(POUNDS, 'pounds'), (OUNCES, 'ounces')]
    unit = models.CharField(max_length = 2, choices = UNIT_CHOICES, default = POUNDS)

    recipe = models.ForeignKey(Recipe, related_name = 'malt_weights', on_delete = models.CASCADE)

    class Meta:
        ordering = ('-weight', 'malt', )

    def __str__(self):
        return str(self.weight) + ' ' + self.unit + '. ' + str(self.malt)

class HopAddition(models.Model):
    hop = models.ForeignKey(Hop, related_name = 'hop_additions', on_delete = models.CASCADE)
    weight = models.DecimalField(max_digits = 4, decimal_places = 1)

    GRAMS = 'g'
    OUNCES = 'oz'
    UNIT_CHOICES = [(GRAMS, 'grams'), (OUNCES, 'ounces')]
    unit = models.CharField(max_length = 2, choices = UNIT_CHOICES, default = GRAMS)

    duration = models.SmallIntegerField()
    recipe = models.ForeignKey(Recipe, related_name = 'hop_additions', on_delete = models.CASCADE)

    class Meta:
        ordering = ('-duration', 'hop', )

    def __str__(self):
        return str(self.weight) + self.unit + ' ' + str(self.hop) + ' ' + str(self.duration) + ' min.'
