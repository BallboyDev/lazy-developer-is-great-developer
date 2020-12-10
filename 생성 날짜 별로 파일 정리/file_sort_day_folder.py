"""===========================================
파일이름 : file_sort_day_folder.py
함수기능 : 실행시 같은 폴더 내에 있는 파일들의 목록을 텍스트 파일로 만든후 생성 날짜별로 폴더 생성후 정리
최초개발 : 2018-04-22
최종수정 : 2018-04-28
copyright ⓒ 2017 S.W.Yang All Rights Reserved
==============================================
2018-04-25
-> 파일이름 내부의 공백 문자 인식 수정
2018_04_25
-> 프로그램 실행시 file_list.txt.파일 폴더로 위치이동 오류 수
2018-04-28
-> dir명령어 수정으로 디렉토리 탐색 제외
-> 실행 속도가 빨라짐
==========================================="""

import sys, os

os.system("dir > file_list.txt")
all_lst = open("file_list.txt", "r")
lines = all_lst.readlines()


for i in range(len(lines)):
    if(lines[i].count("오전") or lines[i].count("오후")):
        if(lines[i][39:-1] == "file_sort_day_forder.py"):
            continue
        if(lines[i][39:-1] == "file_list.txt"):
            continue
        #if(not(lines[i].count("<DIR>"))):
        os.system("mkdir %s" % lines[i][:10])
        os.system("move %s %s" % (lines[i][39:-1].replace(" ", "?"), lines[i][:10]))
