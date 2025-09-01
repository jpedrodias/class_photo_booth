"""
Tarefas assíncronas para envio de emails usando Redis Queue (RQ)
"""
import traceback
import os
import shutil
from datetime import datetime
from flask import render_template
from flask_mail import Mail, Message
from rq import get_current_job
import redis
import json


def send_verification_email(app_config, email, code, request_url_root):
    """
    Tarefa assíncrona para envio de email de verificação
    """
    job = get_current_job()
    job_id = job.get_id() if job else None
    
    try:
        # Configurar Flask Mail
        from flask import Flask
        import os
        app = Flask(__name__, template_folder=os.path.join(os.path.dirname(__file__), 'templates'))
        app.config.update(app_config)
        
        mail = Mail(app)
        
        # Renderizar template HTML
        with app.app_context():
            verify_link = f"{request_url_root.rstrip('/')}/login/verify?email={email}&code={code}"
            html_body = render_template('template_email_send_verification.html', code=code, verify_link=verify_link)
            
            msg = Message(
                subject='Verificação de Email - Class Photo Booth',
                sender=app.config.get('MAIL_DEFAULT_SENDER'),
                recipients=[email],
                html=html_body
            )
            
            # Atualizar status da tarefa
            if job:
                job.meta['status'] = 'sending'
                job.meta['progress'] = 50
                job.save_meta()
            
            # Enviar email
            mail.send(msg)
            
            print(f"Email de verificação enviado com sucesso para: {email}")
            
            # Atualizar status da tarefa como sucesso
            if job:
                job.meta['status'] = 'completed'
                job.meta['progress'] = 100
                job.meta['message'] = f'Email de verificação enviado com sucesso para {email}'
                job.save_meta()
            
            return {
                'success': True,
                'message': f'Email de verificação enviado com sucesso para {email}',
                'email': email
            }
            
    except Exception as e:
        error_msg = f"Erro ao enviar email de verificação para {email}: {str(e)}"
        print(error_msg)
        print(f"Traceback completo: {traceback.format_exc()}")
        
        # Atualizar status da tarefa como erro
        if job:
            job.meta['status'] = 'failed'
            job.meta['progress'] = 100
            job.meta['error'] = error_msg
            job.save_meta()
        
        return {
            'success': False,
            'error': error_msg,
            'email': email
        }


def send_password_reset_email(app_config, email, reset_code, request_url_root):
    """
    Tarefa assíncrona para envio de email de recuperação de password
    """
    job = get_current_job()
    job_id = job.get_id() if job else None
    
    try:
        # Configurar Flask Mail
        from flask import Flask
        import os
        app = Flask(__name__, template_folder=os.path.join(os.path.dirname(__file__), 'templates'))
        app.config.update(app_config)
        
        mail = Mail(app)
        
        # Renderizar template HTML
        with app.app_context():
            reset_link = f"{request_url_root.rstrip('/')}/login/reset_password?email={email}&code={reset_code}"
            html_body = render_template('template_email_send_password_reset.html', code=reset_code, reset_link=reset_link)
            
            msg = Message(
                subject='Recuperação de Password - Class Photo Booth',
                sender=app.config.get('MAIL_DEFAULT_SENDER'),
                recipients=[email],
                html=html_body
            )
            
            # Atualizar status da tarefa
            if job:
                job.meta['status'] = 'sending'
                job.meta['progress'] = 50
                job.save_meta()
            
            # Enviar email
            mail.send(msg)
            
            print(f"Email de recuperação de password enviado com sucesso para: {email}")
            
            # Atualizar status da tarefa como sucesso
            if job:
                job.meta['status'] = 'completed'
                job.meta['progress'] = 100
                job.meta['message'] = f'Email de recuperação enviado com sucesso para {email}'
                job.save_meta()
            
            return {
                'success': True,
                'message': f'Email de recuperação enviado com sucesso para {email}',
                'email': email
            }
            
    except Exception as e:
        error_msg = f"Erro ao enviar email de recuperação para {email}: {str(e)}"
        print(error_msg)
        print(f"Traceback completo: {traceback.format_exc()}")
        
        # Atualizar status da tarefa como erro
        if job:
            job.meta['status'] = 'failed'
            job.meta['progress'] = 100
            job.meta['error'] = error_msg
            job.save_meta()
        
        return {
            'success': False,
            'error': error_msg,
            'email': email
        }


