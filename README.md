# nomad-cafe-server
8기 7조 디지털 노마드를 위한 주변 카페 알리미(Server)
---

### 기술 스택
WAS : Python(Django)   
WS : Nginx   
WSGI : Gunicorn   
DB : MongoDB   
Container : Docker   
Authentication : AWS Cognito   
CI/CD : Github Action

### 구조

##### 아키텍쳐(기본 구상안)

![Django With Gunicorn, Nginx and Docker](_images/example_architecture.jpg)

##### 아키텍쳐(W Microservices)

**예시**
![NCP 예시](https://xv-ncloud.pstatic.net/images/architectures/10-1.%20Microservices%20with%20NKS%20%20@2x_1566206781015.png)

##### 아키텍쳐(W/O Microservices)

**예시**
![NCP 예시](https://xv-ncloud.pstatic.net/images/architectures/1-1_%EC%86%8C%EA%B7%9C%EB%AA%A8%20%EC%9B%B9%EC%82%AC%EC%9D%B4%ED%8A%B8_1558003564488.png)

### WAS

##### Setup

**Docker**

```bash
curl -fsSL https://get.docker.com/ | sudo sh
```

**docker-compose**

```bash
sudo get-apt install docker-compose
```

**django**

```bash
# 개발 초기 단계의 docker-compose를 활용
# Dockerfile, docker-compose.yml 작성 선 진행
# 위 파일의 코드는 파일 참조
# Service name은 docker-compose 내 service name
# App name은 django에서 사용할 app name

docker-compose run <Service name> django-admin.py startproject <Project name> .
docker-compose run <Service name> django-admin.py startapp <App name> .
```

nginx 설정 후 Project folder의 settings.py에서 다음 설정 추가   

```python
# settings.py

...
ALLOWED_HOSTS = ['web'] # nginx에서 설정한 service name
...

```

static file을 한 곳에 몰아주는 설정 추가

`python`
```python
# settings.py

...
STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(BASE_DIR, 'static_root')
...

```

`bash`
```bash
python3 manage.py collectstatic
```


**nginx**

```bash
# project folder 하위의 특정 위치(여기선 config/nginx)에 nginx.conf 작성
# docker-compose.yml에 volume에서 nginx.conf 파일이 작성된 위치 mount
# wwwroot는 Dockerfile 작성 시 root 폴더

services:
    ...
    nginx:
        ...
        volumes:
            - .:/wwwroot
            - ./config/nginx:/etc/nginx/conf.d

# static file 관리를 위해 django의 static file이 모인 폴더 위치 설정
# static_root는 django collectstatic 시 설정한 폴더 이름
server {
    ...
    location /static/ {
        alias /wwwroot/static_root/;
    }
}
```

**gunicorn**

```bash
# requirements.txt에 gunicorn 추가 필수
# 구동은 docker-compose.yml에 작성

services:
    ...
    web: # Service name
        ...
        command: gunicorn was.wsgi:application --bind 0.0.0.0:8000 # was는 django의 project name
```

### 참조 링크
[Django RestAPI Quickstart](https://www.django-rest-framework.org/tutorial/quickstart/)

[Django 프로젝트 배포(with docker, nginx, gunicorn)](https://teamlab.github.io/jekyllDecent/blog/tutorials/docker%EB%A1%9C-django-%EA%B0%9C%EB%B0%9C%ED%95%98%EA%B3%A0-%EB%B0%B0%ED%8F%AC%ED%95%98%EA%B8%B0(+-nginx,-gunicorn))

[Django 설치 가이드-1](https://inma.tistory.com/125)

[Django 설치 가이드-2](https://soyoung-new-challenge.tistory.com/74)

[Django with AWS Cognito](https://djangostars.com/blog/bootstrap-django-app-with-cognito/)

[NCP 레퍼런스 아키텍쳐](https://www.ncloud.com/intro/architecture)

[Github action 정리](https://zzsza.github.io/development/2020/06/06/github-action/)

[Django Static file 처리](https://nachwon.github.io/django-deploy-4-static/)

[Django Testcode 작성](https://new93helloworld.tistory.com/285)