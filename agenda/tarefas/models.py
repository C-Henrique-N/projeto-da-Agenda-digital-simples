from django.db import models

class Tarefa(models.Model):
    titulo = models.CharField(max_length=100)
    descricao =models.TextField(blank=True)
    data = models.DateField()
    horario = models.TimeField()
    prioridade = models.CharField(max_length=20)
    concluida = models.BooleanField(default=False)

    def __str__(self):
        return self.titulo
