import os
import pytex2png

def main():

        characters = ["\\alpha", "\\beta"]
        for c in characters:
            stri = c.replace("\\", "")
	    pytex2png.convert(c,"tset/"+stri+".png")


if __name__ == "__main__":
    main()
