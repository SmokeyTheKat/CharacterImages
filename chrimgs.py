from PIL import Image
import sys
import os
import time

argv = sys.argv
argc = len(argv)
inputFile = ""
width = 170
height = 40
contrast = 40
gchars = [
	" ",
	"▏",
	"▎",
	"▍",
	"▌",
	"▋",
	"▊",
	"▉",
	"█",
]

if "-help" in argv or "--help" in argv or argc == 1:
	print("CharacterImages --help")
	print("	Args:")
	print("		\"-s\"		size of output characters")
	print("					-s 30x40")
	print("					-s 331x182")
	print("		\"-c\"		contrast level of inputed image")
	print("		\"-g\"		group of chars to use for images")
	print("					-g variety")
	print("					-g blocks")
	print("					-g vboxes")
	print("					-g hboxes")
	print("					-g dots")
	print("					-g specials")
	print("		\"-d\"		replaces spaces with dots")
	print("	EX:")
	print("		python3 chrimgs filepath.png -d -g blocks")
	print("		python3 chrimgs filepath.png -c 50 -g hboxes > output.txt")
	exit()

for i in range(argc):
	if argv[i] == "-s":
		asize = argv[i+1].split("x")
		width = int(asize[0])
		height = int(asize[1])
	elif argv[i] == "-c":
		contrast = int(argv[i+1])
	elif argv[i] == "-g":
		if argv[i+1] == "blocks":
			gchars = [
				"░",
				"▒",
				"▓",
				"█"
			]
		elif argv[i+1] == "variety":
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
		elif argv[i+1] == "hboxes":
			gchars = [
				" ",
				"▏",
				"▎",
				"▍",
				"▌",
				"▋",
				"▊",
				"▉",
				"█",
			]
		elif argv[i+1] == "vboxes":
			gchars = [
				" ",
				"▁",
				"▂",
				"▃",
				"▄",
				"▅",
				"▆",
				"▇",
				"█",
			]
		elif argv[i+1] == "specials":
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
		elif argv[i+1] == "dots":
			gchars = [
				" ",
				".",
				",",
				"'",
				"\"",
				"*",
			]
		
if "-d" in argv:
	for i in range(len(gchars)):
		if gchars[i] == " ":
			gchars[i] = "."


def changecontrast(im, v):
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
	img = rimg.convert("RGB")
	img = changecontrast(img, contrast)
	img = img.resize((width, height), Image.ANTIALIAS)
	oimg = [ [ [0,0,0] for i in range(width) ] for i in range(height) ]
	pixels = img.load()
	for y in range(height):
		for x in range(width):
			oimg[y][x][0] = pixels[x,y][0]
			oimg[y][x][1] = pixels[x,y][1]
			oimg[y][x][2] = pixels[x,y][2]
			gv = int((oimg[y][x][0] + oimg[y][x][1] + oimg[y][x][2]) / 3)
			oimg[y][x][0] = gv
			oimg[y][x][1] = gv
			oimg[y][x][2] = gv
	for y in range(height):
		for x in range(width):
			gv = oimg[y][x][0]
			img.putpixel((x,y), (gv,gv,gv))
	for y in range(height):
		for x in range(width):
			print(getpix(oimg[y][x][0]), end="")
		print()
	exit()
if argc > 1:
	inputFile  = argv[1];
	main()
