#################################################################
# User (class) - Proy2 Expoandes: IntroISIS 2024-10
#################################################################

from src import config as cf

#################################################################
# imports

from src.objects.answerLog import AnswerLog

assert cf

#################################################################
# class definition

class User:
    
    # constructor
    
    def __init__( self, usernameU, passwordU ):
        """Nuevo User para la base de datos

        Args:
            this (User): this object
            usernameU (str): username del usuario
            passwordU (str): password del usuario
        """
        self.username = usernameU
        self.password = passwordU
        self.answerLog = AnswerLog( usernameU )

    # metodos

    def newQuestionSet( self, questions ):
        """Agrega un nuevo set de preguntas al usuario

        Args:
            this (User): this object
            questionsU (dict): preguntas -> { int: str } = { 1:'q1', 2:'q2', ... , n:'qn' }
        """
        self.answerLog.newQuestionSet( questions, {} )
        
    def updateQuestion( self, questionID, newQuestion, requiresNewAnswer ):
        """Actualiza el contenido de una pregunta.
        Si la pregunta no existe, no hace nada.
        Si questionID = n+1 -> agrega una nueva pregunta

        Args:
            this (User): this object
            questionID (int): numero de la pregunta
            newAnswer (str): nueva respuesta
            requiresNewAnswer (bool): determina si se necesita una nueva respuesta o no
        """
        questionSet = self.answerLog.questions
        lastQuestionID = questionSet.keys()[-1]
        
        if (questionID in questionSet) or (questionID == lastQuestionID+1):
            self.answerLog.updateQuestion( questionID, newQuestion, requiresNewAnswer )
        
    def newAnswerSet( self, answers ):
        """Agrega un nuevo set de respuestas al usuario

        Args:
            this (User): this object
            answersU (dict): respuestas -> { int: str } = { 1:'a1', 2:'a2', ... , n:'an' }
        """
        self.answerLog.newAnswerSet( answers )
        
    def updateAnswer( self, questionID, newAnswer ):
        """Actualiza la respuesta de un usuario a una pregunta específica.
        Si la pregunta no existe, no hace nada.

        Args:
            this (User): this object
            questionID (int): numero de la pregunta
            newAnswer (str): nueva respuesta
        """
        answerSet = self.answerLog.answers
        
        if questionID in answerSet:
            self.answerLog.updateAnswer( questionID, newAnswer )
            
        