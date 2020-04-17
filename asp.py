import os

def getTime(lang):
    print(lang['prompt1'])
    try:
        return {
            'hours':int( input(lang['hours']) ),
            'minutes':int( input(lang['minutes']) ),
            'seconds':int( input(lang['seconds']) )
        }
    except ValueError:
        print(lang['error1'])
        return getTime(lang)

def shutdown(seconds):
    command = 'shutdown -s -t ' + str( int(seconds) )
    os.system(command)
    #print(command)

def TimetoSeconds(time):
    final = int( time['seconds'] )
    final += int( time['hours'] * 3600 )
    final += int( time['minutes'] * 60 )
    return int(final)

def shutdownSequence(lang):
    time = getTime( language(lang) )
    seconds = TimetoSeconds(time)
    shutdown(seconds)

def language(key):
    languages = {
        'en': {
            'hours':'Hours:',
            'minutes':'Minutes: ',
            'seconds':'Seconds: ',
            'prompt1':'Type the count down time:',
            'error1':'This is not a whole number.',
            'menu1':'Press S to comence entering shutdown time. Press A to abort all current queue. : ',
            'msg1':'shutdown aborted'
        },
        'es': {
            'hours':'Hora:',
            'minutes':'Minutos: ',
            'seconds':'Segundos: ',
            'prompt1':'Escriba el tiempo de apague:',
            'error1':'Esto no es un numero entero.',
            'menu1':'Presione S para comenzar a ingresar el tiempo de apagado. Presione A para cancelar toda la cola actual. : ',
            'msg1':'Apague cancelado'
        }
    }
    return languages[key]

def abortShutdown():
    command = "shutdown -a"
    os.system(command)
    #print(command)

def menu(lang):
    la = language(lang)
    user_input = input( la['menu1'] )
    if user_input == 'S':
        shutdownSequence(lang)
    elif user_input == 'A':
        abortShutdown()
        print()
    else:
        menu(lang)

def main(lang):
    menu( lang )

main('es')