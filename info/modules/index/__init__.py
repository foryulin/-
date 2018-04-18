from flask import Blueprint
# 创建蓝图

index_blu = Blueprint('index',__name__)

# 将views文件与其他文件关联起来
from . import view

