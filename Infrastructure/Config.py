
# should load from json file or pythons native config but basic
# initalization is sufficient for this example
config = {'oracle': 'hub',
          'numPredictions' : 5}


class Config():
    def __init__(self):
        #mock loading
        self.config = config
        pass

    # Unsafe - nullable
    # I wont bother implementing some sort of checker/handler equivalent to Option<T> in statically typed languages

    def Get(self,path):
        # obviously no path or any parsing involved in this toy
        if (path in config):
            return self.config[path]
        Global.Logger.warning('key not found in configuration')
        return None



