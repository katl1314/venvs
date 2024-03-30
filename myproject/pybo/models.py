from pybo import db

# 모델 정의
class Question(db.Model):
    # primary_key: 기본키(PK) 여부
    id = db.Column(db.Integer, primary_key=True)
    # nullable : null 허용 여부 False or True
    # db.String(maxLength) : 글자수 지정된 문자열
    subject = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text(), nullable=False)
    create_date = db.Column(db.DateTime(), nullable=False)
# 답변 모델 정의
class Answer(db.Model):
    # id는 db.Integer타입이면서 기본키
    id = db.Column(db.Integer, primary_key=True)
    # ForeignKey: 외래키(FK) 지정
    # db.ForeignKey(연결할 기존 모델의 속성, ondelete='CASCADE'[삭제 시 연동])
    question_id = db.Column(db.Integer, db.ForeignKey('question.id', ondelete='CASCADE'))
    # db.relationship <= 타 모델을 참조한다. (모델명, backref <= 역참조)
    question = db.relationship('Question', backref=db.backref('answer_set',))
    content = db.Column(db.Text(), nullable=False)
    create_date = db.Column(db.Date, nullable=False)