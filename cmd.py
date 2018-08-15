"""
import sys
import time

for i in range(11):
    sys.stdout.write("\rこれは{}です。".format(i))
    sys.stdout.flush()
    time.sleep(0.1)
print()
"""
import sys
import getpass#Password
import itertools

#色設定
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)

#設定
maxlength = 6
result_view = True
alphabets = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
ALPHABETS = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
numbers = ['0','1','2','3','4','5','6','7','8','9']
use = numbers

password = getpass.getpass('Please set a password of ' + str(maxlength) + 'characters or less.\n' + str(maxlength) + '文字以下のパスワードを設定してください\nPassword:')
if password == '':
    print('Password is empty.\nパスワードが空です')
elif len(password) > maxlength:
    print('Password must be ' + Fore.RED + str(maxlength) + ' characters or less' + Fore.RESET + '.\nパスワードは' + Fore.RED + str(maxlength) + '文字以下' + Fore.RESET + 'で設定して下さい\n')
else:
    for a in password:
        if a in use:
            continue
        else:
            print(Fore.RED + 'The password contains characters that can not be used\nパスワードに使用できない文字が含まれています')
            break
    else:
        if password == getpass.getpass('Please enter your password again for confirmation.\n確認の為、もう一度パスワードを入力してください\nPassword:') :

            for n in range(1,maxlength + 1):
                for x in itertools.product(use,repeat=n):
                    result = ''.join(x)
                    if password == result:
                        sys.stdout.write("\r")
                        #sys.stdout.flush()
                        sys.stdout.write(Fore.GREEN + 'As a result of a brute force attack,we found that the password is "{}".'.format(result))
                        #sys.stdout.flush()
                        break
                    elif result_view:
                        sys.stdout.write('\r' + Fore.RED + 'Password did not match! : ' + '{}'.format(result))
                        #sys.stdout.flush()
                else:
                  continue
                break
            else:
                sys.stdout.write('\r' + Fore.RED + 'As a result of a brute force attack,we can not found password.')

        else:
          print('\nIt did not match the first password.\n最初のパスワードと一致しませんでした')

print()