def send_account_updated_email(app_config, email, user_name, request_url_root):
    """
    Tarefa assíncrona para envio de email de notificação de conta atualizada
    """
    job = get_current_job()
    job_id = job.get_id() if job else None
    
    try:
        # Configurar Flask Mail
        from flask import Flask
        import os
        app = Flask(__name__, template_folder=os.path.join(os.path.dirname(__file__), 'templates'))
        app.config.update(app_config)
        
        mail = Mail(app)
        
        # Renderizar template HTML
        with app.app_context():
            html_body = render_template('template_email_account_updated.html', user_name=user_name, request_url_root=request_url_root)
            
            msg = Message(
                subject='Conta Atualizada - Class Photo Booth',
                sender=app.config.get('MAIL_DEFAULT_SENDER'),
                recipients=[email],
                html=html_body
            )
            
            # Atualizar status da tarefa
            if job:
                job.meta['status'] = 'sending'
                job.meta['progress'] = 50
                job.save_meta()
            
            # Enviar email
            mail.send(msg)
            
            print(f"Email de notificação de conta atualizada enviado com sucesso para: {email}")
            
            # Atualizar status da tarefa como sucesso
            if job:
                job.meta['status'] = 'completed'
                job.meta['progress'] = 100
                job.meta['message'] = f'Email de notificação enviado com sucesso para {email}'
                job.save_meta()
            
            return {
                'success': True,
                'message': f'Email de notificação enviado com sucesso para {email}',
                'email': email
            }
            
    except Exception as e:
        error_msg = f"Erro ao enviar email de notificação para {email}: {str(e)}"
        print(error_msg)
        print(f"Traceback completo: {traceback.format_exc()}")
        
        # Atualizar status da tarefa como erro
        if job:
            job.meta['status'] = 'failed'
            job.meta['progress'] = 100
            job.meta['error'] = error_msg
            job.save_meta()
        
        return {
            'success': False,
            'error': error_msg,
            'email': email
        }

def send_notification_teacher_email(app_config, email, subject, body, turma_nome, professor_nome, request_url_root):
    """
    Envia email de notificação para o professor responsável pela turma
    """
    job = get_current_job()
    job_id = job.get_id() if job else None
    
    try:
        # Configurar Flask Mail
        from flask import Flask
        import os
        app = Flask(__name__, template_folder=os.path.join(os.path.dirname(__file__), 'templates'))
        app.config.update(app_config)
        
        mail = Mail(app)
        
        # Renderizar template do email e criar mensagem
        with app.app_context():
            from datetime import datetime
            html_body = render_template(
                'template_email_send_notification_teacher.html',
                subject=subject,
                body=body,
                turma_nome=turma_nome,
                professor_nome=professor_nome,
                current_date=datetime.now().strftime('%d/%m/%Y %H:%M'),
                request_url_root=request_url_root
            )
            
            # Criar mensagem dentro do contexto da aplicação
            msg = Message(
                subject=subject,
                recipients=[email],
                html=html_body
            )
            
            # Atualizar status da tarefa
            if job:
                job.meta['status'] = 'sending'
                job.meta['progress'] = 50
                job.save_meta()
            
            # Enviar email dentro do contexto
            mail.send(msg)
        
        print(f"Email de notificação enviado com sucesso para: {email}")
        
        # Atualizar status da tarefa como sucesso
        if job:
            job.meta['status'] = 'completed'
            job.meta['progress'] = 100
            job.meta['message'] = f'Email de notificação enviado com sucesso para {email}'
            job.save_meta()
        
        return {
            'success': True,
            'email': email,
            'turma': turma_nome,
            'professor': professor_nome
        }
        
    except Exception as e:
        error_msg = f"Erro ao enviar email de notificação para {email}: {str(e)}"
        print(error_msg)
        print(f"Traceback completo: {traceback.format_exc()}")
        
        # Atualizar status da tarefa como erro
        if job:
            job.meta['status'] = 'failed'
            job.meta['progress'] = 100
            job.meta['error'] = error_msg
            job.save_meta()
        
        return {
            'success': False,
            'error': error_msg,
            'email': email
        }


