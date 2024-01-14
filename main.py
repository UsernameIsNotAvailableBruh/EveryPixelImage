import PIL.Image
import time
import itertools
import os.path, pathlib

def _Generator():
    xCount = 0
    PixelList = ((itertools.product(range(256), range(256), range(256))))
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
for x in range(4120, 4151):
    Image = CreateImage(_Generator(), x)
    Image.save(pathlib.Path(f"{os.path.dirname(__file__)}/EveryPixelImage{x}.png"))
print(time.perf_counter()-start)
print(time.process_time())
print(time.thread_time())