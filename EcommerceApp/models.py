from django.db import models


class Slide(models.Model):
    title = models.CharField(max_length=50, blank=False,)
    name = models.CharField(max_length=30, blank=False)
    img = models.ImageField(upload_to='Slideimg', blank=False)

    def __str__(self):
        return self.name


class hedar(models.Model):
    name = models.CharField(max_length=50, blank=False)
    img = models.ImageField(upload_to='hedarimg')

    def __str__(self):
        return self.name


class newsletter(models.Model):
    img = models.ImageField(upload_to='newsletterimg')


class newArrivals(models.Model):
    name = models.CharField(max_length=50, blank=False)
    price = models.FloatField(blank=False)
    img = models.ImageField(upload_to='newArrivalsimg')

    def __str__(self):
        return self.name


class newArrivalsSecond(models.Model):
    name = models.CharField(max_length=50, blank=False)
    price = models.FloatField(blank=False)
    img = models.ImageField(upload_to='newArrivalsSecondimg',blank=False)

    def __str__(self):
        return self.name


class trending(models.Model):
    name = models.CharField(max_length=50, blank=False)
    price = models.FloatField(blank=False)
    img = models.ImageField(upload_to='trendingimg', blank=False)

    def __str__(self):
        return self.name


class trendingSecond(models.Model):
    name = models.CharField(max_length=50, blank=False)
    price = models.FloatField(blank=False)
    img = models.ImageField(upload_to='trendingSecondimg', blank=False)

    def __str__(self):
        return self.name


class TopRated(models.Model):
    name = models.CharField(max_length=50, blank=False)
    price = models.FloatField(blank=False)
    img = models.ImageField(upload_to='TopRatedimg', blank=False)

    def __str__(self):
        return self.name


class TopRatedSecond(models.Model):
    name = models.CharField(max_length=50, blank=False)
    price = models.FloatField(blank=False)
    img = models.ImageField(upload_to='TopRatedSecondimg', blank=False)

    def __str__(self):
        return self.name


class newProducts(models.Model):
    name = models.CharField(max_length=50, blank=False)
    price = models.FloatField(blank=False)
    Img = models.ImageField(upload_to='newProductimg', blank=False)
    secondImg = models.ImageField(blank=False)

    def __str__(self):
        return self.name
