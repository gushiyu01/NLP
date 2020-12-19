from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired
from flask import Flask, render_template, redirect
from changestep import do_it

app = Flask(__name__)  # 创建一个 Flask 应用
app.secret_key = 'abc'


class MyForm(FlaskForm):
    name = StringField('name', validators=[DataRequired()])
    age = StringField('age', validators=[DataRequired()])


@app.route('/', methods=('GET', 'POST'))
def submit():
    form = MyForm()
    print(form.name.data)
    print(form.age.data)
    if form.validate_on_submit():
        return redirect('/success')
    return render_template('submit.html', form=form)


@app.route('/success')
def success():
    return render_template('success.html')


if __name__ == '__main__':
    app.run(debug=True, port=8080)
