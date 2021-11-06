from django.db import models
from django.utils import timezone
from datetime import datetime

from PIL import Image





class LogMessage(models.Model):
    message = models.CharField(max_length=300)
    log_date = models.DateTimeField("date logged")

    def __str__(self):
        """Returns a string representation of a message."""
        date = timezone.localtime(self.log_date)
        return f"'{self.message}' logged on {date.strftime('%A, %d %B, %Y at %X')}"


#**************
#1 Users
#2 Project
#3 Exercise
#4 Administrator
#**************

# Користувачі
#      - ім'я
#      - прізвище
#      - дата народження
#      - посада
#      - аватар (опціонально)  


class Users(models.Model):
    name = models.CharField('Имя',max_length=30)
    surname = models.CharField('Фамилия',max_length=30)
    birth = models.DateField('День рождения')
    position = models.CharField('Должность',max_length=30)
    avatar = models.ImageField(verbose_name="Фото" ,upload_to='logo_user',  max_length=100,null=True,)


# Проекти
#      - ім'я
#      - опис (для поля застосувати контент едітор, наприклад TinyMCE)
#      - строковий унікальний ідентифікатор (буде використовуватися в url PATH для перегляду проекту)


class Project(models.Model):
    name = models.CharField('Названия проекта',max_length=40)
    description = models.TextField('Описание',max_length=1000)


    def __str__(self):
        return self.name


# Задачи
#      - тема
#       - опис
#       - дата початку, дата закінчення завдання
#       - тип завдання (фіча, баг)
#       - пріоритет завдання (нормальний, високий, терміново)
#       - оцінений час в годинах
#       - масив коментарів до задачі
#       - виконавець (зв'язок з таблицею користувачі)
#       - автор (зв'язок з таблицею користувачі), значення встановлюється при створенні завдання, недоступно для редагування
#       - проект (зв'язок з таблицею проект)     


class Exercise(models.Model):
    FEATURE = 'FE'
    BAG = 'BA'
    TYPE_OF_EXERCISE = [
        (FEATURE, 'Feature'),
        (BAG, 'Bag'),
    ]
    type_of_exercise = models.CharField('Тип задания',max_length = 2, choices = TYPE_OF_EXERCISE, default = FEATURE )

    def is_upperclass(self):
        return self.type_of_exercise in {self.BAG}
    
    topic = models.CharField(max_length=40)
    description = models.TextField(max_length=2000)
    start_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateField()
    time = models.TimeField()
   



