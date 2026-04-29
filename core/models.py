from django.db import models

class Departamento(models.Model):
    codigo = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100, null=True, blank=True)
    sigla = models.CharField(max_length=10, unique=True)
    descricao = models.CharField(max_length=250, null=True, blank=True)
    # Usamos related_name para evitar conflito, pois Funcionario também tem ForeignKey para Departamento
    gerente = models.ForeignKey('Funcionario', on_delete=models.SET_NULL, null=True, blank=True, related_name='departamentos_gerenciados')

    def __str__(self):
        return self.sigla

class Funcionario(models.Model):
    codigo = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=150)
    sexo = models.CharField(max_length=1)
    dt_nasc = models.DateField(null=True, blank=True)
    salario = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    supervisor = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True)
    depto = models.ForeignKey(Departamento, on_delete=models.SET_NULL, null=True, blank=True, related_name='funcionarios')

    def __str__(self):
        return self.nome

class Projeto(models.Model):
    codigo = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=50, unique=True)
    descricao = models.CharField(max_length=250, null=True, blank=True)
    responsavel = models.ForeignKey(Funcionario, on_delete=models.SET_NULL, null=True, blank=True)
    depto = models.ForeignKey(Departamento, on_delete=models.SET_NULL, null=True, blank=True)
    data_inicio = models.DateField(null=True, blank=True)
    data_fim = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.nome

class Atividade(models.Model):
    codigo = models.AutoField(primary_key=True)
    descricao = models.CharField(max_length=250)
    projeto = models.ForeignKey(Projeto, on_delete=models.SET_NULL, null=True, blank=True)
    data_inicio = models.DateField(null=True, blank=True)
    data_fim = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.descricao
