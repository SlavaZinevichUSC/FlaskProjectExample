from Models import ModelEndpoint as ModelInit
from Global import Core
from Infrastructure import Config, Logger, Resolver
from Api import ApiEndpoint as ApiInit


# This project is designed as a monolithic App instance which is different from backend design like lambda etc
# but I'm using this as an opportunity to demonstrate front end (a la react) design patterns for the DR position

class Initializer():
    def __init__(self):
        Core.Logger = Logger.Logger()
        Core.Config = Config.Config()
        Core.Resolver = Resolver.Resolver()
        # Order Specific initialization, we must make sure dependency order has the following ordered property:
        # App -> Infrastructure -> Domain specific directories/packages/applications
        Core.Resolver.AddResource("model", ModelInit.ModelEndpoint())
        Core.Resolver.AddResource("api", ApiInit.ApiEndpoint())
