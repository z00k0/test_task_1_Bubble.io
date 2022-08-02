from django.db import models


class Automobile(models.Model):
    BMW = 'BMW'
    Audi = 'Audi'
    Mercedes = 'Mercedes'
    BRANDS = (
        (None, 'Выберите модель автомобиля'),
        (BMW, BMW),
        (Audi, Audi),
        (Mercedes, Mercedes)
    )
    model = models.CharField(max_length=100)
    brand = models.CharField(max_length=10, choices=BRANDS)
    photo = models.ImageField(upload_to='uploaded_photo')
