from flask import Blueprint, render_template

# 블루프린트 객체 생성
bp = Blueprint('main', __name__, url_prefix='/')

# 3.31 질문 조회 및 질문 상세 내용 조회 기능 구현

# 모델 객체를 불러오고...
from pybo.models import Question, Answer

# 라우트 함수 등록
@bp.route('/')
def root():
    # Quesion의 create_date를 기준으로 내림차순한 리스트 조회
    question_list = Question.query.order_by(Question.create_date.desc())
    # render_template(template_name[html], content[data])
    return render_template('question/question_list.html', question_list=question_list)

# Blueprint의 3번째 인자 url_prefix는 접두어 URL을 정할 때 사용한다.
# 예를 들어 url_prefix가 '/main'이라고 가정하면, http://localhost:5000/main 이후에 route가 적용된다.