from PIL import Image
import sys

picMatrix = [
    [0, 0,0,0,0,0, 0,0, 0,0,0,0,0, 0,0, 0,0,0,0,0, 0],
    [0, 1,1,1,1,1, 0,0, 1,1,1,1,1, 0,0, 1,1,1,1,1, 0],
    [0, 1,0,0,0,0, 0,0, 0,0,0,0,1, 0,0, 1,0,0,0,1, 0],
    [0, 1,0,0,0,0, 0,0, 0,0,0,0,1, 0,0, 1,0,0,0,1, 0],
    [0, 1,1,1,1,1, 0,0, 1,1,1,1,1, 0,0, 1,0,0,0,1, 0],
    [0, 0,0,0,0,1, 0,0, 1,0,0,0,0, 0,0, 1,0,0,0,1, 0],
    [0, 0,0,0,0,1, 0,0, 1,0,0,0,0, 0,0, 1,0,0,0,1, 0],
    [0, 1,1,1,1,1, 0,0, 1,1,1,1,1, 0,0, 1,1,1,1,1, 0],

    [0, 0,0,0,0,0, 0,0, 0,0,0,0,0, 0,0, 0,0,0,0,0, 0],
    [0, 0,0,0,0,0, 0,0, 0,0,0,0,0, 0,0, 0,0,0,0,0, 0],
    [0, 0,0,0,0,0, 0,0, 0,0,0,0,0, 0,0, 0,0,0,0,0, 0],

    # 妹子名字矩阵
    [0, 1,0,1,0,1, 0,0, 1,0,0,0,0, 0,0, 1,1,1,0,0, 0],
    [0, 1,0,1,0,1, 0,0, 1,0,0,0,0, 0,0, 1,0,0,1,0, 0],
    [0, 0,0,0,0,0, 0,0, 1,0,0,0,0, 0,0, 1,0,0,0,1, 0],
    [0, 0,1,0,1,0, 0,0, 1,0,0,0,0, 0,0, 1,0,0,1,0, 0],
    [0, 0,1,0,1,0, 0,0, 1,1,1,1,1, 0,0, 1,1,1,0,0, 0],

    [0, 0,0,0,0,0, 0,0, 0,0,0,0,0, 0,0, 0,0,0,0,0, 0],
]
w = len(picMatrix[0])
h = len(picMatrix)

mw = 100

toImage = Image.new('RGBA', (100 * w, 100 * (h + 1)))

def save_photo_wall(noTipImage, imgCount):
    imgIndex = 0
    needImgNum = 0
    for y in range(h):
        for x in range(w):
            try:
                if picMatrix[y][x] == 1:
                    needImgNum = needImgNum + 1
                    fromImage = Image.open(r"./images/%s.jpg" % str(imgIndex % imgCount))
                    fromImage = fromImage.resize((100, 100), Image.ANTIALIAS)
                    toImage.paste(fromImage, (x * mw, y * mw))
                    imgIndex = imgIndex + 1
                else:
                    pass
            except IOError:
                pass

    # 底部加文字图片
    if not noTipImage:
        tipImage = Image.open(r"./images2/tip.png")
        tipImage.resize((100 * (w - 2), 100), Image.ANTIALIAS)
        toImage.paste(tipImage, (100, int((y + 0.7) * mw)))

    print('img_count needed for no-repeat-img-fragment: %s' % needImgNum)

    toImage.show()

    # todo sr
    toImage.save('she.png')

if __name__ == '__main__':
    imgCount = 10
    lenArgv = len(sys.argv)
    noTipImage = False
    if lenArgv > 1:
        noTipImage = bool(int(sys.argv[1]))
    if lenArgv > 2:
        imgCount = int(sys.argv[2])

    save_photo_wall(noTipImage, imgCount)

