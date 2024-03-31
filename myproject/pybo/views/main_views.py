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

"""
url_for: Flask의 기능으로 라우트가 설정한 함수명으로 URL을 역으로 찾아준다. 
.을 구분하여 앞에서부터 뒤로 해석하여 함수를 찾는다.
question은 등록된 블루프린트 이름, list는 함수를 의미한다.

werkzeug.utils의 기능 redirect는 지정한 url을 리다이렉터 한다.
"""

