import sys, time

def printch(prnt_string, sleep = 0.15, clear= False):
    if clear:
        for char in prnt_string:
            if char == '\n':
                os.system('cls' if os.name == 'nt' else 'clear')
                #time.sleep(1)
                print()
            else:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(sleep)
    else:
        for char in prnt_string:
            if char == '\n':
                #time.sleep(0)
                print()
            else:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(sleep)
    time.sleep(1)
    print('\nНачало через - ')
    for i in range(5,0,-1):
        sys.stdout.write(f'{i}...')
        sys.stdout.flush()
        time.sleep(1.5)
