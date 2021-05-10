import os
import sys


def renameImgs(inputPath) -> None:
  """
  renameImgs Rename images by replacing string filenames with castable
  float values

  Args:
      inputPath (str): path to data of study folder
  """

  imgPath = f"{inputPath}/img"
  imgDir = os.listdir(imgPath)

  for img in imgDir:
    oldName = img
    newName = img.replace(',', '.')
    os.rename(f"{imgPath}/{oldName}", f"{imgPath}/{newName}")


def main() -> None:
  """
  main Tool for handling data before analysis
  """

  args = sys.argv

  if len(args) == 2:
    renameImgs(args[1])
  else:
    sys.exit("Usage: python3 datahandler.py <inputPath>")


if __name__ == "__main__":
  main()
