# pass_generator.py
- generates a random 30 character password
- -n allows a Number of passwords to be created
- -o allows for an output file

### Usage

##### Generate Random Password
```
./pass_generator
```

##### Generate 10 random passwords and write them to a file
```
./pass_generator -n 10 -o [FILE].txt
```

##### CODE
```python
#!/usr/bin/python3
import time
import random
import string
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-o", "--output", metavar="FILE", help="output password(s) to FILE")
parser.add_argument("-n", "--number", type=int, default=1, help="number of passwords to generate (default: 1)")
args = parser.parse_args()
utc_time = time.time()
random.seed(utc_time)
allowed_punctuation = '!?@#$*+_'
password_characters = string.ascii_letters + string.digits + allowed_punctuation
passwords = ["".join(random.choices(password_characters, k=30)) for _ in range(args.number)]
if args.output:
    with open(args.output, "w") as f:
        f.write("\n".join(passwords))
    print(f"{len(passwords)} passwords written to file '{args.output}'")
else:
    for password in passwords:
        print(password)
```