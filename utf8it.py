import cchardet as chardet
import codecs
import glob
import os
import shutil
import sys
import ntpath


def wrong():
    print("Wrong usage. Type utf8it [-options] [file/folder(1)] [file/folder(2)]...\")\n"
          "Options:\n"
          "        e : Show file encoding without converting it\n"
          "Run the script without arguments for options menu\n")


def dirconv(folder, s):
    os.chdir(folder)
    for file in glob.glob("**/*.srt", recursive=True):
        print(convert(file, s))


def convert(filename, s):
    print(ntpath.basename(filename) + " ... ", end='')
    targetFileName = filename + ".new"
    file = open(filename, "rb").read()
    enc = chardet.detect(file)["encoding"]
    if s == 1:
        if not (enc == "UTF-8"):
            with codecs.open(filename, "r", enc) as f:
                with codecs.open(targetFileName, "w", "utf-8") as targetFile:
                    contents = f.read()
                    targetFile.write(contents)
            shutil.move(targetFileName, filename)
            return "Done!"
        else:
            return "Already UTF-8 encoded"
    else:
        return enc


if len(sys.argv) > 1:
    s = 1
    if sys.argv[1] == "-e" and len(sys.argv) >= 2:
        s = 2
    for i in range(s, len(sys.argv)):
        arg = sys.argv[i]
        if os.path.isfile(arg):
            print(convert(arg, s))
        elif os.path.isdir(arg):
            dirconv(arg, s)
        else:
            wrong()
            break
else:
    while True:
        print("1)Convert a file\n"
              "2)Convert files in directory ending with .srt\n"
              "0)Exit\n")
        choise = input()
        if choise == "0":
            quit()
        elif choise == "1":
            file = input("Enter file directory: \n")
            print(convert(file, 1))
        elif choise == "2":
            fol = input("Enter directory: ")
            if os.path.isdir(fol):
                dirconv(fol, 1)
        else:
            print("Choose from range 0-2")