# coding=utf-8
# http://blog.csdn.net/pfm685757/article/details/48651389
# http://python.jobbole.com/87240/
# http://www.360doc.com/content/14/0306/11/13084517_358166737.shtml
# http://peak.telecommunity.com/DevCenter/setuptools?action=highlight&value=PythonEggs

"""
简介:
 setuptools是Python distutils增强版的集合，它可以帮助我们更简单的创建和分发Python包，尤其是拥有依赖关系的。用户在使用setuptools创建的包时，并不需要已安装setuptools，只要一个启动模块即可。

功能亮点：

    利用EasyInstall自动查找、下载、安装、升级依赖包
    创建Python Eggs
    包含包目录内的数据文件
    自动包含包目录内的所有的包，而不用在setup.py中列举
    自动包含包内和发布有关的所有相关文件，而不用创建一个MANIFEST.in文件
    自动生成经过包装的脚本或Windows执行文件
    支持Pyrex，即在可以setup.py中列出.pyx文件，而最终用户无须安装Pyrex
    支持上传到PyPI
    可以部署开发模式，使项目在sys.path中
    用新命令或setup()参数扩展distutils，为多个项目发布/重用扩展
    在项目setup()中简单声明entry points，创建可以自动发现扩展的应用和框架

总之，setuptools就是比distutils好用的多，基本满足大型项目的安装和发布

使用:1.安装setuptools
     1) 最简单安装，假定在ubuntu下
      sudo apt-get install python-setuptools
     2) 启动脚本安装
      wget http://peak.telecommunity.com/dist/ez_setup.py
      sudo python ez_setup.py

    2.创建一个简单的包 执行python setup.py bdist_egg即可打包一个test的包了。
    demo
    |-- build
    |   `-- bdist.linux-x86_64
    |-- demo.egg-info
    |   |-- dependency_links.txt
    |   |-- PKG-INFO
    |   |-- SOURCES.txt
    |   `-- top_level.txt
    |-- dist
    |   `-- demo-0.1-py2.7.egg
    `-- setup.py
    在dist中生成的是egg包

"""
from setuptools import setup, find_packages


setup(

  name='NewName',               # 新包名
  version='1.0.0',              # 版本
  packages=find_packages('src'),  # 需要打包的目录列表,包含所有src中的包
                                  # 排除特定的包find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"])
  package_dir={'': 'src'},        # 告诉distutils包都在src下
  package_data={
        '': ['*.txt'],           # 任何包中含有.txt文件，都包含它
        'demo': ['data/*.dat'],  # 包含demo包data文件夹中的 *.dat文件
    },
  install_requires=[             # 依赖列表
        'Flask>=0.10',
        'Flask-SQLAlchemy>=1.5,<=2.1'
    ],
  zip_safe=False,
  fullname='',                # 包名-版本
  author='Liu',               # 作者
  author_email='liutiansi@gmail.com',  # 作者邮箱
  maintainer='',                       # 维护人员
  maintainer_email='',                 # 维护人员邮箱
  contact='',                          # 联系人
  contact_email='',                    # 联系人邮箱
  url='http://blog.liuts.com',         # 包的主页
  download_url='',                     # 程序的下载地址
  license='',                          # 程序的授权信息
  licence='',                          # 程序的授权信息别名
  description='My Blog Distribution Utilities',  # 简介
  long_description='',    # 详细介绍
  platforms='',           # 程序适用的软件平台列表
  classifiers='',         # 程序的所属分类列表
  keywords='',            # 程序的关键字列表
  provides='',            # 依赖?
  requires='',            # 要求
  obsoletes='',           # 过时?
  py_modules=['test'],    # 需要打包的python文件列表
  data_files='',          # 打包时需要打包的数据文件，如图片，配置文件等
  scripts='',             # 安装时需要执行的脚步列表

)    

# sfdsfsfdsfsdf
# 0203231