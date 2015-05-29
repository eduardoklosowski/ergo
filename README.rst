Ergo
====

.. _Bower: http://bower.io/
.. _Django: https://www.djangoproject.com/
.. _Ergo: https://github.com/eduardoklosowski/ergo
.. _Python: https://www.python.org/

Este é o core do projeto Ergo.


Requisitos
----------

- Bower_
- Python_ 2.7 ou 3
- Django_ 1.8


Instalação
----------

- Tenha o Bower_ e Python_ instalado no sistema.
- Instale o Ergo_ com o `pip`::

    pip install https://github.com/eduardoklosowski/ergo/archive/master.zip

- Crie os arquivos de configuração com o comando::

    python -m ergo initconfig

- Configure o `SECRET_KEY` no arquivo `settings.py`.


Banco de Dados
~~~~~~~~~~~~~~

- Crie o banco de dados com o `migration`::

    python manage.py migrate

- Crie um usuário::

    python manage.py createsuperuser


Arquivos Estáticos
~~~~~~~~~~~~~~~~~~

- Atualize os pacotes do Bower_::

    python manage.py bower install

- Colete os arquivos estáticos::

    python manage.py collectstatic

- Gere o cache dos arquivos::

    python manage.py compress


Iniciar Servidor (Gunicorn)
~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Instalar os pacotes `gunicorn` e `dj-static` com o `pip`::

    pip install gunicorn dj-static

- Iniciar o serviço e conectar em http://127.0.0.1:8080/::

    gunicorn -b 0.0.0.0:8080 wsgistatic --access-logfile - --error-logfile -


Licença
-------

Este projeto é distribuido sobre a licença GNU Affero General Public License (veja LICENSE).
