# @Author: s1rius
# @Date: 2023-09-18 20:23:21
# @LastEditTime: 2023-09-18 20:23:39
# @Description: https://s1rius.space/

import hashlib
import os
from PIL import Image


def main():
    pass1 = setPasswd(0)
    print(pass1)
    for n in range(1, 37):
        password = setPasswd(n)
        setZip(n, password)


def setPasswd(num):
    md5 = hashlib.md5(str(num).encode("utf-8")).hexdigest()[0:4].upper()
    dic = {
        "A": "._",
        "B": "_...",
        "C": "_._.",
        "D": "_..",
        "E": ".",
        "F": ".._.",
        "G": "__.",
        "H": "....",
        "I": "..",
        "J": ".___",
        "K": "_._",
        "L": "._..",
        "M": "__",
        "N": "_.",
        "O": "___",
        "P": ".__.",
        "Q": "__._",
        "R": "._.",
        "S": "...",
        "T": "_",
        "U": ".._",
        "V": "..._",
        "W": ".__",
        "X": "_.._",
        "Y": "_.__",
        "Z": "__..",
        "1": ".____",
        "2": "..___",
        "3": "...__",
        "4": "...._",
        "5": ".....",
        "6": "_....",
        "7": "__...",
        "8": "___..",
        "9": "____.",
        "0": "_____",
    }
    passwd = ""

    for i in md5:
        passwd += dic[i] + " "

    print(md5)
    print(passwd)

    pxi = 0
    x_list = []
    for i in passwd:
        if i == ".":
            x_list.append(pxi)
            pxi += 1
        elif i == "_":
            x_list.append(pxi)
            x_list.append(pxi + 1)
            x_list.append(pxi + 2)
            pxi += 3
        else:
            pxi += 1

        pxi += 1

    print(x_list)

    img = Image.open("r.png")

    for x in x_list:
        for y in range(2):
            img.putpixel((x, y), (222, 51, 45))

    img.save(f"{num}.png")
    img.close()

    return md5


def setZip(num, password):
    command = f"7z a -tzip {num} {num-1}.zip {num-1}.png -p{password} -sdel"
    os.system(command)


if __name__ == "__main__":
    main()
