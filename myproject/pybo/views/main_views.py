from flask import Blueprint

# 블루프린트 객체 생성
bp = Blueprint('main', __name__, url_prefix='/')

# 라우트 함수 등록
@bp.route('/hello')
def hello_pybo():
    return 'Hello, World!!'

# Router 함수 등록 root
@bp.route('/')
def index():
    return 'Pybo index'

# Blueprint의 3번째 인자 url_prefix는 접두어 URL을 정할 때 사용한다.
# 예를 들어 url_prefix가 '/main'이라고 가정하면, http://localhost:5000/main 이후에 route가 적용된다.