## Ftest 自动化测试框架 by python

### 1 目录结构

|---bin                                                              可执行文件

​         |---Ftest.cmd                                         Ftest可执行文件

|---config                                                         配置文件

​          |---env.py                                             环境变量的配置文件

|---lib                                                              一些所需的库

​          |---excel.py                                          对测试用例表进行操作的库

​          |---Fassert.py                                      进行断言的库

​          |---request.py                                      对http请求和回复做了封装

​          |---win_log.py                                      在windows系统cmd窗口输出有颜色的log

​          |---linux_log.py                                   在linux系统shell窗口输出有颜色的log

|---runner

​          |---ftest.py                                          整个框架的入口文件

​          |---run.py                                            案例运行的库

|---tools

​           |---report                                            测试报告模板

​           |---testcase                                         测试用例文件的模板

​           |---report.py                                       生成测试报告

​           |---template.py                                  生成测试用例文件

|---example                                                   测试的例子

​           |---dataapi.json                                  环境变量

​           |---dataapi.py                                     测试用例文件 

​           |---DataApi.xlsx                                  测试用例表

​           |---generate.py                                   使用tools中的生成测试用例文件的工具生成的测试用例文件

​           |---onetest.py                                      使用tools中生成报告工具，生成的单个或指定几个用例运行的报告

​           |---testout.html                                   生成的指定目录运行的测试报告

|---reference                                                   一些引用的文件

|---document                                                  一些文档

### 2 使用

最好在windows使用Ftest。

前提：（1）安装python 2.7 并将python路径加入环境变量

​            （2）安装requests模块：pip install requests

​            （3）安装xlrd模块：pip install xlrd

#### 2.1 安装Ftest

（1）下载库：使用git下载Ftest库到本地

地址：git  clone  https://gitee.com/fured/AutoInterfaceTest.git

（2）将模块路径添加到环境变量

将模块下载到本地后，打开project/bin/Ftest.cmd可看到：

![](.\cmd.PNG)

其中，“D:\GIT\AutoInterfaceTest\project”是笔者的Ftest模块的路径，需要将这个路径换成你自己的路径 即”xxx\project“

其中，“D:\GIT\AutoInterfaceTest\project\tools”是笔者的Ftest中模板所在的文件夹，需要将这个路径换成你自己的模板路径即”xxx\project\tools“

其中，python2是笔者自己电脑上python 2.7的名字，由于笔者的电脑上安装了python2.7 和python3.5 所以为了进行区分，进行了这样的设置。一般都是python，所以需要将“python2”修改为“python”

（3）验证

在cmd命令行输入：Ftest

如果显示如下内容表示安装成功：

![](.\Ftest.PNG)

#### 2.2 输出测试用例表  

（1）作用

测试用例表是用来组织测试用例的，是使用Ftest进行测试的必备的文件。

用例表示例文件：project/example/DataApi.xlsx示例如下：

![](.\table.PNG)

auto_id：用例的编号，必须是唯一的；

Desc：用例的描述信息；

ClassName：用例在用例文件中使用的类名，必须与用例文件中对应；

Directory：用例所属的目录结构，为了便于扩展目录，将目录写在用例后面。

（2）要求

A.每个用例必须有三个信息：auto_id、Desc、ClassName；

B.表结构不能变；

C.auto_id不能重复，ClassName不能重复；

（3）建议

A.直接将project/example/DataApi.xlsx复制一份，直接修改其中的用例数据即可；

B.文件名和表名尽量使用英文名字。

####2.3 输出环境变量文件

（1）作用

用于设置一些在编写测试用例过程中常用的变量，比如进行http接口测试的时候，就可以将域名设置成环境变量，这样当需要修改域名的时候就不用去逐一修改每个用例的域名，只需要改变环境变量文件即可。

环境变量文件示例：project/example/datapi.json

![](.\env.PNG)

红笔标记的都不是必须要有的环境变量。

（2）要求

A.环境变量文件必须是json文件；

B.“testexcel”环境变量是必选要有的，用于表明用例表文件的名称；

C.“tablesname”是必须有的，用于表明用例表的名称；

D."case"是必选有的，用于表明测试用例文件的名字，且不能带“.py“，当然在生成测试用例文件的时候就不需要这个环境变量。

####2.4 生成测试用例文件

（1）作用

生成测试用例文件，这样就方便进行测试用例的编写。

