from app.views import PessoaViewSets

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'', PessoaViewSets)
urlpatterns = router.urls