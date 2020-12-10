"""===========================================
파일이름 : 코드 반복 작성 프로그램
함수기능 : text_modify_repeat_work.py
최초개발 : 6월 말쯤
개 발 자 : Franciscus S.W.Yang
Copyleft ○ 2018 All Wrongs Reserved

history
19/11/26
- 여러 변수 입력 기능 추가
- 텍스트 파일 외에 print()출력 기능 추가
- data.txt 파일 UTF8 encoding 후 읽기 기능 추가
19/12/18
- 변환 폼 설정 기능 추가 및 변환 기능 자동화
- 변환 문자열 저장 기능 삭제

note
- 변환 된 문자열 저장 기능 또는 실행파일로 만들기
- 빈라인 인식 문제 해결
- 주석 인식 및 생성 기능 추가

사용설명
1. form.txt 파일에 변환할 문자열을 작성한다.
(변환문자열은 #<X>로 작성을 한다.)
2. data.txt 파일에 변환 데이터를 입력한다.
3. 파이썬 파일을 idle에서 실행한다.

==========================================="""

import re

def transform(formtxt, name, index):
    a = formet(formtxt)
    temp = formtxt
    name_list = name.split()
    for i in a:
        temp = temp.replace(i, name_list[a[i]])
    print(temp)
    

def formet(formtxt):
    a = {}
    list1 = list(set(re.findall("<#[0-9]>", formtxt)))
    for i in list1:
        a[i] = int(''.join(re.findall("[0-9]", i)))
    return a

data = open("./data.txt", "r", encoding='UTF8')
#result = open("./save.txt", "w")
form = open("./form.txt", "r", encoding='UTF8')

formtxt = form.read()
num = 1
while True:
    line = data.readline()
    if not line: break
    transform(formtxt, line, num)
    
    num = num + 1

data.close()
#result.close()
form.close()


