#This is not related at all

import time
import PIL.Image

start = time.perf_counter()

ImageWidth = ImageHeight = 10_000
Detail = 1000

x1 = y1 = .25
x2 = y2 = .5

PIL.Image.effect_mandelbrot((ImageWidth, ImageHeight), (x1, y1, x2, y2), Detail).show()

print(time.process_time())
print(time.thread_time())
print(time.perf_counter()-start)
