INSERT_ENGLISH_VOCABULARY = """
   INSERT INTO "english_voc" (vocabulary, tl1, tl2, tl3, pronunc, definition, example_sentence) values (%s, %s, %s, %s, %s, %s, %s);
"""

CREATE_ENGLISH_VOCABULARY_TABLE = """
    CREATE TABLE "english_voc" (
        vocabulary_id SERIAL PRIMARY KEY,
        vocabulary varchar(32) not null,
        tl1 varchar(32) not null,
        tl2 varchar(32),
        tl3 varchar(32),
		pronunc varchar(32),
        definition text,
        example text,
		timestamp timestamp default current_timestamp

    );
"""

GET_ENGLISH_ALL_VOCABULARIES = """
    SELECT * FROM "english_voc"
"""

GET_ENGLISH_TRANSLATION_FOR_VOCABULARY = """
    SELECT translation_text FROM english_voc_translation where vocabulary_id = %s;
"""

GET_ENGLISH_VOCABULARY_ROW_COUNT = """
    SELECT COUNT(*) FROM "english_voc" where vocabulary = %s;
"""