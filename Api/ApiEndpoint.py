from .Flask import FlaskFactory

class ApiEndpoint():
    def __init__(self):
        self.app = FlaskFactory.CreateApp()
        pass