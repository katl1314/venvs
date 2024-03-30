from flask import Flask

# create_app 함수명은 Flask에서 정의한 이름으로, 다른 이름 사용시 실행하지 않는다.
# 플라스크 서버 실행시 create_app함수를 실행하는 것.
def create_app():
    # Flask 애플리케이션 생성
    # __name__ <= 모듈명
    app = Flask(__name__)

    # @app.route('/')
    # def home():
    #     return 'Hello, World!!!'

    # views 디렉터리에서 main_views를 가져온다.
    from .views import main_views
    app.register_blueprint(main_views.bp); #blueprint를 등록한다.
    return app

