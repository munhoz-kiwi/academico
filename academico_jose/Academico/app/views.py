from django.shortcuts import render
from .models import *


def home(request):
    return render(request, 'academico/home.html')

# PESSOAS


def lista_pessoas(request):
    pessoas = Pessoa.objects.all()
    return render(request, 'academico/pessoas.html', {'pessoas': pessoas})


def lista_alunos(request):
    alunos = Aluno.objects.all()
    return render(request, 'academico/alunos.html', {'alunos': alunos})


def lista_professores(request):
    professores = Professor.objects.all()
    return render(request, 'academico/professores.html', {'professores': professores})


# BASES
def lista_ufs(request):
    ufs = UF.objects.all()
    return render(request, 'academico/ufs.html', {'ufs': ufs})


def lista_cidades(request):
    cidades = Cidade.objects.all()
    return render(request, 'academico/cidades.html', {'cidades': cidades})


def lista_ocupacoes(request):
    ocupacoes = Ocupacao.objects.all()
    return render(request, 'academico/ocupacoes.html', {'ocupacoes': ocupacoes})


def lista_areas_saber(request):
    areas = AreaSaber.objects.all()
    return render(request, 'academico/areas.html', {'areas': areas})


def lista_turnos(request):
    turnos = Turno.objects.all()
    return render(request, 'academico/turnos.html', {'turnos': turnos})


# INSTITUIÇÃO / CURSO

def lista_instituicoes(request):
    instituicoes = InstituicaoEnsino.objects.all()
    return render(request, 'academico/instituicoes.html', {'instituicoes': instituicoes})


def lista_cursos(request):
    cursos = Curso.objects.all()
    return render(request, 'academico/cursos.html', {'cursos': cursos})


def lista_turmas(request):
    turmas = Turma.objects.all()
    return render(request, 'academico/turmas.html', {'turmas': turmas})


# DISCIPLINAS

def lista_disciplinas(request):
    disciplinas = Disciplina.objects.all()
    return render(request, 'academico/disciplinas.html', {'disciplinas': disciplinas})


def lista_curso_disciplinas(request):
    curso_disciplinas = CursoDisciplina.objects.all()
    return render(request, 'academico/curso_disciplinas.html', {'curso_disciplinas': curso_disciplinas})


# MATRÍCULAS

def lista_matriculas(request):
    matriculas = Matricula.objects.all()
    return render(request, 'academico/matriculas.html', {'matriculas': matriculas})


# AVALIAÇÕES

def lista_avaliacoes(request):
    avaliacoes = Avaliacao.objects.all()
    return render(request, 'academico/avaliacoes.html', {'avaliacoes': avaliacoes})


def lista_tipos_avaliacao(request):
    tipos = AvaliacaoTipo.objects.all()
    return render(request, 'academico/tipos_avaliacao.html', {'tipos': tipos})


# FREQUÊNCIA

def lista_frequencias(request):
    frequencias = Frequencia.objects.all()
    return render(request, 'academico/frequencias.html', {'frequencias': frequencias})


# OCORRÊNCIAS

def lista_ocorrencias(request):
    ocorrencias = Ocorrencia.objects.all()
    return render(request, 'academico/ocorrencias.html', {'ocorrencias': ocorrencias})
