# 项目简介
ZACLIS是一个易于部署的博客系统，包含完整的博客页面和后台管理系统，您只需要在您的服务器运行start脚本，即可建立属于自己的博客。

您可以观看我们的demo网站： http://wizeaz.top/


# ZACLIS博客技术框架
前端使用bootstrap框架搭配html+css+javascript

后端使用python+Django框架


# 成员分工
张业鸿：后端框架搭建、项目测试、前端需求指导

梁耀：前端界面制作

宋佶明：UML图绘制，UML文档编写、后端上传图片功能制作

陈俊言：PPT及相关文档编写

# UML设计图部分
- 用例图

![用例图](/projectFiles/useCaseDiagram.png)

- 类图

![类图](/projectFiles/classDiagram.png)

- 活动图

访客：
![活动图1](/projectFiles/activityDiagram1.png)

博主：
![活动图2](/projectFiles/activityDiagram2.png)

- 顺序图

![顺序图](/projectFiles/ssd.png)

- ER图

![ER图](/projectFiles/ERDiagram.png)


# 使用方法

**环境准备：系统需安装python 3.2及以上版本，并安装pip包依赖工具**

首次使用需要在ZACLIS/myBlog目录下运行`python manage.py createsuperuser`命令来创建超级用户，以进入后台管理系统。

## Linux/mac系统
linux系统下运行`start.sh`命令部署到服务器或是本地
然后浏览器访问 服务器或是本地ip地址 即可
如需进入管理系统，访问 本地ip/console  输入管理账号密码即可

**注：需要执行权限，可用chmod u+x ./start.sh确保有执行权限**

## Windows系统
直接双击运行 start.bat 文件即可实现本地部署
进入管理系统方法同上



