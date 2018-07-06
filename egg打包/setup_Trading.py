# coding=utf-8

import os
import sys
import shutil
import time

from setuptools import setup, find_packages


# 这是进行打包的方法
def setup_egg():
    setup(
        name='AI_Trading',
        version='1.0.0',
        package_data={'': ['*.*']},
        packages=find_packages(),
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
eggFile = 'AI_Trading-' + gpaVer + "-py" + str(sys.version_info[0]) + '.' + str(sys.version_info[1]) + '.egg'

# os.name是用来判断平台的，nt代表的是win系统，linux是posix
if os.name == "nt":
    eggPath = os.path.abspath(os.path.split(os.path.realpath(__file__))[0] + '\\dist\\' + eggFile)
    print(eggPath)
else:
    eggPath = os.path.abspath(os.path.split(os.path.realpath(__file__))[0] + '/dist/' + eggFile)
    print(eggPath)


# 更改环境变量
def write_environment():
    path = r'/etc/environment'
    home_path = os.environ['HOME']
    path_list = []
    sign = False
    file = open(path, 'r')
    b = file.readlines()
    file.close()
    so_path = home_path + '/AI_Trading/so/A6so/'+':'+home_path+'/AI_Trading/so/Hsso'
    for data in b:
        if data.find(so_path) > 0 and data.startswith('LD_LIBRARY_PATH'):
            return True
    for data in b:
        if data.startswith('LD_LIBRARY_PATH'):
            sign = True
            break
    if sign:
        for data in b:
            if data.startswith('LD_LIBRARY_PATH'):
                ld_list = data.split('=')
                path_list.append(ld_list[0] + '=' + home_path + '/AI_Trading/so/A6so/'+':'+home_path+'/AI_Trading/so/Hsso' + ':' + ld_list[1])
            else:
                path_list.append(data)
        path1 = r'/etc/environment'
        file1 = open(path1, 'w')
        for data in path_list:
            file1.write(data)
        file1.close()
    else:
        for data in b:
            path_list.append(data)
        path_list.append('LD_LIBRARY_PATH=' + home_path + '/AI_Trading/so/A6so/'+':'+home_path+'/AI_Trading/so/Hsso')
        path1 = r'/etc/environment'
        file1 = open(path1, 'w')
        for data in path_list:
            file1.write(data)
        file1.close()
    return False


def uninstall():
    """卸载AI_Trading安装包"""

    # 在系统的环境变量中，进行查找安装路径
    gpaPath = []
    for x in sys.path:
        x = os.path.abspath(x)
        print(eggPath)
        print(x.lower())
        if x.lower().find('ai_trading-') > 0 and x.lower().find('dist-packages') > 0:
            gpaPath.append(x)
            print(x)
    if (len(gpaPath) == 0):
        print(u'AI_Trading！！！')
        return

    # 切换当前的工作目录
    if os.name == "nt":
        os.chdir(sys.prefix + '\Scripts')

    # 卸载命令
    # result = os.popen('sudo easy_install --m AI_Trading')

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
    """安装AI_Trading包"""

    # 切换当前工作目录
    if os.name == "nt":
        os.chdir(sys.prefix + '\Scripts')
    # 将依赖文件放在~/AI_Trading下
    os.popen('sudo rm -rf ~/AI_Trading')
    time.sleep(1)
    os.popen('sudo mkdir -p ~/AI_Trading/')
    time.sleep(1)
    os.popen('sudo cp -r so/ ~/AI_Trading/')
    time.sleep(1)
    os.popen('sudo cp /etc/environment /etc/environment_cp')



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
    # print(result.read())
    egg_path = result.readlines()
    for data in egg_path:
        if data.startswith('Installed'):
            print(data)
            b=data.split('\n')
            path1 = b[0]
            path2 = path1.split(' ')[1]
            path3 = os.path.join(path2,'AI_Trading/A6')
            os.popen('sudo chmod -R 777 '+path3)
            break
    # 安装完成
    print(u'安装成功')

    # 更改环境变量
    sign_env = write_environment()
    if sign_env:
        return
    print(u'6s后重启')
    time.sleep(6)

    # 环境变量设置完成后需要重启
    os.popen('sudo shutdown -r now')


if len(sys.argv) >= 2:
    if (sys.argv[1] == 'install'):
        if (not os.path.exists(eggPath)):
            print((u'文件不存在:' + eggPath))
            exit()


        print(u'开始卸载旧版本AI_Trading安装包')
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
