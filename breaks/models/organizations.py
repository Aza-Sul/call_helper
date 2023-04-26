from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Organization(models.Model):
    name = models.CharField('Название', max_length=255)
    director = models.ForeignKey(User, models.RESTRICT, 'organizations', verbose_name='Директор')
    employees = models.ManyToManyField(User, 'organization_employees', verbose_name='Сотрудники', blank=True)

    class Meta:
        verbose_name = 'Организация'
        verbose_name_plural = 'Организации'
        ordering = ('name',)

    def __str__(self):
        return f'{self.name}'
