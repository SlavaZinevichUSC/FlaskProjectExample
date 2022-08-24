from .Torch import TorchOracle
class ModelEndpoint():
    def __init__(self):
        self.model = TorchOracle.Load()

    def GetPredictions(self, image):
        return self.model.Predict(image)