"""
Tarefas assíncronas para envio de emails usando Redis Queue (RQ)
"""
import traceback
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
        app = Flask(__name__)
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
        app = Flask(__name__)
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


def send_account_updated_email(app_config, email, user_name):
    """
    Tarefa assíncrona para envio de email de notificação de conta atualizada
    """
    job = get_current_job()
    job_id = job.get_id() if job else None
    
    try:
        # Configurar Flask Mail
        from flask import Flask
        app = Flask(__name__)
        app.config.update(app_config)
        
        mail = Mail(app)
        
        # Renderizar template HTML
        with app.app_context():
            html_body = render_template('template_email_account_updated.html', user_name=user_name)
            
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
