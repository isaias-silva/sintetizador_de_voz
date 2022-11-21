import random
import string
import pyttsx3
  
#Inicializa a engine
engine = pyttsx3.init()

#Envia comandos para alterar as propriedades
#de voz e velocidade
engine.setProperty("voice", "brazil")
engine.setProperty("rate", 80)

#Processa as modificações feitas até o momento
engine.runAndWait() 


#Loop principal
while True:
    #Pega a entrada do usuário
    frase = input(">") 
    if frase != "sair!":
        #Coloca frase na fila de processamento da engine
        engine.say(frase)
        #Executa os comandos da fila (no caso, say(frase) )
        filename=''.join(random.choice(string.ascii_letters + string.digits) for _ in range(7))+'.mp3'
        engine.save_to_file(frase,filename)
        engine.runAndWait()
    else:
        break