#!/usr/bin/env python3
"""
Script para inicializar a base de dados do Class Photo Booth
"""

from app import app, db

if __name__ == '__main__':
    print("Inicializando base de dados...")
    with app.app_context():
        db.create_all()
        print("Base de dados inicializada com sucesso!")
    print("\nAgora pode executar a aplicação com: python app.py")
    print("O primeiro utilizador a registar-se receberá permissões de administrador.")
