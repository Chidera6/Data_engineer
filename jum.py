import json
import re
import pandas as pd


with open('jumia_search_output.txt',"r",encoding='utf8') as f:
    my_data = json.load(f)
    for a in my_data.values():
        b = str(a)
        removerating = re.sub(r'\d out of \d'," ",b)
        removebyverifiedpurchase = re.sub( r"((by\s([a-zA-Z]*\s*)[a-z]*\s*)purchase)"," ",removerating,re.DOTALL,re.IGNORECASE)
        removemorebyverifiedpurchase = re.sub(r'((by\s([a-zA-Z]*\s*)[a-z]*\s*)).*purchase'," ", removebyverifiedpurchase,re.DOTALL,re.IGNORECASE)
        date_match = re.findall(r'(\d{2}-\d{2}-\d{4})',removemorebyverifiedpurchase,re.DOTALL)
        post_match = re.findall(r'([a-zA-Z]\D\D\D\D\D\D\D\D\D\D\D\D\D\D\D\D+)',removemorebyverifiedpurchase,re.DOTALL)
              
        jumiadata = {
            "Dates":date_match,
            "Posts":post_match
             }
        

        df = pd.DataFrame.from_dict(jumiadata,orient='index',)
        df = df.transpose()
        print(df)
      
   
     
  

        