import pandas as pd

class FilterBreachedData:
    def __init__(self):
        pass

    def filter_breached_data(self,dict_data:list):
        new_dict_data = list()

        for i in dict_data:
            df  = pd.DataFrame([i])
            df = df[['username', 'email']]

            dict_output = df.to_dict(orient='records')[0]
            new_dict_data.append(dict_output)

        return new_dict_data
    
    def search_in_filter_data(self,dict_data:list,username:str,email:str):
        for i in dict_data:
            if i['username'] == username or i['email'] == email:
                return True
        return False

        