from rest_framework import status
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ReadOnlyModelViewSet

from api.serializers import PokemonSerializer
from pokedex.models import Pokemon


class PokemonViewSet(ReadOnlyModelViewSet):
    permission_classes = [IsAuthenticated]
    pagination_class = LimitOffsetPagination
    serializer_class = PokemonSerializer

    def get_queryset(self):
        groups = self.request.user.token.payload["groups"]
        return Pokemon.objects.filter(types__name__in=groups)

    def retrieve(self, request, *args, **kwargs):
        identifier = kwargs["pk"]
        queryset = self.get_queryset()

        try:
            pokemon = (
                queryset.get(public_id=identifier)
                if identifier.isdigit()
                else queryset.get(name=identifier)
            )
        except Pokemon.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        return Response(pokemon.json)
