import unittest
import src.master_data as mdm

class Test_MasterData(unittest.TestCase):

    def test_Key(self):
        
        myMDM = mdm.MasterDataDict()
        self.assertEqual(myMDM.getGoldenKey('SampleDP','SampleName'),'')
        myMDM.addKey('SampleDP','SampleName','GoldenName')
        self.assertEqual(myMDM.getGoldenKey('SampleDP','SampleName'),'GoldenName')
        myMDM.addKey('SampleDP','SampleName2','GoldenName2')
        self.assertEqual(myMDM.getGoldenKey('SampleDP','SampleName2'),'GoldenName2')
        self.assertEqual(myMDM.getGoldenKey('NoDP','SampleName2'),'')
        self.assertEqual(myMDM.getGoldenKey('NoDP','SampleName2', anyDataProvider=True),'GoldenName2')
