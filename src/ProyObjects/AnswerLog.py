#################################################################
# AnswerLog (class) - Proy2 Expoandes: IntroISIS 2024-10
#################################################################


#################################################################
# imports


#################################################################
# class definition

class AnswerLog:
    
    def __init__( this, usernameU, questionsU, answersU ):
        """Nuevo AnswerLog de un usuario
        preguntas -> { int: str } = { 1:'q1', 2:'q2', ... , n:'qn' }
        respuestas -> { int: str } = { 1:'a1', 2:'a2', ... , n:'an' }

        Args:
            this (AnswerLog): this object
            usernameU (str): username del usuario al cual le pertenece el AnswerLog
        """
        this.username = usernameU
        this.questions = {}
        this.answers = {}
        
    def newQuestionSet( this, questionsU ):
        """Nuevo diccionario de preguntas del AnswerLog

        Args:
            this (AnswerLog): this object
            questionsU (dict): preguntas -> { int: str } = { 1:'q1', 2:'q2', ... , n:'qn' }
        """
        this.questions = questionsU
        
    def newAnswerSet( this, answersU ):
        """Nuevo diccionario de respuestas del AnswerLog

        Args:
            this (AnswerLog): this object
            answersU (dict): respuestas -> { int: str } = { 1:'a1', 2:'a2', ... , n:'an' }
        """
        this.answers = answersU
        
    def updateAnswer( this, answerID, newAnswer ):
        """Actualiza la respuesta de un usuario a una pregunta específica.

        Args:
            this (User): this object
            answerID (int): numero de la pregunta
            newAnswer (str): nueva respuesta
        """
        this.answers[answerID] = newAnswer