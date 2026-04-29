import sqlite3

def executar_driver():
    conexao = sqlite3.connect('db.sqlite3')
    cursor = conexao.cursor()
    print("\n--- INICIANDO TESTE VIA DRIVER (SQLITE3) ---")

    try:
        # A) Inserir uma atividade num projeto (Vamos inserir no projeto com ID 1)
        sql_insert = """
            INSERT INTO core_atividade (descricao, projeto_id) 
            VALUES ('Nova Atividade via Driver', 1);
        """
        cursor.execute(sql_insert)
        print("[OK] Nova atividade inserida com sucesso (Driver).")

        # B) Atualizar o líder de um projeto (Atualizar o responsável do projeto ID 1)
        sql_update = """
            UPDATE core_projeto 
            SET responsavel_id = 2 
            WHERE codigo = 1;
        """
        cursor.execute(sql_update)
        print("[OK] Líder do projeto atualizado com sucesso (Driver).")
        conexao.commit()

        # C) Listar todos os projetos e as suas atividades
        print("\n--- LISTA DE PROJETOS E ATIVIDADES (DRIVER) ---")
        sql_select = """
            SELECT p.nome, a.descricao 
            FROM core_projeto p
            LEFT JOIN core_atividade a ON p.codigo = a.projeto_id
            ORDER BY p.nome;
        """
        cursor.execute(sql_select)
        
        for linha in cursor.fetchall():
            nome_projeto = linha[0]
            desc_atividade = linha[1] if linha[1] else "Sem atividades"
            print(f"Projeto: {nome_projeto} | Atividade: {desc_atividade}")

    except sqlite3.Error as erro:
        print("Erro na base de dados:", erro)
    finally:
        if conexao:
            conexao.close()

if __name__ == '__main__':
    executar_driver()