from django.db import models

class CoreModel(models.Model):

    name = models.CharField(
        max_length=100,
    )

    cpf = models.CharField(
        max_length=11,
        default="",
    )

    def __str__(self) -> str:
        return f'nome: {self.name}, cpf: {self.cpf}'