class MasterDataDict:

    def __init__(self):
        self.dataProviders = {}

    def getGoldenKey(self,dataProvider:str, naturalKey:str, anyDataProvider:bool = False):

        goldenKey = ''

        if dataProvider in self.dataProviders:
            if naturalKey in self.dataProviders[dataProvider]:
                goldenKey = self.dataProviders[dataProvider][naturalKey]
                return goldenKey
        
        if anyDataProvider:
            for dp in self.dataProviders:
                if naturalKey in self.dataProviders[dp]:
                    goldenKey = self.dataProviders[dp][naturalKey]
                    return goldenKey

        return goldenKey
    
    def addKey(self,dataProvider:str, naturalKey:str, goldenKey:str):
        if dataProvider not in self.dataProviders:
            self.dataProviders[dataProvider] = {}

        self.dataProviders[dataProvider][naturalKey] = goldenKey
        

        