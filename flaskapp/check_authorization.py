#!/usr/bin/env python3
"""
Script para verificar os valores de autorização na base de dados
"""

from app import app, db, Aluno

def check_autorization_values():
    print("Verificando valores de autorização na base de dados...")
    
    with app.app_context():
        alunos = Aluno.query.all()
        
        print(f"\nEncontrados {len(alunos)} alunos:")
        print("-" * 80)
        
        for aluno in alunos:
            print(f"ID: {aluno.id:3d} | Nome: {aluno.nome:30s} | Autorização: {aluno.autorizacao!r:5s} | Tipo: {type(aluno.autorizacao)}")
        
        print("-" * 80)
        
        # Contar por valor
        true_count = sum(1 for a in alunos if a.autorizacao is True)
        false_count = sum(1 for a in alunos if a.autorizacao is False)
        none_count = sum(1 for a in alunos if a.autorizacao is None)
        
        print(f"Resumo:")
        print(f"  True:  {true_count}")
        print(f"  False: {false_count}")
        print(f"  None:  {none_count}")

if __name__ == '__main__':
    check_autorization_values()
