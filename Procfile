release: python3 manage.py migrate
web: gunicorn loja.wsgi --preload --log-file -
web2: uvicorn loja.asgi:application 