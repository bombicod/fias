from django.db import models

from fias.fields import UUIDField

from .normdoc_kind import NDocKind
from .normdoc_type import NDocType

__all__ = ['NormDoc']


class NormDoc(models.Model):
    """
    Сведения по нормативному документу,
    являющемуся основанием присвоения адресному элементу наименования
    """

    class Meta:
        verbose_name = 'Нормативный документ'
        verbose_name_plural = 'Нормативные документы'

    name = models.TextField('Наименование документа', max_length=8000)
    date = models.DateField('Дата документа')
    number = models.CharField('Номер документа', max_length=150)
    type = models.ForeignKey(NDocType, on_delete=models.CASCADE, related_name='+',
                             verbose_name='Тип документа')
    kind = models.ForeignKey(NDocKind, on_delete=models.CASCADE, related_name='+',
                             verbose_name='Вид документа')

    updatedate = models.DateField('Дата обновления')
    orgname = models.CharField('Наименование органа, создавшего нормативный документ', max_length=255, blank=True)
    regnum = models.CharField('Номер государственной регистрации', max_length=100, blank=True)

    regdate = models.DateField('Дата государственной регистрации', blank=True, null=True)
    accdate = models.DateField('Дата вступления в силу нормативного документа', blank=True, null=True)

    comment = models.TextField('Комментарий', max_length=8000, blank=True)

    def __str__(self):
        return self.number
