# Teste Django

## Instalação
### Dependências (usando [Poetry](https://python-poetry.org/))
- `poetry install`
### Configuração
- Copie o arquivo `.env.example` -> `.env` e edite de acordo com as suas necessidades
- Migre o banco de dados: `poetry run python manage.py migrate`

### Rodando em desenvolvimento
- `poetry run python manage.py runserver`

## Usando
### Criando o primeiro usuário (admin)
- `poetry run python manage.py createsuperuser`
- Acesse a interface de admin em `/admin`, e edite o usuário mudando o perfil para `Administrador`

## Testes
### Rodando os testes
- `poetry run python manage.py test`