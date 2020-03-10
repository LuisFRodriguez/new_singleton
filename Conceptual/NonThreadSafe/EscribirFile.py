
class EscribirFile(object):

    __instance = None

    def __new__(self, msg_: str):
        self.__msg = msg_
        if EscribirFile.__instance is None:
            EscribirFile.__instance = object.__new__(self)
        return EscribirFile.__instance

    def printFile(self):
        f = open("log.txt", "a")
        f.write(self.__msg)
        f.write('\n')
        f.close()
        return self.__msg
