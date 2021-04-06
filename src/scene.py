from PIL import Image

import analyzer


class Scene:

  def __init__(self, number, start, end, img) -> None:
    self.number_ = number

    self.start_ = start
    self.end_ = end
    self.duration_ = end - start

    self.img_ = img.replace(':', '').replace('/', '').replace('?', '')[:100]
    self.imgPath_ = ""
    self.imgDims_ = (0, 0)

    self.fixationsX_ = []
    self.fixationsY_ = []
    self.distance_ = []
    self.pupilLeft_ = []
    self.pupilRight_ = []

  def getStart(self):
    return self.start_

  def getEnd(self):
    return self.end_

  def appendFixationsX(self, value):
    self.fixationsX_.append(value)

  def appendFixationsY(self, value):
    self.fixationsY_.append(value)

  def appendDistance(self, value):
    self.distance_.append(value)

  def appendPupilLeft(self, value):
    self.pupilLeft_.append(value)

  def appendPupilRight(self, value):
    self.pupilRight_.append(value)

  def loadImg(self, dataPath):
    assert self.img_

    self.imgPath_ = f"{dataPath}/Web/{self.img_}.png"
    self.imgDims_ = Image.open(self.imgPath_).size

  def transformData(self):
    self.fixationsX_ = [abs(int(val / 100 * self.imgDims_[0]))
                        for val in self.fixationsX_]
    self.fixationsY_ = [abs(int(val / 100 * self.imgDims_[1]))
                        for val in self.fixationsY_]

  def fixationsArray(self):
    fixs = []

    for idx in range(len(self.fixationsX_)):
      duration = 0.1
      fixX = self.fixationsX_[idx]
      fixY = self.fixationsY_[idx]

      values = [duration, fixX, fixY]
      fixs.append(values)

    return fixs

  def render(self, outputPath):
    assert self.fixationsX_
    assert self.fixationsY_
    assert self.imgDims_
    assert self.imgPath_

    rawFigure = analyzer.draw_raw(
        self.fixationsX_, self.fixationsY_, self.imgDims_, self.imgPath_,
        savefilename=f"{outputPath}/raw-{self.number_}")

    # fixationsFigure = analyzer.draw_fixations(
    #     fixations, self.imgDims_, self.imgPath_,
    #     savefilename=f"{outputPath}/fixations")

    fixations = self.fixationsArray()
    heatmapFigure = analyzer.draw_heatmap(
        fixations, self.imgDims_, self.imgPath_,
        savefilename=f"{outputPath}/heatmap-{self.number_}")
