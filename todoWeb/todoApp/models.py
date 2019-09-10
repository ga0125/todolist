from django.db import models

class Todo(models.Model):
    title = models.CharField(max_length=80) #Parâmetro do campo titulo criado e configurado para 80 caracteres
    desc = models.CharField(max_length=200) # Parâmetro do campo descrição criado e configurado para 200 caracteres
    deadline = models.DateField(blank=True, null=True)
    complete = models.BooleanField(default=False)
    completed_at = models.DateTimeField(blank=True, null=True)
    def __str__(self):
        template = '{0.title} {0.desc} {0.deadline}'
        return template.format(self)