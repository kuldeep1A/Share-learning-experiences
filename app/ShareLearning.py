from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///experiences.db'
db = SQLAlchemy(app)


class Experience(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    image = db.Column(db.String(100))
    video = db.Column(db.String(100))
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)


@app.route('/')
def experience_list():
    experiences = Experience.query.all()
    return render_template('experience_list.html', experiences=experiences)


@app.route('/experiences/<int:id>')
def experience_detail(id):
    experience = Experience.query.get(id)
    return render_template('experience_detail.html', experience=experience)


@app.route('/experiences/new', methods=['GET', 'POST'])
def experience_create():
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        image = request.form['image']
        video = request.form['video']
        experience = Experience(title=title, description=description, image=image, video=video)
        db.session.add(experience)
        db.session.commit()
        return redirect(url_for('experience_list'))
    else:
        return render_template('experience_create.html')


if __name__ == '__main__':
    app.run(debug=True)
