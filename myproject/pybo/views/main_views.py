from flask import Blueprint, render_template, url_for
from werkzeug.utils import redirect
# 블루프린트 객체 생성
# Blueprint의 3번째 인자 url_prefix는 접두어 URL을 정할 때 사용한다.
bp = Blueprint('main', __name__, url_prefix='/')

# 라우트 함수 등록
# 예를 들어 url_prefix가 '/main'이라고 가정하면, http://localhost:5000/main 이후에 route가 적용된다.

@bp.route('/')
def home():
    # views/question_list으로 리다이렉트
    # 플라스크에서 제공하는 url_for을 사용함.
    return redirect(url_for('question.list'))



