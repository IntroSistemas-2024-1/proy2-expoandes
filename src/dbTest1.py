#################################################################
# dbTest1 (test_file) - Proy2 Expoandes: IntroISIS 2024-10
#################################################################

import config as cf

#################################################################
# imports

from src.objects.answerLog import AnswerLog
from src.objects.user import User

import pandas as pd
from pandas import DataFrame as df

assert cf

#################################################################
# test

print( f'\n==== Inicio Prueba ====\n')

dummy_username = 'Pedro'
dummy_password = '1234'
dummy_question1 = 'Cuantos anios tienes?'
dummy_question2 = 'Tienes mascotas?'
dummy_answer1 = '20'
dummy_answer2 = 'Si'

dummy_user = User(dummy_username, dummy_password)

dummy_question_set = { 1:dummy_question1, 2:dummy_question2 }
dummy_user.newQuestionSet( dummy_question_set )

dummy_answer_set = { 1:dummy_answer1, 2:dummy_answer2 }
dummy_user.updateAnswer( 1, dummy_answer1 )
dummy_user.updateAnswer( 2, dummy_answer2 )

user_answer_log = dummy_user.answerLog

user_question_set = user_answer_log.questions
user_answer_set = user_answer_log.answers

for questionID in user_question_set:
    # get question vs. answer
    question = user_question_set[ questionID ]
    answer = user_answer_set[ questionID ]
    print( f'Question: {question} -> test result = { question == dummy_question_set[ questionID ] }')
    print( f'Answer: {answer} -> test result = { answer == dummy_answer_set[ questionID ] }')
    print('\n')
