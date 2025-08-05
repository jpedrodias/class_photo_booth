#!/usr/bin/env python3
"""
Script para reinicializar a base de dados do Class Photo Booth
ATENÇÃO: Isto irá apagar todos os dados existentes!
"""

import os
from app import app, db, init_db

def reset_database():
    """Remove base de dados existente e cria nova"""
    
    # Localizar ficheiro da base de dados
    db_path = None
    if hasattr(app.config, 'SQLALCHEMY_DATABASE_URI'):
        db_uri = app.config['SQLALCHEMY_DATABASE_URI']
        if db_uri.startswith('sqlite:///'):
            db_path = db_uri.replace('sqlite:///', '')
    
    if not db_path:
        # Tentar localização padrão
        db_path = os.path.join(os.path.dirname(__file__), 'instance', 'database.db')
    
    # Remover ficheiro da base de dados se existir
    if os.path.exists(db_path):
        print(f"Removendo base de dados existente: {db_path}")
        os.remove(db_path)
    
    # Criar diretório instance se não existir
    instance_dir = os.path.dirname(db_path)
    if instance_dir and not os.path.exists(instance_dir):
        os.makedirs(instance_dir)
    
    # Recriar base de dados
    print("Criando nova base de dados...")
    with app.app_context():
        db.create_all()
    
    print("Base de dados reinicializada com sucesso!")
    print("\nO primeiro utilizador a registar-se receberá permissões de administrador.")

if __name__ == '__main__':
    resposta = input("ATENÇÃO: Isto irá apagar todos os dados existentes! Continuar? (sim/não): ")
    if resposta.lower() in ['sim', 's', 'yes', 'y']:
        reset_database()
    else:
        print("Operação cancelada.")
