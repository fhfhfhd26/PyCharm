import os

# 출력 파일 객체 선언
outfp = None

# 출력할 파일명 입력
outfn = input("출력할 파일명 입력 : ")

outfp = open(outfn, "w", encoding="utf-8")

instr = ""

# 글자를 입력한대로 출력하기를 한다.
while True:
    instr = input("저장할 텍스트 입력 : ")

    # 빠져나갈 조건 : 입력을 안하고 엔터 누르기
    if not instr:
        break

    outfp.writelines(instr)
outfp.close()
