#!/usr/bin/env python
import os
import sys

'''
# 默认端口 8000
python manage.py runserver

# 指定 IP 和端口（如果需要外部访问）
python manage.py runserver 0.0.0.0:8000
'''
if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'web_t.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)
