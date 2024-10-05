from language import Language
import pandas as pd
import csv
import os


class English(Language):
    all = []

    def __init__(self, vocabulary, translations=None, pronunc=None, definition=None, example=None) -> None:
        super().__init__(vocabulary, translations, pronunc, definition, example)
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

            # Dynamically collect all translation keys following the tl# naming scheme
            translations = [english_vocabulary[k] for k in english_vocabulary.keys() if k.startswith('tl') and english_vocabulary[k] is not None]

            English(
                vocabulary=english_vocabulary.get('vocabulary'),
                translations=translations,
                pronunc=english_vocabulary.get('pronunc'),
                definition=english_vocabulary.get('definition'),
                example=english_vocabulary.get('example')
            )

    @classmethod
    def instantiate_from_xlsx(cls, file):
        data = pd.read_excel(file, sheet_name='Tabelle1')
        data = data.where(pd.notnull(data), None)

        for index, rows in data.iterrows():
            # Dynamically collect all translation columns following the tl# naming scheme
            translations = [rows[col] for col in rows.index if col.startswith('tl') and rows[col] is not None]

            English(
                vocabulary=rows['vocabulary'],
                translations=translations,
                pronunc=rows['pronunc'],
                definition=rows['definition'],
                example=rows['example']
            )    


    # DO NOT USE THIS METHOD!
    def backup_create_insert_string(self): 
        return f"INSERT into english_voc (vocabulary, tl1, tl2, tl3, definition) values ({self.vocabulary}, {self.tl1}, {self.tl2}, {self.tl3}, {self.definition});"

    @classmethod
    def instantiate_from_web(cls, vocabulary):
        import english_util

        # Get data from the website
        code = english_util.get_data_from_website(vocabulary)

        # Return if vocabulary is not found
        if code == '404':
            print(f"{vocabulary} couldn't be found!")
            return 

        # Collect translations dynamically from english_util -> right now a bit unnecerssary but it might 
        translations = english_util.get_translations(vocabulary)

        # Create the English instance
        English(
            vocabulary=vocabulary,
            translations=translations,
            pronunc=english_util.get_pronunciation(),
            definition=english_util.get_definition(),
            example=english_util.get_example_sentence()
        )

        # Clean up downloaded files
        os.remove('oxf.html')


    