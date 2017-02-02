Starting the worker process

    celery -A proj worker -l info
Start the celery beat service using the django scheduler:

    celery -A proj beat -l info -S django
后台
    
    nohup celery -A proj beat -l info -S django