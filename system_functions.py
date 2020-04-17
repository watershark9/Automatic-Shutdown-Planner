import os
def shutdown(seconds):
    command = 'shutdown -s -t ' + str( int(seconds) )
    #os.system(command)
    print(command)

def abortShutdown():
    command = "shutdown -a"
    #os.system(command)
    print(command)