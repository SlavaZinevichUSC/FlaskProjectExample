from flask import Flask, request, jsonify
from . import ImageReader
from Global import Core

def CreateApp():
    app = Flask(__name__)
    @app.route('/binary', methods=['POST'])
    def Endpoint():
        file = request.files['image']
        img = ImageReader.FromBinary(file)
        preds = Core.model.GetPredictions(img)
        response = 
        pass
    return app



