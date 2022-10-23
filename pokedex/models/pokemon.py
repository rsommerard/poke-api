from django.db.models import CharField, IntegerField, JSONField, ManyToManyField, Model


class Pokemon(Model):
    public_id = IntegerField(db_index=True)
    name = CharField(max_length=255, db_index=True)
    url = CharField(max_length=255)
    types = ManyToManyField("pokedex.Type", related_name="pokemons")
    json = JSONField()
