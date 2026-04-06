from django.db import models

#base

class UF(models.Model):
    sigla = models.CharField(max_length=2)
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.sigla

class Cidade(models.Model):
    nome = models.CharField(max_length=100)
    uf = models.ForeignKey(UF, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.nome} - {self.uf}"


class Ocupacao(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome


class AreaSaber(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome


class Turno(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome


class AvaliacaoTipo(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome


#rf01

class Pessoa(models.Model):
    nome = models.CharField(max_length=100)
    pai = models.CharField(max_length=100)
    mae = models.CharField(max_length=100)
    cpf = models.CharField(max_length=11)
    data_nasc = models.DateField()
    email = models.EmailField()

    cidade = models.ForeignKey(Cidade, on_delete=models.SET_NULL, null=True)
    ocupacao = models.ForeignKey(Ocupacao, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.nome


#heranca
class Aluno(Pessoa):
    pass


class Professor(Pessoa):
    pass


#rf03

class InstituicaoEnsino(models.Model):
    nome = models.CharField(max_length=100)
    site = models.URLField()
    telefone = models.CharField(max_length=20)

    cidade = models.ForeignKey(Cidade, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.nome


#rf05

class Curso(models.Model):
    nome = models.CharField(max_length=100)
    carga_horaria_total = models.IntegerField()
    duracao_meses = models.IntegerField()

    area_saber = models.ForeignKey(AreaSaber, on_delete=models.SET_NULL, null=True)
    instituicao = models.ForeignKey(InstituicaoEnsino, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.nome


#rf06

class Turma(models.Model):
    nome = models.CharField(max_length=50)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, null=True)
    turno = models.ForeignKey(Turno, on_delete=models.SET_NULL, null=True)

    alunos = models.ManyToManyField(Aluno, blank=True)

    def __str__(self):
        return self.nome


#rf07

class Disciplina(models.Model):
    nome = models.CharField(max_length=100)
    area_saber = models.ForeignKey(AreaSaber, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.nome


#rf08
class Matricula(models.Model):
    instituicao = models.ForeignKey(InstituicaoEnsino, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)

    data_inicio = models.DateField()
    data_previsao_termino = models.DateField()

    def __str__(self):
        return f"{self.aluno} - {self.curso}"


#rf09

class Avaliacao(models.Model):
    descricao = models.CharField(max_length=200)

    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE)
    tipo = models.ForeignKey(AvaliacaoTipo, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.descricao


#rf10

class Frequencia(models.Model):
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE)
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)

    numero_faltas = models.IntegerField()

    def __str__(self):
        return f"{self.aluno} - {self.disciplina}"


#rf13
class Ocorrencia(models.Model):
    descricao = models.TextField()
    data = models.DateField()

    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE)
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)

    def __str__(self):
        return self.descricao


#rf14

class CursoDisciplina(models.Model):
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE)

    carga_horaria = models.IntegerField()
    periodo = models.IntegerField()

    def __str__(self):
        return f"{self.curso} - {self.disciplina}"