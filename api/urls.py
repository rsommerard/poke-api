from rest_framework.routers import SimpleRouter

from api.views.pokemon import PokemonViewSet

router = SimpleRouter()
router.register(r"pokemon", PokemonViewSet, basename="pokemon")

urlpatterns = router.urls
