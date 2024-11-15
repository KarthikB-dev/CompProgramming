class MovingAverage:

    def __init__(self, size: int):
      self.window = []
      self.sum = 0.0
      self.count = 0.0
      self.size = size

    def next(self, val: int) -> float:
      self.sum += val
      self.count += 1
      self.window.append(val)

      if self.count > self.size:
        self.sum -= self.window[0]
        self.window.pop(0)

      return self.sum / min(self.count, self.size)