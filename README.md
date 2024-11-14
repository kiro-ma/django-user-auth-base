# django-user-auth-base
API de autenticação em Django, incluindo registro, login, logout e autenticação de usuários, projetada para ser facilmente integrada em projetos web. Ideal para iniciantes ou como base para sistemas de autenticação personalizados.

Funcionalidades

    Registro de usuários
    Login e logout
    Autenticação de usuários com JWT ou sessões
    Implementação utilizando as URLs de autenticação padrão do Django

Requisitos

    Python 3.13 ou superior
    Django 4.x ou superior

# Como Instalar

Clone este repositório:

    git clone https://github.com/kiro-ma/django-user-auth-base.git

Instale as dependências:

Certifique-se de que você está utilizando um ambiente virtual (recomendado). Se ainda não tiver um, crie um ambiente virtual:

    python3 -m venv venv

Ative o ambiente virtual:

No Windows:

    .\venv\Scripts\activate

No macOS/Linux:

    source venv/bin/activate

Após ativar o ambiente virtual, instale as dependências listadas no requirements.txt:

    pip install -r requirements.txt

Instale o Django:

Caso não tenha o Django instalado, você pode instalar diretamente com o comando:

    pip install django

Ou, se preferir, pode consultar a documentação oficial do Django para mais detalhes sobre a instalação.
    
    https://docs.djangoproject.com/en/5.1/

# Configuração inicial do Django:

No diretório do projeto, execute o comando abaixo para realizar a migração do banco de dados:

python manage.py migrate

Criar um superusuário (admin):

    python manage.py createsuperuser

Acesse o painel administrativo em http://127.0.0.1:8000/admin/ e a API de autenticação em http://127.0.0.1:8000/auth/.

# Contribuição

Sinta-se à vontade para contribuir com melhorias, correções ou novas funcionalidades! Se você tiver sugestões, basta abrir uma issue ou enviar um pull request.
