from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ObjectDoesNotExist

from ..models import Cargo


@require_http_methods(["GET","POST"])
def home(request):
	return HttpResponse("Olá, Cadastro de Cargo!")

@csrf_exempt
@require_http_methods(["POST","GET"])
def listar(request):
	CargoList = Cargo.objects.all()
	html = "<ul>"
	for c in CargoList:
		html+=f"<li>{c.nome} (id={c.id})</li>"
	html+= "</ul>"
	return HttpResponse(html)

def detalhar(request, id_cargo):
	cargo = Cargo.objects.get(id=id_cargo)
	return HttpResponse(f"Detalhou {cargo.nome} (id={cargo.id})")

def excluir(request, id_cargo):
	try:
		cargo = Cargo.objects.get(id=id_cargo)
		cargo.delete()		
		return HttpResponse(f"Excluiu {cargo.nome} (id={cargo.id})")
	except ObjectDoesNotExist:
		return HttpResponse("Cargo não encontrada")

def cadastrar(request):
	c = Cargo(nome="Atendente", salario=1500)
	c.save()
	return HttpResponse(f"{c.nome} cadastrado com sucesso (id={c.id})")