生成的测试用例文件实例：project/example/generate.py

![](.\tem.PNG)

（2）命令

> Ftest    tool    -g   filename.py   -e env.json

filename.py：生成文件的名字

env.json：环境文件

改变生成文件中的project_name和desc，尽量使用英文。

注意：用例文件的生成并不是增量生成的，如果生成一次，当你又在用例表中增加了一个用例的时候，又去生成同名的文件，那么之前的文件将被覆盖。

（3）要求

A.生成的文件名必须要是py文件；

B.环境文件中必须要有：”testexcel“和"tablename"。

####2.5 编写测试用例

（1）介绍

生产测试用例文件后，可以看到每个测试用例均由三部分组成：setUp、test、tearDown

其中：setUp是在实际测试开始之前的动作，是准备工作；

​            test才是真正的测试；

​            tearDown是在测试完成之后的动作，如进行验证。

运行顺序：setUp()------>test()------>tearDown()

示例文件：project/example/dataapi.py

![](.\case.PNG)

（2）编写教程

A.日志打印格式

为了使打印的测试过程中的日志，更加人性化，阅读起来更加方便，这里封装了打印函数。

>Flog.output("content")      #输出正常的日志
>
>Flog.right("content")          #输出正确的日志（绿色）
>
>Flog.error("content")         #输出错误的日志（红色）

一般只使用Flog.output()即可

B.发送http请求

>Request.method = "get"                  #设置请求方式，目前只支持”get“和”post“（必选）
>
>Request.headers = {"Content-Type":"application/json"}   #设置请求头（可选）
>
>Request.params = {"aa":"bb"}                #设置请求参数（可选）
>
>Request.url = "url"                 #设置请求url（必选）
>
>Request.send() #发送请求，会返回一个response对象 ，可以通过Request.response来使用这个response对象

C.获取响应数据

>Response.Code(Request.response)    #获取响应状态码
>
>Response.Body(Request.response)    #获取返回的数据实体
>
>Response.Url(Request.response)       #获取发送的url
>
>Response.ResponseTime(Request.response)    #获取响应时间
>
>Response.DataSize(Request.response)    #获取返回数据的大小

注:Request.response 也就是requests模块中，发送请求后返回书对象。

D.设置和获取环境变量

> Ftest.setGlobalVariable(key,value)     #设置一个环境变量，设置之后可以在其它用例和自身用例中使用
>
> Ftest.getGlobalVariable(key)          #获取环境变量文件中设置的环境变量或者之前代码中设置的环境变量
>
> Ftest.key            # #获取环境变量文件中设置的环境变量或者之前代码中设置的环境变量，另一种方式

E.断言使用

> Fassert.equal(message,a.b)   #断言a = b，其中message是这个断言的信息或说明
>
> Fassert.unequal(message,a,b)    #断言a != b
>
> Fassert.greater(message.a,b)    #断言 a>b
>
> Fassert.greaterequal(message,a,b)       #断言 a>=b
>
> Fassert.less(message,a,b)              #断言 a < b
>
> Fassert.lessequal(message,a,b)        #断言 a<=b
>
> Fassert.true(message,a)             #断言 a == true
>
> Fassert.false(message,a)              #断言   a == false

F.其他

用例文件是使用python编写的，所有符合python语法的东西都可以使用，如：调用数据库，查看数据等。

####2.6 执行测试用例 

（1）目录信息查询

> Ftest info -t -e env.json           #查看全部的用例信息
>
> Ftest info -d dirname  -e env.json       #查看dirname目录的用例信息

（2）单个或者指定用例执行

A.单个用例执行

> Ftest   run  -o  5   -e  env.json     #运行auto_id编号为5的案例
>
> Ftest   run  -o  5   -e  env.json   --report  result.html   #运行auto_id编号为5的案例并生成报告result.html
>
> Ftest   run  -o  "1,2,5"   -e env.json    #运行auto_id编号为1，2，5的三个案例
>
> Ftest   run  -o  "1,2,5"   -e env.json   --report result.html #运行auto_id编号为1，2，5的三个案例并生成result.html报告

B.执行指定目录的信息

> Ftest   run  -d  dirname   -e  env.json     #运行dirname目录下的所有用例
>
> Ftest   run  -d  dirname   -e  env.json   --report  result.html   #运行dirname目录下的所有用例并生成报告result.html