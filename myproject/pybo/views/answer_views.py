from flask import Blueprint, url_for, request, render_template
from werkzeug.utils import redirect
from datetime import datetime
from pybo import db
from pybo.models import Answer, Question
from ..forms import AnswerForm

bp = Blueprint('answer', __name__, url_prefix='/answer')

@bp.route('/create/<int:question_id>/', methods=('post',))
def create(question_id):
    form = AnswerForm()
    question = Question.query.get(question_id)

    print('form.data ---- ', form.data)
    print('form.validate_on_submit() ---- ', form.validate_on_submit())

    if form.validate_on_submit():
        content = form.data['content']

        answer = Answer(content=content, create_date=datetime.now())
        # question객체를 통해 역참조하는 answer을 사용하여 추가한다.
        question.answer_set.append(answer)
        db.session.commit()
        return redirect(url_for('question.detail', question_id=question_id))

    return render_template('question/question_detail.html', form=form, question=question)
