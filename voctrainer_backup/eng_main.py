from english import English
import db
from psycopg2.sql import SQL
import english_queries as eq
from random import randint
import english_util as eng_util


### 'Please use the new class function "create_object_via_web"'###
# this function uses the class method to create objects with the data from a excel file and pushes the newly created data to the database
def insert_new_words_from_xlsx(file):
    pass

    #English.instantiate_from_xlsx(file)


def create_object_via_web(vocabulary):
    # if True (vocabulary not in database) -> create object and gather information
    vocabulary_exists_in_db = eng_util.check_for_duplicates(vocabulary)

    if vocabulary_exists_in_db:
        English.instantiate_from_web(vocabulary)

    else:
        print(f'{vocabulary} is already in your vocabulary collection!' )

def insert_objects_into_db():

    cnxn = db.db_connection()

    for eng in English.all:
        cnxn.insert_data(SQL(eq.INSERT_ENGLISH_VOCABULARY),(eng.vocabulary, eng.tl1, eng.tl2, eng.tl3, eng.pronunc, eng.definition, eng.example))
        print(eng)


"""
this function gets all available vocabulary from the database and randomly throws definitions to the user
the user has to guess the word and gets feedback about his input
this function crashes when the amount > available words in the database
probably I should fix this some time
"""
def vocabulary_test(amount=10):
    cnxn = db.db_connection()
    vocs = cnxn.get_data(SQL(eq.GET_ENGLISH_ALL_VOCABULARIES),())

    for i in range(0,amount):
        random_int = randint(0, len(vocs)-i)
        
        # give user definition and wait for input
        voc = vocs[random_int]
        print(voc['definition'])
        user_input = input()

        # check if user gave correct answer
        if user_input == voc['vocabulary']:
            print(f"Correct! eng: {voc['vocabulary']}, ger: {voc['tl1']}, pronunciation: {voc['pronunc']}, example: {voc['example_sentence']}")
        else:
            print(f"False! eng: {voc['vocabulary']}, ger: {voc['tl1']}, pronunciation: {voc['pronunc']}, example: {voc['example_sentence']}")
        
        vocs.pop(random_int)






#insert_objects_into_db()

"""
create_object_via_web('commotion')
create_object_via_web('ceased')
create_object_via_web('defiance')

create_object_via_web('tender')
create_object_via_web('centurion')
create_object_via_web('notion')
create_object_via_web('reared')
create_object_via_web('wept')
create_object_via_web('nurture')
create_object_via_web('dispose')
create_object_via_web('canopies')
create_object_via_web('converse')
create_object_via_web('auxiliary')
create_object_via_web('usher')
create_object_via_web('shrubbery')
create_object_via_web('shroud')
create_object_via_web('ornate')
create_object_via_web('detergent')
create_object_via_web('deduce')
create_object_via_web('distinct')
create_object_via_web('cane')
create_object_via_web('rigid')
create_object_via_web('endowed')
create_object_via_web('blurb')
create_object_via_web('intrigue')
insert_objects_into_db()
"""

#vocabulary_test()


