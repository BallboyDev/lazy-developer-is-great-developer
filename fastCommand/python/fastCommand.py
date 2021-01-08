import json, os, sys

class JsonData:
    def __init__(self):
        with open('./command.json', 'r') as jsonData:
            self.__command = json.load(jsonData)

    @property
    def path(self):
        return self.__path

    @path.setter
    def path(self, path):
        self.__path = path

    @property
    def command(self):
        return self.__command

    @command.setter
    def command(self, command):
        self.__command = command

    def getData(self, keys, tree = {}):
        command = self.__command if len(tree) == 0 else tree

        if str(type(command[keys[0]])) == "<class 'dict'>":
            self.getData(['init'] if len(keys[1:]) == 0 else keys[1:], command[keys[0]])

        # elif str(type(command[keys[0]])) == "<class 'list'>":
        #     self.execute(command[keys[0]])

        elif str(type(command[keys[0]])) == "<class 'str'>":
            self.execute(command[keys[0]])

    def execute(self, command):
        os.system(f'{command}')

    def toString(self):
        print("=== path ===")
        print(json.dumps(self.__path, indent='\t'))
        print('=== command ===')
        print(json.dumps(self.__command, indent='\t'))

if __name__ == '__main__':
    JsonData().getData(sys.argv[1:])