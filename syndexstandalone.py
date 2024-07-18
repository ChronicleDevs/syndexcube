#!/usr/bin/env python

"""
 ░▒▓███████▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓███████▓▒░░▒▓███████▓▒░░▒▓████████▓▒░▒▓█▓▒░░▒▓█▓▒░ 
░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░ 
░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░ 
 ░▒▓██████▓▒░ ░▒▓██████▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓██████▓▒░  ░▒▓██████▓▒░  
       ░▒▓█▓▒░  ░▒▓█▓▒░   ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░ 
       ░▒▓█▓▒░  ░▒▓█▓▒░   ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░ 
░▒▓███████▓▒░   ░▒▓█▓▒░   ░▒▓█▓▒░░▒▓█▓▒░▒▓███████▓▒░░▒▓████████▓▒░▒▓█▓▒░░▒▓█▓▒░ 

    S       Y       N       D       E       X   -    C       U       B       E  
    
SYNDEX CUBE is a simple encryption method that place the original words to random position in a cube (3D array)
Syndex cube is my experimental program. It is created because my curiousity and experiment with Python
Syndex cube might not as effective as other encryption, it takes long time to encrypt big data

and I never tested to crack the syndex cube, so for security, i really couldn't make sure it is secure or not.

CUBE could be bigger than default (10), the most secure for short data is 256 cube length
and for bigger data is  16 cube length.

Syndex could encrypt a binary file.
Tested encrypting & decrypting a python compiled binary file to cube file

Author: github.com/ChronicleDevs (Codename N)
Idea by: N, and K

"""


import math
import string
from colorama import Fore as F
from colorama import Style as S
import random
import base64
from cryptography.fernet import Fernet, InvalidToken
import ast
import binascii
R = S.RESET_ALL

