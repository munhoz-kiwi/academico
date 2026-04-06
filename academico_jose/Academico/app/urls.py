from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    path('ufs/', views.lista_ufs, name='ufs'),
    path('pessoas/', views.lista_pessoas, name='pessoas'),
    path('alunos/', views.lista_alunos, name='alunos'),
    path('professores/', views.lista_professores, name='professores'),

    path('cidades/', views.lista_cidades, name='cidades'),
    path('ocupacoes/', views.lista_ocupacoes, name='ocupacoes'),
    path('areas/', views.lista_areas_saber, name='areas'),
    path('turnos/', views.lista_turnos, name='turnos'),

    path('instituicoes/', views.lista_instituicoes, name='instituicoes'),
    path('cursos/', views.lista_cursos, name='cursos'),
    path('turmas/', views.lista_turmas, name='turmas'),

    path('disciplinas/', views.lista_disciplinas, name='disciplinas'),
    path('curso-disciplinas/', views.lista_curso_disciplinas, name='curso_disciplinas'),

    path('matriculas/', views.lista_matriculas, name='matriculas'),
    path('avaliacoes/', views.lista_avaliacoes, name='avaliacoes'),
    path('tipos-avaliacao/', views.lista_tipos_avaliacao, name='tipos_avaliacao'),

    path('frequencias/', views.lista_frequencias, name='frequencias'),
    path('ocorrencias/', views.lista_ocorrencias, name='ocorrencias'),
]
