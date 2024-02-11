import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    if re.search("<iframe(.)*><\/iframe>", s):
        url_patt = re.search(r"(http(s)*:\/\/(www\.)*youtube\.com\/embed\/)([a-z_A-Z_0-9]+)", s)
        if url_patt:
            split_url = url_patt.groups()
            return "https://youtu.be/" + split_url[3]


if __name__ == "__main__":
    main()