#!/usr/bin/env python3
import random
import readline
import json

def load_questions_from_file(file_name):
    with open(file_name, 'r') as file:
        return json.load(file)

def generate_question(question_dict):
    question_text = question_dict['question']
    choices = [choice.split('. ')[1] for choice in question_dict['choices']]  # Remove the letter from each choice
    answer = question_dict['answer']
    
    return question_text, choices, answer


def get_questions():
    question_data = load_questions_from_file('questions.json')
    
    print('Choose the sections to include in the test:')
    print('0 - Select All')
    print('1 - Documentation and Policy')
    print('2 - Recon')
    print('3 - Initial Access')
    print('4 - Post Exploitation')
    print('5 - Persistence')
    print('6 - Privilege Escalation')
    print('7 - Lateral Movement')
    print('8 - Logging')
    print('9 - Enumeration')
    print('10 - Infrastructure')
    print('11 - Halting Conditions')
    print('12 - Sanitization')
    print('13 - Phishing')

    while True:
        sections = input('Enter the sections to include separated by commas (e.g., 0,1,2): ')
        print()
        sections = sections.split(',')

        questions = []

        for section in sections:
            section = section.strip()
            
            if section == '0':
                questions += (
                    question_data['documentation_questions'] +
                    question_data['recon_questions'] +
                    question_data['initial_access_questions'] +
                    question_data['post_exploitation_questions'] +
                    question_data['persistence_questions'] +
                    question_data['privilege_escalation_questions'] +
                    question_data['lateral_movement_questions'] +
                    question_data['logging_questions'] +
                    question_data['enumeration_questions'] +
                    question_data['infrastructure_questions'] +
                    question_data['halting_conditions_questions'] +
                    question_data['sanitization_questions'] +
                    question_data['phishing_questions']
                )
            elif section == '1':
                questions += question_data['documentation_questions']
            elif section == '2':
                questions += question_data['recon_questions']
            elif section == '3':
                questions += question_data['initial_access_questions']
            elif section == '4':
                questions += question_data['post_exploitation_questions']
            elif section == '5':
                questions += question_data['persistence_questions']
            elif section == '6':
                questions += question_data['privilege_escalation_questions']
            elif section == '7':
                questions += question_data['lateral_movement_questions']
            elif section == '8':
                questions += question_data['logging_questions']
            elif section == '9':
                questions += question_data['enumeration_questions']
            elif section == '10':
                questions += question_data['infrastructure_questions']
            elif section == '11':
                questions += question_data['halting_conditions_questions']
            elif section == '12':
                questions += question_data['sanitization_questions']
            elif section == '13':
                questions += question_data['phishing_questions']
            else:
                print(f'Invalid section: {section}. Please enter valid section numbers.')
                continue

        if questions:
            break
        else:
            print('Error: No sections selected. Please select at least one section.')

    num_questions = input('Enter the number of questions for the quiz (default 10): ')
    print()
    if not num_questions:
        num_questions = 10
    else:
        num_questions = int(num_questions)
    random.shuffle(questions)
    return questions[:num_questions]


def main():
    questions = get_questions()
    random.shuffle(questions)

    score = 0
    missed_questions = []  # Create a list to store missed questions
    for idx, question_dict in enumerate(questions, start=1):
        question, choices, answer = generate_question(question_dict)
        
        # Display the question and choices
        print(f'\nQuestion {idx}: {question}')
        for i, choice in enumerate(choices, start=65):  # ASCII code for 'A'
            print(f'{chr(i)}. {choice}')

        user_answer = input('> ')

        if user_answer.upper() == answer:  # Compare with the correct answer
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
