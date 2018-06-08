# -*- coding: utf-8 -*-
# https://www.ordenacionjuego.es/en/calculo-digito-control

# NIF is mostly a number; so, just by divide if by 23 we get the last digit: the verification one

class ETL(): 

    def encode2json_text(self, data_list, main_name="products"):
        my_json='{"%s":[\n' % main_name
        for itms in data_list:        # itms is a dict
            my_json = my_json + '\t{'
            for k,v in itms.items():      
                # print(str(k)+': '  + str(v))
                #~{{{my_json=+'"%f "', str(k)  
                my_json = my_json + '\n\t"{}": "{}", '.format(str(k), str(v)) #https://pyformat.info
            
            my_json = my_json + '}\n'
        my_json = my_json + ']}'
        return my_json


    def separate(self):
        SPLIT_DIGIT = 8 
        first_part = NIF[:SPLIT_DIGIT]
        last_part   = NIF[SPLIT_DIGIT:]
        return first_part,last_part
        
 
if __name__ == '__main__':
    etl=ETL()
    data_list = [   { "column_A":"product_Ana", "column_B":1, "column_C":34.39 },
                        { "column_A":"product_Banana", "column_B":3, "column_C":14.39 },]
    print etl.encode2json_text(data_list)[0]
    #assert last_digit("S9126639E") == False, "vero"
    

"""
{"employees":[
    { "firstName":"John", "lastName":"Doe" },
    { "firstName":"Anna", "lastName":"Smith" },
    { "firstName":"Peter", "lastName":"Jones" }
]}
"""
