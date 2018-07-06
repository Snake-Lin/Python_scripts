# -* -coding: UTF-8 -* -
from __future__ import print_function
__author__ = 'Arvin'

"""
github:https://github.com/ArvinMei/py2so.git
执行前提：
    系统安装python-devel 和 gcc
    Python安装cython

编译整个当前目录：
    python py-setup.py
编译某个文件夹：
    python py-setup.py BigoModel

生成结果：
    目录 build 下

生成完成后：
    启动文件还需要py/pyc担当，须将启动的py/pyc拷贝到编译目录并删除so文件

"""

import sys
import os
import shutil
import time
from distutils.core import setup
from Cython.Build import cythonize

# 开始计时
startTime = time.time()

# 当前文件夹上层路径
currDir = os.path.abspath('.')

# Sys.argv[]是用来获取命令行参数的，sys.argv[0]表示代码本身文件路径，所以参数从1开始
parentPath = sys.argv[1] if len(sys.argv) > 1 else ""

# 获取setup当前文件绝对路径
setupFile = os.path.join(os.path.abspath('.'), __file__)

# 生成so文件等存储文件夹名
build_dir = "build"

# 拼接出temp文件夹路径存储.o文件
build_temp_dir = build_dir + "/temp"


def getpy(basepath=os.path.abspath('.'), parentpath='', name='', excepts=(), copyother=False, delC=False):
    """
    Describe:获取py文件的路径,删除.c文件,删除temp文件夹(.o文件),复制目标文件,__init__,readme文件
    :param basepath:根路径
    :param parentpath:父路径
    :param name:文件/夹
    :param excepts:排除文件
    :param copyother:是否copy其他文件
    :param delC:删除.c文件
    :return:py文件的迭代器
    """
    # '/home/gnohz/下载/py2so-master/setup.py'
    fullPath = os.path.join(basepath, parentpath, name)

    for fname in os.listdir(fullPath):

        ffile = os.path.join(fullPath, fname)
        # 判断是不是文件夹
        if os.path.isdir(ffile) and fname != build_dir and not fname.startswith('.'):

            for f in getpy(basepath, os.path.join(parentpath, name), fname, excepts, copyother, delC):

                yield f

        # 如果是文件
        elif os.path.isfile(ffile):
            # 取文件后缀.so, .o , .s后缀
            ext = os.path.splitext(fname)[1]

            if ext == ".c":
                # 如果是setup生成的.c文件,就删除
                if delC and os.stat(ffile).st_mtime > startTime:
                    os.remove(ffile)
            # 排除'.pyc', '.pyx',excepts文件
            elif ffile not in excepts and os.path.splitext(fname)[1] not in('.pyc', '.pyx'):

                # __ 是__init__.py文件
                if os.path.splitext(fname)[1] in('.py', '.pyx') and not fname.startswith('__'):

                    yield os.path.join(parentpath, name, fname)

                # 复制目标文件夹,__init__,readme文件
                elif copyother:
                        dstdir = os.path.join(basepath, build_dir, parentpath, name)

                        if not os.path.isdir(dstdir):
                            os.makedirs(dstdir)

                        shutil.copyfile(ffile, os.path.join(dstdir, fname))
        else:
            pass


# 获取目标文件py列表
module_list = list(getpy(basepath=currDir, parentpath=parentPath, excepts=setupFile))

try:
    # .py文件转化为 .c .so .o文件,script_args:代替命令行python setup.py build_ext -b ....
    setup(ext_modules=cythonize(module_list), script_args=["build_ext", "-b", build_dir, "-t", build_temp_dir],
          requires=['Cython'])

except Exception as ex:
    print("error! ", ex.message)

else:

    module_list = list(getpy(basepath=currDir, parentpath=parentPath, excepts=setupFile, copyother=True))

# 删除目标文件生成的.c文件
module_list = list(getpy(basepath=currDir, parentpath=parentPath, excepts=setupFile, delC=True))

# 删除temp文件夹及文件夹下的.o文件
if os.path.exists(build_temp_dir):

    shutil.rmtree(build_temp_dir)

# 程序计时
print("complate! time:", time.time() - startTime, 's')
print("----------------------------------------Successfully---------------------------------------------")