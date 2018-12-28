# coding :utf-8
from functools import wraps
from flask import session,redirect,url_for


#登录限制装饰器                                                               没看懂
def login_required(func):
    @wraps(func)
    def warpper(*args,**kwargs):
        if session.get('user_id'):
            return func(*args,**kwargs)
        else:
            return redirect(url_for('login'))
    return warpper
