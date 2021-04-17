import sys

from analysis import Analysis

DEBUG_IN = "data/Sujet 14"
DEBUG_OUT = "out"


def main():
  args = sys.argv

  if len(args) == 1:
    analysis = Analysis(DEBUG_IN, DEBUG_OUT)
    analysis.run()
  elif len(args) == 3:
    analysis = Analysis(args[1], args[2])
    analysis.run()
  else:
    sys.exit("Usage: python3 main.py <inputPath> <outputPath>")


if __name__ == "__main__":
  main()
