import PIL.Image
import time
import itertools
import os.path, pathlib

def _Generator():
    xCount = 0
    PixelList = ((itertools.product(range(256), range(256), range(256), range(256))))
    for x in (PixelList):
        xCount += 1
        yield x
    print(xCount)
    yield True

def CreateImage(PixelGen, size=4096) -> PIL.Image.Image:
    #size should be above or equal to 4096 but under ...
    im = PIL.Image.new("RGB", (size, size))
    PixelMap = im.load()
    for x in range(40000):
        for y in range(size):
            Pixel = next(PixelGen)
            if Pixel == True:
                print("Done!")
                return im
            try: PixelMap[x, y] = Pixel
            except: 
                print("error but...")
                return im

start = time.perf_counter()
Image = CreateImage(_Generator(), 65536)
Image.save(pathlib.Path(f"{os.path.dirname(__file__)}/EveryPixelImage.png"))
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
