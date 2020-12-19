# from flask_wtf.file import FileField
# from flask_wtf import FlaskForm
# from flask import Flask, render_template
# from werkzeug.utils import secure_filename
# import os
# from flask_bootstrap import Bootstrap
# from wtforms import StringField, DateField, RadioField, SelectMultipleField
# from wtforms.validators import DataRequired, InputRequired, Length
#
#
#
# class PhotoForm(FlaskForm):
#     name = StringField(label='姓名', validators=[InputRequired()])
#     city = StringField('城市', validators=[Length(min=4, max=25, message='输入的长度不符合要求')])
#     birthday = DateField(label='生日', format="%Y-%m-%d", validators=[DataRequired('日期格式不正确')])
#     gender = RadioField(label='性别', choices=[(1, 'male'), (2, 'female')])
#     interest = SelectMultipleField(label='兴趣', choices=[(1, 'Football'), (2, 'Movies'), (3, 'Reading')])
#
#
# app2 = Flask(__name__)  # 创建一个 Flask 应用
# app2.secret_key = 'abcd'
# app2.config['UPLOAD_FOLDER'] = './file'
# bootstrap = Bootstrap(app2) # 为应用初始化 bootstrap
#
#
# @app2.route('/upload', methods=['GET', 'POST'])
# def upload():
#     form = PhotoForm()
#     filepath = None
#     if form.validate_on_submit():
#         filename = secure_filename(form.photo.data.filename)
#         file = form.photo.data
#         filepath = os.path.join(app2.config['UPLOAD_FOLDER'], filename)
#         file.save(filepath)
#     else:
#         filename = None
#     return render_template('upload.html', form=form, filename=filename)
#
#
# if __name__ == '__main__':
#     app2.run(debug=True, port=8080)
