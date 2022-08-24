from PIL import Image

#Basically wrapper around PIL to ease library changes
def FromBinary(file):
    try:
        return Image.open(file)
    except:
        return None




