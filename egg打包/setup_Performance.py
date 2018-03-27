# coding=utf-8

import os
import sys
import shutil
from setuptools import setup, find_packages


# 这是进行打包的方法
def setup_egg():
    setup(
        name='AI_Perfromance',
        version='1.0.0',
        packages=find_packages(),
        package_data={'': ['*.*']},
        zip_safe=False,
        description='test_demo egg ',
        long_description='egg test_demo ',
        author='yang',
        license="Gpl",
        keywords=('test_demo', 'egg'),
        url="",
    )


# 安装包的文件名
gpaVer = '1.0.0'

# 获取安装包的绝对路径,安装包与setup.py在同一目录中
eggFile = 'AI_Perfromance-' + gpaVer + "-py" + str(sys.version_info[0]) + '.' + str(sys.version_info[1]) + '.egg'

# os.name是用来判断平台的，nt代表的是win系统，linux是posix
if os.name == "nt":
    eggPath = os.path.abspath(os.path.split(os.path.realpath(__file__))[0] + '\\dist\\' + eggFile)
    print(eggPath)
else:
    eggPath = os.path.abspath(os.path.split(os.path.realpath(__file__))[0] + '/dist/' + eggFile)
    print(eggPath)


def uninstall():
    """卸载AI_Perfromance安装包"""

    # 在系统的环境变量中，进行查找安装路径
    gpaPath = []
    for x in sys.path:
        x = os.path.abspath(x)
        print(eggPath)
        print(x.lower())
        if x.lower().find('ai_perfromance-') > 0 and x.lower().find('dist-packages') > 0 :
            gpaPath.append(x)
            print(x)

    if (len(gpaPath) == 0):
        print(u'AI_Perfromance！！！')
        return

    # 切换当前的工作目录
    if os.name == "nt":
        os.chdir(sys.prefix + '\Scripts')

    # 卸载命令
    # result = os.popen('easy_install --m AI_Perfromance')

    # 打印卸载信息
    # print(result.read())

    # 删除安装目录
    for x in gpaPath:
        print(('remove dir:' + x))
        shutil.rmtree(x, True)

    noRemove = []
    # 是否卸载成功
    for x in gpaPath:
        if (os.path.exists(x)):
            noRemove.append(x)

    if (len(noRemove) != 0):
        print(u'卸载失败，以下目录未删除成功：')
        for x in noRemove:
            print(x)
    else:
        print(u'卸载成功！！！')


def install():
    """安装AI_Perfromance包"""

    # 切换当前工作目录
    if os.name == "nt":
        os.chdir(sys.prefix + '\Scripts')

    # 执行安装命令
    python35_sign = False
    for data in sys.path:
        if data.endswith('5') and data.startswith('/usr'):
            python35_sign = True
    if python35_sign:
        result = os.popen('easy_install3 ' + eggPath)
    else:
        result = os.popen('easy_install ' + eggPath)

    # 打印安装信息
    print(result.read())

    # 安装完成
    print(u'安装成功')


if len(sys.argv) >= 2:
    if (sys.argv[1] == 'install'):
        if (not os.path.exists(eggPath)):
            print((u'文件不存在:' + eggPath))
            exit()

        print(u'开始卸载旧版本AI_Perfromance安装包')
        uninstall()

        print(u'开始安装')
        install()
    elif (sys.argv[1] == 'uninstall'):
        print(u'开始卸载')
        uninstall()

    elif (sys.argv[1] == 'bdist_egg'):
        print(u'开始打包：egg')
        setup_egg()

    else:
        print(u'参数错误，请输入参数 install/uninstall')

else:
    uninstall()
    print(u'请输入参数 install/uninstall')
