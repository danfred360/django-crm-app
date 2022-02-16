from django.db import models

class Ingredient(models.Model):
    name = models.CharField(max_length=200)
    cost = models.DecimalField(max_digits=6, decimal_places=2)\

    def __str__(self):
        return str(self.name) + " -- $" + str(self.cost) 

class Meal(models.Model):
    name = models.CharField(max_length=200)
    ingredients = models.ManyToManyField(Ingredient)
    cost = models.DecimalField(max_digits=6, decimal_places=2)
    suggested_price = models.DecimalField(max_digits=6, decimal_places=2)
    ingredient_notes = models.TextField()
    preparation_notes = models.TextField()

    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        return reverse('meal-detail', args=[str(self.id)])

class OrderOfMeals(models.Model):
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

class Order(models.Model):
    meals_ordered = models.ManyToManyField(OrderOfMeals)
    client_name = models.CharField(max_length=200)
    notes = models.TextField()
