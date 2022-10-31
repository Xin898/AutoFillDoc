# -*- coding:utf-8-*-
# Author: Xin Ge
# Created on 19.09.2022

from distutils.filelist import findall
from distutils.log import info
import os
import re



'''
    get all files from current directory
'''
def getDirList(curr_dir):
    doc_list = os.listdir(curr_dir)
    for i in doc_list:
        print(i)
    return doc_list

'''
    parse carrent filenames to set
'''
def parseDocName(doc_list):
    
    info_list = []
        
    for i in doc_list:
        pre_str = i.split('.')[0]
        print(pre_str)
        pre = re.compile(u'[\u4e00-\u9fa5]')
        res = re.findall(pre,pre_str)
        res1=''.join(res)
        print(res1,pre_str[(len(res1)):])
        info_list.append((res1,pre_str[(len(res1)):]))
        
    return info_list

if __name__ =='__main__':
    
    doc_list = getDirList(os.getcwd())
    parseDocName(doc_list)



