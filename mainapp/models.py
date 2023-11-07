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
    region = models.ForeignKey(Region, on_delete=models.CASCADE, related_name="applications_by_region")
    city = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    # father_name = models.CharField(max_length=255, null=True, blank=True)
    phone_number = models.CharField(max_length=255)
    # phone_number2 = models.CharField(max_length=255, null=True, blank=True)
    date_of_birth = models.DateField()
    appeal = models.CharField(max_length=255, null=True, blank=True)
    position = models.ForeignKey(Position, on_delete=models.CASCADE, related_name="applications_by_position")
    # degree = models.ForeignKey(Degree, on_delete=models.CASCADE, related_name="applications_by_degree")
    # university = models.CharField(max_length=255, null=True, blank=True)
    family = models.ForeignKey(Family, on_delete=models.CASCADE, null=True, related_name="applications_by_family")
    address = models.CharField(max_length=500)
    # languages = models.CharField(max_length=255)
    last_work = models.CharField(max_length=255)
    last_position = models.CharField(max_length=255)
    work_time = models.CharField(max_length=255)
    computer_science = models.ForeignKey(ComputerScience, on_delete=models.CASCADE,
                                         related_name="applications_by_computer_science", null=True, blank=True)
    about = models.CharField(max_length=1000, null=True, blank=True)
    # photo = models.ImageField(upload_to="images")
    photo = models.FileField(upload_to="images")
    date_time = models.DateTimeField(auto_created=True, auto_now_add=True)
    objects = models.Manager()

    def __str__(self): return self.first_name
