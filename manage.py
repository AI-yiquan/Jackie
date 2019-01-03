# --*-- coding:utf-8 --*--
from flask_migrate import Migrate,MigrateCommand
from flask_script import Manager
from ihome import get_app,db,models

# 调用工厂函数,获取app
app = get_app('develop')
# 让迁移时，app和数据库建立关联
Migrate(app,db)
# 实例化管理器对象
manager=Manager(app)
# 添加迁移脚本
manager.add_command('db',MigrateCommand)

if __name__ == '__main__':
    # print app.url_map
    manager.run()