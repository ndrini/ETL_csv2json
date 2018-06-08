# -*- coding: utf-8 -*-

# TO DO
# check input filter (no CIF)


import unittest
import ETL_csv2json as C2J  
# import led_lamps as ll

ETL=C2J.ETL()

class TestStringMethods(unittest.TestCase):
    def setUp(self):
        pass

    def test_encode2json_text(self):
        data_list = [   { "column_A":"product_Ana", "column_B":1, "column_C":34.39 },
                        { "column_A":"product_Banana", "column_B":3, "column_C":14.39 },]
        self.assertEqual(ETL.encode2json_text(data_list)[0], "{")

        my_json = ETL.encode2json_text(data_list)
        self.assertEqual(my_json[0], "{")
        self.assertEqual(my_json[-1], "}")
        self.assertIn("product_Banana", my_json)
 
if __name__ == '__main__':
    unittest.main()

