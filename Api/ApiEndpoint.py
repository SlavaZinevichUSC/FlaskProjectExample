from .Flask import FlaskFactory
from Global import Core
import os


#Endpoint provides the interface for the domain
class ApiEndpoint():
    def __init__(self, name):
        self.app = FlaskFactory.CreateApp(name)
        pass

    def Run(self):
        port = int(os.environ.get('PORT', Core.Config.Get('port')))
        self.app.run(host="0.0.0.0", port=port)
