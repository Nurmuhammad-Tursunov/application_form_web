from django.db import models


class Region(models.Model):
    name = models.CharField(max_length=255)
    objects = models.Manager()
    def __str__(self): return self.name


class Position(models.Model):
    name = models.CharField(max_length=255)
    deleted = models.BooleanField(default=False)
    objects = models.Manager()
    def __str__(self): return self.name


class Degree(models.Model):
    name = models.CharField(max_length=255)
    objects = models.Manager()
    def __str__(self): return self.name


class Family(models.Model):
    name = models.CharField(max_length=255)
    objects = models.Manager()
    def __str__(self): return self.name


class ComputerScience(models.Model):
    name = models.CharField(max_length=255)
    objects = models.Manager()
    def __str__(self): return self.name


class Application(models.Model):
    city = models.CharField(max_length=255, null=True, default="-")
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)
    date_of_birth = models.DateField(null=True, default="01.01.1900")
    appeal = models.CharField(max_length=255, null=True, blank=True, default="-")
    position = models.CharField(max_length=255, null=True, blank=True, default="-")
    # position = models.ForeignKey(Position, on_delete=models.CASCADE, related_name="applications_by_position", null=True)
    degree = models.CharField(max_length=255, null=True, blank=True, default="-")
    # degree = models.ForeignKey(Degree, on_delete=models.CASCADE, related_name="applications_by_degree", null=True)
    address = models.CharField(max_length=500, null=True, default="-")
    language_ru = models.CharField(max_length=500, null=True, default="-")
    computer_science = models.CharField(max_length=255, null=True, blank=True, default="-")
    # computer_science = models.ForeignKey(ComputerScience, on_delete=models.CASCADE,
    #                                      related_name="applications_by_computer_science", null=True, blank=True)
    photo = models.FileField(upload_to="images", null=True)
    date_time = models.DateTimeField(auto_created=True, auto_now_add=True)
    objects = models.Manager()

    def __str__(self): return self.first_name
