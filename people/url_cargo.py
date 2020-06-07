from django.urls import path

from .views import cargo_views as cv

urlpatterns = [
	path('', cv.home, name="index"),
	path('listar/', cv.listar, name="listar"),
	path('detalhar/<int:id_cargo>/', cv.detalhar, name="detalhar"),
	path('excluir/<int:id_cargo>/', cv.excluir, name="excluir"),
	path('cadastrar/', cv.cadastrar, name="cadastrar")
]