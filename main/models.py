from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()
class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    class Meta:
        ordering = ('name',)
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name

class Diet(models.Model):
    category = models.ForeignKey(Category, related_name='diets', on_delete=models.CASCADE)
    title = models.CharField('Название', max_length= 50)
    description = models.TextField('Описание', max_length=200)
    ccal = models.fields.IntegerField('Калорийность')
    protein = models.IntegerField('Белки')
    fat = models.IntegerField('Жиры')
    carbohydrate = models.IntegerField('Углеводы')
    picture = models.ImageField('Картинка', upload_to='img', default='')
    type = models.BooleanField('Тип', default=True)
    diet = models.PositiveSmallIntegerField('Рацион',default=0)

    def __str__(self):
        return self.title



class Cart(models.Model):
    owner = models.ForeignKey('Customer',verbose_name='Покупатель', on_delete=models.CASCADE, default=0)
    days = models.PositiveSmallIntegerField('Количество дней')
    type = models.BooleanField('Тип', default=True)
    diet = models.PositiveSmallIntegerField('Рацион', default=0)
    price = models.DecimalField('Цена', max_digits=6, decimal_places=2, default=0)
    def __str__(self):
        return self.id

class Customer(models.Model):

    user = models.ForeignKey(User,verbose_name='Пользователь', on_delete= models.CASCADE)
    bonus = models.PositiveSmallIntegerField('Скидка', default=0)
    def __str__(self):
        return "Покупатель: {}".format(self.user.username)
