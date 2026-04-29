import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app.settings')
django.setup()

from core.models import Projeto, Atividade, Funcionario

def executar_orm():
    print("\n--- INICIANDO TESTE VIA ORM (DJANGO) ---")
    
    # A) Inserir uma atividade num projeto
    projeto_alvo = Projeto.objects.first() 
    Atividade.objects.create(
        descricao='Nova Atividade via ORM',
        projeto=projeto_alvo
    )
    print("[OK] Nova atividade inserida com sucesso (ORM).")

    # B) Atualizar o líder de algum projeto
    novo_lider = Funcionario.objects.last() 
    projeto_alvo.responsavel = novo_lider
    projeto_alvo.save()
    print("[OK] Líder do projeto atualizado com sucesso (ORM).")

    # C) Listar todos os projetos e as suas atividades
    print("\n--- LISTA DE PROJETOS E ATIVIDADES (ORM) ---")
    projetos = Projeto.objects.all().order_by('nome')
    
    for proj in projetos:
        print(f"Projeto: {proj.nome}")
        # O Django permite procurar as atividades ligadas a este projeto facilmente
        atividades = proj.atividade_set.all() 
        if atividades.exists():
            for ativ in atividades:
                print(f"  - {ativ.descricao}")
        else:
            print("  - Sem atividades")

if __name__ == '__main__':
    executar_orm()