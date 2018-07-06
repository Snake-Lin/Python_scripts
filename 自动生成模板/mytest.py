
'''
功能 : 创建文件时自动生成文件头注释,自动添加系统文件信息.

设置位置 :
File-Default Settings-Editor-File and Code Templates-Python Script

'''

# *************************经典模板*******************************
# -*- coding:utf-8 -*-
'''
@author: ${USER}
@file: ${NAME}.py
@software: ${PRODUCT_NAME}
@project: ${PROJECT_NAME}
@time: ${DATE} ${TIME}
@desc: Description information.
'''
# ****************************************************************
'''
其他参数设置
${PROJECT_NAME} - 当前项目的名称
${NAME} - 在文件创建期间，您在新文件对话框中指定的新文件的名称
${USER} - 当前用户的登录名
${DATE} - 当前系统日期
${TIME} - 当前系统时间
${YEAR} - 本年度
${MONTH} - 当前月份
${DAY} - 当月的当前日期
${HOUR} - 当前时间
${MINUTE} - 当前分钟
${PRODUCT_NAME} - 将创建文件的IDE的名称
${MONTH_NAME_SHORT} - 名的前三个字母。例子:1月、2月等
${MONTH_NAME_FULL} - 全名一个月。例子:1月、2月,等等。.
'''