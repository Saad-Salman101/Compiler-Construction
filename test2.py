import re

keyword = {"if":"if","switch":"switch","choice":"choice","crack":"crack","default":"default","although":"although",
        "then":"then","otherwise":"otherwise","subject":"subject","retaliate":"retaliate",
          "digit":"DT","point":"DT","char":"DT","word":"DT","bool":"DT","function":"function","implicit":"implicit", 
          'new': 'new','array':'array','continue':'continue',"none":"none","inherit":"inherit", "public":"public", "private":"private",
          "protected":"protected", "self":"self", "super":"super"}

opr = {"+":"PM","-":"PM","*":"MDM","/":"MDM","%":"MDM","!":"NOT","~":"NOT","&&":"&&","||":"||","and":"and","or":"or",
      "<":"RO",">":"RO","<=":"RO",">=":"RO","!=":"RO","==":"RO","=":"Assign","<<":"shiftOp",">>":"shiftOp","+=":"AssignOp",
       "*=":"AssignOp","/=":"AssignOp","%==":"AssignOp","<<=":"AssignOp",">>=":"AssignOp","++":"IncDec","--":"IncDec",
      "**":"Power"}
      
punc = {",":"," , ";":";" , ":":":" , ".":"." , "{":"{" , "}":"}" , "(":"(" , ")":")" ,
        "[":"[" , "]":"]" }

tokens = []###123456
# source_code ='digit result = 100;\ndigit result = 150;\ndigit result = 200;\ndigit result = 300;\ndigit result = 400;\n'.splitlines()
# for i,word in enumerate(source_code):

with open("C:/Users/hh/Desktop/CC/program.txt", 'r') as f:
    source_code = f.read().splitlines()

def split(string, delimiters=' \t\n'):
    result = []
    word = ''
    for c in string:
        if c not in delimiters:
            word += c
        elif word:
            result.append(word)
            word = ''

    if word:
        result.append(word)

    return result

def listToString(s): 
    # initialize an empty string 
    str1 = " " 
    # return string  
    return (str1.join(s)) 
c=0

for word in source_code:
    c+=1
    word = split(word)
    word = listToString(word)
    for i in split(word):
        if i in keyword.keys(): 
            tokens.append(['DATATYPE', i,c])
        # This will look for an identifier which would be just a word
        # elif re.match("[a-z]", i or re.match("[A-Z]", i)):
        #     tokens.append(['IDENTIFIER', i ,c])
        # This will look for an operator
        elif i in opr.keys():
            tokens.append(['OPERATOR', i ,c ])
        elif i in punc.keys():
            tokens.append(['PUNTUATER', i ,c ])
        # This will look for integer items and cast them as a number 
        elif re.match(r'^_+[a-zA-Z_0-9]*[A-Za-z0-9]$|^[A-Za-z]+[A-Za-z_0-9]*[A-Za-z0-9]$|^[A-Za-z]+$',i):
            tokens.append(["IDENTIFIER", i , c])
        
        elif re.match(r"^'[a-zA-Z0-9]'$|^'[!@#$%^&*()-=+{}|;:<>,.?/']'$|^'\\[\'\"\\]'$|^'\\[ntrafb0]'$",i):
            tokens.append(["CHARACTER", i , c])

        elif i[len(i) - 1] == ';':
            if re.match(r"\d+\.\d+",i):
                tokens.append(["Float", i , c])
            elif re.match(r'\d\d\d',i):
                tokens.append(["INTEGER", i , c])
            elif re.match(r'[\w\W\s]?',i):
                tokens.append(["CHARACTER", i , c])
            elif re.match(r'[\w\W\s]*',i):
                tokens.append(["STRING", i , c])
            else: 
                tokens.append(["CONSTANT", i[:-1],c])
        else:
            tokens.append(["INVALID_TOKEN", i , c]) 
                

print(c)
print(tokens)
# with open("program.txt", 'r') as f:
#     lines = f.read().replace('/n','')
