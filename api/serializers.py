from rest_framework.serializers import ModelSerializer

from pokedex.models import Pokemon


class PokemonSerializer(ModelSerializer):
    class Meta:
        model = Pokemon
        fields = ["url", "name"]
