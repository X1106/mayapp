from wtforms.form import Form
from wtforms.fields import StringField, PasswordField, SubmitField,TextAreaField
from wtforms.validators import DataRequired, Email, EqualTo
from wtforms import ValidationError
from wtforms.widgets import TextArea    
from Flask .models import User

class LoginForm(Form):
    email = StringField('ログインID ', validators=[DataRequired(), Email()],default="portfolio@gmail.com")
    password = PasswordField('パスワード', validators=[DataRequired()])
    submit = SubmitField('ログイン')

class RegisterForm(Form):
    email = StringField('e-mail: ', validators=[DataRequired(),Email('メールアドレスが誤っています')])
    username = StringField('名前: ', validators=[DataRequired()])
    password = PasswordField(
        'パスワード:', validators=[DataRequired(), EqualTo('password_confirm', message='パスワードが一致しません')]
    )
    password_confirm = PasswordField('パスワード確認: ', validators=[DataRequired()])
    submit = SubmitField('登録')

    def validate_email(self, field):
        if User.select_by_email(field.data):
            raise ValidationError('メールアドレスは既に登録されています')

class UserForm(Form): 
    name2 = StringField('会社名',validators=[DataRequired('会社名を入力して下さい')])
    manager2 = StringField('ご担当者名',validators=[DataRequired('名前を入力して下さい')])
    mail2 = StringField('連絡先',validators=[DataRequired('連絡先を入力して下さい')])
    memo2=TextAreaField('コメント',widget=TextArea())
    submit = SubmitField('送信')



    