::将模块的路径加入系统python模块路径
@SET PYTHONPATH=%PYTHONPATH%;D:\GIT\AutoInterfaceTest\project

::将模板路径添加到环境变量，以便程序调用
@SET TEMPLATEPATH=D:\GIT\AutoInterfaceTest\project\tools

@python2 %~dp0..\runner\ftest.py %1 %2 %3 %4 %5 %6 %7 %8 %9 
