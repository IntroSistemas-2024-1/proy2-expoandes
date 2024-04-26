#################################################################
# AnswerLog (class) - Proy2 Expoandes: IntroISIS 2024-10
#################################################################


#################################################################
# imports


#################################################################
# class definition

class AnswerLog:
    
    # constructor
    
    def __init__( this, usernameU ):
        """Nuevo AnswerLog de un usuario
        preguntas -> { int: str } = { 1:'q1', 2:'q2', ... , n:'qn' }
        respuestas -> { int: str } = { 1:'a1', 2:'a2', ... , n:'an' }

        Args:
            this (AnswerLog): this object
            usernameU (str): username del usuario al cual le pertenece el AnswerLog
        """
        this.username = usernameU
    
    # metodos 
       
    def newQuestionSet( this, questionsU ):
        """Nuevo diccionario de preguntas del AnswerLog y genera un diccionario de respuestas
        con los mismos índices

        Args:
            this (AnswerLog): this object
            questionsU (dict): preguntas -> { int: str } = { 1:'q1', 2:'q2', ... , n:'qn' }
        """
        this.questions = questionsU
        
        answersU = {}
        for questionID in questionsU.keys():
            answersU[ questionID ] = None
        
        this.answers = answersU
        
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
        this.questions[ questionID ] = newQuestion
        
        if (requiresNewAnswer) or (questionID not in this.answers):
            this.answers[ questionID ] = None
        
    def newAnswerSet( this, answersU ):
        """Nuevo diccionario de respuestas del AnswerLog

        Args:
            this (AnswerLog): this object
            answersU (dict): respuestas -> { int: str } = { 1:'a1', 2:'a2', ... , n:'an' }
        """
        this.answers = answersU
        
    def updateAnswer( this, questionID, newAnswer ):
        """Actualiza la respuesta de un usuario a una pregunta específica.

        Args:
            this (User): this object
            questionID (int): numero de la pregunta
            newAnswer (str): nueva respuesta
        """
        this.answers[ questionID ] = newAnswer