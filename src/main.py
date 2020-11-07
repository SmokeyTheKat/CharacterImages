from PIL import Image
import sys
import os
import time

ags = sys.argv
agsc = len(ags)

inputFile = ""
outputFile = ""
'''
gchars = [
	" ",
	".",
	",",
	"-",
	"+",
	"=",
	"*",
	"?",
	"$",
	"%",
	"&",
	"#",
	"@",
]
'''
'''
gchars = [
	" ",
	"░",
	"▒",
	"▓",
	"█"
]
'''
gchars = [
	" ",
	".",
	"`",
	"'",
	",",
	":",
	";",
	"\"",
	"^",
	"*",
	"s",
	"c",
	"t",
	"b",
	"%",
	"8",
	"D",
	"G",
	"N",
	"M",
	"W",
	"#",
	"@"
]



def changecon(im, v):
	f = (259 * (v + 255)) / (255 * (259 - v))
	def contrast(c):
		value = 128 + f * (c - 128)
		return max(0, min(255, value))
	return im.point(contrast)

def vmap(v, l1, h1, l2, h2):
	return int((v-l1) * ((h2-l2)/(h1-l1)) + l2)

def getpix(v):
	return gchars[vmap(v, 0, 255, 0, len(gchars)-1)]

def main():
	rimg = Image.open(inputFile)
	w = 50
	h = 15
	img = rimg.convert("RGB")
	#img = changecon(img, 2)
	img = img.resize((w, h), Image.ANTIALIAS)
	oimg = [ [ [0,0,0] for i in range(w) ] for i in range(h) ]
	pixels = img.load()
	for y in range(h):
		for x in range(w):
			oimg[y][x][0] = pixels[x,y][0]
			oimg[y][x][1] = pixels[x,y][1]
			oimg[y][x][2] = pixels[x,y][2]
			gv = int((oimg[y][x][0] + oimg[y][x][1] + oimg[y][x][2]) / 3)
			oimg[y][x][0] = gv
			oimg[y][x][1] = gv
			oimg[y][x][2] = gv
	for y in range(h):
		for x in range(w):
			gv = oimg[y][x][0]
			img.putpixel((x,y), (gv,gv,gv))
	for y in range(h):
		for x in range(w):
			print(getpix(oimg[y][x][0]), end="")
		print()
	exit()

if agsc == 3:
	inputFile  = ags[1];
	outputFile = ags[2];
	main()
