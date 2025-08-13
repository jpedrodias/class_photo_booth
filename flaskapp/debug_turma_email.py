#!/usr/bin/env python3
"""
Script de debug para verificar os emails dos professores das turmas
"""

from app import app, db, Turma

def debug_turma_emails():
    print("Verificando emails dos professores das turmas...")
    
    with app.app_context():
        turmas = Turma.query.all()
        
        if not turmas:
            print("Nenhuma turma encontrada na base de dados")
            return
        
        for turma in turmas:
            print(f"Turma: {turma.nome}")
            print(f"  Professor: '{turma.nome_professor}'")
            print(f"  Email Professor: '{turma.email_professor}'")
            print(f"  ID: {turma.id}")
            print("-" * 40)

if __name__ == "__main__":
    debug_turma_emails()
