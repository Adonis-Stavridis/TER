import csv
import os
import sys

DATA_START = 97


def stringToFloat(string):
  return float(string.replace(',', '.'))


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

  outFile.write(
      "Temps, Fixations/X, Fixations/Y, Distance, Pupille/Gauche, Pupille\Droite\n")

  for row in csvReader:
    temps = stringToFloat(row[2])
    fixationsX = stringToFloat(row[13])
    fixationsY = stringToFloat(row[15])
    distance = stringToFloat(row[3])
    pupilleGauche = stringToFloat(row[5])
    pupilleDroite = stringToFloat(row[7])

    # duration = float(row[12].replace(',', '.'))
    # duration = TEMP_DURATION

    outFile.write(
        f'{temps},{fixationsX},{fixationsY},{distance},{pupilleGauche},{pupilleDroite}\n')

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
    sys.exit("Usage: python3 csvhandler.py -s <inputFile> <outputFile>")

  if (args[1] == '-s'):
    handleCSV(args[2], args[3])
  else:
    transformCSV(args[1], args[2])

if __name__ == "__main__":
  main()
