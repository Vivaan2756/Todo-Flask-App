from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_required, current_user
from app.models import Task
from app import db

tasks_bp = Blueprint('tasks', __name__)

@tasks_bp.route('/')
@login_required
def view_tasks():
    tasks = Task.query.filter_by(user_id=current_user.id).all()
    return render_template("tasks.html", tasks=tasks)

@tasks_bp.route('/add', methods=['POST'])
@login_required
def add_task():
    title = request.form.get('title')
    if title:
        new_task = Task(title=title, status="Pending", user_id=current_user.id)
        db.session.add(new_task)
        db.session.commit()
    return redirect(url_for("tasks.view_tasks"))

@tasks_bp.route('/toggle/<int:id>', methods=['POST'])
@login_required
def toggle_status(id):
    task = Task.query.get(id)
    if task and task.user_id == current_user.id:
        if task.status == "Pending":
            task.status = "Working"
        elif task.status == "Working":
            task.status = "Done"
        else:
            task.status = "Pending"
        db.session.commit()
    return redirect(url_for("tasks.view_tasks"))

@tasks_bp.route('/clear', methods=["POST"])
@login_required
def clear_tasks():
    tasks = Task.query.filter_by(user_id=current_user.id).all()
    for task in tasks:
        db.session.delete(task)
    db.session.commit()
    flash('All tasks cleared')
    return redirect(url_for("tasks.view_tasks"))



    