import matplotlib
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

    self.timestamps_ = []
    self.fixationsX_ = []
    self.fixationsY_ = []
    self.distance_ = []
    self.pupilLeft_ = []
    self.pupilRight_ = []

    self.combinedFixations_ = []

  def getStart(self):
    return self.start_

  def getEnd(self):
    return self.end_

  def appendTimestamps(self, value):
    self.timestamps_.append(value)

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

    self.imgPath_ = f"{dataPath}/img/{self.img_}.png"
    self.imgDims_ = Image.open(self.imgPath_).size

  def transformData(self):
    if (not self.timestamps_ or not self.fixationsX_ or not self.fixationsY_):
      return

    self.fixationsX_ = [abs(int(val / 100 * self.imgDims_[0]))
                        for val in self.fixationsX_]
    self.fixationsY_ = [abs(int(val / 100 * self.imgDims_[1]))
                        for val in self.fixationsY_]

    durs = []
    for idx in range(len(self.timestamps_) - 1):
      tempDur = self.timestamps_[idx+1] - self.timestamps_[idx]
      durs.append(tempDur)
    durs.append(durs[-1])

    for idx in range(len(self.fixationsX_)):
      duration = durs[idx]
      fixX = self.fixationsX_[idx]
      fixY = self.fixationsY_[idx]

      values = [duration, fixX, fixY]
      self.combinedFixations_.append(values)

  def render(self, outputPath):
    self.renderRaw(outputPath)
    self.renderHeatmap(outputPath)
    # self.renderScanpath(outputPath)

  def renderRaw(self, outputPath):
    assert self.imgDims_
    assert self.imgPath_

    if (not self.fixationsX_ or not self.fixationsY_):
      return

    print(f"Rendering: {outputPath}/raw-{self.number_}")
    figure = analyzer.draw_raw(self.fixationsX_, self.fixationsY_,
                               self.imgDims_, self.imgPath_,
                               f"{outputPath}/raw-{self.number_}")
    matplotlib.pyplot.close(figure)

  def renderHeatmap(self, outputPath):
    assert self.imgDims_
    assert self.imgPath_

    if not self.combinedFixations_:
      return

    print(f"Rendering: {outputPath}/heatmap-{self.number_}")
    figure = analyzer.draw_heatmap(self.combinedFixations_, self.imgDims_,
                                   self.imgPath_,
                                   savefilename=f"{outputPath}/heatmap-{self.number_}")
    matplotlib.pyplot.close(figure)

  def renderScanpath(self, outputPath):
    assert self.imgDims_
    assert self.imgPath_

    if not self.combinedFixations_:
      return

    print(f"Rendering: {outputPath}/scanpath-{self.number_}")
    figure = analyzer.draw_scanpath(self.combinedFixations_, [],
                           self.imgDims_, self.imgPath_,
                           savefilename=f"{outputPath}/scanpath-{self.number_}")
    matplotlib.pyplot.close(figure)
