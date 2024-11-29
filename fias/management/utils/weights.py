from fias.config import weights
from fias.models import SocrBase


def rewrite_weights():
    SocrBase.objects.all().update(item_weight=64)

    for name, value in weights.items():
        SocrBase.objects.filter(scname=name).update(item_weight=value)
