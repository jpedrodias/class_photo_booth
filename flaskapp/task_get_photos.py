import requests
import json
from io import BytesIO
from PIL import Image

# Configurações do servidor
BASE_URL = 'http://localhost:5000'  # Ajuste se o servidor estiver noutra porta

# Credenciais de teste (substitua pelos seus dados)
USERNAME = 'my_username'  # Substitua pelo username real
PASSWORD = 'my_password'  # Substitua pela password real

def test_photo_api():
    # Criar sessão para manter cookies de autenticação
    session = requests.Session()
    
    print("1. Fazendo login...")
    
    # Dados para login via API
    login_data = {
        'username': USERNAME,
        'password': PASSWORD,
        'remember_me': True
    }
    
    # Headers para JSON
    headers = {
        'Content-Type': 'application/json'
    }
    
    # Fazer login via API
    login_response = session.post(f'{BASE_URL}/api/login', json=login_data, headers=headers)
    
    if login_response.status_code != 200:
        print(f"Erro no login: {login_response.status_code}")
        print(login_response.text)
        return
    
    login_result = login_response.json()
    if not login_result.get('success'):
        print(f"Login falhou: {login_result.get('error', 'Erro desconhecido')}")
        return
    
    token = login_result.get('token')
    if not token:
        print("Token não encontrado na resposta do login")
        return
    
    print(f"Login bem-sucedido! Bem-vindo, {login_result['user']['name']}!")
    print(f"Token obtido: {token[:50]}...")
    
    print("\n2. Obtendo foto com o token...")
    
    # Parâmetros para obter foto
    photo_params = {
        'token': token,
        'processo': '90004',  # Processo desejado
        'size': 'thumb'  # ou 'original'
    }
    
    # Obter foto
    photo_response = session.get(f'{BASE_URL}/api/photos/', params=photo_params)
    
    if photo_response.status_code != 200:
        print(f"Erro ao obter foto: {photo_response.status_code}")
        print(photo_response.text)
        return
    
    print("Foto obtida com sucesso!")
    
    # Verificar se é uma imagem
    content_type = photo_response.headers.get('content-type', '')
    if 'image' in content_type:
        print(f"Tipo de conteúdo: {content_type}")
        
        # Salvar a imagem (opcional)
        with open('test_photo.jpg', 'wb') as f:
            f.write(photo_response.content)
        print("Imagem salva como 'test_photo.jpg'")
        
        # Verificar tamanho da imagem
        image_size = len(photo_response.content)
        print(f"Tamanho da imagem: {image_size} bytes")
    else:
        print(f"Resposta não é uma imagem: {content_type}")
        print(photo_response.text)

if __name__ == '__main__':
    test_photo_api()
