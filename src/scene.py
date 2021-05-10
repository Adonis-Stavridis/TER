import matplotlib
from PIL import Image

import analyzer


class Scene:
  """
  Scene Organise eye-tracking of a scene to render its analysis

  Attrs:
      self.number_ (int): scene number
      self.start_ (float): start time
      self.end_ (float): end time
      self.duration_ (float): duration of scene
      self.img_ (str): name of image associated to scene
      self.imgPath_ (str): path to image
      self.imgDims_ (tuple of int): dimensions of image
      self.timestamps_ (array of float): timestamps
      self.fixationsX_ (array of float): fixations on X axis
      self.fixationsY_ (array of float): fixations on Y axis
      self.distance_ (array of float): distances of eyes from screen
      self.pupilLeft_ (array of float): diameters of left pupil
      self.pupilRight_ (array of float): diameters of right pupil
      self.combinedFixations_ (array of tuple): data passed for rendering 
  """

  def __init__(self, number, start, end, img) -> None:
    """
    __init__ Initialize Scene

    Args:
        number (int): scene number
        start (float): start time
        end (float): end time
        img (str): name of image associated to scene
    """

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

  def getStart(self) -> float:
    """
    getStart Get start time

    Returns:
        float: start time
    """

    return self.start_

  def getEnd(self) -> float:
    """
    getEnd Get end time

    Returns:
        float: end time
    """

    return self.end_

  def appendTimestamps(self, value) -> float:
    """
    appendTimestamps Append a value to timestamps

    Args:
        value (float): timestamp
    """

    self.timestamps_.append(value)

  def appendFixationsX(self, value) -> float:
    """
    appendFixationsX Append a value to fixations on X axis

    Args:
        value (float): fixation on X axis
    """

    self.fixationsX_.append(value)

  def appendFixationsY(self, value) -> float:
    """
    appendFixationsY Append a value to fixations on Y axis

    Args:
        value (float): fixation on Y axis
    """

    self.fixationsY_.append(value)

  def appendDistance(self, value) -> float:
    """
    appendDistance Append a value to distances

    Args:
        value (float): distance to screen
    """

    self.distance_.append(value)

  def appendPupilLeft(self, value) -> float:
    """
    appendPupilLeft Append a value to diameters of left pupil

    Args:
        value (float): left pupil diameter
    """

    self.pupilLeft_.append(value)

  def appendPupilRight(self, value) -> float:
    """
    appendPupilRight Append a value to diameters of right pupil

    Args:
        value (float): right pupil diameter
    """

    self.pupilRight_.append(value)

  def loadImg(self, dataPath) -> None:
    """
    loadImg Load information of an image

    Args:
        dataPath (str): path to data of study folder
    """

    assert self.img_

    self.imgPath_ = f"{dataPath}/img/{self.img_}.png"
    self.imgDims_ = Image.open(self.imgPath_).size

  def transformData(self) -> None:
    """
    transformData Transform percentage data into pixel positions on image
    """

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

  def render(self, outputPath) -> None:
    """
    render Render raw data and heatmap on image

    Args:
        outputPath (str): path to ouput folder
    """

    self.renderRaw(outputPath)
    self.renderHeatmap(outputPath)
    # self.renderScanpath(outputPath)

  def renderRaw(self, outputPath) -> None:
    """
    renderRaw Render raw data

    Args:
        outputPath (str): path to output folder
    """

    assert self.imgDims_
    assert self.imgPath_

    if (not self.fixationsX_ or not self.fixationsY_):
      return

    print(f"Rendering: {outputPath}/raw-{self.number_}")
    figure = analyzer.draw_raw(self.fixationsX_, self.fixationsY_,
                               self.imgDims_, self.imgPath_,
                               f"{outputPath}/raw-{self.number_}")
    matplotlib.pyplot.close(figure)

  def renderHeatmap(self, outputPath) -> None:
    """
    renderHeatmap Render heatmap

    Args:
        outputPath (str): path to output folder
    """

    assert self.imgDims_
    assert self.imgPath_

    if not self.combinedFixations_:
      return

    print(f"Rendering: {outputPath}/heatmap-{self.number_}")
    figure = analyzer.draw_heatmap(self.combinedFixations_, self.imgDims_,
                                   self.imgPath_,
                                   savefilename=f"{outputPath}/heatmap-{self.number_}")
    matplotlib.pyplot.close(figure)

  def renderScanpath(self, outputPath) -> None:
    """
    renderScanpath Render scanpath

    Args:
        outputPath (str): path to output folder
    """

    assert self.imgDims_
    assert self.imgPath_

    if not self.combinedFixations_:
      return

    print(f"Rendering: {outputPath}/scanpath-{self.number_}")
    figure = analyzer.draw_scanpath(self.combinedFixations_, [],
                                    self.imgDims_, self.imgPath_,
                                    savefilename=f"{outputPath}/scanpath-{self.number_}")
    matplotlib.pyplot.close(figure)
