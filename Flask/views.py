from flask import Blueprint,render_template,request,redirect,session,url_for
from Flask.forms import LoginForm, RegisterForm,UserForm
from Flask.models import User
from flask_login import login_user, login_required, logout_user
from flask_mail import Mail
from flask_mail import Message

bp = Blueprint('app', __name__, url_prefix='')
mail = Mail()

@bp.route('/',methods=['GET','POST'])
def home():
    return render_template('home.html')

@bp.route('/logout')
@login_required
def logout():
    logout_user() 
    return redirect(url_for('app.home'))

@bp.route('/login',methods=['GET','POST'])
def login():
    form = LoginForm(request.form)
    if request.method == 'POST' and form.validate():
        user = User.select_by_email(form.email.data)
        if user and user.validate_password(form.password.data):
            login_user(user, remember=True)
            next = request.args.get('next')
            if not next:
                next = url_for('app.portfolio')
            return redirect(next)
    return render_template('login.html',form=form)

@bp.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm(request.form)
    if request.method == 'POST' and form.validate():
        user = User(
            email = form.email.data,
            username = form.username.data,
            password = form.password.data
        )
        user.add_user()
        return redirect(url_for('app.portfolio'))
    return render_template('register.html', form=form)

@bp.route('/portfolio')
@login_required
def portfolio(): 
    return render_template('portfolio.html')

def sendCntactForm():
     msg=Message('aswdc',sender='x1106ktag@gmail.com',
     recipients=['x1106ktag@gmail.com'])
     msg.body="エントリー連絡"
     msg.html =render_template('send_mail.html')
     mail.send(msg)

@bp.route('/inquiry',methods=['GET','POST'])
def inquiry():
    form = UserForm(request.form)
    if request.method == "POST" and form.validate():
        session['name2'] = form.name2.data
        session['manager2'] = form.manager2.data
        session['mail2'] = form.mail2.data
        session['memo2'] = form.memo2.data
        sendCntactForm()
        return redirect(url_for('app.send_out'))  
    return render_template('inquiry.html',form=form)

@bp.route('/send_out',methods=['GET','POST'])
def send_out():
    return render_template('send_out.html')