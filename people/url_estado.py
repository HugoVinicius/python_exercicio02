from django.urls import path

from .views import estado_views as ev

urlpatterns = [
	path('', ev.home, name="index"),
	path('listar/', ev.listar, name="listar"),
	path('detalhar/<int:id_estado>/', ev.detalhar, name="detalhar"),
	path('excluir/<int:id_estado>/', ev.excluir, name="excluir"),
	path('cadastrar/', ev.cadastrar, name="cadastrar")
]