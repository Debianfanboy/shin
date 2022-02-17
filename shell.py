import shin
import time
import sys
from colorama import Fore, Style

print("Shin Lang v0.2 | Author: Shinero")

#for green "shin" and red ">>>"
while True:
    text = input(Fore.GREEN + 'shin' + Fore.RED  + ' >>> ' + Style.RESET_ALL)

    if text.strip() == "": continue

    result, error = shin.run('<stdin>', text)

    if error:
        print(error.as_string())

    elif result:
        if len(result.elements) == 1:
                print(repr(result.elements[0]))

        else:
            print(repr(result))

