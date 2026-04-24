# data-in-microsoft-graph-api

Este projeto em Python captura dados de arquivos no OneDrive via Microsoft Graph API e os salva em armazenamento na nuvem (AWS S3 ou Google Cloud Storage) para criar uma camada raw de dados.

## Funcionalidades

- Autenticação com Microsoft Graph API usando MSAL
- Download de arquivos do OneDrive
- Upload para AWS S3 ou Google Cloud Storage
- Estrutura para camada raw de dados

## Pré-requisitos

- Python 3.8+
- Conta Microsoft com acesso ao OneDrive
- Aplicativo registrado no Azure AD para Graph API
- Credenciais para AWS S3 ou GCS

## Instalação

1. Clone o repositório
2. Instale as dependências:
   ```
   pip install -r requirements.txt
   ```
   ou
   ```
   make install
   ```
3. Copie `.env.example` para `.env` e preencha com suas credenciais

## Configuração

### Microsoft Graph API

1. Registre um aplicativo no [Azure Portal](https://portal.azure.com)
2. Adicione permissões: `Files.Read.All` ou `Files.Read`
3. Obtenha CLIENT_ID, CLIENT_SECRET, TENANT_ID
4. USER_ID é o ID do usuário do OneDrive (pode ser obtido via Graph API)

### AWS S3

- Configure AWS_ACCESS_KEY, AWS_SECRET_KEY, S3_BUCKET

### Google Cloud Storage

- Configure GCS_BUCKET e GCS_CREDENTIALS_PATH (caminho para service account JSON)

## Uso

Execute o script principal:

```python
python src/main.py
```

ou

```bash
make run
```

## Testes

Execute os testes:

```bash
pytest tests/
```

ou

```bash
make test
```

## Estrutura do Projeto

```
.
├── src/
│   └── main.py
├── tests/
│   ├── __init__.py
│   └── test_main.py
├── .env.example
├── .gitignore
├── CONTRIBUTING.md
├── LICENSE
├── Makefile
├── README.md
└── requirements.txt
```

## Contribuição

Veja [CONTRIBUTING.md](CONTRIBUTING.md) para diretrizes de contribuição.