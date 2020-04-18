import system_functions as sf
import datetime

def shutdown_procedure(input_time):
    present = datetime.datetime.now()
    
    if input_time < present:
        print('Not valid Time')
    else:
        time_diferance = input_time - present
        sf.shutdown( time_diferance.total_seconds() )

def abort_shutdown_procedure():
    sf.abortShutdown()
