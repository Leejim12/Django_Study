# Django

- 시작일 : 230109

### mysql 쓰고싶을때
1. mysql client install
> pip install mysqlclient

2. setting.py 설정
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'test',
        'USER':'root',
        'PASSWORD':'tiger',
        'HOST':'localhost',
        'PORT':'3306',
    }
}
```