import random
import os
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] =\
    'sqlite:///' + os.path.join(basedir, 'database.db')

db = SQLAlchemy(app)


class Rsp(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    computer = db.Column(db.String(10), nullable=False)
    user = db.Column(db.String(10), nullable=False)
    result = db.Column(db.String(50), nullable=False)


with app.app_context():
    db.create_all()


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/', methods=['POST'])
def rsp_create():
    # form으로 데이터 입력 받기
    rock_receive = request.args.get("rock")
    scissors_receive = request.args.get("scissors")
    paper_receive = request.args.get("paper")

    # 가위 바위 보 입력 받은 값으로 연산
    result_computer = 0
    result_user = 0
    result = 0

    # 
    rsp = Rsp(computer=result_computer,
              user=result_user, result=result)
    db.session.add(rsp)
    db.session.commit()

    return 'Data received and stored successfully!'


if __name__ == '__main__':
    app.run(debug=True)
