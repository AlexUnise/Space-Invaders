class pile:
    def __init__(self):
        self.__pile=[]
    def empiler(self,element):
        self.__pile.append(element)
        return self.__pile
    def sommet(self):
        if len(self.__pile)==[]:
            return none
        else:
            return self.__pile[-1]
    def depiler(self):
        if len(self.__pile)!=[]:
            element=self.__pile.pop(-1)
            return element,self.__pile