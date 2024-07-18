#!/usr/bin/env python

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
parser.add_argument("-p", "--keypass", metavar="Syncube Key", help="Store KEY to the decryption method", required=False)
parser.add_argument("-s", "--cubesize", metavar="Syncube size (0-unlimited)", default=256, type=int, help="Set custom size to cube", required=False)
parser.add_argument("-o", "--optimized", metavar="false or true", default=False, type=bool, help="Set encryption (is optimized or not) method to the encryptor", required=False)
parser.add_argument("-v", "--verbose", metavar="false or true", default=False, type=bool, help="Set encryption (is optimized or not) method to the encryptor", required=False)


# parser.add_argument("-s", "--shell", help="Enter Hence shell", required=False)

args = parser.parse_args()
try:
    
    if args.decrypt:
        if args.iv == None or args.keypass == None:
            print("Please specify IV and Key when decrypting; \ne. g. :\n\t syncube -d (your file) (output file) -i (your iv) -p (your key)")
            exit(2)
        with open(args.file, 'r') as wc:
            sy = SyndexCube.SyndexCube.decrypt(wc.read(), args.iv, args.keypass)
            with open(args.output_file, 'w') as wba:
                try:
                    wba.write(sy)
                except TypeError:
                    with open(args.output_file, 'wb') as waa:
                        waa.write(sy)
            
    else:
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
                    w.write(cube)
        print(" -- Syncube: Key -> "+str(v))
        print(" -- Syncube: IV -> "+str(i))
        
        if (os.path.exists(os.path.abspath(args.output_file))):
            print("[ "+Fore.GREEN+"Syncube"+S.RESET_ALL+" ] Complete encrypting : " +Fore.LIGHTCYAN_EX+args.file+S.RESET_ALL)
        
except Exception as e:
    print(traceback.format_exc())
    print("[ "+Fore.GREEN+"HWRapper"+S.RESET_ALL+" ] Failed to encrypt : " +Fore.LIGHTCYAN_EX+args.file)