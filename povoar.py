import os
import django

# Liga o script às configurações do seu projeto Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app.settings')
django.setup()

from core.models import Departamento, Funcionario, Projeto, Atividade

def povoar():
    print("A limpar a base de dados...")
    Atividade.objects.all().delete()
    Projeto.objects.all().delete()
    Funcionario.objects.all().delete()
    Departamento.objects.all().delete()

    print("A adicionar Departamentos e Funcionários...")
    dhc = Departamento.objects.create(sigla='DHC', descricao='Dep História')
    dct = Departamento.objects.create(sigla='DCT', descricao='Dep Computação')

    ana = Funcionario.objects.create(nome='Ana', sexo='F', salario=2500.00, depto=dhc)
    taciano = Funcionario.objects.create(nome='Taciano', sexo='M', salario=2500.00, depto=dct)
    
    dhc.gerente = ana
    dhc.save()
    dct.gerente = taciano
    dct.save()

    print("A adicionar Projetos...")
    apf = Projeto.objects.create(nome='APF', descricao='Analisador de Ponto de Função', depto=dct, responsavel=taciano)
    monitoria = Projeto.objects.create(nome='Monitoria', descricao='Projeto de Monitoria', depto=dhc, responsavel=ana)

    print("A adicionar Atividades...")
    Atividade.objects.create(descricao='APF - Atividade 1', projeto=apf)
    Atividade.objects.create(descricao='Monitoria - Atividade 1', projeto=monitoria)

    print("Base de dados povoada com sucesso!")

if __name__ == '__main__':
    povoar()