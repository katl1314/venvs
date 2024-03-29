## Pybo Project

### 목표
Flask를 이용한 간단한 CRUD 프로젝트 구성

### 개발 환경 셋팅
**파이썬 설치**: 
https://www.python.org/downloads/

**가상 환경 셋팅**

venvs 모듈을 이용한 가상환경 생성 (이름: myproject)
```commandline
python -m venvs myproject
```

### 생성된 가상 환경에 접근하기
```commandline
cd Scripts
activate
```
그러면 명령 프롬프트 맨 앞에 가상 환경 이름이 표시됨.

### Flask 설치
pip를 이용하여 Flask를 설치한다.
```commandline
pip install Flask
```

### Flask 서버 실행
```commandline
set FLASK_APP=pybo # Flask application 셋팅
flask run
```
만약 환경변수 FLASK_APP에 pybo라는 값을 설정하면
pybo.py가 있으면 pybo.py를 가리킬것이고, pybo.py파일이 아닌 pybo폴더가 있으면 자동으로
pybo폴더를 가리키게 된다.

pybo/__init__.py 파일 내부는 다음과 같다.
```python
from flask import Flask

# create_app 함수명은 Flask에서 정의한 이름으로, 다른 이름 사용시 실행하지 않는다.
# 플라스크 서버 실행시 create_app함수를 실행하는 것.
def create_app():
    # Flask 애플리케이션 생성
    # __name__ <= 모듈명
    app = Flask(__name__)

    @app.route('/')
    def home():
        return 'Hello, World!!!'
    return app
```
Flask는 기본적으로 create_app함수를 서버 실행 시 호출하도록 되어있음
다른 이름 사용시 동작하지 않는다.


## 파이썬 모듈
```python
import 모듈
```
모듈 내 모든 기능들을 가져온다.

```python
from 모듈 import 이름
```
모둘 내에서 원하는 기능만 가져온다.
예를 들어
```python
from 공구통 import 플라이어
```