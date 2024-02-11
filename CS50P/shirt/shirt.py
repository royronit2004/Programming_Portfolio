#shirt
from posixpath import splitext
import sys
from PIL import Image, ImageChops, ImageOps


def main():
    chk_cmdl_arg()

    try:
        imgf = Image.open(sys.argv[1])
    except FileNotFoundError:
        sys.exit("Input does not exist")

    shirtf = Image.open("shirt.png")
    size = shirtf.size

    muppet = ImageOps.fit(imgf, size)

    muppet.paste(shirtf, shirtf)

    muppet.save(sys.argv[2])


def chk_cmdl_arg():

    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    file1 = splitext(sys.argv[1])
    file2 = splitext(sys.argv[2])
    print(file1)
    print(file2)

    if chk_extsn(file1[1]) == False:
        sys.exit("Invalid input")
    if chk_extsn(file2[1]) == False:
        sys.exit("Invalid output")

    if file1[1].lower() != file2[1].lower():
        sys.exit("Input and output have different extensions")


def chk_extsn(file):
    if file in [".jpg",".jpeg",".png"]:
        return True
    return False



if __name__ == "__main__":
    main()