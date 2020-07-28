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

### 참조 링크
[Django 프로젝트 배포(with docker, nginx, gunicorn)](https://teamlab.github.io/jekyllDecent/blog/tutorials/docker%EB%A1%9C-django-%EA%B0%9C%EB%B0%9C%ED%95%98%EA%B3%A0-%EB%B0%B0%ED%8F%AC%ED%95%98%EA%B8%B0(+-nginx,-gunicorn))

[Django 설치 가이드-1](https://inma.tistory.com/125)

[Django 설치 가이드-2](https://soyoung-new-challenge.tistory.com/74)

[Django with AWS Cognito](https://djangostars.com/blog/bootstrap-django-app-with-cognito/)

[NCP 레퍼런스 아키텍쳐](https://www.ncloud.com/intro/architecture)
