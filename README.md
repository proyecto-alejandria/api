API del Proyecto Alejandría
===========================

Requisitos para desarrollo:

* Python 3.10 + pip

## Configuración

La configuración del sistema se carga mediante [django-environ](https://django-environ.readthedocs.io/en/latest/) a través del fichero `.env`; se proporciona un fichero `.env.example` de ejemplo. Los [URIs](https://es.wikipedia.org/wiki/Identificador_de_recursos_uniforme) deben seguir el [formato apropiado](https://datatracker.ietf.org/doc/html/rfc3986#section-3).

> Es necesario establecer la variable `SECRET_KEY` para ejecutar el servidor de desarrollo de Django.

Las variables disponibles son las siguientes:

### Principal

#### `SECRET_KEY`

* Tipo: `str`
* Sin valor por defecto

Establece el [`SECRET_KEY` de Django](https://docs.djangoproject.com/en/4.0/ref/settings/#std:setting-SECRET_KEY).

#### `DEBUG`

* Tipo: `bool`
* Valor por defecto: `True`

Establece el [`DEBUG` de Django](https://docs.djangoproject.com/en/4.0/ref/settings/#std:setting-DEBUG).

Adicionalmente, se utiliza para configurar determinadas entradas de configuración como los validadores de contraseña 

#### `DB_URL`

* Tipo: URI
* Valor por defecto: `db.sqlite3` junto al `manage.py`

Utilizado para establecer la base de datos por defecto en la entrada [`DATABASES` de Django](https://docs.djangoproject.com/en/4.0/ref/settings/#std:setting-DATABASES).

### Seguridad

#### `ALLOWED_HOSTS`

* Tipo: lista de `str`
* Valor por defecto: `[]`

Establece el [`ALLOWED_HOSTS` de Django](https://docs.djangoproject.com/en/4.0/ref/settings/#std:setting-ALLOWED_HOSTS).

#### `USE_HTTPS`

* Tipo: `bool`
* Valor por defecto: `False`

Establece si determinados elementos (principalmente cookies) deben servirse solamente sobre HTTPs.

### Comunicación

#### `ADMINS`

* Tipo: lista de `str`
* Valor por defecto: `[]`

Establece el [`ADMINS` de Django](https://docs.djangoproject.com/en/4.0/ref/settings/#std:setting-ADMINS).

El valor se analiza y transforma al formato apropiado utilizando [`getaddresses`](https://docs.python.org/3/library/email.utils.html#email.utils.getaddresses).

#### `DEFAULT_FROM_EMAIL`

* Tipo: `str`
* Valor por defecto: la dirección de e-mail del proyectoa

Establece el [`DEFAULT_FROM_EMAIL` de Django](https://docs.djangoproject.com/en/4.0/ref/settings/#std:setting-DEFAULT_FROM_EMAIL).

#### `EMAIL_URL`

* Tipo: URI
* Sin valor por defecto
* El valor es necesario cuando `DEBUG` es `False`

Establece el [`DEFAULT_FROM_EMAIL` de Django](https://docs.djangoproject.com/en/4.0/ref/settings/#std:setting-DEFAULT_FROM_EMAIL).

En modo `DEBUG`, se utiliza el *backend* de correo por consola; en caso contrario, es necesario establecer esta entrada de configuración.

#### `EMAIL_USE_SSL`

* Tipo: `bool`
* Valor por defecto: `True`

Establece el [`EMAIL_USE_SSL` de Django](https://docs.djangoproject.com/en/4.0/ref/settings/#std:setting-EMAIL_USE_SSL).
