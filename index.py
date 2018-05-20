from PIL import Image
import os, sys

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
ms = 20


toImage = Image.new('RGBA', (100 * w, 100 * (h + 1)))

def save_photo_wall(imgCount):
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
    tipImage = Image.open(r"./images2/tip.png")
    tipImage.resize((100 * (w - 2), 100), Image.ANTIALIAS)
    print(x, y)
    toImage.paste(tipImage, (100, int((y + 0.7) * mw)))

    print('不重复需要照片数: %s' % needImgNum)

    toImage.show()

    # todo sr
    # toImage.save('ta.jpg')

if __name__ == '__main__':
    save_photo_wall(40)

