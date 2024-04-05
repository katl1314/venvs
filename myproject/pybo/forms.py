# 플라스크 폼 모듈을 불러오고...
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired

# 질문 폼 생성
class QuestionForm(FlaskForm):
    # StringField(label, validators=[wtforms.validators]
    subject = StringField('제목', validators=[DataRequired()])
    content = TextAreaField('내용', validators=[DataRequired()])