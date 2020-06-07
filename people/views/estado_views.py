from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ObjectDoesNotExist

from ..models import Estado

@require_http_methods(["GET","POST"])
def home(request):
	return HttpResponse("Olá! seja bem vindo ao cadastro de Estado")

@csrf_exempt
@require_http_methods(["POST","GET"])
def listar(request):
	listaEstado = Estado.objects.all()
	html = "<ul>"
	for estado in listaEstado:
		html+=f"<li>{estado.nome}  prefeito:{estado.prefeito}(id={estado.id})</li>"
	html+= "</ul>"
	return HttpResponse(html)

def detalhar(request, id_estado):
	estado = Estado.objects.get(id=id_estado)
	return HttpResponse(f"Detalhou {estado.nome} prefeito:{estado.prefeito}(id={estado.id})")

def excluir(request, id_estado):
	try:
		estado = Estado.objects.get(id=id_estado)
		estado.delete()		
		return HttpResponse(f"Excluiu {estado.nome} prefeito:{estado.prefeito}(id={estado.id})")
	except ObjectDoesNotExist:
		return HttpResponse("Estado não encontrada")

def cadastrar(request):
	e = Estado(nome="Matheus", prefeito="Juninho Martins", codigo_ibge="1234567")
	e.save()
	return HttpResponse(f"{e.nome} cadastrado com sucesso (id={e.id})")