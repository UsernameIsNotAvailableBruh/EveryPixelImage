import PIL.Image
import time
import itertools
import os.path, pathlib

def _Generator(Repeat=3):
    #xCount = 0
    PixelList = ((itertools.product(range(256), repeat=Repeat)))
    for x in (PixelList):
        #xCount += 1
        yield x
    #print(xCount)
    yield True

Count = 0
def CreateImage(PixelGen, size=4096) -> PIL.Image.Image:
    #size should be above or equal to 4096
    global Count
    im = PIL.Image.new("RGB", (size, size))
    PixelMap = im.load()
    for x in range(40000):
        for y in range(size):
            Pixel = next(PixelGen)
            if Pixel == True:
                Count += 1
                print(f"Done! Image #{Count}")
                return im
            try: PixelMap[x, y] = Pixel
            except: 
                print("error but...")
                return im

if __name__ == "__main__":
    start = time.perf_counter()
    AllImages: list[PIL.Image.Image] = []
    for x in range(4200, 4230):
        Image = CreateImage(_Generator(), x)
        AllImages.append(Image)
    AllImages[-1].save(pathlib.Path(f"{os.path.dirname(__file__)}/EveryPixelGif.gif"), append_images=AllImages[::-1][:-1], save_all=True, loop=0, duration=len(AllImages)/1000)
    print(time.perf_counter()-start)
    print(time.process_time())
    print(time.thread_time())