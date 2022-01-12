import hashlib
import sys
import os
import shutil


def textsha1(text):
    sha_1 = hashlib.sha1()
    sha_1.update(text.encode("utf-8"))
    return sha_1.hexdigest()


def imagesha1(image):
    ih = hashlib.sha1(image).hexdigest()
    return ih


def hash(outdir, file):
    inputtext = file[:-4]
    inputimage = open(f"{outdir}/{file}", "rb").read()
    inputtext = sharpcheck(inputtext)
    firsthash = textsha1(inputtext)[0:10].upper()
    secondhash = imagesha1(inputimage)[0:10].upper()
    return f"{inputtext} [{firsthash}-{secondhash}]"


def copyfiles(indir, outdir):
    for name in os.listdir(indir):
        src = f"{indir}/{name}"
        hashname = hash(indir, name)
        dst = f"{outdir}/{hashname}.png"
        shutil.copy2(src, dst)


# 샵이 들어가 있는 파일들 대응
def sharpcheck(filename):
    return filename.split(" #")[0]


if __name__ == "__main__":
    input_dir = "./input"
    output_dir = "./output"
    print("xUnity.Autotranslator용 텍스쳐 파일명 처리 프로그램")
    print("Snowyegret / 버전: 0.0.2")
    print("프로그램 시작")

    # input폴더 체크
    if os.path.isdir(input_dir) == False:
        print('"input" 폴더가 없습니다.')
        print("생성 후 다시 실행해 주세요.")
        os.system("pause")
        sys.exit()

    # output폴더 체크, 없을 시 생성
    if os.path.isdir(output_dir) == False:
        print('"output" 폴더가 없습니다. 폴더를 생성합니다.')
        os.mkdir(output_dir)
        print('"output" 폴더 생성 완료!')

    copyfiles(input_dir, output_dir)
    print("작업 완료!")
    os.system("pause")
