# 3.31 질문 조회 및 질문 상세 내용 조회 기능 구현

from flask import Blueprint, render_template, redirect, url_for

# 데이터 처리할 모델 불러오기
from pybo.models import Question

from ..forms import QuestionForm

bp = Blueprint('question', __name__, url_prefix='/question')

# 라우터 함수 등록
@bp.route('/list')
def list():
    # Quesion의 create_date를 기준으로 내림차순한 리스트 조회
    question_list = Question.query.order_by(Question.create_date.desc())
    # render_template(template_name[html], content[data])
    return render_template('question/question_list.html', question_list=question_list)

# /detail/1
# /detail/2
# 다음과 같이 url의 parameter를 추가로 받기 위해서는 마지막에 /으로 닫아야함.
@bp.route('/detail/<int:question_id>/')
def detail(question_id):
    # id을 통해 question값을 가져오고
    # question = Question.query.get_or_404(question_id)
    question = Question.query.get(question_id)
    return render_template('question/question_detail.html', question=question)

# 질문 등록
@bp.route('/create/')
def create():
    print("create 되었다 맨이야!")
    # rediect에도 url_for를 사용하여 question.views.py의 list함수를 실행한다.
    form = QuestionForm()
    return render_template('question/question_form.html', form=form)