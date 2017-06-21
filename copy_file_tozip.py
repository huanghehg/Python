#!/usr/bin/python
#-*- coding:utf-8 -*-

import zipfile
import glob
import os

def hh_zipfile(filepath):
	#去掉路径最后的 `／`
	if filepath.endswith('/'):
		filepath=filepath[0:-1]

	# 获取路径的文件及名称
	zipfilename = os.path.basename(filepath)

	if zipfilename :
		print(zipfilename)	
	else :
		zipfilename = '归档'	

	# 生成一个zip文件  
	f = zipfile.ZipFile(zipfilename + '.zip','w',zipfile.ZIP_DEFLATED)

	# 遍历当前路径下的所有文件
	for parent, dirnames, filenames in os.walk(filepath):

		for filename in filenames:
			# 拼全路径
			filenamepath = os.path.join(parent, filename)
			# 如果是当前文件路径下的子路径，就获取子路径名字
			subpath = os.path.relpath(filenamepath,start=filepath)
			# 将文件写入到zip文件中 后面的 `zipfilename + '/' + subpath`  配置zip文件目录层级结构 ，不填的话会默认为传入的路径层级结构
			f.write(filenamepath,zipfilename + '/' + subpath)
	# 不执行close 不会在硬盘写入
	f.close

# 输入文件路径
filepath = input('输入待压缩文件夹！\n')

if os.path.isdir(filepath): #如果文件路径存在就压缩
	hh_zipfile(filepath)
else :
	print ('请输入正确的文件路径')