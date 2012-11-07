# -*- coding: utf-8 -*-
from fabric.api import *

username = 'usuario'
prod_server = '%s@50.116.43.65' % username
media_server = '%s@50.116.44.140' % username
project_path = '/home/%s/project/' % username
env_path = '/home/%s/env/bin/activate' % username

env.hosts = [prod_server]

def deploy():
    """faz o deploy da aplicação no servidor"""
    log('Iniciando deploy da aplicação')
    pull()
    push()
    remote_pull()
    compass_compile()
    compress()
    collectstatic()
    remote_migrate_all()
    # restart_server()

def server():
    """inicia o servidor de desenvolvimento local"""
    log('Iniciando servidor de desenvolvimento do Django')
    local('python manage.py runserver 0.0.0.0:8000')

def gunicorn():
    """inicia o servidor de desenvolvimento local usando gunicorn"""
    log('Iniciando servidor de desenvolvimento do Django com gunicorn')
    local('gunicorn app.wsgi:application -w 4 -b 0.0.0.0:8000')    
    
def co():
    """commit local"""
    local('git commit -a')

def commit_all():
    """commit local"""
    local('git add .')
    local('git commit -a')

def commit_all():
    """commit local"""
    local('git add .')
    local('git commit -a')

def push():
    """git push local"""
    log("Enviando alterações")
    local('git push origin master')

def pull():
    """git pull local"""
    log("Atualizando cópia local")
    local('git pull origin master')


def commit_push(message=None):
    """commit e push local"""
    if message:
        co(message=message)
        pull()
        push()

def remote_pull():
    """git pull remoto"""
    log('Atualizando aplicação no servidor')
    with cd(project_path):
        run('git pull origin master')

def cw():
    """inicia o compass local no modo watch"""
    local('compass watch app/static')

def compass_compile():
    """compila o compassa remoto"""
    log('Compilando arquivos SASS')
    with cd(project_path):
        run('compass compile -e production app/static')

def manage(cmd=None):
    """executa comandos no manage.py remoto"""
    if cmd:
        run('source %s; python manage.py %s' % (env_path, cmd))

def collectstatic():
    """collectstatic remoto"""
    log('Coletando arquivos estáticos')
    with cd(project_path):
        manage('collectstatic --noinput --ignore scss --ignore *.rb')

def remote_migrate_all():
    """migrate remoto"""
    log('Executando migração remota do banco de dados')
    with cd(project_path):
        manage('migrate')
        
def migrate():
    """migrate local"""
    log('Executando migração do banco de dados')
    local('python manage.py migrate')

def compress():
    """compress remoto"""
    log('Compactando arquivos JavaScript e CSS')
    with cd(project_path):
        manage('compress')

def restart_server():
    """reinicia nginx e uwsgi"""
    log('Reiniciando serviços do servidor (NGINX, WSGI)')
    sudo('/etc/init.d/nginx stop')
    sudo('/etc/init.d/nginx start')
    run('stop_uwsgi')
    run('start_uwsgi')

def restart_media_server():
    """reinicia o servidor de media"""    
    log('Reiniciando serviços do servidor de media (NGINX)')
    env.hosts = [media_server]
    sudo('/etc/init.d/nginx stop')
    sudo('/etc/init.d/nginx start')

def revert():
    """ Revert git via reset --hard @{1} """
    log('Revertendo aplicação para o ultimo commit')
    with cd(project_path):
        run('git reset --hard @{1}')

def update_requirements():
    """instala as dependencias no servidor"""
    pull()
    push()
    remote_pull()    
    with cd(project_path):
        run('source %s; pip install -r requirements.txt' % env_path ) 

def translate():
    "atualiza os arquivos de tradução e compila"
    log('Atualizando traduções en, es')
    local('django-admin.py makemessages --locale=en --ignore=app/templates/admin --ignore=app/settings.py')
    local('django-admin.py makemessages --locale=es --ignore=app/templates/admin --ignore=app/settings.py')
    local('django-admin.py compilemessages')

def translate_remote():
    "compila tradução no servidor"
    log('compilando tradução no servidor')
    with cd(project_path):
        run('source %s; django-admin.py compilemessages')

def upload_public_key():
    """faz o upload da chave ssh para o servidor"""
    log('Adicionando chave publica no servidor')
    ssh_file = '~/.ssh/id_rsa.pub'
    target_path = '~/.ssh/uploaded_key.pub'
    put(ssh_file, target_path)
    run('echo `cat ~/.ssh/uploaded_key.pub` >> ~/.ssh/authorized_keys && rm -f ~/.ssh/uploaded_key.pub')

def linux():
    username = 'root'
    prod_server = '%s@10.42.43.18' % username
    project_path = '/DADOS/ProjetosPython/zipper_galeria/03_site/project'
    env_path = '/root/envs/zipper/bin/activate'

def login():
    local("ssh %s" % prod_server)

def log(message):
    print """
==============================================================
%s
==============================================================
    """ % message