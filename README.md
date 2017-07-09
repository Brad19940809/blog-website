# awesome-python3-webapp


##A python webapp tutorial.

### 说明
- 该博客网站使用python3搭建，没用到任何web框架。
- web服务器使用nginx，做为反向代理服务器和静态文件代理。
- 数据库选用mysql。
- 进程管理工具选用supervisor，注意其目前只支持python2。
- 自动化部署工具为fabric，选用的也是Python。

### 前期准备
- 安装需要的扩展模块： `pip3 install -r requirements.txt`
- 导入数据库: `mysql -u root -p < schema.sql`
- 
- nignx 和 supervisor的配置文件都在`conf` 文件夹里面。
- 补上服务器和数据库配置，如密码等等。
- 当在服务器端建立好对应的目录之后，便可以用fabric部署上去：  
先 `fab2 build`, 打包好需要的文件。
再`fab2 deploy` 便可以部署上去。
