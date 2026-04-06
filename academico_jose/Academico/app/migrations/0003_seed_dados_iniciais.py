from datetime import date

from django.db import migrations


def seed_models(apps, schema_editor):
    UF = apps.get_model("app", "UF")
    Cidade = apps.get_model("app", "Cidade")
    Ocupacao = apps.get_model("app", "Ocupacao")
    AreaSaber = apps.get_model("app", "AreaSaber")
    Turno = apps.get_model("app", "Turno")
    AvaliacaoTipo = apps.get_model("app", "AvaliacaoTipo")
    Pessoa = apps.get_model("app", "Pessoa")
    Aluno = apps.get_model("app", "Aluno")
    Professor = apps.get_model("app", "Professor")
    InstituicaoEnsino = apps.get_model("app", "InstituicaoEnsino")
    Curso = apps.get_model("app", "Curso")
    Turma = apps.get_model("app", "Turma")
    Disciplina = apps.get_model("app", "Disciplina")
    Matricula = apps.get_model("app", "Matricula")
    Avaliacao = apps.get_model("app", "Avaliacao")
    Frequencia = apps.get_model("app", "Frequencia")
    Ocorrencia = apps.get_model("app", "Ocorrencia")
    CursoDisciplina = apps.get_model("app", "CursoDisciplina")

    ufs = []
    for sigla, nome in [
        ("SP", "Sao Paulo"),
        ("RJ", "Rio de Janeiro"),
        ("MG", "Minas Gerais"),
        ("BA", "Bahia"),
        ("PR", "Parana"),
    ]:
        ufs.append(UF.objects.create(sigla=sigla, nome=nome))

    cidades = []
    for i, nome in enumerate(["Campinas", "Niteroi", "Belo Horizonte", "Salvador", "Curitiba"]):
        cidades.append(Cidade.objects.create(nome=nome, uf=ufs[i]))

    ocupacoes = []
    for nome in ["Estudante", "Professor", "Pesquisador", "Coordenador", "Analista"]:
        ocupacoes.append(Ocupacao.objects.create(nome=nome))

    areas = []
    for nome in ["Computacao", "Matematica", "Fisica", "Biologia", "Engenharia"]:
        areas.append(AreaSaber.objects.create(nome=nome))

    turnos = []
    for nome in ["Manha", "Tarde", "Noite", "Integral", "EAD"]:
        turnos.append(Turno.objects.create(nome=nome))

    tipos = []
    for nome in ["Prova", "Trabalho", "Seminario", "Projeto", "Exercicio"]:
        tipos.append(AvaliacaoTipo.objects.create(nome=nome))

    pessoas = []
    for i in range(5):
        pessoas.append(
            Pessoa.objects.create(
                nome=f"Pessoa {i + 1}",
                pai=f"Pai {i + 1}",
                mae=f"Mae {i + 1}",
                cpf=f"0000000000{i + 1}",
                data_nasc=date(1990 + i, 1 + i, 10 + i),
                email=f"pessoa{i + 1}@academico.local",
                cidade=cidades[i],
                ocupacao=ocupacoes[i],
            )
        )

    alunos = []
    for i in range(5):
        alunos.append(
            Aluno.objects.create(
                nome=f"Aluno {i + 1}",
                pai=f"Pai Aluno {i + 1}",
                mae=f"Mae Aluno {i + 1}",
                cpf=f"1000000000{i + 1}",
                data_nasc=date(2000 + i, 2, 5 + i),
                email=f"aluno{i + 1}@academico.local",
                cidade=cidades[i],
                ocupacao=ocupacoes[0],
            )
        )

    for i in range(5):
        Professor.objects.create(
            nome=f"Professor {i + 1}",
            pai=f"Pai Professor {i + 1}",
            mae=f"Mae Professor {i + 1}",
            cpf=f"2000000000{i + 1}",
            data_nasc=date(1980 + i, 3, 8 + i),
            email=f"professor{i + 1}@academico.local",
            cidade=cidades[i],
            ocupacao=ocupacoes[1],
        )

    instituicoes = []
    for i in range(5):
        instituicoes.append(
            InstituicaoEnsino.objects.create(
                nome=f"Instituicao {i + 1}",
                site=f"https://instituicao{i + 1}.edu.br",
                telefone=f"(11) 3000-000{i + 1}",
                cidade=cidades[i],
            )
        )

    cursos = []
    for i in range(5):
        cursos.append(
            Curso.objects.create(
                nome=f"Curso {i + 1}",
                carga_horaria_total=1600 + (i * 200),
                duracao_meses=24 + (i * 6),
                area_saber=areas[i],
                instituicao=instituicoes[i],
            )
        )

    disciplinas = []
    for i in range(5):
        disciplinas.append(
            Disciplina.objects.create(
                nome=f"Disciplina {i + 1}",
                area_saber=areas[i],
            )
        )

    turmas = []
    for i in range(5):
        turma = Turma.objects.create(
            nome=f"Turma {i + 1}",
            curso=cursos[i],
            turno=turnos[i],
        )
        turma.alunos.add(alunos[i])
        turmas.append(turma)

    for i in range(5):
        CursoDisciplina.objects.create(
            curso=cursos[i],
            disciplina=disciplinas[i],
            carga_horaria=60 + (i * 10),
            periodo=i + 1,
        )

    for i in range(5):
        Matricula.objects.create(
            instituicao=instituicoes[i],
            curso=cursos[i],
            aluno=alunos[i],
            data_inicio=date(2026, 1, 10 + i),
            data_previsao_termino=date(2028 + i, 12, 15),
        )

    for i in range(5):
        Avaliacao.objects.create(
            descricao=f"Avaliacao {i + 1}",
            curso=cursos[i],
            disciplina=disciplinas[i],
            tipo=tipos[i],
        )

    for i in range(5):
        Frequencia.objects.create(
            curso=cursos[i],
            disciplina=disciplinas[i],
            aluno=alunos[i],
            numero_faltas=i,
        )

    for i in range(5):
        Ocorrencia.objects.create(
            descricao=f"Ocorrencia {i + 1}",
            data=date(2026, 3, 1 + i),
            curso=cursos[i],
            disciplina=disciplinas[i],
            pessoa=pessoas[i],
        )


def unseed_models(apps, schema_editor):
    model_names = [
        "Ocorrencia",
        "Frequencia",
        "Avaliacao",
        "Matricula",
        "CursoDisciplina",
        "Turma",
        "Disciplina",
        "Curso",
        "InstituicaoEnsino",
        "Professor",
        "Aluno",
        "Pessoa",
        "AvaliacaoTipo",
        "Turno",
        "AreaSaber",
        "Ocupacao",
        "Cidade",
        "UF",
    ]
    for model_name in model_names:
        apps.get_model("app", model_name).objects.all().delete()


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0002_uf_alter_cidade_uf"),
    ]

    operations = [
        migrations.RunPython(seed_models, unseed_models),
    ]
