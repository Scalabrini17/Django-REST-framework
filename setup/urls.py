from django.contrib import admin
from django.urls import path, include
from escola.views import EstudanteViewsSet, CursoViewsSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('estudantes', EstudanteViewsSet, basename='Estudante')
router.register('cursos', CursoViewsSet, basename='Cursos')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls))
]
