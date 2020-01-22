import os

infp = None
outfp = None

copystr = ""

infn = input("복사할 파일명을 입력해 주세요 : ")
outfn = "2"+infn

# 파일명으로 존재하면 처리
if os.path.exists(infn):
    # 파일 읽기로 연결
    # open(연결 파일명, 모드(r/w/a/+))
    infp = open(infn, 'r', encoding="utf-8")
    outfp = open(outfn, 'w', encoding="utf-8")

    # 한줄단위로 읽어와서 화면에 표시
    while True:
        # 한줄단위 읽기
        copystr = infp.readline()
        # 무한 while을 빠져나가는 조건 : 읽어온 데이터가 없다.
        if not copystr:
            break
        outfp.writelines(copystr)
    infp.close()
    outfp.close()
# 파일명이 존재하지 않을때 처리
else:
    print("파일이 존재하지 않습니다.")
