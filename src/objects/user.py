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
    
    def __init__( this, usernameU, passwordU ):
        """Nuevo User para la base de datos

        Args:
            this (User): this object
            usernameU (str): username del usuario
            passwordU (str): password del usuario
        """
        this.username = usernameU
        this.password = passwordU
        this.answerLog = AnswerLog( usernameU )

    # metodos

    def newQuestionSet( this, questions ):
        """Agrega un nuevo set de preguntas al usuario

        Args:
            this (User): this object
            questionsU (dict): preguntas -> { int: str } = { 1:'q1', 2:'q2', ... , n:'qn' }
        """
        this.answerLog.newQuestionSet( questions )
        
    def updateQuestion( this, questionID, newQuestion, requiresNewAnswer ):
        """Actualiza el contenido de una pregunta.
        Si la pregunta no existe, no hace nada.
        Si questionID = n+1 -> agrega una nueva pregunta

        Args:
            this (User): this object
            questionID (int): numero de la pregunta
            newAnswer (str): nueva respuesta
            requiresNewAnswer (bool): determina si se necesita una nueva respuesta o no
        """
        questionSet = this.answerLog.questions
        lastQuestionID = questionSet.keys()[-1]
        
        if (questionID in questionSet) or (questionID == lastQuestionID+1):
            this.answerLog.updateQuestion( questionID, newQuestion, requiresNewAnswer )
        
    def newAnswerSet( this, answers ):
        """Agrega un nuevo set de respuestas al usuario

        Args:
            this (User): this object
            answersU (dict): respuestas -> { int: str } = { 1:'a1', 2:'a2', ... , n:'an' }
        """
        this.answerLog.newAnswerSet( answers )
        
    def updateAnswer( this, questionID, newAnswer ):
        """Actualiza la respuesta de un usuario a una pregunta específica.
        Si la pregunta no existe, no hace nada.

        Args:
            this (User): this object
            questionID (int): numero de la pregunta
            newAnswer (str): nueva respuesta
        """
        answerSet = this.answerLog.answers
        
        if questionID in answerSet:
            this.answerLog.updateAnswer( questionID, newAnswer )
            
        