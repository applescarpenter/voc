from bs4 import BeautifulSoup
import time


"""
checks in the database if the vocabulary is already existing
returns True if not 
"""
def check_for_duplicates(vocabulary):
    from psycopg2.sql import SQL
    import english_queries as eq
    import db
    cnxn = db.db_connection()

    vocabulary_count = cnxn.get_data(SQL(eq.GET_ENGLISH_VOCABULARY_ROW_COUNT),(vocabulary,))

    # if row count is bigger than 0 then there is already an entry to this vocabulary
    if vocabulary_count[0]['count'] == 0:
        return True
    else:
        return False

"""
get the data of a word from web scraping oxford dictionary

"""
def get_data_from_website(vocabulary):

    import requests
    
    url = "https://www.oxfordlearnersdictionaries.com/definition/english/" + vocabulary

    #create header so that the site does not see this request as a bot
    headers = requests.utils.default_headers()
    
    headers.update(
        {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36 Edg/101.0.1210.53'
        }
    )
    # get request to get the definition
    response = requests.get(url, headers=headers)

    
    if not response.status_code == 404:

        with open('oxf.html', 'w+', encoding='utf-8') as f:
            f.write(response.text)

        # sleep for two seconds so that there is not to much traffic at once - fair use
        time.sleep(2)
    else:
    
        return '404'


def get_definition():
    """get definition of requested vocabulary from oxford dictionaries


    Returns:
        string: definition of the requested vocabulary
    """

    # read scrapped html file from function get_data_from_website
    with open('oxf.html', 'r', encoding='utf-8') as data:
        soup = BeautifulSoup(data, 'lxml')

    # extract text from html
    definition = soup.find("span",{"class":"def"})

    # if definition not found print warning and return empty string to prevent exception
    print(definition)
    if definition == None:
        print('Definition could not be found!')
        definition = ''
        return definition

    return definition.text

def get_pronunciation():
    """get pronunciation from oxford dictionaries

    Returns:
        string: pronunciation of vocabulary
    """


    with open('oxf.html', 'r', encoding='utf-8') as data:
            soup = BeautifulSoup(data, 'lxml')
    
    pron = soup.find("span", {"class":"phon"})

    if pron == None:
        print('Pronunciation not found!')
        return''
    else:
        # pronunciation has sometimes '/' in string
        return pron.text.replace('/','')

    


def get_example_sentence():

    with open('oxf.html', 'r', encoding='utf-8') as data:
        soup = BeautifulSoup(data, 'lxml')

    example_sentence = soup.find("span", {"class":"unx"})
    if not example_sentence:
        example_sentence = soup.find("span", {"class":"x"})
        
    if example_sentence == None:
        print('Example sentence not found!')
    else:
        return example_sentence.text


### get data by pons API

def get_translation(vocabulary):
    """gets translation from pons-api

    The api is horrible because it's a mix of html and json but its free!
    

    Returns:
        _type_: _description_
    """
    import requests
    headers = requests.utils.default_headers()

    headers.update(
        {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36 Edg/101.0.1210.53',
            'X-Secret': '18a0b30c537618d711672986f7e736e6837f3490344f7e694c87a62580503fde',
            'Accept':'application/json',
            'Content-Type': 'application/json'

        }
        
    )
    
    api = f"https://api.pons.com/v1/dictionary?q={vocabulary}&l=deen&language=de"


    res = requests.get(api, headers=headers)


    content = res.json()
    # only grab first translation
    translation = content[0].get('hits')[0].get('roms')[0].get('arabs')[0].get('translations')[0].get('target')
    # remove polluted html tags in string
    translation = remove_html_tags(translation)
    
    return translation

def remove_html_tags(input):
    """removes weird html tags from input
    the pons api returns weird mix of json and html
    example: part1 <html_tags> part2
    if there aren't any return input

    Args:
        input (string): string with htmltag

    Returns:
        string: cleaned string
    """
    import re


    if '<' in input:
        # if input is like 'xxx <html_tags>'
        if input[-1:] == '>':

            clean = re.compile('<.*>')

        # if input is like 'xxx <html_tags> xxx'
        else:
            clean = re.compile('<.*> ')
    
    
        

        # bug: "Akk Dat etw" in string
        return re.sub(clean, '', input).replace('Akk','').replace('Dat','').replace('etw','')

    else:
        return input


if __name__ == '__main__':
    #print(get_pronunciation('strive'))
    #print(get_example_sentence())
    dbg = check_for_duplicates('prosperous')


