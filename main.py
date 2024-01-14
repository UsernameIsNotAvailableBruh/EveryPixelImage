import PIL.Image
import PIL.ImageColor
import time
import itertools
import numpy
import io
import os.path, pathlib

PixelList = ((itertools.product(range(256), range(256), range(256))))
#((0,0,0), (0,0,255), (0,255,0), (255,0,0), (255,255,255))
Count = 0
xCount = 0
def Generator():
    global Count, xCount
    for x in (PixelList):
        xCount += 1
        yield x
    Count += 1
    print(xCount)
    yield True

def CreateImage(size=4096):
    #size should be above 4096
    im = PIL.Image.new("RGB", (size, size))
    PixelMap = im.load()
    g = Generator()
    for x in range(40000):
        for y in range(size):
            Pixel = next(g)
            if Pixel == True:
                im.show()
                im.save(pathlib.Path(f"{os.path.dirname(__file__)}/EveryPixelImage.png"))
                print("Done!")
                return
            try: PixelMap[x, y] = Pixel
            except: 
                print("error but...")
                im.show("EveryPixel.jpg")
                return

start = time.perf_counter()
CreateImage()
print(time.perf_counter()-start)
print(time.process_time())
print(time.thread_time())
exit()
start = time.perf_counter()

ImageWidth = ImageHeight = 10_000
Detail = 1000

x1 = y1 = .25
x2 = y2 = .5

PIL.Image.effect_mandelbrot((ImageWidth, ImageHeight), (x1, y1, x2, y2), Detail).show()

print(time.process_time())
print(time.thread_time())
print(time.perf_counter()-start)
