该项目用于演示如何使用sqlalchemy模块和sqlmodel模块操作MySQL数据库，包括：

- 数据库表格创建
- 数据新增、查询、修改、删除等基本操作（CRUD）
- 数据库迁移工具Alembic的使用

### 准备环境

安装MySQL数据库: 自行在本地安装或者使用docker安装, docker安装命令如下：

```shell
docker-compose up -d
```

### 安装依赖

```shell
pip install -r requirements.txt
```

### 脚本说明

#### 表格创建

- 使用sqlalchemy模块创建表格: `src/models/sqlalchemy_create_table.py`
- 使用sqlmodel模块创建表格: `src/models/sqlmodel_create_table.py`

#### CRUD操作

- 使用sqlalchemy模块进行CRUD操作: `src/sqlalchemy_crud.py`
- 使用sqlmodel模块进行CRUD操作: `src/sqlmodel_crud.py`


### 数据库迁移工具Alembic

1. 安装Alembic

```shell
pip install alembic
```

2. 初始化Alembic

```shell
cd src
alembic init alembic
```

3. 修改alembic.ini配置文件

```shell
# sqlalchemy.url = driver://user:pass@localhost/dbname
sqlalchemy.url = mysql+pymysql://root:root@localhost/test
```

4. 修改alembic/env.py配置文件

```python
import os
import sys
# 返回当前路径的上级路径
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from models.sqlalchemy_init_db import Base
target_metadata = Base.metadata
```

5. 修改响应的MySQL表结构，创建迁移脚本

```shell
alembic revision --autogenerate -m "create table"
```

6. 执行迁移脚本

```shell
alembic upgrade head
```

7. 查看数据库表变更历史

```shell
alembic history
```

8. 回滚数据库表变更

```shell
alembic downgrade -1
```

### 参考文档

1. [Alembic官方文档](https://alembic.sqlalchemy.org/en/latest/tutorial.html)
2. [SQLAlchemy 异步操作](https://www.cnblogs.com/gupingan/p/18300469)
3. 



