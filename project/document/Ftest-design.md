## Ftest 测试框架 by python  

### 1 前言

在写Ftest之前，使用的接口自动化测试工具是：postman+newman+jenkins的框架，postman写用例并测试单个用例的编写是否正确，最后生成json格式的测试用例集，交给newman来执行并生成报告。最后放在jenkins上实现接口自动化测试的持续集成。这个框架在使用的过程中遇到了如下的瓶颈：

（1）postman和newman是以node.js为基础的，在编写测试用例的时候上手慢；

（2）虽然postman和newman是以nodejs为基础的，但是它并没有提供所有的nodejs的功能，只提供最基本的功能，如不能导入库，这样在编写测试用例的时候就有了很大的限制；

（3）在测试验证阶段，很多时候我们都需要查数据库，而newman和postman并不能直接操作数据库，需要人工查看数据库，很不方便；

（4）一个项目的测试用例可能有很多，有时候并不需要执行所有的测试用例，有时只需要执行其中的一部分，而newman不支持这样的功能。

综上所述，就有了使用python写一个自动化接口测试的框架，但在写的过程中，慢慢发现这并不仅仅是接口测试的框架，完全可以用于其它的测试，如前段web的自动化测试，当然目前生成报告的功能只能用于接口测试。

### 2 需求

（1）查看测试用例目录结构，包括：查看所有的测试用例目录结构和指定目录的测试用例；

（2）执行单个测试用例；

（3）执行指定的多个测试用例；

（4）执行指定目录下的所有测试用例；

（5）在用例执行过程中，输出清晰明了的日志；

（6）接口测试，输出测试报告。

###3 设计

整体设计图：

![](.\jiegou.PNG)

#### 3.1 用例展示

用例展示是将测试用例信息展示在命令行界面，这样就不需要每次再去看用例表。要实现用例展示，需要准备两个文件，一是用例表；二是环境文件。

用例表就是一个结构固定的excel表文件，可以参见project/example/DataApi.xsls

![](.\table.PNG)

环境文件是一个json文件，用于存放需要的环境变量，在此处需要的变量有：testexcel：用例表的文件名，tablename：用例表名，可以参见project/example/dataapi.json

![](.\env.PNG)

涉及到的源代码文件：project/config/env.py      #初始化环境

​                                      project/lib/excel.py           #获取用例信息数据，使用xlrd模块

​                                      project/runner/ftest.py         #程序入口，以及消费用例信息数据即将数据展示出来

程序流程图：

![](.\show.PNG)

#### 3.2用例执行 

用例执行是在命令行通过命令来执行用例，具体的命令可以参考使用文档。用例执行的过程中，需要提供三个文件：一是用例表；二是环境文件；三是用例文件

其中，用例文件是测试人员编写的测试用例，是一个python文件，其中一个类就是一个用例。

涉及到的源代码文件：project/config/env.py       #初始化环境文件

​                                      project/lib/excel.py            #获取要执行的用例信息

​                                      project/runner/ftest.py          #程序入口

​                                      project/runner/run.py               #运行用例

​                                      project/lib/request.py              #接口测试时用来发送http请求

​                                      project/lib/Fassert.py            #为测试用例提供断言功能

程序流程图：

![](.\run.PNG)

#### 3.3 日志输出

日志输出是在用例执行的过程中输出了，原本直接使用print即可，但为了让输出更加直观和可阅读，对输出做了处理。

涉及到的源代码文件：project/lib/win_log.py   #windows系统日志输出设置

​                                      project/lib/linux_log.py     #linux系统日志输出设置

效果：

![](.\xiaoguo.PNG)                        

其中，正常打印的信息是青色的；断言正确信息是绿色的；断言错误或者异常信息是红色的，这样就可以很容易定位出问题所在。

#### 3.4 报告输出

在进行接口自动化测试过程中，可以选择是否生成测试报告，若选择了生成报告，则会在测试结束后生成html形式的测试报告。

涉及到的源代码文件：project/tools/report           #测试报告模板

​                                      project/tools/report.py             #生成报告的程序

​                                      project/lib/run.py                   #为生成报告程序提供测试统计数据

​                                      project/lib/request.py           #为生成报告程序提供单个测试用例的数据

效果图:

![](.\report.PNG)

#### 3.5 用例文件生成

为了方便编写测试用例，提供了生成测试用例模板的工具，可以在开始编写用例之前通过这个工具生成文件。

涉及到的源代码文件：project/tools/testcase          #用例文件的模板

​                                      project/tools/template.py            #生成文件的程序

效果图：

![](.\tem.PNG)

 