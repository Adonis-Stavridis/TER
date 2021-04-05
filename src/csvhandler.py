import csv
import os
import sys

DATA_START = 97

IMG_TIME = 34
IMG_URL = 35

DATA_TIME = 2
DATA_FIX_X = 13
DATA_FIX_Y = 15
DATA_DIST = 3
DATA_L_PUP = 5
DATA_R_PUP = 7


def simplifyCSV(inputFile, outputFile):
  inFile = open(inputFile, 'r', encoding="utf-16")
  outFile = open(outputFile, 'w', encoding="utf-16")

  for line in inFile:
    replaceCommas = line.replace(',', '.')
    replaceSemicolons = replaceCommas.replace(';', ',')
    outFile.write(replaceSemicolons)

  inFile.close()
  outFile.close()


def transformCSV(inputFile, outputFile):
  inFile = open(inputFile, 'r', encoding="utf-16")
  outFile = open(outputFile, 'w', encoding="utf-16")

  csvReader = csv.reader(inFile, delimiter=',')

  for idx in range(DATA_START):
    next(csvReader)

  outFile.write("Temps, Image\n")

  for row in csvReader:
    temps = row[IMG_TIME]
    image = row[IMG_URL]

    if (temps == image == ''):
      break

    outFile.write(f"{temps}, {image}\n")

  outFile.write("\n")

  csvReader = csv.reader(inFile, delimiter=',')

  for idx in range(DATA_START):
    next(csvReader)

  outFile.write(
      "Temps, Fixations/X, Fixations/Y, Distance, Pupille/Gauche, Pupille\Droite\n")

  for row in csvReader:
    temps = row[DATA_TIME]
    fixationsX = row[DATA_FIX_X]
    fixationsY = row[DATA_FIX_Y]
    distance = row[DATA_DIST]
    pupilleGauche = row[DATA_L_PUP]
    pupilleDroite = row[DATA_R_PUP]

    outFile.write(
        f"{temps}, {fixationsX}, {fixationsY}, {distance}, {pupilleGauche}, {pupilleDroite}\n")

  inFile.close()
  outFile.close()


def handleCSV(inputFile, outputFile):
  outFolder = os.path.dirname(outputFile)
  tempFile = f"{outFolder}/temp.csv"
  simplifyCSV(inputFile, tempFile)
  transformCSV(tempFile, outputFile)
  os.remove(tempFile)


def main():
  args = sys.argv
  if len(args) < 3 or len(args) > 4:
    sys.exit("Usage: python3 csvhandler.py [-s|-t] <inputFile> <outputFile>")

  if (args[1] == '-s'):
    simplifyCSV(args[2], args[3])
  elif(args[1] == '-t'):
    transformCSV(args[2], args[3])
  else:
    handleCSV(args[1], args[2])


if __name__ == "__main__":
  main()
