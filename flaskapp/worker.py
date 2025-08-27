#!/usr/bin/env python3
"""
Worker script para processar tarefas de email em background usando Redis Queue (RQ)
Modos de execução:
- python worker.py --verify: Verifica conexão Redis e sai
- python worker.py --forever: Executa em loop infinito com reinício automático
- python worker.py: Executa uma vez apenas
"""
import os
import sys
import redis
import time
import argparse
from rq import Worker, Queue

# Adicionar o diretório do app ao path para importar os módulos
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

def verify_redis_connection(redis_url, max_retries=10):
    """
    Verifica conexão com Redis
    Retorna True se conectou com sucesso, False caso contrário
    """
    for attempt in range(max_retries):
        try:
            redis_conn = redis.from_url(redis_url)
            redis_conn.ping()  # Testar conexão
            print(f"Conexão Redis verificada com sucesso: {redis_url}")
            return True
        except Exception as e:
            if attempt < max_retries - 1:
                print(f"Tentativa {attempt + 1}/{max_retries} de conectar ao Redis falhou: {e}")
                time.sleep(2)
            else:
                print(f"Falha ao conectar ao Redis após {max_retries} tentativas: {e}")
                return False

def run_worker_once(redis_url):
    """
    Executa o worker uma vez apenas
    """
    try:
        # Conectar ao Redis
        redis_conn = redis.from_url(redis_url)
        redis_conn.ping()  # Testar conexão
        
        # Criar queue
        email_queue = Queue('email', connection=redis_conn)
        
        print(f"Worker RQ iniciado. Conectado ao Redis: {redis_url}")
        print(f"Processando queue: {email_queue.name}")
        print("Worker rodando uma vez...")
        
        # Iniciar worker (burst=True para executar uma vez)
        worker = Worker([email_queue], connection=redis_conn)
        worker.work(burst=True, logging_level='INFO')
        
        print("Worker finalizado.")
        
    except KeyboardInterrupt:
        print("Worker RQ interrompido.")
        sys.exit(0)
    except Exception as e:
        print(f"Erro no worker RQ: {e}")
        sys.exit(1)

def run_worker_forever(redis_url):
    """
    Executa o worker em loop infinito com reinício automático
    """
    while True:
        try:
            # Conectar ao Redis
            redis_conn = redis.from_url(redis_url)
            redis_conn.ping()  # Testar conexão
            
            # Criar queue
            email_queue = Queue('email', connection=redis_conn)
            
            print(f"Worker RQ iniciado. Conectado ao Redis: {redis_url}")
            print(f"Processando queue: {email_queue.name}")
            print("Worker rodando para sempre...")
            
            # Iniciar worker
            worker = Worker([email_queue], connection=redis_conn)
            worker.work(burst=False, logging_level='INFO')
            
        except KeyboardInterrupt:
            print("Worker RQ interrompido pelo usuário.")
            sys.exit(0)
        except Exception as e:
            print(f"Erro no worker RQ: {e}")
            print("Reiniciando worker em 5 segundos...")
            time.sleep(5)

def main():
    """
    Função principal para iniciar o worker RQ baseado nos argumentos
    """
    parser = argparse.ArgumentParser(description='Redis Queue Worker para processamento de emails')
    parser.add_argument('--verify', action='store_true', help='Apenas verifica conexão Redis e sai')
    parser.add_argument('--forever', action='store_true', help='Executa em loop infinito com reinício automático')
    
    args = parser.parse_args()
    
    # Configurações Redis (devem coincidir com as do app)
    redis_url = os.getenv('RQ_REDIS_URL', 'redis://redis:6379/1')
    
    if args.verify:
        # Modo verificação
        print("Verificando conexão Redis...")
        success = verify_redis_connection(redis_url)
        sys.exit(0 if success else 1)
        
    elif args.forever:
        # Modo loop infinito
        run_worker_forever(redis_url)
        
    else:
        # Modo padrão: executa uma vez
        run_worker_once(redis_url)

if __name__ == '__main__':
    main()
