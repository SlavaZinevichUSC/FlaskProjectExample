from .Torch import TorchOracle

#endpoint provides the interface of the domain.
class ModelEndpoint:
    def __init__(self):
        self.model = TorchOracle.Load()

    def GetPredictions(self, image, numPredictions = None):
        return self.model.Predict(image, numPredictions = numPredictions)
