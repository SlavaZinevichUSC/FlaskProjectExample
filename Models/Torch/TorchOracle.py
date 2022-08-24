import urllib.request

import torch
from Global import Core
from torchvision import transforms
import urllib3

def Load():
    type = Core.Config.Get('oracle')
    if(type == "local"):
        return Local()
    elif(type == "hub"):
        return FromHub()
    Core.Logger.error("Invalid oracle config name")
    return None

def FromHub():
    return TorchOracle(torch.hub.load('pytorch/vision:v0.10.0', 'resnet50', pretrained=True), GetPredictionMap())

def FromFile(path):
    return TorchOracle(torch.load(path), GetPredictionMap())

def Local():
    return FromFile('/Users/slavazinevich/Documents/USC/DirectedResearch/Models/Torch/resNet50.pth')

def GetPredictionMap(url = 'https://raw.githubusercontent.com/pytorch/hub/master/imagenet_classes.txt'):
    return [line.decode().rstrip() for line in urllib.request.urlopen(url)]





class TorchOracle():
    def __init__(self, model, map):
        self.model = model
        self.predMap = map

    #Stolen directly from https://pytorch.org/hub/pytorch_vision_resnet/
    def Predict(self, image, numPredictions = None):
        numPredictions = self.__GetDefaultNum(numPredictions)
        preprocess = transforms.Compose([
            transforms.Resize(256),
            transforms.CenterCrop(224),
            transforms.ToTensor(),
            transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
        ])
        input_tensor = preprocess(image)
        input_batch = input_tensor.unsqueeze(0)

        if torch.cuda.is_available():
            input_batch = input_batch.to('cuda')
            self.model.to('cuda')

        with torch.no_grad():
            output = self.model(input_batch)
        probabilities = torch.nn.functional.softmax(output[0], dim=0)
        _, topind = torch.topk(probabilities, numPredictions)
        return [self.predMap[topind[i].item()] for i in range(topind.size(0))]

    def __GetDefaultNum(self, numPredictions):
        if numPredictions is None:
            numPredictions = Core.Config.Get('default_num_predictions')
            if numPredictions is None:
                Core.Logger.warning("default prediction number is not define in config")
                numPredictions = 5
        return numPredictions