## como rodar o projeto ?
* Clone esse repositório
* Crie um virtualenv com Python3
* Ative o virtualenv
* Intale as dependências
* Rode as migrações
...
git clone https://gitjub.com/rg3915/estoque.git
cd estoque
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python contrib/env_gen.py
python manage.py migrate

## Links

Python decouple: https://github.com/henriquebastos/python-decouple

https://simpleisbetterthancomplex.com/2015/11/26/package-of-the-week-python-decouple.html