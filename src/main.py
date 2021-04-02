import csv
from matplotlib.pyplot import savefig

from numpy.lib.function_base import disp

from csvhandler import handleCSV, simplifyCSV

DATA_INPUT = 'data/Sujet 8/Sujet 8.csv'
DATA_START = 97

TEMP_DURATION = 0.07044232112

OUTPUT_DIR = 'out/'

TEMP_DISP_SIZE = [1920, 977]

TEMP_INPUT_IMG = 'data/custom/img.png'


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


def getFixations(csvReader, pixelSize):
  for idx in range(DATA_START):
    next(csvReader)

  fixations = []

  for row in csvReader:
    duration = TEMP_DURATION
    xVal = float(row[13].replace(',', '.'))
    yVal = float(row[15].replace(',', '.'))

    xVal = abs(int(xVal / 100.0 * pixelSize[0]))
    yVal = abs(int(yVal / 100.0 * pixelSize[1]))

    values = [duration, xVal, yVal]

    fixations.append(values)

  return fixations


def main():
  handleCSV(DATA_INPUT, f'{OUTPUT_DIR}test.csv')
  # csvFile = open(DATA_INPUT, encoding='utf-16')
  # csvReader = csv.reader(csvFile, delimiter=';')

  # # simplifyCSV(f'{OUTPUT_DIR}test',csvReader)

  # # xPct, yPct = getFixationsPct(csvReader)

  # # xArray = pctToPixel(xPct, TEMP_DISP_SIZE[0])
  # # yArray = pctToPixel(yPct, TEMP_DISP_SIZE[1])

  # # rawFigure = analyzer.draw_raw(
  # #     xArray, yArray, TEMP_DISP_SIZE, TEMP_INPUT_IMG,
  # #     f'{OUTPUT_DIR}raw')

  # fixations = getFixations(csvReader, TEMP_DISP_SIZE)

  # # fonctionne pas encore
  # fixationsFigure = analyzer.draw_fixations(
  #     fixations, TEMP_DISP_SIZE, TEMP_INPUT_IMG,
  #     savefilename=f'{OUTPUT_DIR}fixations')

  # heatmapFigure = analyzer.draw_heatmap(
  #     fixations, TEMP_DISP_SIZE, TEMP_INPUT_IMG,
  #     savefilename=f'{OUTPUT_DIR}heatmap')


if __name__ == "__main__":
  main()
