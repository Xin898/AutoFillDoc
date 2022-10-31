# -*- coding:utf-8-*-
# Author: Xin Ge
# Created on 19.09.2022

from docUtils import getDirList
from docUtils import parseDocName
from transaction import fillDoc2
import os

doc_dir = os.getcwd()
input_dir = os.path.join(doc_dir,'input')
output_dir = os.path.join(doc_dir,'output')

if __name__ == '__main__':
    print('step 1')
    doc_list = getDirList(input_dir)
    print('step 2')
    info_list = parseDocName(doc_list)
    print('step 3')
    fillDoc2(doc_dir,info_list)
    print('end')

