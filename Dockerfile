# FROM python:3.6.5-slim
# WORKDIR /app/src
# RUN pip install Django==2.0.7
# RUN django-admin startproject trydjango
# CMD ["python", "./trydjango/manage.py", "runserver", "0.0.0.0:8000"]

FROM python:3.8

# 시스템 업데이트 및 필요한 라이브러리 설치
RUN apt-get update && apt-get install -y \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# 작업 디렉토리 설정
WORKDIR /mysite

COPY . /mysite/

RUN pip install Django
RUN pip install pymysql
RUN pip install mysqlclient
RUN pip install bootstrap4
RUN pip install posts
RUN pip install cryptography


#RUN python3 manage.py startapp board
#RUN python3 manage.py startapp blog
#RUN python3 manage.py startapp common



# Django 설정 파일 및 앱 설정 파일 복사
COPY ./main/settings.py /main/mysite/config/

WORKDIR ./main/mysite/

# 데이터베이스 마이그레이션
# RUN python manage.py makemigrations
# RUN python manage.py migrate

# # 슈퍼유저 생성
# RUN python manage.py createsuperuser --noinput \
#     --username=admin \
#     --email=admin@example.com

# Django 서버 실행
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