def process_bulk_upload(app_config, uploaded_files, temp_dir):
    """
    Tarefa assíncrona para processar upload em lote de fotos
    """
    job = get_current_job()
    job_id = job.get_id() if job else None

    try:
        # Importar módulos necessários
        import os
        import cv2
        import numpy as np
        import shutil
        import zipfile
        from werkzeug.utils import secure_filename
        import uuid
        
        # Definir constantes globais necessárias
        PHOTOS_DIR = app_config['PHOTOS_DIR']
        THUMBS_DIR = app_config['THUMBS_DIR']

        # Configurar SQLAlchemy diretamente
        from flask_sqlalchemy import SQLAlchemy
        from sqlalchemy import create_engine
        from sqlalchemy.orm import sessionmaker
        
        # Criar engine e sessão diretamente
        engine = create_engine(app_config['SQLALCHEMY_DATABASE_URI'])
        SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
        db_session = SessionLocal()
        
        # Importar modelos
        from app import Aluno, Turma

        # Função auxiliar para processar um único arquivo
        def process_single_file(file_info, db_session, Aluno, Turma, PHOTOS_DIR, THUMBS_DIR, temp_dir):
            """Processa um único arquivo de imagem"""
            file_path = file_info['path']
            original_filename = file_info['original_filename']
            file_errors = []
            
            try:
                # Extrair número do processo do nome do arquivo (sem extensão)
                processo = os.path.splitext(original_filename)[0]
                print(f"DEBUG: Processando arquivo {original_filename}, processo extraído: '{processo}'")

                # Verificar se existe aluno com esse processo
                aluno = db_session.query(Aluno).filter_by(processo=processo).first()
                print(f"DEBUG: Busca por aluno com processo '{processo}': {'ENCONTRADO' if aluno else 'NÃO ENCONTRADO'}")
                if aluno:
                    print(f"DEBUG: Aluno encontrado - ID: {aluno.id}, Nome: {aluno.nome}, Processo: {aluno.processo}")
                
                if not aluno:
                    file_errors.append(f"Arquivo {original_filename}: aluno com processo {processo} não encontrado")
                    print(f"DEBUG: Adicionando erro - aluno não encontrado para processo {processo}")
                    return False, file_errors

                # Obter turma do aluno
                turma = aluno.turma
                print(f"DEBUG: Turma do aluno: {'ENCONTRADA' if turma else 'NÃO ENCONTRADA'}")
                if turma:
                    print(f"DEBUG: Turma - ID: {turma.id}, Nome: {turma.nome}, Nome Seguro: {turma.nome_seguro}")
                
                if not turma:
                    file_errors.append(f"Arquivo {original_filename}: aluno não está associado a uma turma")
                    print(f"DEBUG: Adicionando erro - aluno sem turma")
                    return False, file_errors

                # Criar diretórios se não existirem
                foto_dir = turma.get_foto_directory()
                thumb_dir = turma.get_thumb_directory()
                print(f"DEBUG: Diretórios - Foto: {foto_dir}, Thumb: {thumb_dir}")

                # Criar diretórios de forma segura
                if not os.path.exists(foto_dir):
                    os.makedirs(foto_dir, exist_ok=True)
                    print(f"DEBUG: Diretório criado: {foto_dir}")
                if not os.path.exists(thumb_dir):
                    os.makedirs(thumb_dir, exist_ok=True)
                    print(f"DEBUG: Diretório criado: {thumb_dir}")

                # Caminhos dos arquivos
                photo_path = os.path.join(foto_dir, f'{processo}.jpg')
                thumb_path = os.path.join(thumb_dir, f'{processo}.jpg')
                
                print(f"DEBUG: Caminhos dos arquivos - Foto: {photo_path}, Thumb: {thumb_path}")
                print(f"DEBUG: Arquivo de entrada existe: {os.path.exists(file_path)}")

                # Processar imagem
                image = cv2.imread(file_path)
                print(f"DEBUG: Imagem carregada: {'SUCESSO' if image is not None else 'FALHA'}")
                if image is not None:
                    print(f"DEBUG: Dimensões da imagem: {image.shape}")
                
                if image is None:
                    file_errors.append(f"Arquivo {original_filename}: não foi possível ler a imagem")
                    print(f"DEBUG: Adicionando erro - não foi possível ler imagem: {file_path}")
                    return False, file_errors

                # Salvar foto original com compressão
                success = cv2.imwrite(photo_path, cv2.imdecode(cv2.imencode('.jpg', image, [cv2.IMWRITE_JPEG_QUALITY, 95])[1], cv2.IMREAD_COLOR))
                print(f"DEBUG: Salvamento da foto original: {'SUCESSO' if success else 'FALHA'} - {photo_path}")
                if not success:
                    file_errors.append(f"Arquivo {original_filename}: erro ao salvar foto original")
                    print(f"DEBUG: Adicionando erro - falha ao salvar foto original")
                    return False, file_errors

                # Criar thumbnail
                height, width, _ = image.shape
                min_dim = min(height, width)
                start_x = (width - min_dim) // 2
                start_y = (height - min_dim) // 2
                cropped_image = image[start_y:start_y + min_dim, start_x:start_x + min_dim]
                thumbnail = cv2.resize(cropped_image, (250, 250))

                # Salvar thumbnail com compressão
                thumb_success = cv2.imwrite(thumb_path, cv2.imdecode(cv2.imencode('.jpg', thumbnail, [cv2.IMWRITE_JPEG_QUALITY, 50])[1], cv2.IMREAD_COLOR))
                print(f"DEBUG: Salvamento do thumbnail: {'SUCESSO' if thumb_success else 'FALHA'} - {thumb_path}")
                if not thumb_success:
                    file_errors.append(f"Arquivo {original_filename}: erro ao salvar thumbnail")
                    print(f"DEBUG: Adicionando erro - falha ao salvar thumbnail")
                    return False, file_errors

                print(f"DEBUG: Foto e thumbnail salvas com sucesso para {processo}")

                # Atualizar flags na base de dados
                aluno.foto_tirada = True
                aluno.foto_existe = True
                turma.update_last_modified()
                
                print(f"DEBUG: Base de dados atualizada para aluno {processo}")
                return True, []

            except Exception as e:
                error_msg = f"Erro ao processar arquivo {original_filename}: {str(e)}"
                print(f"DEBUG: {error_msg}")
                file_errors.append(error_msg)
                return False, file_errors

        processed_files = 0
        successful_uploads = 0
        errors = []

        # Atualizar status inicial
        if job:
            job.meta['status'] = 'processing'
            job.meta['progress'] = 0
            job.meta['message'] = 'Iniciando processamento dos arquivos...'
            job.save_meta()

        # Verificar se é um único arquivo ou múltiplos arquivos
        if len(uploaded_files) == 1:
            file_info = uploaded_files[0]
            file_path = file_info['path']
            original_filename = file_info['original_filename']
            
            # Verificar se é um arquivo ZIP
            if original_filename.lower().endswith('.zip'):
                print(f"DEBUG: Processando arquivo ZIP: {original_filename}")
                # Processar ZIP
                try:
                    with zipfile.ZipFile(file_path, 'r') as zip_ref:
                        # Listar arquivos no ZIP
                        zip_files = zip_ref.namelist()
                        print(f"DEBUG: Arquivos encontrados no ZIP: {zip_files}")
                        
                        # Filtrar apenas arquivos de imagem
                        image_extensions = ['.jpg', '.jpeg', '.png', '.bmp', '.tiff', '.tif']
                        image_files = [f for f in zip_files if any(f.lower().endswith(ext) for ext in image_extensions)]
                        print(f"DEBUG: Arquivos de imagem no ZIP: {image_files}")
                        
                        if not image_files:
                            errors.append("ZIP não contém arquivos de imagem válidos")
                        else:
                            # Extrair arquivos para o diretório temporário
                            for zip_file in image_files:
                                try:
                                    print(f"DEBUG: Processando arquivo do ZIP: {zip_file}")
                                    
                                    # Verificar se o arquivo está em uma subpasta
                                    if '/' in zip_file or '\\' in zip_file:
                                        print(f"DEBUG: Arquivo em subpasta detectado: {zip_file}")
                                    
                                    # Extrair arquivo preservando estrutura temporária
                                    extracted_path = zip_ref.extract(zip_file, temp_dir)
                                    print(f"DEBUG: Arquivo extraído para: {extracted_path}")
                                    
                                    # Obter nome base do arquivo (sempre usar apenas o nome do arquivo)
                                    base_filename = os.path.basename(zip_file)
                                    print(f"DEBUG: Nome base extraído: {base_filename}")
                                    
                                    # Se o arquivo foi extraído em subpasta, movê-lo para o diretório raiz
                                    final_path = os.path.join(temp_dir, base_filename)
                                    
                                    if extracted_path != final_path:
                                        print(f"DEBUG: Movendo arquivo de subpasta: {extracted_path} -> {final_path}")
                                        # Criar diretório de destino se necessário
                                        os.makedirs(os.path.dirname(final_path), exist_ok=True)
                                        shutil.move(extracted_path, final_path)
                                        extracted_path = final_path
                                    
                                    # Verificar se o arquivo foi movido corretamente
                                    if not os.path.exists(extracted_path):
                                        raise FileNotFoundError(f"Arquivo não encontrado após extração: {extracted_path}")
                                    
                                    print(f"DEBUG: Arquivo pronto para processamento: {extracted_path}")
                                    
                                    # Processar arquivo extraído
                                    file_info_single = {
                                        'path': extracted_path,
                                        'original_filename': base_filename
                                    }
                                    success, file_errors = process_single_file(file_info_single, db_session, Aluno, Turma, PHOTOS_DIR, THUMBS_DIR, temp_dir)
                                    if success:
                                        successful_uploads += 1
                                    else:
                                        errors.extend(file_errors)
                                        
                                except Exception as e:
                                    error_msg = f"Erro ao extrair/processar {zip_file}: {str(e)}"
                                    print(f"DEBUG: {error_msg}")
                                    errors.append(error_msg)
                            
                            processed_files = len(image_files)
                            
                except zipfile.BadZipFile:
                    errors.append("Arquivo ZIP inválido ou corrompido")
                except Exception as e:
                    errors.append(f"Erro ao processar ZIP: {str(e)}")
                    
            else:
                # Processar arquivo único
                print(f"DEBUG: Processando arquivo único: {original_filename}")
                success, file_errors = process_single_file(file_info, db_session, Aluno, Turma, PHOTOS_DIR, THUMBS_DIR, temp_dir)
                if success:
                    successful_uploads += 1
                else:
                    errors.extend(file_errors)
                processed_files = 1
        else:
            # Processar múltiplos arquivos (caso futuro)
            print(f"DEBUG: Processando {len(uploaded_files)} arquivos múltiplos")
            for file_info in uploaded_files:
                success, file_errors = process_single_file(file_info, db_session, Aluno, Turma, PHOTOS_DIR, THUMBS_DIR, temp_dir)
                if success:
                    successful_uploads += 1
                else:
                    errors.extend(file_errors)
                processed_files += 1

        # Atualizar progresso
        if job:
            if len(uploaded_files) == 1 and uploaded_files[0]['original_filename'].lower().endswith('.zip'):
                # Para ZIP, progresso baseado no número de arquivos processados
                progress = int((processed_files / max(processed_files, 1)) * 100)
            else:
                # Para arquivo único ou múltiplos, progresso normal
                progress = int((processed_files / len(uploaded_files)) * 100) if uploaded_files else 100
            job.meta['progress'] = progress
            job.meta['message'] = f'Processando arquivo {processed_files} de {len(uploaded_files)}...'
            job.save_meta()

        # Commit das mudanças
        db_session.commit()
        print(f"DEBUG: Processamento concluído. {successful_uploads} arquivos processados com sucesso")
        print(f"DEBUG: Total de erros: {len(errors)}")
        if errors:
            print("DEBUG: Lista de erros:")
            for error in errors:
                print(f"  - {error}")

        # Limpar arquivos temporários
        if os.path.exists(temp_dir):
            shutil.rmtree(temp_dir)
            print(f"DEBUG: Diretório temporário removido: {temp_dir}")

        # Preparar mensagem final
        message = f"Bulk upload concluído: {successful_uploads} arquivos processados com sucesso"
        if errors:
            message += f", {len(errors)} erros encontrados"

        print(f"DEBUG: Mensagem final: {message}")
        print(f"DEBUG: Retornando resultado: success=True, successful_uploads={successful_uploads}, errors={len(errors)}")

        # Atualizar status final
        if job:
            job.meta['status'] = 'completed'
            job.meta['progress'] = 100
            job.meta['message'] = message
            job.meta['successful_uploads'] = successful_uploads
            job.meta['errors'] = errors
            job.save_meta()

        return {
            'success': True,
            'message': message,
            'successful_uploads': successful_uploads,
            'errors': errors
        }

    except Exception as e:
        error_msg = f"Erro no processamento bulk upload: {str(e)}"
        print(error_msg)
        print(f"Traceback completo: {traceback.format_exc()}")

        # Limpar arquivos temporários em caso de erro
        try:
            if os.path.exists(temp_dir):
                shutil.rmtree(temp_dir)
        except:
            pass

        # Atualizar status como erro
        if job:
            job.meta['status'] = 'failed'
            job.meta['progress'] = 100
            job.meta['error'] = error_msg
            job.save_meta()

        return {
            'success': False,
            'error': error_msg
        }
