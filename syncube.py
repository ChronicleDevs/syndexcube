#!/usr/bin/env python
import sys
sys.path.append("/home/wydenial/.local/syndex/lib/")

import random, string, time
def __gen_random(d=8):
    return ''.join(random.choices(string.ascii_letters, k=d))

textchars = bytearray({7,8,9,10,12,13,27} | set(range(0x20, 0x100)) - {0x7f})
is_binary_string = lambda bytes: bool(bytes.translate(None, textchars))
import argparse
import argparse, os
from colorama import Fore
from colorama import Style as S
import SyndexCube
import traceback
parser = argparse.ArgumentParser(description="Encrypt a file with SynCube")
parser.add_argument("file", help="File to encrypt")
parser.add_argument("output_file", help="Output of encrypted file")
parser.add_argument("-d", "--decrypt", help="Decrypt a file, please pass IV and Keypass  arguments when decrypting a cube.", action="store_true")
parser.add_argument("-i", "--iv", metavar="Syncube IV", help="Store IV to the decryption method", required=False)
parser.add_argument("-f", "--cubekey-file", metavar="Cubekey File", help="Store Cubekey file. (Args. IV and Key will be ignored if the CBKeyFile passed)")
parser.add_argument("-p", "--keypass", metavar="Syncube Key", help="Store KEY to the decryption method", required=False)
parser.add_argument("-s", "--cubesize", metavar="Syncube size (0-unlimited)", default=256, type=int, help="Set custom size to cube (The bigger the cube size is, the stronger the encrypted key)", required=False)
parser.add_argument("-t", "--optimized", metavar="false or true", default=False, type=bool, help="Set encryption (is optimized or not) method to the encryptor", required=False)
parser.add_argument("-v", "--verbose", metavar="false or true", default=False, type=bool, help="Show the encryption/decryption process", required=False)
parser.add_argument("-e", "--show-output", metavar="false or true", default=False, type=bool, help="Show the IV and Key directly (not recommended if encrypting big files)", required=False)



