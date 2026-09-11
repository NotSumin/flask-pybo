from flask import Blueprint, render_template, redirect, url_for, request
from datetime import datetime
from pybo.models import Question
from pybo import db

bp = Blueprint('question', __name__, url_prefix='/question')

@bp.route('/list')
def _list():
    question_list = Question.query.order_by(Question.create_date.desc()).all()
    return render_template('question/question_list.html', question_list=question_list)

@bp.route('/detail/<int:question_id>/')
def detail(question_id):
    question = Question.query.get_or_404(question_id)
    return render_template('question/question_detail.html', question=question)

@bp.route('/create', methods=['POST'])
def create():
    content = request.form['content']
    subject = request.form['subject']

    question = Question(subject=subject, content=content, create_date=datetime.now())
    db.session.add(question)
    db.session.commit()
    return redirect(url_for('question._list'))