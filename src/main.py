import csv

import numpy as np
from numpy.core.defchararray import array
from matplotlib import pyplot as plt

from libs.PyGazeAnalyser.pygazeanalyser import gazeplotter
import analyzer

DATA_INPUT = 'data/Sujet 8/Sujet 8.csv'
DATA_START = 97


def simplifyCSV(name, csvReader):
  for idx in range(DATA_START):
    next(csvReader)

  csvFile = open(f"{name}.csv", "w")

  csvFile.write('Time,x,y\n')
  for idx, row in enumerate(csvReader):
    if idx % 3 == 0:
      timeVal = float(row[12].replace(',', '.'))
      xVal = float(row[13].replace(',', '.'))
      yVal = float(row[15].replace(',', '.'))
      csvFile.write(f'{timeVal},{xVal},{yVal}\n')

  csvFile.close()


def getFixationsPct(csvReader):
  for idx in range(DATA_START):
    next(csvReader)

  xFixations = []
  yFixations = []

  for row in csvReader:
    xVal = float(row[13].replace(',', '.'))
    yVal = float(row[15].replace(',', '.'))

    xFixations.append(xVal)
    yFixations.append(yVal)

  return xFixations, yFixations


# Todo: manage 0s and -100s
def pctToPixel(array, pixelSize):
  return [abs(int(val / 100 * pixelSize)) for val in array]


def main():
  csvFile = open(DATA_INPUT, encoding='utf-16')
  csvReader = csv.reader(csvFile, delimiter=';')

  xPct, yPct = getFixationsPct(csvReader)

  imageSize = [1920, 977]
  xArray = pctToPixel(xPct, imageSize[0])
  yArray = pctToPixel(yPct, imageSize[1])

  figure = analyzer.draw_raw(
      xArray, yArray, imageSize, 'data/custom/img.png', 'test.png')


if __name__ == "__main__":
  main()
