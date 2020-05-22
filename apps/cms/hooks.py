from flask import request, session, url_for, redirect, g
from .models import CMSUser
from .views import cms_bp


@cms_bp.before_request
def before_request():
    # 判断当前是否是登录页面
    if not request.path.endswith(url_for('cms.login')):
        user_id = session.get('user_id')
        # 判断是否保存到session
        if not user_id:
            return redirect(url_for('cms.login'))

    if 'user_id' in session:
        user_id = session.get('user_id')
        user = CMSUser.query.get(user_id)
        # 使用g对象保存用户
        if user:
            g.cms_user = user