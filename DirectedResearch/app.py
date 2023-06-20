from App.Initializer import Initializer
from Global import Core


initializer = Initializer(__name__)
Core.Resolver.api.Run()
