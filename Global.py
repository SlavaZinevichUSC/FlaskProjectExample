#mocks globally accessible tools for internal application so I don't have to type a lot
class GlobalTools():
    def __init__(self):
        self.Logger = None
        self.Config = None
        self.Resolver = None
Core = GlobalTools()