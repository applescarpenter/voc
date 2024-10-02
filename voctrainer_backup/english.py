from language import Language
import pandas as pd
import csv
import os


class English(Language):
    all = []
    def __init__(self, vocabulary, tl1, tl2=None, tl3=None, pronunc = None,definition=None, example=None) -> None:
        super().__init__(vocabulary, tl1, tl2, tl3, pronunc, definition, example)

        English.all.append(self)

    @classmethod
    def instantiate_from_csv(cls, file):
        
        with open(file, 'r') as f:
            reader = csv.DictReader(f, delimiter=';')
            english_vocabularies = list(reader)
        

        for english_vocabulary in english_vocabularies:
            # replace empty strings with None
            for k, v in english_vocabulary.items():
                if v == '':
                    english_vocabulary[k] = None

            English(
                vocabulary = english_vocabulary.get('vocabulary'),
                tl1 = english_vocabulary.get('tl1'),
                tl2 = english_vocabulary.get('tl2'),
                tl3 = english_vocabulary.get('tl3'),
                pronunc = english_vocabulary.get('pronunc'),
                definition = english_vocabulary.get('definition'),
                example = english_vocabulary.get('example')
            )

    @classmethod
    def instantiate_from_xlsx(cls, file):
        # read xl
        data = pd.read_excel(file, sheet_name='Tabelle1')
        # change NaN values to None
        data = data.where(pd.notnull(data), None)

        # iterate over DataFrame and assign values
        for index, rows in data.iterrows():

            English(
                vocabulary = rows['vocabulary'],
                tl1 = rows['tl1'],
                tl2 = rows['tl2'],
                tl3 = rows['tl3'],
                pronunc = rows['pronunc'],
                definition = rows['definition'],
                example = None
            )        


    # DO NOT USE THIS METHOD!
    def backup_create_insert_string(self): 
        return f"INSERT into english_voc (vocabulary, tl1, tl2, tl3, definition) values ({self.vocabulary}, {self.tl1}, {self.tl2}, {self.tl3}, {self.definition});"

    @classmethod
    def instantiate_from_web(cls,vocabulary):
        
        import english_util 

        code = english_util.get_data_from_website(vocabulary)

        # return if vocabulary is not found
        if code == '404':
            print(f"{vocabulary} could't be found!")
            return 

        English(
            vocabulary = vocabulary,
            tl1 = english_util.get_translation(vocabulary),
            tl2 = None,
            tl3 = None,
            pronunc = english_util.get_pronunciation(),
            definition = english_util.get_definition(),
            example = english_util.get_example_sentence()

        )
        
        os.remove('oxf.html')


    