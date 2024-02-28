import random
import os
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] =\
    'sqlite:///' + os.path.join(basedir, 'database.db')

db = SQLAlchemy(app)

# computer=컴퓨터의 선택, user=사용자의 선택, result=가위바위보 결과
class Rsp(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    computer = db.Column(db.String(10), nullable=False)
    user = db.Column(db.String(10), nullable=False)
    result = db.Column(db.String(50), nullable=False)


with app.app_context():
    db.create_all()


@app.route('/')
def home():
    rsp_result = Rsp.query.all()

    total_win = Rsp.query.filter_by(result="승리!!").count()
    total_lose = Rsp.query.filter_by(result="패배ㅠㅠ").count()
    total_draw = Rsp.query.filter_by(result="무승부").count()

    return render_template('index.html', data=rsp_result, win=total_win, lose=total_lose, draw=total_draw)


@app.route('/rsp_value', methods=['POST'])
def rsp_value():
    # form으로 데이터 입력 받기
    rock_receive = request.form.get("rock")
    scissors_receive = request.form.get("scissors")
    paper_receive = request.form.get("paper")

    # 가위 바위 보 입력 받은 값으로 연산
    computer, user, result = 0, 0, 0

    # 가위, 바위, 보 리스트
    rsp_list = ['rock', 'scissors', 'paper']
    random_computer = random.choice(rsp_list)

    # 가위,바위,보 연산
    if scissors_receive == "scissors":
        if random_computer == "scissors":
            user = "✌"
            computer = "✌"
            result = "무승부"
        elif random_computer == "rock":
            user = "✌"
            computer = "✊"
            result = "패배ㅠㅠ"
        elif random_computer == "paper":
            user = "✌"
            computer = "🖐"
            result = "승리!!"
    elif rock_receive == "rock":
        if random_computer == "scissors":
            user = "✊"
            computer = "✌"
            result = "승리!!"
        elif random_computer == "rock":
            user = "✊"
            computer = "✊"
            result = "무승부"
        elif random_computer == "paper":
            user = "✊"
            computer = "🖐"
            result = "패배ㅠㅠ"
    elif paper_receive == "paper":
        if random_computer == "scissors":
            user = "🖐"
            computer = "✌"
            result = "패배ㅠㅠ"
        elif random_computer == "rock":
            user = "🖐"
            computer = "✊"
            result = "승리!!"
        elif random_computer == "paper":
            user = "🖐"
            computer = "🖐"
            result = "무승부"

    rsp = Rsp(computer=computer, user=user, result=result)
    db.session.add(rsp)
    db.session.commit()

    return redirect(url_for('home'))

@app.route('/delete_rsp', methods=['POST'])
def delete_rsp():
    db.session.query(Rsp).delete()
    db.session.commit()
    
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
