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

        # Criar departamentos padrão se não existirem
        departamentos_padrao = [
            {'name': 'todos', 'fullname': 'Todos os Utilizadores'},
            {'name': 'pre', 'fullname': 'Pré-Escolar'},
            {'name': '1c', 'fullname': '1º Ciclo'},
            {'name': '2c', 'fullname': '2º Ciclo'},
            {'name': '3c', 'fullname': '3º Ciclo'},
            {'name': 'sec', 'fullname': 'Secundário'},
            {'name': 'profs', 'fullname': 'Professores'},
            {'name': 'funcs', 'fullname': 'Funcionários'},
            {'name': 'coord', 'fullname': 'Coordenação'},
            {'name': 'admin', 'fullname': 'Administração'},
        ]
        
        # Verificar e criar departamentos
        from app import Departamento
        for dept_data in departamentos_padrao:
            existing_dept = Departamento.query.filter_by(name=dept_data['name']).first()
            if not existing_dept:
                dept = Departamento()
                dept.name = dept_data['name']
                dept.fullname = dept_data['fullname']
                db.session.add(dept)
                print(f"Departamento '{dept_data['name']}' criado com sucesso!")
        
        db.session.commit()
        
        # Associar todos os users ao departamento 'todos' (se ainda não estiverem associados)
        from app import UserDepartamento
        dept_todos = Departamento.query.filter_by(name='todos').first()
        if dept_todos:
            users = User.query.all()
            for user in users:
                # Verificar se já está associado ao departamento 'todos'
                existing_assoc = UserDepartamento.query.filter_by(
                    user_id=user.id, 
                    departamento_id=dept_todos.id
                ).first()
                
                if not existing_assoc:
                    user_dept = UserDepartamento()
                    user_dept.user_id = user.id
                    user_dept.departamento_id = dept_todos.id
                    db.session.add(user_dept)
            
            db.session.commit()
            print("Todos os utilizadores associados ao departamento 'todos'!")

        # Criar utilizador administrador
        admin = User.query.filter_by(email='admin@example.com').first()
        if not admin:
            admin = User()
            admin.email = 'admin@example.com'
            admin.name = 'Administrador'
            admin.password = 'ChangeMe1#'
            admin.role = 'admin'
            admin.is_active = True
            
            try:
                db.session.add(admin)
                db.session.commit()
                print("Utilizador administrador criado com sucesso!")
            except Exception as e:
                db.session.rollback()
                print(f"Erro ao criar utilizador administrador: {e}")
        else:
            print("Utilizador administrador já existe!")