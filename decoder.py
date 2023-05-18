import base64
import nbt
import io
import json

# Decodes a base64 gzipped nbt string
def decodeData(string):
    data = nbt.nbt.NBTFile(fileobj = io.BytesIO(base64.b64decode(string))) # Decode nbt data
    return data