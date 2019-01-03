# --*-- coding:utf-8 --*--
from functools import wraps

from flask import session, jsonify, g
from werkzeug.routing import BaseConverter
from ihome.utils.response_code import RET


class RegexConverter(BaseConverter):
    """自定义静态文件路由转换器"""
    def __init__(self,map,*args):
        super(RegexConverter, self).__init__(map)
        self.regex=args[0]

def login_required(view_func):
    """登录校验装饰器"""
    # 如果希望装饰器装饰之后的函数，依然保留原始的名字和说明文档,就需要使用wraps装饰器，装饰内存函数
    @wraps(view_func)
    def wrapper(*args,**kwargs):
        #从session中或取user_id
        user_id = session.get('user_id')
        if not user_id:
            #用户未登录
            return jsonify(re_code=RET.SESSIONERR,msg='用户未登录')
        else:
            #用户已登录使用g变量保存住user_id
            g.user_id=user_id
            return view_func(*args,**kwargs)

    return wrapper