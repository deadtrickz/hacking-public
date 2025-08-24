# Creating Custom Wordlists

## Web Content Based Wordlist

##### cewl
```bash
sudo cewl -d 2 -m 5 -w wordlist.txt www.[SITE].com
```

|Option |Description |
| ---| ---|
|-d| Depth to spider (default 2)|
|-m| Minimum world lenth to scrape (default 3)|
|-w| Write output to file|


## File Based Wordlist

##### SED
- all filenames in /usr/bin
```sh
ls -sa /usr/bin | sed 's/[0-9]*//g' | sed -r 's/\s+//g' |sort -u > $HOME/binaries-wordlist.txt
```

