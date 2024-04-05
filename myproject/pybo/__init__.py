from flask import Flask
# flask_migrate는 파이썬에서 사용하는 데이터베이스 관리 툴인 alembic을 flask에서도 사용할 수 있도록 제공함.
from flask_migrate import Migrate
# Sqlalchemy => Python ORM Library
from flask_sqlalchemy import SQLAlchemy
# create_app 함수명은 Flask에서 정의한 이름으로, 다른 이름 사용시 실행하지 않는다.
# 플라스크 서버 실행시 create_app함수를 실행하는 것.

# 3.30에 추가된 내용
import config

# 객체를 생성 => 전역에 선언해야함
# 블루프린트 같은 타 모듈에서 불러올 수 있어야함.
db = SQLAlchemy()
migrate = Migrate()

# create_app함수는 main함수의 역할이라고 생각함. => 반드시 있어야함.
def create_app():
    # Flask 애플리케이션 생성
    app = Flask(__name__) # 모듈명 전달

    # config.py의 작성된 항목을 app.config 환경 변수로 부르기 위해서 사용됨.
    app.config.from_object(config)

    # ORM
    # db 초기화
    db.init_app(app)
    # migrate 초기화
    migrate.init_app(app, db)

    # migrate객체가 models.py을 참조해야함.
    from . import models

    # views 디렉터리에서 main_views와 question_views을 가져온다.
    from .views import main_views, question_views, answer_views

    # blueprint를 등록한다.
    app.register_blueprint(main_views.bp)
    app.register_blueprint(question_views.bp)
    app.register_blueprint(answer_views.bp)
    return app

