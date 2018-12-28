# encoding :utf-8
from flask import Flask,render_template,request,redirect,url_for,session
import config    #导入配置文件
from models import User,Question
from exts import db
from decorators import login_required
from sqlalchemy import or_

app = Flask(__name__)
app.config.from_object(config)
db.init_app(app)


#主页面
@app.route('/')
def index():
    return render_template('index.html')

#登录
@app.route('/login/',methods=['GET','POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        tel = request.form.get('tel')
        password = request.form.get('password')
        user = User.query.filter(User.tel == tel,User.password ==password).first()
        if user:
            # cookie 保存用户的id
            session['user_id'] = user.id
            # 31天记住登录用户
            session.permanent = True
            return redirect(url_for('index'))
        else:
            return '手机或密码错误请确认后再次登录'



#注册
@app.route('/zhuce/',methods=['GET','POST'])
def zhuce():
    if request.method == 'GET':
        return render_template('zhuce.html')
    else:
        tel = request.form.get('tel')
        username = request.form.get('username')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        #手机号码验证
        user = User.query.filter(User.tel == tel).first()
        if user:
            return "该手机号已被注册"
        else:
            if password1 != password2:
                return "两次密码不同"
            else:
                user = User(tel = tel,username = username,password = password1)
                db.session.add(user)
                db.session.commit()
                #注册成功跳转到登录页面
                return redirect(url_for('login'))

#退出登录
@app.route('/zhuxiao/')
def zhuxiao():
    session.clear()
    return redirect(url_for('index'))

#实习报告
@app.route('/baogao/',methods=['GET','POST'])
@login_required
def baogao():
    if request.method == 'GET':
       return render_template('baogao.html')
    else:
        title = request.form.get('title')
        content = request.form.get('content')
        question = Question(title=title,content = content)
        user_id = session.get('user_id')
        user = User.query.filter(User.id == user_id).first()
        question.author = user
        db.session.add(question)
        db.session.commit()
        return redirect(url_for('index'))

#实习内容
@app.route('/neirong/')
def neirong():
    context = {
        'questions': Question.query.all()
    }
    return render_template('neirong.html',**context)

#实习内容查找
@app.route('/serach/')
def serach():
    q = request.args.get('q')
    #通过标题，内容查找
    questions = Question.query.filter(or_(Question.title.contains(q),Question.content.contains(q)))
    return render_template('neirong.html',questions = questions )

@app.context_processor
def my_context_processor():
    user_id = session.get('user_id')
    if user_id:
        user = User.query.filter(User.id == user_id).first()
        if user:
            return {'user': user}
    return {}

if __name__ == '__main__':
    app.run()