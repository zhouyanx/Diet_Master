from django.db import models
from django.contrib.auth.models import User
import uuid


# Create your models here.
# class User(models.Model):
#     user_name = models.CharField(max_length=30)
#     user_password = models.CharField(max_length=30)
#     user_email = models.EmailField(max_length=45, null=True, blank=True)
class AccountAvatar(models.Model):
    user_id = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar_url = models.CharField(max_length=128)


class WellBeing(models.Model):
    user_id = models.OneToOneField(User, on_delete=models.CASCADE)
    height = models.DecimalField(max_digits=4, decimal_places=1)
    weight = models.DecimalField(max_digits=4, decimal_places=1)
    target_weight = models.DecimalField(max_digits=4, decimal_places=1)
    birthday = models.DateTimeField()
    age = models.IntegerField()
    ddl = models.DateTimeField(blank=True, null=True)


class Nutrients(models.Model):
    user_id = models.OneToOneField(User, on_delete=models.CASCADE)
    calorie = models.IntegerField()
    carbon = models.IntegerField()
    fat = models.IntegerField()
    protein = models.IntegerField()


class Ingredients(models.Model):
    ingredients_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=30)
    calorie = models.IntegerField()
    carbs = models.IntegerField()
    fat = models.IntegerField()
    protein = models.IntegerField()
    img_url = models.URLField()


class Recipes(models.Model):
    recipes_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    User_id = models.ForeignKey(User, on_delete=models.CASCADE)
    update_time = models.DateTimeField()


class LikeFood(models.Model):
    user_id = models.OneToOneField(User, on_delete=models.CASCADE)
    Ingredients_id = models.OneToOneField(Ingredients, on_delete=models.CASCADE)
    update_time = models.DateTimeField()


class DislikeFood(models.Model):
    user_id = models.OneToOneField(User, on_delete=models.CASCADE)
    Ingredients_id = models.OneToOneField(Ingredients, on_delete=models.CASCADE)
    update_time = models.DateTimeField()
