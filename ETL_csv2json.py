# -*- coding: utf-8 -*-
# https://www.ordenacionjuego.es/en/calculo-digito-control

# NIF is mostly a number; so, just by divide if by 23 we get the last digit: the verification one

class ETL(): 

    def encode2json_text(self, data_list):
        return "{product_Banana}"
        

    def separate(self):
        SPLIT_DIGIT = 8 
        first_part = NIF[:SPLIT_DIGIT]
        last_part   = NIF[SPLIT_DIGIT:]
        return first_part,last_part
        
 
if __name__ == '__main__':
    etl=ETL()
    print etl.encode2json_text()[0]
    #assert last_digit("S9126639E") == False, "vero"
    