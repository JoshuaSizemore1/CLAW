from crypto import encodeBase64,decodeBase64
from windowScriptManager import scriptManager

#List of tools to be assinged to buttons
toolList = ["encodeBase64","decodeBase64","bash","md5", "windowScripts"]

def command(commandName):
    match commandName:
        case "encodeBase64":
            print("this is base64")
            encodeBase64()
        case "decodeBase64":
            decodeBase64()
        case "bash":
            print("this is bash")
        case "md5":
            print("this is md5")
        case "windowScripts":
            print("this is windows script manager")
            scriptManager()
            

