from flask import Flask, request, render_template, jsonify
from . import ImageReader
from Global import Core


def BadRequestResponse():
    return "Bad request", 400


def CreateApp():
    folder = Core.Config.Get('template_folder')
    folder = folder if folder is not None else 'templates'
    app = Flask("__main__", template_folder=folder)

    @app.route('/', methods=['GET'])
    def Hello():
        return render_template('index.html')

    @app.route('/binary', methods=['POST'])
    def Endpoint():
        file = request.files['image'] if 'image' in request.files else None
        if file is None:
            return BadRequestResponse()
        img = ImageReader.FromBinary(file)
        if img is None:
            return BadRequestResponse()
        preds = Core.Resolver.model.GetPredictions(img)
        outputPreds = '\n'.join(preds)
        return jsonify({'predictions:': outputPreds})

    return app
