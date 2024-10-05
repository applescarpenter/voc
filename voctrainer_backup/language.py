class Language:
    def __init__(self, vocabulary, translations=None, pronunc=None, definition=None, example=None) -> None:
        self.vocabulary = vocabulary
        if isinstance(translations, str):
            # Wrap the string in a list if a single translation is passed as a string
            self.translations = [translations]
        else:
            # Ensure translations is a list (or set to an empty list if None)
            self.translations = translations if translations is not None else []
        self.pronunc = pronunc
        self.definition = definition
        self.example = example

    def __repr__(self) -> str:
        translations_repr = ", ".join(self.translations) if self.translations else "No translations"
        return (f"{self.__class__.__name__}("
                f"vocabulary={self.vocabulary}, "
                f"translations=[{translations_repr}], "
                f"pronunc={self.pronunc}, "
                f"definition={self.definition}, "
                f"example={self.example})")