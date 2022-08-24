from .Flask import FlaskFactory
from Global import Core
class ApiEndpoint():
    def __init__(self):
        self.app = FlaskFactory.CreateApp()
        pass

    def Run(self):
        self.app.run(host="localhost", port=Core.Config.Get('port'), debug=True)