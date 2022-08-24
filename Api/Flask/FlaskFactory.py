from flask import Flask, request, render_template, jsonify, Response
from . import ImageReader
from Global import Core


def BadRequestResponse():
    return Response("Bad request", status=400)


def CreateApp(name = "__main__"):
    folder = Core.Config.Get('template_folder')
    folder = folder if folder is not None else 'templates'
    app = Flask(name, template_folder=folder)
    #easter egg
    @app.route('/', methods=['GET'])
    def Hello():
        return render_template('index.html')

    #very simple output but more complex input checker/response builder can be created
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
        return jsonify({'predictions': outputPreds})

    return app
