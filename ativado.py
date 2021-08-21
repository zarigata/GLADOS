import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import playsound
import pyjokes
import geocoder

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            if 'gladys' in command:
                command = command.replace('gladys', '')
                print(command)

    except:
        pass
    return command


rodar = 1

def run_glados():
    command = take_command()
    print(command)

    # MUSICA NO YOUTUBE
    if 'play' in command:

        ytmusic = command.replace('play', '')
        talk('playing' + ytmusic + 'on youtube')
        # print('music on youtube')
        pywhatkit.playonyt(ytmusic)
     #tempo
    elif 'what is the time' in command:
        tempo = datetime.datetime.now().strftime('%I:%M %p')
        print(tempo)
        talk('the time is' + tempo)
    # WIKIPEDIA WHAT IS   /////   PRECISSA ATUALIZAR
    elif 'what is' in command:
        whatis = command.replace('what is', '')
        informacao = wikipedia.summary(whatis, 2)
        talk(informacao)
#==============================================================================
    #WIKIPEDIA WHO IS ////// ADICIONAR O FOLOWUP
    elif 'who is' in command:
        whois = command.replace('who is', '')
        informacaopessoa = wikipedia.summary(whois, 2)
        talk(whois)
#===============================================================================
    # gOLD
    elif 'suck me' in command:
        talk('sure wish i was in Aperture science, and could deploy some nerve gas')
#================================================================================
    # TOCAR MP3 NAO ESTA EM FUNCIONAMENTO
    elif 'space' in command:
        playsound.playsound('K:\PROJETOS PYTHON/space22.mp3', True)
#================================================================================
    #GEOLOCALIZADOR
    elif 'where am I' in command:
        g = geocoder.ip('me')
        print(g.lat)
        print(g.lng)
        lati = g.lat
        long = g.lng
        ondeestou = wikipedia.geosearch(lati, long,None,3)
        talk(ondeestou)

    elif 'tell me a joke' in command:
        talk(pyjokes.get_joke())


    # nao entendeu
    else:
        talk('I did not understand what you just said, please, say that again')


while rodar == 1:
    run_glados()

#  .''.
# (~~~~)
#   ||
# __||__
#/______\
#  |  |' _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
#  |  |'|o| - - - - - - - - - - - - - - - - - - - - - - - - -||
#  |  |'| |                                                  ||
#  |  |'| |                      . ' .                       ||
#  |  |'| |                  . '       ' .                   ||
#  |  |'| |              . '    .-'"'-.    ' .               ||
#  |  |'| |          . '      ,"______ ".      ' .           ||
#  |  |'| |      . '        /:  \     |  :\        ' .       ||
#  |  |'| |  . '            ;  . \        ;            ' .   ||
#  |  |'| |    ' .          \: . /       :/          . '     ||
#  |  |'| |        ' .        `./_____| ,/       . '         ||
#  |  |'| |            ' .      `-.,,.-'     . '             ||
#  |  |'| |                ' .           . '                 ||
#  |  |'| |                    ' .   . '                     ||
#  |  |'| |                        '                         ||
#  |  |'|o|-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_||
#  |  |'
#  |  |'           BRASIL ACIMA DE TUDO
#  |  |'                  DEUS ACIMA DE TODOS
#  |  |'