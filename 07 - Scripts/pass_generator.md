# pass_generator.py
- generates a random 30 character password
- -n allows a Number of passwords to be created
- -o allows for an output file

##### CODE
```python
#!/usr/bin/python3
import time
import random
import string
import argparse

# Parse command-line arguments
parser = argparse.ArgumentParser()
parser.add_argument("-o", "--output", metavar="FILE", help="output password(s) to FILE")
parser.add_argument("-n", "--number", type=int, default=1, help="number of passwords to generate (default: 1)")
args = parser.parse_args()

# Get the current time in seconds since the epoch
utc_time = time.time()

# Seed the random number generator with the current time
random.seed(utc_time)

allowed_punctuation = '!?@#$*+_'

# Generate the specified number of passwords with at least 30 characters each
password_characters = string.ascii_letters + string.digits + allowed_punctuation
passwords = ["".join(random.choices(password_characters, k=30)) for _ in range(args.number)]

# Output the password(s) to a file if the -o option is specified
if args.output:
    with open(args.output, "w") as f:
        f.write("\n".join(passwords))
    print(f"{len(passwords)} passwords written to file '{args.output}'")
else:
    for password in passwords:
        print(password)
```