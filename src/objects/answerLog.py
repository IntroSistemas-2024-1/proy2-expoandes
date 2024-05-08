#################################################################
# AnswerLog (class) - Proy2 Expoandes: IntroISIS 2024-10
#################################################################

from src import config as cf

#################################################################
# imports

assert cf

#################################################################
# class definition

class AnswerLog:
    
    # constructor
    
    def __init__( self, usernameU ):
        """Nuevo AnswerLog de un usuario
        preguntas -> { int: str } = { 1:'q1', 2:'q2', ... , n:'qn' }
        respuestas -> { int: str } = { 1:'a1', 2:'a2', ... , n:'an' }
        types -> { int: str } = { 1:'a1', 2:'a2', ... , n:'an' }

        Args:
            this (AnswerLog): this object
            usernameU (str): username del usuario al cual le pertenece el AnswerLog
        """
        self.username = usernameU
    
    # metodos 
       
    def newQuestionSet( self, questionsU, typeU ):
        """Nuevo diccionario de preguntas del AnswerLog y genera un diccionario de respuestas
        con los mismos índices

        Args:
            this (AnswerLog): this object
            questionsU (dict): preguntas -> { int: str } = { 1:'q1', 2:'q2', ... , n:'qn' }
            typeU (dict): { int: str } = { 1:'a1', 2:'a2', ... , n:'an' }
        """
        self.questions = questionsU
        self.types = typeU
        
        answersU = {}
        for questionID in questionsU.keys():
            answersU[ questionID ] = None
        
        self.answers = answersU
        
    def updateQuestion( self, questionID, newQuestion, questionType, requiresNewAnswer ):
        """Actualiza el contenido de una pregunta.
        Si la pregunta no existe, no hace nada.
        Si questionID = n+1 -> agrega una nueva pregunta
        
        Args:
            this (User): this object
            questionID (int): numero de la pregunta
            newQuestion (str): nueva question
            requiresNewAnswer (bool): determina si se necesita una nueva respuesta o no
        """
        self.questions[ questionID ] = newQuestion
        
        if (requiresNewAnswer) or (questionID not in this.answers):
            self.answers[ questionID ] = None
        
    def newAnswerSet( self, answersU ):
        """Nuevo diccionario de respuestas del AnswerLog

        Args:
            this (AnswerLog): this object
            answersU (dict): respuestas -> { int: str } = { 1:'a1', 2:'a2', ... , n:'an' }
        """
        self.answers = answersU
        
    def updateAnswer( self, questionID, newAnswer ):
        """Actualiza la respuesta de un usuario a una pregunta específica.

        Args:
            this (User): this object
            questionID (int): numero de la pregunta
            newAnswer (str): nueva respuesta
        """
        self.answers[ questionID ] = newAnswer