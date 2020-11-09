## como rodar o projeto ?
* Clone esse repositório
* Crie um virtualenv com Python3
* Ative o virtualenv (source .venv/bin/activate)
* Intale as dependências
* Rode as migrações
...
* git clone https://github.com/daabraga/estoque
* cd estoque
* python3 -m venv .venv
* source .venv/bin/activate
* pip install -r requirements.txt
* python3 contrib/env_gen.py
* python3 manage.py migrate
* python3 manage.py createsuperuser
* python3 manage.py runserver


## Links

[Python decouple] https://github.com/henriquebastos/python-decouple

https://simpleisbetterthancomplex.com/2015/11/26/package-of-the-week-python-decouple.html
