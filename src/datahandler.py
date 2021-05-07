import os
import sys

def renameImgs(inputPath):
  imgPath = f"{inputPath}/img"
  imgDir = os.listdir(imgPath)

  for img in imgDir:
    oldName = img
    newName = img.replace(',', '.')
    os.rename(f"{imgPath}/{oldName}", f"{imgPath}/{newName}")


def main():
  args = sys.argv

  if len(args) == 2:
    renameImgs(args[1])
  else:
    sys.exit("Usage: python3 datahandler.py <inputPath>")


if __name__ == "__main__":
  main()
