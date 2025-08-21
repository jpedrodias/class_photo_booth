#!/usr/bin/env python3
"""
Script para inicializar a base de dados do Class Photo Booth

docker exec -it flaskapp /bin/bash -c "python ./init_database.py"
"""

from app import app, db, User


if __name__ == '__main__':
    print("Inicializando base de dados...")
    with app.app_context():
        db.create_all()
        print("Base de dados inicializada com sucesso!")

        admin = User()
        admin.email = 'admin@example.com'
        admin.name = 'Administrador'
        admin.password = 'ChangeMe1#'
        admin.role = 'admin'
        admin.is_active = True
        
        try:
            db.session.add(admin)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            print(f"Erro ao criar utilizador administrador: {e}")


    print("Utilizador administrador criado com sucesso!")
