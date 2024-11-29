from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse


class DishType(models.Model):
    name = models.CharField(max_length=255, unique=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return f"{self.name}"


class Cook(AbstractUser):
    years_of_experience = models.IntegerField(default=0)

    class Meta:
        verbose_name = "cook"
        verbose_name_plural = "cooks"

    def __str__(self):
        if self.years_of_experience == 1:
            experience_str = "1 year of experience"
        elif 2 <= self.years_of_experience <= 4:
            experience_str = f"{self.years_of_experience} years of experience"
        else:
            experience_str = f"{self.years_of_experience} years of experience"
        return f"{self.first_name} {self.last_name} ({experience_str})"


