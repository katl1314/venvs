# 플라스크 폼 모듈을 불러오고...
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired

# 질문 폼 생성 FlaskForm을 상속받는다.
# 제목 필드는 길이가 고정인 StringField를 사용
# 콘텐츠는 글자 수 제한이 없는 TextField를 사용
# validators을 통해 유효성 검사 기능 추가 가능
# DataRequired() => 필수 입력 여부
# Length() => 길이 점검
# Email() => 이메일 포맷 여부

class QuestionForm(FlaskForm):
    # StringField(label, validators=[wtforms.validators]
    subject = StringField('제목', validators=[DataRequired('제목 항목을 필수입니다.')])
    content = TextAreaField('내용', validators=[DataRequired('내용은 필수입니다.')])

class AnswerForm(FlaskForm):
    content = TextAreaField('내용', validators=[DataRequired('내용은 필수입니다.')])