import subprocess
import webbrowser 

edgeBrowser = "C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe"
serverPath = "C:\\xampp\\htdocs\\barista_bro_server"
vsCodePath = "D:\\Program Files\\Microsoft VS Code\\Code.exe"
postmanPath = "C:\\Users\Admin\\AppData\Local\\Postman\\Postman.exe"
tablePlusPath = "D:\\Program Files\\TablePlus\\TablePlus.exe"
facebookUrl = "https://www.facebook.com"

def openDevServer(path):
    try:
        subprocess.Popen([vsCodePath, path])
        print("Succesfully opened", path)
    except Exception as e:
        print("Error:", e)
    
def openPostman(path):
    try:
        subprocess.Popen(path)
        print("Succesfully opened", path)
    except Exception as e:
        print("Error:", e)

def openTablePlus(path):
    try:
        subprocess.Popen(path)
        print("Succesfully opened", path)
    except Exception as e:
        print("Error:", e)

def openBrowser(urlPath):
    try:
        webbrowser.register('edge', None, webbrowser.BackgroundBrowser(edgeBrowser))
        webbrowser.get('edge').open(urlPath)
    except Exception as e:
        print("Error:", e)


