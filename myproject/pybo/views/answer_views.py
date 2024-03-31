from flask import Blueprint, url_for, request
from werkzeug.utils import redirect
from datetime import datetime
from pybo import db
from pybo.models import Answer, Question

bp = Blueprint('answer', __name__, url_prefix='/answer')

@bp.route('/create/<int:question_id>/', methods=('post',))
def create(question_id):
    # request객체를 통해 form으로 전달한 값을 추출 가능
    question = Question.query.get(question_id)
    content = request.form['content']
    create_date = datetime.now()
    answer = Answer(content=content, create_date=create_date)
    # 질문에 대한 답변 추가 => 파이썬 리스트 추가 시 append을 이용한다.
    question.answer_set.append(answer);
    db.session.commit(); # 데이터베이스에 데이터 추가 적용
    print("Answer가 추가되었습니다.")
    return redirect(url_for('question.detail', question_id=question_id))