class SyndexCube:
    def __init__(self, cubeSize: int = 256, optimizedEncryption: bool = False, verbose: bool = False) -> None:
        """SyndexCube initiator method

        Args:
            cubeSize (int, optional): set the cube size. Defaults to 256.
            optimizedEncryption (bool, optional): use optimized encryption or not. Defaults to False.
            verbose (bool, optional): show all process. Defaults to False.
        """
        self.__is_verbose = verbose
        self.__optimized = optimizedEncryption
        self.__cubeSize = cubeSize
        
        
    def __verbose(self, msg, quot, noend=False):
        
        if noend: print("["+F.GREEN+quot+R+"] "+msg, end="")
        else: print("["+F.GREEN+quot+R+"] "+msg)
        
        
    def __gen_dummy(self):
        return random.choice(string.ascii_letters+string.digits+string.punctuation)
        
    def __initialize_cube (self, size):
        if self.__is_verbose: self.__verbose("Initializing CUBE with size : "+F.CYAN+str(self.__cubeSize)+R, "SyndexCube"+R+":"+F.YELLOW+"__initialize_cube()")
        
        return [[[self.__gen_dummy() for _ in range(size)] for _ in range(size)] for _ in range(size)]
    def __multcrypt(self, data):
        if self.__is_verbose: self.__verbose("Generating mult encryption.. ", "SyndexCube"+R+":"+F.YELLOW+"__multcrypt()")
    
            
        _ = Fernet.generate_key()
        x = Fernet(_)
        return _, x.encrypt(data).decode()
    
    def __calc_cube_size (self, elength):
        if self.__is_verbose: self.__verbose("Calculating CUBE Size : ", "SyndexCube"+R+":"+F.YELLOW+"__calc_cube_size()", True)
        
        r = math.ceil(elength ** (1/3))
        if self.__is_verbose: print(F.CYAN+str(r))
        return r
    
    @staticmethod
    def decrypt(cube: str|list|tuple, iv: any, key: any) -> str|bytes:
        """Decrypt syncube encryption

        Args:
            cube (str | list | tuple): Cube to decrypt
            iv (str | any): Initial vector to search the correct string
            key (str | any): Key to decrypt the inner data, use SYNDEXOPTIMIZEDREGION when using optimized encryption

        Returns:
            str | bytes: Return decrypted message
        """
        optimized=False
        encoded_str = None
        if type(cube) == str: cube = ast.literal_eval(cube)
        if key == "SYNDEXOPTIMIZEDREGION":
            optimized = True
        try:
            if not optimized:
                encoded_str = ''.join([str(cube[x][y][z]) for x,y,z in ast.literal_eval(base64.b64decode(iv).decode("utf-8"))])
            
                lo = Fernet(key)
                return base64.b64decode(lo.decrypt(encoded_str))
            else:
                encoded_str = ''.join([str(cube[x][y][z]) for x,y,z in ast.literal_eval(base64.b64decode(iv).decode("utf-8"))])
                return base64.b64decode(encoded_str)
        except InvalidToken:
            print(F.RED+"ERROR"+R+" Incorrect Key (Fernet invalid token error)")
            
        except (binascii.Error, UnicodeDecodeError):
            print(F.RED+"ERROR"+R+" Incorrect IV (binascii padding error)")
            exit(2)
            
    
    def __encrypt(self, binary_data: any) -> any:

        if self.__is_verbose: self.__verbose("Encrypting data ", "SyndexCube"+R+":"+F.YELLOW+"encrypt(data)")
        
        encoded_str = base64.b64encode(binary_data)
        key = "SYNDEXOPTIMIZEDREGION"
        if not self.__optimized:
            key, chiper = self.__multcrypt(encoded_str)
            cube_sz = self.__calc_cube_size(len(chiper)*self.__cubeSize)
            cube = self.__initialize_cube(cube_sz)
            iv = self.__randomize_pos(cube, chiper)
        else:
            cube_sz = self.__calc_cube_size(len(encoded_str)*self.__cubeSize)
            cube = self.__initialize_cube(cube_sz)
            iv = self.__randomize_pos(cube, encoded_str)
        return cube, base64.b64encode(str(iv).encode()), key

    def __randomize_pos (self, cube, encoded_str):
        if self.__is_verbose: self.__verbose("Placing data into the cube : ", "SyndexCube"+R+":"+F.YELLOW+"randpos(data)", True)
        
        size = len(cube)
        coord = []
        used_pos = set()
        if type(encoded_str) == bytes: encoded_str = encoded_str.decode()
        for char in encoded_str:
            while True:
                x, y, z = random.randint(0, size-1), random.randint(0, size-1), random.randint(0, size-1)
                if (x,y,z) not in used_pos:
                    cube[x][y][z] = char
                    coord.append((x,y,z))
                    used_pos.add((x,y,z))
                    break

        if self.__is_verbose: print(F.CYAN+"record fail not found (success)"+R)
            
        return coord
    def encrypt(self, data: any, write=""):
        """Encrypt a message to syncube

        Args:
            binary_data (str | any): Message to encrypt
            write (str, optional): name file to write

        Returns:
            any: encrypted message (cube, iv, key)
        """
        import _io
        if type(data) != bytes and not type(data) == _io.BufferedReader: data = data.encode()
        cube, iv, key = self.__encrypt(data)
        if self.__is_verbose:
            print(F.RED+"ENCRYPTED"+R+" : "+F.YELLOW+str(cube))
            
            print(F.CYAN+"IV"+R+" : "+F.LIGHTGREEN_EX+str(iv))
            print(F.CYAN+"KEY"+R+" : "+F.LIGHTGREEN_EX+str(key))
        if len(write) > 0:
            with open(write, "w") as l:
                l.write(str(cube))
                l.close()
        return cube, iv, key

textchars = bytearray({7,8,9,10,12,13,27} | set(range(0x20, 0x100)) - {0x7f})
is_binary_string = lambda bytes: bool(bytes.translate(None, textchars))
import argparse
import argparse, os
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
            sy = SyndexCube.decrypt(wc.read(), args.iv, args.keypass)
            with open(args.output_file, 'w') as wba:
                try:
                    wba.write(sy)
                except TypeError:
                    with open(args.output_file, 'wb') as waa:
                        waa.write(sy)
            
    else:
        print("Encrypting ..")
        k = SyndexCube(args.cubesize, args.optimized, args.verbose)
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
        print(" -- Syncube: Key -> "+str(v))
        print(" -- Syncube: IV -> "+str(i))
        
        if (os.path.exists(os.path.abspath(args.output_file))):
            print("[ "+F.GREEN+"Syncube"+S.RESET_ALL+" ] Complete encrypting : " +F.LIGHTCYAN_EX+args.file+S.RESET_ALL)
        
except Exception as e:
    print(traceback.format_exc())
    print("[ "+F.GREEN+"HWRapper"+S.RESET_ALL+" ] Failed to encrypt : " +F.LIGHTCYAN_EX+args.file)