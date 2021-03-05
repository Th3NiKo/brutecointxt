# bruteforcetxt

## Table of contents
* [Description](#description)
* [Getting Started](#getting-started)
** [Quick start](#quick-start)
** [Docker](#docker)
* [Usage](#usage)
* [Output](#output)

## Description
Simple script to brute force text file filled with passphrases and print any keys with available balance. \
Program check for both compressed and uncompressed versions of addresses using [bit](https://github.com/ofek/bit) library.

DISCLAIMER: Program created for educational purposes only. \
Don't steal anybody bitcoins and don't use easy to guess passphrases.

## Getting Started

### Quick start
You need python3.x in order to use script.

Libraries used: [tqdm](https://github.com/tqdm/tqdm) and [bit](https://github.com/ofek/bit). You can install both using pip.

```
pip install -r requirements.txt
```

Check if script works and show help
```
python brutecointxt.py -h
```

### Docker
Simple dockerfile included.

Example build (if u are inside script folder):
```
docker build -t bruteforcetxt .
```

then u can use it (as one time run on test.txt)
```
docker run --rm --name bruteforcetxt-running bruteforcetxt
```
or to use script from console
```
docker run -it --name bruteforcetxt-run bruteforcetxt /bin/bash  
```

## Usage

```
brutecointxt.py [-h] -t TEXT_FILE [-l] [-u] [-r] [-n]

-h, --help            show this help message and exit
  -t TEXT_FILE, --txt TEXT_FILE
                        Text file (UTF-8 encoding) with passphrases. Each line
                        containting one example. (example: passphrases.txt)
  -l, --lowercase       Additional check for lowercased version of passphrases
  -u, --uppercase       Additional check for uppercased version of passphrases
  -r, --reverse         Additional check for reversed version of passphrases
  -n, --no-uncomp       Do not check uncompressed version of addresses
```

Example use:
```
python brutecointxt.py -t passphrases.txt > output.txt
```
I recommend redirecting output to file as above to avoid loading bar misplacing. \
Empty file simply means that no addresses with avaliable balance were found.

If u want to check additionaly for **lowercase, uppercase and reversed** version of passphrases (it's going to be slower)
```
python brutecointxt.py -l -u -r -t passphrases.txt > output.txt
```

If u want to check **only compressed addresses** (it's going to be faster) 
```
python brutecointxt.py -n passphrases.txt > output.txt
```

## Output
Example output for default options
```

Passphrase:  bitcoin is awesome
Private key hex:  23d4a09295be678b21a5f1dceae1f634a69c1b41775f680ebf8165266471401b
Private key wif:  KxRMt7KypfEsLNSikhxTPYepDMBizHNmH5Bii3wssgesxrkHNJg6
Compressed address:  1JRW4d8vHZseMEtYbgJ7MwPG1TasHUUVNq
Uncompressed address:  14NWDXkQwcGN1Pd9fboL8npVynD5SfyJAE
Balance:  1.11

Passphrase:  Bitcoin is awesome123
Private key hex:  fba656d058d6808ddfccc19adda92ec19a4dd0ec465cedb252fb1edcd426f049
Private key wif:  L5etHr5JZE7BN9MVCJ67nn2teaFSVFjdXugDkdBiThct9KjRDfGw
Compressed address:  1Ef4TwFNkPtbdRjmyZ5P4ExcgpA5pK5T4e
Uncompressed address:  13msVisdxKsFDUjo59R77AAthynWqqKUmP
Balance:  2.22

```

Example output for -n option (without uncompressed)
```

Passphrase:  bitcoin is awesome
Private key hex:  23d4a09295be678b21a5f1dceae1f634a69c1b41775f680ebf8165266471401b
Private key wif:  KxRMt7KypfEsLNSikhxTPYepDMBizHNmH5Bii3wssgesxrkHNJg6
Compressed address:  1JRW4d8vHZseMEtYbgJ7MwPG1TasHUUVNq
Balance:  0.0

Passphrase:  Bitcoin is awesome123
Private key hex:  fba656d058d6808ddfccc19adda92ec19a4dd0ec465cedb252fb1edcd426f049
Private key wif:  L5etHr5JZE7BN9MVCJ67nn2teaFSVFjdXugDkdBiThct9KjRDfGw
Compressed address:  1Ef4TwFNkPtbdRjmyZ5P4ExcgpA5pK5T4e
Balance:  0.0


```