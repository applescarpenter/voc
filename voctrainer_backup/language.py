class Language:
    def __init__(self, vocabulary,tl1, tl2=None, tl3=None, pronunc=None, definition=None, example=None) -> None:
        self.vocabulary = vocabulary
        self.tl1 = tl1
        self.tl2 = tl2
        self.tl3 = tl3
        self.pronunc = pronunc
        self.definition = definition
        self.example = example

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.vocabulary}, {self.tl1}, {self.tl2}, {self.tl3}, {self.pronunc}, {self.definition}, {self.example})"


