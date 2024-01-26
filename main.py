import PIL.Image
import time
import itertools
import os.path, pathlib

def Generator(Repeat:int=3):
    #xCount = 0
    PixelList = itertools.product(range(256), repeat=Repeat)
    for x in (PixelList):
        #xCount += 1
        yield x
    #print(xCount)
    yield True

def OneColorGen(Color:str):
    #color should be r g or b
    match Color.lower():
        case "r":
            Func = lambda x: (x, 0, 0)
        case "g":
            Func = lambda x: (0, x, 0)
        case "b":
            Func = lambda x: (0, 0, x)
        case _:
            Func = lambda x: (x, x, x, x)
    List256 = map(Func, list(range(256)))
    for x in List256:
        yield x
    yield True

def TwoColorGen(Color:str="rb"):
    Color = Color.lower()[:2]
    DoubleColorList = [[0]*256, [0]*256, [0]*256]
    if "r" in Color:
        DoubleColorList[0] = range(256)
    if "g" in Color:
        DoubleColorList[1] = range(256)
    if "b" in Color:
        DoubleColorList[2] = range(256)
    DoubleColorList = itertools.product(*DoubleColorList)
    yield from DoubleColorList
    yield True

Count = 0
def CreateImage(PixelGen, size=4096) -> PIL.Image.Image:
    global Count
    im = PIL.Image.new("RGBA", (size, size))
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
    print("Generating a 24 bit image containing every 24 bit pixel...")
    Bit24Image = CreateImage(Generator(), 4096)
    print("Image generated.")
    Bit24ImageLocation = pathlib.Path(f"{os.path.dirname(__file__)}/Every24bitPixel.png")
    Bit24Image.save(Bit24ImageLocation)
    print(f"Image saved. ({Bit24ImageLocation})")
    ##NOTE: **Generating 32 bit is VERY SLOW! The resulting image is also very large, around 16MB.**
    #Bit24Image = CreateImage(Generator(Repeat=4), 4096) 
    #Bit24Image.save(pathlib.Path(f"{os.path.dirname(__file__)}/Every32bitPixel.png"))
    print("Generating one colored images")
    AllImages256 = [CreateImage(OneColorGen("r"), 16), CreateImage(OneColorGen("g"), 16), CreateImage(OneColorGen("b"), 16), CreateImage(OneColorGen(""), 16)]
    for Index, x in enumerate(AllImages256):
        x.save(pathlib.Path(f"{os.path.dirname(__file__)}/Pixel{Index+1}.png"))
    print("Images generated. Creating gif...")
    AllImages256[-1].save(pathlib.Path(f"{os.path.dirname(__file__)}/OneColorGif.gif"), append_images=AllImages256[::-1][:-1], save_all=True, loop=0, duration=len(AllImages256)/1000)
    print("Gif created")
    AllImagesTwoColor: list[PIL.Image.Image] = []
    for TwoColors in itertools.combinations_with_replacement("rgb", 2):
        TwoColors = "".join(TwoColors)
        print(TwoColors)
        AllImagesTwoColor.append(CreateImage(TwoColorGen(TwoColors), int((256**3)**.5)))
    for Index, Image in enumerate(AllImagesTwoColor):
        Image.save(pathlib.Path(f"{os.path.dirname(__file__)}/TwoColor{Index+1}.png"))
    AllImagesTwoColor[-1].save(pathlib.Path(f"{os.path.dirname(__file__)}/OneColorGif.gif"), append_images=AllImagesTwoColor[::-1][:-1], save_all=True, loop=0, duration=len(AllImagesTwoColor)/1000)
    print(time.perf_counter()-start)
    print(time.process_time())
    print(time.thread_time())
