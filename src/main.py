import sys

from analysis import Analysis

DEBUG_TYPE = "vr"
DEBUG_IN = "data/vr/Sujet 1"
DEBUG_OUT = "out"


def main():
  args = sys.argv

  if len(args) == 1:
    analysis = Analysis(DEBUG_TYPE, DEBUG_IN, DEBUG_OUT)
    analysis.run()
  elif len(args) == 3:
    analysis = Analysis(args[1], args[2], args[3])
    analysis.run()
  else:
    sys.exit("Usage: python3 main.py <tea|vr> <inputPath> <outputPath>")


if __name__ == "__main__":
  main()
