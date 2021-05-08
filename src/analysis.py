import csv
import os

from joblib import Parallel, delayed

import csvhandler
import scene


class Analysis:

  def __init__(self, dataPath, outPath, handlecsv=True):
    self.dataPath_ = dataPath

    dataName = os.path.basename(self.dataPath_)
    catName = os.path.basename(os.path.dirname(self.dataPath_))
    inputPath = f"{self.dataPath_}/{dataName}.csv"
    dirName = f"{outPath}/{catName}"
    self.outputPath_ = f"{dirName}/{dataName}"
    self.catName_ = catName

    if not os.path.exists(outPath):
      os.mkdir(outPath)

    if not os.path.exists(dirName):
      os.mkdir(dirName)

    if not os.path.exists(self.outputPath_):
      os.mkdir(self.outputPath_)

    if handlecsv:
      self.csvPath_ = self.handleCSV(catName, dataName, inputPath)
    else:
      self.csvPath_ = inputPath

    self.scenes_ = []

  def run(self):
    self.readCSV()

    Parallel(n_jobs=-1)(delayed(self.parallelRun)(scene)
                        for scene in self.scenes_)

  def parallelRun(self, scene):
    assert self.scenes_
    assert self.dataPath_
    assert self.outputPath_

    scene.loadImg(self.dataPath_)
    scene.transformData()
    scene.render(self.outputPath_)

  def handleCSV(self, catName, dataName, inputPath):
    assert self.outputPath_

    outputPath = f"{self.outputPath_}/{dataName}.csv"
    csvhandler.handleCSV(catName, inputPath, outputPath)
    return outputPath

  def readCSV(self):
    assert self.csvPath_

    if self.catName_ == "tea":
      encoding = "utf-16"
    else:
      encoding = "utf-8"

    csvFile = open(self.csvPath_, encoding=encoding)
    csvReader = csv.reader(csvFile)

    self.createScenes(csvReader)
    self.setupScenes(csvReader)

  def createScenes(self, csvReader):
    startArray = []
    endArray = []
    imgArray = []

    next(csvReader)

    for row in csvReader:
      if not row:
        break

      start = float(row[0])
      img = row[1][1:]

      startArray.append(start)
      imgArray.append(img)

    for idx in range(1, len(startArray)):
      endArray.append(startArray[idx])
    endArray.append(endArray[-1] + 1.0)

    sceneNumber = 0
    for idx in range(len(startArray)):
      if not imgArray[idx]:
        continue

      newScene = scene.Scene(
          sceneNumber, startArray[idx], endArray[idx], imgArray[idx])
      sceneNumber += 1
      self.scenes_.append(newScene)

  def setupScenes(self, csvReader):
    assert self.scenes_

    scenesNumber = len(self.scenes_)

    curSceneIdx = 0
    curScene = self.scenes_[curSceneIdx]
    curSceneStart = curScene.getStart()
    curSceneEnd = curScene.getEnd()

    next(csvReader)

    for row in csvReader:
      time = float(row[0])

      if time >= curSceneEnd:
        curSceneIdx += 1
        if curSceneIdx >= scenesNumber:
          break
        curScene = self.scenes_[curSceneIdx]
        curSceneStart = curScene.getStart()
        curSceneEnd = curScene.getEnd()

      if time < curSceneStart:
        continue

      fixationsX = float(row[1])
      fixationsY = float(row[2])
      distance = float(row[3])
      pupilLeft = float(row[4])
      pupilRight = float(row[5])

      if (fixationsX < 0 or fixationsX > 100 or fixationsY < 0 or
              fixationsY > 100):
        continue

      curScene.appendTimestamps(time)
      curScene.appendFixationsX(fixationsX)
      curScene.appendFixationsY(fixationsY)
      curScene.appendDistance(distance)
      curScene.appendPupilLeft(pupilLeft)
      curScene.appendPupilRight(pupilRight)
