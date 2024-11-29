from django.db.models import Model


class FakeModel(Model):
    class Meta:
        app_label = 'nofias'


class FakeModel2(Model):
    class Meta:
        app_label = 'nofias'
