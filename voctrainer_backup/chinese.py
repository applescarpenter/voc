from language import Language
import pandas as pd

class Chinese(Language):
    
    def __init__(self, word, pinyin,  tl1, tl2=None, tl3=None,tl4 = None, tl5 = None, pronunc=None, definition=None, additional_info=None, topic1=None, topic2=None, topic3=None, pinyin_tone_number=None, hsk=None) -> None:
        super().__init__(word, tl1, tl2, tl3, pronunc, definition)
        self.pinyin = pinyin
        self.additional_info = additional_info
        self.topic1 = topic1
        self.topic2 = topic2
        self.topic3 = topic3
        self.pinyin_tone_numer = pinyin_tone_number
        self.tl4 = tl4
        self.tl5 = tl5
        self.hsk = hsk

    
    @classmethod
    def instantiate_from_xlsx(cls, file):

        data = pd.read_excel()

        data = data.where(pd.notnull(data), None)

        for index, rows in data.iterrows():
            Chinese(
                word = rows['hanzi'],
                pinyin = rows['pinyin'],
                tl1 = rows['tl1'],
                tl2 = rows['tl2'],
                tl3 = rows['tl3'],
                tl4 = rows['tl4'],
                tl5 = rows['tl5'],
                pronunc = rows['pronunc'],
                definition = None,
                additional_info = rows['additional_info'],
                topic1 = rows['topic1'],
                topic2 = rows['topic2'],
                topic3 = rows['topic3'],
                pinyin_tone_number = rows['pinyin_tone_number'],
                hsk = rows['hsk_level']


            )