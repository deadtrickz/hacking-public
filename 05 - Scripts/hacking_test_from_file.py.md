# hacking_test_from_file.py
---
- uses a json file "questions.json" to read the questions
- must be in the same directory as the python file

```python
#!/usr/bin/env python3
import random
import readline
import json

users = ['wonderbread-svc', 'root', 'svc-mgr-d01', 'cole.justin-admin', 'coral-svc-acct', 'aaron.waters-admin']
domains = ['123.com', '123.com']
passwords = ['12345', '123456!', '1234567!']
hashes = ['fakehash1', 'fakehash2', 'fakehash3']
ips = ['192.168.1.5', '192.168.1.4', '192.168.1.8', '192.168.1.76', '192.168.1.41']
payloads = ['~/Desktop/F8edG4b.exe', '~/Downloads/not-evil.exe', '~/Desktop/notnot.exe', '~/Documents/backstreet-boys-full-album-mp3-dark-ripper.zip.exe' ]
exfil = ['c:\\Users\\jjustin\\passwords.txt', 'c:\\Users\\mmichaels\\hashdump.txt', '/etc/password', 'c:\\Users\\Public\\financial-data.pdf', 'c:\\Users\\sjustin\\Documents\\not-not\\company-secrets.docx', 'c:\\Users\\Public\\budget.xlsx']
pids = ['7247', '565', '228', '8294', '35', '17023', '24972', '424', '1790', '1801', '1291', '1413']
hostnames = ['webserver01.fake.com', 'mailserver08.fake.com', 'database-sql-04.fake.com', 'fileserver-04.fake.com', 'dc01.fake.com']
ports = ['22', '80', '443', '3389', '8080', '21', '4444', '5756', '9891']
emails = ['j.carver@yahoo.com', 'martin.z.pfaftz@fake.com', 'brack.l.camplinton@fake.com', 'coral.w.dead@fake.com', 'capt.lt.jg@fake.com']
services = ['http', 'https', 'ssh', 'ftp', 'smtp']
file_paths = ['/var/log/syslog', '/etc/passwd', 'C:\\Windows\\System32\\config\\SAM', '/var/www/html/index.html']
txt_files = ['~/Desktop/test.txt', '~/Documents/payload.txt', '~/Downloads/b64-txt-file.txt', '~/Desktop/12345.txt']
commands = ['whois', 'net user', 'whoami']
dir_wordlists = ['/usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt', '/usr/share/wordlists/dirb/common.txt', '/usr/share/wordlists/seclists/Discovery/Web-Content/directory-list-lowercase-2.3-medium.txt', '/usr/share/wordlists/seclists/Discovery/Web-Content/dirsearch.txt']
sleep = [5, 10, 15, 20, 30]
jitter = ['45', '65', '80']
listener = ['https_443', 'https_turtle', 'https_lownslow', 'https_not_evil']

def generate_question(question_dict):
    question = '\n'.join(question_dict['question'])
    answer = question_dict['answer']
    alternate_answers = question_dict.get('alternate_answers', [])

    random_var = {} 
    for var_name in ['<IP>', '<user>', '<pass>', '<domain>', '<hash>', '<payload>', '<exfil>', '<pid>', '<hostname>', '<port>', '<email>', '<service>', '<file_path>', '<txt>', '<command>', '<dirw>', '<sleep>', '<jitter>', '<listener>']:
        if var_name in question:
            if var_name == '<sleep>':
                var_key = 'sleep'
                random_value = random.choice(globals()[var_key])
                # Convert sleep minutes to seconds for answer
                random_value_seconds = str(int(random_value) * 60)
                answer = answer.replace('<sleep_seconds>', random_value_seconds, 1)
                question = question.replace(var_name, str(random_value), 1)  # Convert random_value to string here
            elif var_name == '<pass>':
                var_key = 'passwords'
            elif var_name == '<hash>':
                var_key = 'hashes'
            elif var_name == '<exfil>':
                var_key = 'exfil'
            elif var_name == '<pid>':
                var_key = 'pids'
            elif var_name == '<hostname>':
                var_key = 'hostnames'
            elif var_name == '<port>':
                var_key = 'ports'
            elif var_name == '<email>':
                var_key = 'emails'
            elif var_name == '<service>':
                var_key = 'services'
            elif var_name == '<file_path>':
                var_key = 'file_paths'
            elif var_name == '<txt>':
                var_key = 'txt_files'
            elif var_name == '<command>':
                var_key = 'commands'
            elif var_name == '<dirw>':
                var_key = 'dir_wordlists'
            elif var_name == '<jitter>':
                var_key = 'jitter'
            elif var_name == '<listener>':
                var_key = 'listener'
            else:
                var_key = var_name[1:-1].lower() + 's'

            random_value = random.choice(globals()[var_key])
            question = question.replace(var_name, str(random_value), 1)  # Convert random_value to string here
            answer = answer.replace(var_name, str(random_value), 1)

            for i, alt_answer in enumerate(alternate_answers):
                alternate_answers[i] = alt_answer.replace(var_name, str(random_value), 1)

            random_var[var_name] = random_value

    return question, answer, alternate_answers, random_var

def load_questions_from_file(file_name):
    with open(file_name, 'r') as file:
        return json.load(file)

question_data = load_questions_from_file('questions.json')

recon_questions = question_data['recon_questions']
webenum_questions = question_data['webenum_questions']
sa_questions = question_data['sa_questions']
crackmapexec_questions = question_data['crackmapexec_questions']
psexec_questions = question_data['psexec_questions']
cs_questions = question_data['cs_questions']

def get_questions():
    print('Answer all questions with the arguments in the order they are listed, where applicable')
    print('When possible, the IP should be the last line in a command. Otherwise refer to the tool being used')
    print('')
    print('Choose the sections to include in the test:')
    print('0 - All sections')
    print('1 - Recon/Discovery')
    print('2 - Web Enumeration')
    print('3 - Situational Awareness')
    print('4 - Crackmapexec')
    print('5 - Psexec')
    print('6 - Cobalt Strike')
#    print('7 - TBD')
# annoying and complicated ssh questions
## ssh -L <local_port>:<remote_host>:<remote_port> <target>
# hydra/johntheripper
## hydra -l <username> -P <wordlist> <target> <protocol>
# netcat
# sqlmap
# wget/certutil/curl
# proxychains
# pdf recon
# 
    while True:
        sections = input('Enter the sections to include separated by commas (e.g. 1,2,3 or 0 for all): ')
        print()
        sections = sections.split(',')
        if '0' in sections and len(sections) > 1:
            print('Error: Cannot select 0 with other sections')
        else:
            break
    questions = []
    if '0' in sections:
        questions += recon_questions + webenum_questions + sa_questions + crackmapexec_questions + psexec_questions + cs_questions
    else:
        if '1' in sections:
            questions += recon_questions
        if '2' in sections:
            questions += webenum_questions
        if '3' in sections:
            questions += sa_questions
        if '4' in sections:
            questions += crackmapexec_questions
        if '5' in sections:
            questions += psexec_questions
        if '6' in sections:
            questions += cs_questions
        if '7' in sections:
            questions += TBD
    num_questions = input('Enter the number of questions for the quiz (default 10): ')
    print()
    if not num_questions:
        num_questions = 10
    else:
        num_questions = int(num_questions)
    random.shuffle(questions)
    return questions[:num_questions]
#    return questions

def main():
    questions = get_questions()
    random.shuffle(questions)

    score = 0
    missed_questions = []  # Create a list to store missed questions
    for idx, question_dict in enumerate(questions, start=1):
        question, answer, alternate_answers, random_var = generate_question(question_dict)
        print(f'Question {idx}: {question}')
        user_answer = input('> ')

        if user_answer.strip() == answer.strip() or user_answer.strip() in [alt.strip() for alt in alternate_answers]:  # Removed .lower() calls
            print('Correct!\n')
            score += 1
        else:
            print(f'Incorrect. The correct answer is: {answer}\n')
            missed_questions.append((question, answer))  # Add the missed question and its answer to the list

    # Print missed questions
    if missed_questions:
        print("Missed questions:")
        for idx, (question, answer) in enumerate(missed_questions, start=1):
            print(f'{idx}. {question}')
            print(f'   Correct answer: {answer}\n')
    else:
        print("You answered all questions correctly!")

    # Print score after missed questions
    print(f'You scored {score}/{len(questions)} ({(score/len(questions))*100:.2f}%)\n')

if __name__ == '__main__':
    main()

```