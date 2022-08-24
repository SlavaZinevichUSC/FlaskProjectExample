
#Mocks a messaging toolchain/container to decouple domains
class Resolver():
    def __init__(self):
        pass

    def AddResource(self, resourceName, resourceObject):
        if (hasattr(self, resourceName)):
            Logger.warning(f"Tried to add duplicate resource {resourceName}. Replacing resource")
        setattr(self, resourceName, resourceObject)
