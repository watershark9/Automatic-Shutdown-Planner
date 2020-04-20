import system_functions as sf
import datetime
import platform

def shutdown_procedure(input_time):
    present = datetime.datetime.now()

    if input_time < present:
        return 'Not valid time'
    else:
        time_diferance = input_time - present
        sf.shutdown( time_diferance.total_seconds() )
        return 'Shutdown Queued'

def abort_shutdown_procedure():
    sf.abortShutdown()

def is_OS_Valid(os):
    valid_os_list = [
        'Windows'
    ]
    if os == valid_os_list[0]:
        return True
    else:
        return False

def validate_OS():
    if is_OS_Valid( platform.system() ) == False:
        import sys
        sys.exit("Not valid OS")

def startup_script():
    validate_OS()