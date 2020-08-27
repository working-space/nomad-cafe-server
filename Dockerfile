FROM python:3.7

ENV PYTHONUNBUFFERED 1

RUN mkdir /wwwroot
WORKDIR /wwwroot

ADD requirements.txt /wwwroot/

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

ADD . /wwwroot/

# 하위에 DJANGO 설정 값 환경 변수로 추가
ENV DJANGO_SECRET_KEY <KEY>
ENV DJANGO_DEBUG False
ENV DJANGO_ALLOWED_HOSTS <HOST GROUPS SEPERATED BY SPACE>
ENV DB_NAME <NAME>
ENV DB_HOST <HOST>

RUN python manage.py collectstatic --noinput