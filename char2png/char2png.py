import os
from pytex2png import pytex2png

def main():

        characters = ["\\alpha", "\\beta"]
        for c in characters:
            stri = c.replace("\\", "")
	    pytex2png.convert(c,"output/"+stri+".png")


if __name__ == "__main__":
    main()
