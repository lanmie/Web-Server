# Web-Server

简介
----

- 基于使用 Socket 进行通信， 解析 HTTP 协议，构建完整的 Web Server
- 采用 MVC 架构，实现数据与页面的分离， 提高代码的可复用性
- 实现用户管理功能，包括注册、登录、密码 加盐 保护、Session 管理和 权限 管理等功能

功能演示
--------

- 测试账号：pin  密码：123

- 登录

![avatar](https://github.com/lanmie/Web-Server/blob/master/static/weibo1.gif)

- 发微博和评论

![avatar](https://github.com/lanmie/Web-Server/blob/master/static/weibo2add.gif)

- 编辑、删除微博和评论

![avatar](https://github.com/lanmie/Web-Server/blob/master/static/weibo2edit_delete.gif)

依赖
-----

- Python 3
- MySQL
- jinja2
- pymysql

如何运行
---------

- 需要您在根目录下自行添加 `secret.py` 文件，内容为：
```
mysql_password = 'your password'
```
- 运行 `reset.py` 
- 运行 `server.py`