args = parser.parse_args()
try:
    
    if args.decrypt:
        if os.path.exists(args.output_file):
            print(Fore.YELLOW+"WARNING"+S.RESET_ALL+": There is a file on the output path. Are you sure to replace the file? \n"+Fore.GREEN+"y/Y"+S.RESET_ALL+" - Yes, replace it.\n"+Fore.RED+"n/N"+S.RESET_ALL+" - No, don't replace it. Leave the file.\n"+Fore.CYAN+"r/R"+S.RESET_ALL+" - Rename the file with random name.")
            while True:
                o = input("\n-> ")
                if o.lower().strip() == "y":
                    break
                elif o.lower().strip() == "r":
                    args.output_file = args.output_file+"."+__gen_random(6)
                    break
                else:
                    exit(2)
                
        # Priority : f - ivk
        if (args.iv == None or args.keypass == None) and args.cubekey_file == None:
            print("Please specify IV and Key when decrypting; \ne. g. :\n\tsyncube -d (your file) (output file) -i (your iv) -p (your key)\n\tOR\n\tsyncube -d (your file) (output file) -f (cubekey file)")
            exit(2)
        IV = ""
        Keygex = ""
        if args.cubekey_file == None and (args.iv != None and args.keypass != None):
            IV = args.iv
            Keygex = args.key
        if args.cubekey_file != None:
            with open(args.cubekey_file, "r") as wc:
                wp = wc.read()
                try:
                    __reignregion = wp.split("/")
                    __ivreg = __reignregion[0]
                    __keyreg = __reignregion[-1]
                    
                    __is_optimized = False
                    if __keyreg == "SYNDEXOPTIMIZEDREGION": __is_optimized = True
                    if not __is_optimized:
                        if not ((__keyreg.startswith("b'") and __keyreg.endswith("'")) and (__ivreg.startswith("b\'") and __ivreg.endswith("'"))):
                            raise IndexError()
                    else:
                        if not __ivreg.endswith("]]]"):
                            raise IndexError()
        
                    if __ivreg.startswith("b\'") and __ivreg.endswith("'"):
                        __ivreg = __ivreg[2:-1]
                    if __keyreg.startswith("b\'") and __keyreg.endswith("'"):
                        __keyreg = __keyreg[2:-1]
                    
                    Keygex = __keyreg
                    IV = __ivreg
                except IndexError:
                    print("Decryption failed, File : "+Fore.YELLOW+args.cubekey_file+S.RESET_ALL+" is not a valid cubekey file")

        with open(args.file, 'r') as wc:
            st = time.time()

            sy = SyndexCube.SyndexCube.decrypt(wc.read(), IV, Keygex)
            with open(args.output_file, 'w') as wba:
                try:
                    wba.write(sy)
                except TypeError:
                    with open(args.output_file, 'wb') as waa:
                        waa.write(sy)
                        
                et = time.time()
                col = et - st
                print("File decryption took ~"+Fore.CYAN+str(col)+S.RESET_ALL+" seconds")
            if (os.path.exists(os.path.abspath(args.output_file))):
                print("[ "+Fore.GREEN+"Syncube"+S.RESET_ALL+" ] Complete decrypting : " +Fore.LIGHTCYAN_EX+args.file+S.RESET_ALL)

                
                
                
            
    else:
        if os.path.exists(args.output_file):
            print(Fore.YELLOW+"WARNING"+S.RESET_ALL+": There is a file on the output path. Are you sure to replace the file? \n"+Fore.GREEN+"y/Y"+S.RESET_ALL+" - Yes, replace it.\n"+Fore.RED+"n/N"+S.RESET_ALL+" - No, don't replace it. Leave the file.\n"+Fore.CYAN+"r/R"+S.RESET_ALL+" - Rename the file with random name.")
            while True:
                o = input("\n-> ")
                if o.lower().strip() == "y":
                    break
                elif o.lower().strip() == "r":
                    args.output_file = args.output_file+"."+__gen_random(6)
                    break
                else:
                    exit(2)
        args.output_file = args.output_file+".cbex"
        
        st = time.time()
        print("Encrypting ..")
        k = SyndexCube.SyndexCube(args.cubesize, args.optimized, args.verbose)
        cube, i, v = [None, None, None]
        if is_binary_string(open(args.file, 'rb').read(1024)):
            with open(args.file, 'rb') as wc:
                cube, i,v = k.encrypt(wc.read())
                with open(args.output_file, 'w') as w:
                    w.write(str(cube))
        else:
            with open(args.file, 'r') as wc:
                cube, i,v = k.encrypt(wc.read())
                with open(args.output_file, 'w') as w:
                    w.write(str(cube))
        
        if args.show_output:
            print(" -- Syncube: Key -> "+str(v))
            print(" -- Syncube: IV -> "+str(i))
        else:
            cfg =args.file+"."+__gen_random()+".cbkey"
            with open(cfg, "w") as wf:
                print(" -- Writing the key to a file: "+Fore.YELLOW+cfg+S.RESET_ALL)
                ctx = str(i)+"/"+str(v)
                wf.write(ctx)
        et = time.time()
        elapsed_time = et - st
        print("File encryption took ~"+Fore.CYAN+str(elapsed_time)+S.RESET_ALL+" seconds")
        if (os.path.exists(os.path.abspath(args.output_file))):
            print("[ "+Fore.GREEN+"Syncube"+S.RESET_ALL+" ] Complete encrypting : " +Fore.LIGHTCYAN_EX+args.file+S.RESET_ALL)
except FileNotFoundError as e:
    print("SyndexCUBE enc/dec failed due to an "+Fore.RED+"ERROR"+S.RESET_ALL)
    print("File not found : "+Fore.RED+str(e.filename)+S.RESET_ALL)
except Exception as e:
    print(traceback.format_exc())
    print("[ "+Fore.GREEN+"HWRapper"+S.RESET_ALL+" ] Failed to encrypt : " +Fore.LIGHTCYAN_EX+args.file)
