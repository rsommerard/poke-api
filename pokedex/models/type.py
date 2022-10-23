from django.db.models import CharField, Model


class Type(Model):
    name = CharField(max_length=255, db_index=True, unique=True)
