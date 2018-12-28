# coding :utf-8

from flask_script import Manager
from flask_migrate import Migrate,MigrateCommand
from shixi1 import app
from exts import db
from models import User,Question

manager = Manager(app)

#使用Mig绑定qpp和db
migrate = Migrate(app,db)

#添加迁移的脚本命令到manger中
manager.add_command('db',MigrateCommand)

if __name__ == "__main__":
    manager.run()