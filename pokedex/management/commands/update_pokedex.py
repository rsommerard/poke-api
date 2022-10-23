import httpx
from django.core.management.base import BaseCommand

from pokedex.models import Pokemon, Type


class Command(BaseCommand):
    def handle(self, *args, **options):
        types = {}

        response = httpx.get("https://pokeapi.co/api/v2/type")
        json = response.json()

        for result in json["results"]:
            type, _ = Type.objects.get_or_create(name=result["name"])
            types[type.name] = type

        response = httpx.get("https://pokeapi.co/api/v2/pokemon/")
        pokemons = response.json()

        while pokemons["results"]:
            for pokemon in pokemons["results"]:
                response = httpx.get(pokemon["url"])
                detail = response.json()

                pokemon, _ = Pokemon.objects.get_or_create(
                    public_id=detail["id"],
                    name=detail["name"],
                    url=pokemon["url"],
                    json=detail,
                )

                for type in [slot["type"]["name"] for slot in detail["types"]]:
                    pokemon.types.add(types[type])

            if not pokemons["next"]:
                break

            response = httpx.get(pokemons["next"])
            pokemons = response.json()
