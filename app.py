
   !pip install nlpcloud
   import nlpcloud

   class NLPApp:
    def __init__ (self):
     self.__database={}
     self.__firstmenu()
  
    def __firstmenu(self):
     first_input=input('''
          Hi , welcome Human
          Select any one of this
          1--> New User ?, No worries ,Register
          2--> Old User , Login
          Any other number--> Came by mistake , exit ? 
                  '''  )
    if first_input=='1':
      self.__register()
    elif first_input=='2':
      self.__login()
    else :
      exit()

  def __secondmenu(self):
    second_input=input('''
          Hi , welcome Human , how to proceed
          Select any one of this
          1--> use ner
          2--> use language detection
          3--> sentiment analysis
          Any other number--> exit ? 
           ''')
    if second_input=='1':
      self.__ner()
    if second_input=='2':
      self.__language_detection()
    if second_input=='3':
      self.__sentiment_analysis()
    else :
      exit()

  def __register(self):
    name= input(" Enter name ")
    email=input("Enter Email ")
    password=input("Enter Password")

    if email in self.__database:
      print('already exists')
    else :
      self.__database[email]=[name,password]
      print("Registeration Done")
      print(self.__database)
      self.__firstmenu()

  def __login(self):
    email=input("Enter  email ")
    password=input("Enter Password ")
    if email in self.__database:
     if  self.__database[email][1] == password :
      print("Login successful")
      self.__secondmenu()
     else:
      print("Wrong Password ")
      self.__login()

    else :
      print("Email is not registered")
      self.__firstmenu()


  def __sentiment_analysis(self):
    para=input("Enter Para ")
    client = nlpcloud.Client("distilbert-base-uncased-emotion", " your own API key", gpu=False, lang="en")
    response = client.sentiment(para)
    L = []
    for i in response['scored_labels']:
     L.append(i['score'])
    index = sorted(list(enumerate(L)), key=lambda x: x[1], reverse=True)[0][0]
    print(response['scored_labels'][index]['label'])
    self.__secondmenu()


  def __ner(self):
    text = input("Enter text for NER (Named Entity Recognition): ")
    client = nlpcloud.Client(
        "finetuned-gpt-neox-20b",  
        " your own API key",  
        gpu=True,
        lang="en"
    )
    response = client.entities(text)
    if 'entities' in response and response['entities']:
        print("
Named Entities Found:")
        for entity in response['entities']:
            print(f"- {entity['text']} ({entity['tag']})")
    else:
        print("No named entities found.")
    self.__secondmenu()


  def __language_detection(self):
    text = input("Enter text to detect language: ")
    client = nlpcloud.Client(
        "python-langdetect",
        " your own API key"  
    )
    response = client.langdetection(text)
    print(f"
Detected Language: {response['language']}")
    self.__secondmenu()

obj = NLPApp()

