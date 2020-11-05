from django.contrib.auth.models import User
from django.db import models
from projeto.core.models import TimeStampedModel
from projeto.produto.models import Produto


MOVIMENTO = (
	('e', 'entrada'),
	('s', 'saida'),
)


class Estoque(TimeStampedModel):
	funcionario = models.ForeignKey(User, on_delete = models.CASCADE)
	nf = models.PositiveIntegerField('nota fiscal', null = true, blank = true)
	movimento = models.CharField(max_length = 1, choices = MOVIMENTO)

	class Meta:
		ordering = ('-created',)

		def _str_(self):
			return srt(self.pk)

class EstoqueItens(models.model):
	estoque = models.ForeignKey(Estoque, on_delete = models.CASCADE)
	produto = models.ForeignKey(Estoque, on_delete = models.CASCADE)
	quantidade = models.PositiveIntegerField()
	saldo = models.PositiveIntegerField()

	class Meta:
			ordering = ('pk',)

	def _str_(self):
		return '{} - {} - {}'.format(self.pk, self.estoque.pk, self.produto)


