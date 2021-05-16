import csv
import os
import sys

from data import Tea, Vr


def simplifyCSV(catName, inputFile, outputFile) -> None:
  """
  simplifyCSV Simplifies csv file by replacing string values with castable
  float values, and sets ',' as separator

  Args:
      catName (str): name of category of study (tea or vr)
      inputFile (str): path to input csv file
      outputFile (str): path to output folder
  """

  if catName == "tea":
    encoding = "utf-16"
  else:
    encoding = "utf-8"

  inFile = open(inputFile, 'r', encoding=encoding)
  outFile = open(outputFile, 'w', encoding=encoding)

  for line in inFile:
    replaceCommas = line.replace(',', '.')
    replaceSemicolons = replaceCommas.replace(';', ',')
    outFile.write(replaceSemicolons)

  inFile.close()
  outFile.close()


def teaTransformCSV(inputFile, outputFile) -> None:
  """
  teaTransformCSV Transform csv file for a Tea study

  Args:
      inputFile (str): path to input csv file
      outputFile (str): path to output folder
  """

  inFile = open(inputFile, 'r', encoding="utf-16")
  outFile = open(outputFile, 'w', encoding="utf-16")

  csvReader = csv.reader(inFile, delimiter=',')

  for idx in range(Tea.DATA_START):
    next(csvReader)

  outFile.write("Temps, Image\n")

  for row in csvReader:
    temps = row[Tea.IMG_TIME]
    image = row[Tea.IMG_URL]

    if (temps == image == ''):
      break

    outFile.write(f"{temps}, {image}\n")

  outFile.write("\n")

  csvReader = csv.reader(inFile, delimiter=',')

  for idx in range(Tea.DATA_START):
    next(csvReader)

  outFile.write(
      "Temps, Fixations/X, Fixations/Y, Distance, Pupille/Gauche, Pupille/Droite\n")

  for row in csvReader:
    temps = row[Tea.DATA_TIME]
    fixationsX = row[Tea.DATA_FIX_X]
    fixationsY = row[Tea.DATA_FIX_Y]
    distance = row[Tea.DATA_DIST]
    pupilleGauche = row[Tea.DATA_L_PUP]
    pupilleDroite = row[Tea.DATA_R_PUP]

    outFile.write(
        f"{temps}, {fixationsX}, {fixationsY}, {distance}, {pupilleGauche}, {pupilleDroite}\n")

  inFile.close()
  outFile.close()


def vrTransformCSV(inputFile, dataFile, outputFile) -> None:
  """
  vrTransformCSV Transform csv file for a Vr study

  Args:
      inputFile (str): path to input csv file
      dataFile (str): path to original csv file
      outputFile (str): path to output folder
  """

  inFile = open(inputFile, 'r')
  outFile = open(outputFile, 'w')

  csvReader = csv.reader(inFile, delimiter=',')

  imgDir = os.listdir(f"{os.path.dirname(dataFile)}/img")
  imgNames = [float(os.path.splitext(img)[0]) for img in imgDir]
  imgNames.sort()

  outFile.write("Temps, Image\n")
  for img in imgNames:
    outFile.write(f"{img}, {img}\n")
  outFile.write(f"{float('inf')},\n")
  outFile.write("\n")

  csvReader = csv.reader(inFile, delimiter=',')

  outFile.write(
      "Temps, Fixations/X, Fixations/Y, Distance, Pupille/Gauche, Pupille/Droite\n")

  for row in csvReader:
    temps = row[Vr.DATA_TIME]
    fixationsX = row[Vr.DATA_FIX_X]
    fixationsY = row[Vr.DATA_FIX_Y]
    distance = row[Vr.DATA_DIST]
    pupilleGauche = row[Vr.DATA_L_PUP]
    pupilleDroite = row[Vr.DATA_R_PUP]

    outFile.write(
        f"{temps}, {fixationsX}, {fixationsY}, {distance}, {pupilleGauche}, {pupilleDroite}\n")

  inFile.close()
  outFile.close()


def handleCSV(catName, inputFile, outputFile) -> None:
  """
  handleCSV Transform csv file into template csv file format

  Args:
      catName (str): name of category of study (tea or vr)
      inputFile (str): path to input csv file
      outputFile (str): path to output folder
  """

  outFolder = os.path.dirname(outputFile)
  tempFile = f"{outFolder}/temp.csv"
  simplifyCSV(catName, inputFile, tempFile)
  if catName == 'tea':
    teaTransformCSV(tempFile, outputFile)
  elif catName == 'vr':
    vrTransformCSV(tempFile, inputFile, outputFile)
  else:
    sys.exit(
        "Usage: python3 csvhandler.py [-s|-t] <tea|vr> <inputFile> <outputFile>")
  os.remove(tempFile)


def main() -> None:
  """
  main Tool for transforming an input csv file of category Tea or Vr into a
  more understandable template csv file
  """

  args = sys.argv
  if len(args) < 4 or len(args) > 5:
    sys.exit(
        "Usage: python3 csvhandler.py [-s|-t] <tea|vr> <inputFile> <outputFile>")

  if (args[1] == '-s'):
    simplifyCSV(args[3], args[4])
  elif(args[1] == '-t'):
    if args[2] == 'tea':
      teaTransformCSV(args[3], args[4])
    elif args[2] == 'vr':
      vrTransformCSV(args[3], args[4])
    else:
      sys.exit(
          "Usage: python3 csvhandler.py [-s|-t] <tea|vr> <inputFile> <outputFile>")
  else:
    if args[1] != 'tea' and args[1] != 'vr':
      sys.exit(
          "Usage: python3 csvhandler.py [-s|-t] <tea|vr> <inputFile> <outputFile>")
    handleCSV(args[1], args[2], args[3])


if __name__ == "__main__":
  main()
