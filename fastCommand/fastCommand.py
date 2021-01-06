import json, os, sys

class jsonData:
    def __init__(self):
        with open('./command.json', 'r') as jsonData:
            data = json.load(jsonData)
        self.setPath(data["programPath"])
        self.setCommand(data["command"])

        
    def setPath(self, path):
        self.path = path
    
    def setCommand(self, command):
        self.command = command

    def toString(self):
        print("=== path ===")
        print(json.dumps(self.path, indent='\t'))
        print('=== command ===')
        print(json.dumps(self.command, indent='\t'))

if __name__ == '__main__':
    jsonData().toString()