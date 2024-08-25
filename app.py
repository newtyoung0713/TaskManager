from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db'  # Using SQLite Database
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)

class Task(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  title = db.Column(db.String(100), nullable=False)
  description = db.Column(db.String(200), nullable=True)
  priority = db.Column(db.String(50), nullable=False)
  due_date = db.Column(db.DateTime, nullable=False)
  status = db.Column(db.String(50), nullable=False)

@app.route('/')
def index():
  tasks = Task.query.order_by(Task.due_date).all()
  return render_template('index.html', tasks=tasks)

@app.route('/create', methods=['GET', 'POST'])
def create_task():
  if request.method == 'POST':
    title = request.form['title']
    description = request.form['description']
    priority = request.form['priority']
    due_date = datetime.strptime(request.form['due_date'], '%Y-%m-%d')
    new_task = Task(title=title, description=description, priority=priority, due_date=due_date, status="Pending")
    db.session.add(new_task)
    db.session.commit()
    return redirect(url_for('index'))
  return render_template('create_task.html')

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_task(id):
  task = Task.query.get_or_404(id)  # If did not get anything, return 404
  if request.method == 'POST':
    task.title = request.form['title']
    task.description = request.form['description']
    task.priority = request.form['priority']
    task.due_date = datetime.strptime(request.form['due_date'], '%Y-%m-%d')
    task.status = request.form['status']
    
    db.session.commit()
    return redirect(url_for('index'))
  return render_template('edit_task.html', task=task)

@app.route('/delete/<int:id>', methods=['POST'])
def delete_task(id):
  task = Task.query.get_or_404(id)  # If did not get anything, return 404
  db.session.delete(task)
  db.session.commit()
  return redirect(url_for('index'))

if __name__ == '__main__':
  app.run(debug=True)