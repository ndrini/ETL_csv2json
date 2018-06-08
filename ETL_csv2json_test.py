# -*- coding: utf-8 -*-

# TO DO
# check input filter (no CIF)


import unittest
import ETL_csv2json as C2J  
# import led_lamps as ll

class TestStringMethods(unittest.TestCase):
    def setUp(self):
        pass

    def test_encode2json_text(self):
        data_list = [   { "column_A":"product_Ana", "column_B":1, "column_C":34.39 },
                        { "column_A":"product_Banana", "column_B":3, "column_C":14.39 },]

        self.assertEqual(True, True)

        self.assertEqual(C2J.encode2json_text()[0], "{")

 
if __name__ == '__main__':
    unittest.main()

