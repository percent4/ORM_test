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


### 参考文档



