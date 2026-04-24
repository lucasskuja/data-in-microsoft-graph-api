import os
import requests
from msal import ConfidentialClientApplication
from dotenv import load_dotenv
import boto3
from google.cloud import storage

# Carregar variáveis de ambiente
load_dotenv()

# Configurações
CLIENT_ID = os.getenv('CLIENT_ID')
CLIENT_SECRET = os.getenv('CLIENT_SECRET')
TENANT_ID = os.getenv('TENANT_ID')
USER_ID = os.getenv('USER_ID')  # ID do usuário do OneDrive
SCOPE = ['https://graph.microsoft.com/.default']

# Função para obter token de acesso
def get_access_token():
    app = ConfidentialClientApplication(
        CLIENT_ID,
        authority=f"https://login.microsoftonline.com/{TENANT_ID}",
        client_credential=CLIENT_SECRET,
    )
    result = app.acquire_token_for_client(scopes=SCOPE)
    if 'access_token' in result:
        return result['access_token']
    else:
        raise Exception("Falha ao obter token de acesso")

# Função para baixar arquivo do OneDrive
def download_onedrive_file(file_path, access_token):
    url = f"https://graph.microsoft.com/v1.0/users/{USER_ID}/drive/root:/{file_path}:/content"
    headers = {'Authorization': f'Bearer {access_token}'}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.content
    else:
        raise Exception(f"Erro ao baixar arquivo: {response.status_code} - {response.text}")

# Função para upload para S3
def upload_to_s3(data, bucket_name, key, aws_access_key, aws_secret_key, region='us-east-1'):
    s3 = boto3.client(
        's3',
        aws_access_key_id=aws_access_key,
        aws_secret_access_key=aws_secret_key,
        region_name=region
    )
    s3.put_object(Bucket=bucket_name, Key=key, Body=data)

# Função para upload para GCS
def upload_to_gcs(data, bucket_name, blob_name, credentials_path):
    client = storage.Client.from_service_account_json(credentials_path)
    bucket = client.bucket(bucket_name)
    blob = bucket.blob(blob_name)
    blob.upload_from_string(data)

# Função principal
def main(file_path, storage_type, **kwargs):
    access_token = get_access_token()
    data = download_onedrive_file(file_path, access_token)
    
    if storage_type == 's3':
        upload_to_s3(data, **kwargs)
    elif storage_type == 'gcs':
        upload_to_gcs(data, **kwargs)
    else:
        raise ValueError("Tipo de armazenamento não suportado")

if __name__ == "__main__":
    # Exemplo de uso
    file_path = "Documents/example.xlsx"  # Caminho no OneDrive
    storage_type = "s3"  # ou "gcs"
    if storage_type == "s3":
        kwargs = {
            'bucket_name': os.getenv('S3_BUCKET'),
            'key': 'raw/example.xlsx',
            'aws_access_key': os.getenv('AWS_ACCESS_KEY'),
            'aws_secret_key': os.getenv('AWS_SECRET_KEY')
        }
    elif storage_type == "gcs":
        kwargs = {
            'bucket_name': os.getenv('GCS_BUCKET'),
            'blob_name': 'raw/example.xlsx',
            'credentials_path': os.getenv('GCS_CREDENTIALS_PATH')
        }
    main(file_path, storage_type, **kwargs)