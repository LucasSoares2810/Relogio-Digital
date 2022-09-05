import sys
import time
import sevseg

try:
    while True:
        print('\n' * 60)
        currentTime = time.localtime()
        hours = str(currentTime.tm_hour % 12)
        if hours == '0':
            hours = '12'

        minutes = str(currentTime.tm_min)
        second = str(currentTime.tm_sec)

        hDigits = sevseg.getSevSegStr(hours, 2)
        hTopRow, hMiddleRow, hBottomRow = hDigits.splitlines()

        mDigits = sevseg.getSevSegStr(minutes, 2)
        mTopRow, mMiddleRow, mBottomRow = hDigits.splitlines()

        sDigits = sevseg.getSevSegStr(second, 2)
        sTopRow, sMiddleRow, sBottomRow = sDigits.splitlines()

        # Monstra os digitos
        print(hTopRow + '     ' + mTopRow + '    ' + sTopRow)
        print(hMiddleRow + '  *  ' + mMiddleRow + '  *  ' + sMiddleRow)
        print(hBottomRow + '  *  ' + mBottomRow + '  *  ' + sBottomRow)
        print()
        print('Pressione "Q" para sair')

        # Mantem o loop até os segundos mudarem
        while True:
            time.sleep(0.01)
            if time.localtime().tm_sec != currentTime.tm_sec:
                break

except KeyboardInterrupt:
    print('RELÓGIO DIGITAL')
    sys.exit() # Quando Ctrl-C é pressionado no final do programa

