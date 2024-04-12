# Sistema usando python/django para gestão de exames médicos
# 1º: Criar o ambiente virtual -> python3 -m venv venv (USO NO LINUX)
# 2º: Ativar o ambiente -> source venv/bin/activate
# 3º: Fazer instalação do Django e as demais bibliotecas: 
#     pip install django
#     pip install pillow
# 4º: Criar o projeto Django: django-admin startproject vitalab .
# 5º: Para rodar o projeto: python manage.py runserver
# 6º: Dividir o projeto em apps o Primeiro app é o de usuarios
# 7º: Criar o app: python manage.py startapp usuarios 
# 8º: Criação da URL: Na url da raiz do seu projeto vc adiciona o modulo include, cria um outro path e adiciona pasta de url do seu app. Isso vai fazer com o as urls do seu app sejam incluidos na url do projeto  
#      path('usuarios/',include('usuarios.urls'))
# 9º: crie o arquivo urls.py dentro de usuarios
# 10º: Adicione no setting(indica onde achar os templates): os.path.join(BASE_DIR, 'templates')
# 11º: Após configurar o template deve-se fazer as migrations: python manage.py makemigrations e depois python manage.py migrate
