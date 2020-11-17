import re

# This is a sample code for Project 01.
# The output format and processing of the input files and lists need to be different in your project.

LOCATIONS     = ['İstanbul']            # In this sample code we hard-coded the entity list to make things work below,
ORGANIZATIONS = ['Pegasus Havayolları'] # but in your project, you will create these lists by reading from a file
#    ...       =                  ...
#    ...       =                  ...

SAMPLE_TEXT = """
                Sabancı Üniversitesi 1999 yılında Prof. Dr. Tosun Terzioğlu 
                kurucu rektörlüğünde İstanbul, Tuzla ilçesinde kurulmuştur.
                                                                              """
# RULE_EXAMPLE 1
if 'Üniversite' in SAMPLE_TEXT:
    print("ORGANIZATION", re.findall(r'[A-ZÇĞİÖŞÜ][a-zçğıöşü]* Üniversite\w+',SAMPLE_TEXT))
# RULE_EXAMPLE 2
if 'yıl' in SAMPLE_TEXT:
    print("DATE", re.findall(r'\d{4}(?=\s+yıl\w+)',SAMPLE_TEXT))
# RULE_EXAMPLE 3
if 'Prof. Dr.' in SAMPLE_TEXT:
    print("PERSON", re.findall(r'(?<=Prof. Dr. )[A-ZÇĞİÖŞÜ][a-zçğıöşü]*\s[A-ZÇĞİÖŞÜ][a-zçğıöşü]*',SAMPLE_TEXT))
# RULE_EXAMPLE 4
for uppercaseWord in re.finditer(r'[A-ZÇĞİÖŞÜ][a-zçğıöşü]*',SAMPLE_TEXT):
    uppercaseWord = SAMPLE_TEXT[uppercaseWord.start():uppercaseWord.end()]
    if uppercaseWord in LOCATIONS:
        print("LOCATION", uppercaseWord)
# RULE_EXAMPLE 5
if 'ilçe' in SAMPLE_TEXT:
    print("LOCATION", re.findall(r'[A-ZÇĞİÖŞÜ][a-zçğıöşü]*(?=\s+ilçe\w+)',SAMPLE_TEXT))

# These rules are very simple examples. You should modify them and also write new ones.