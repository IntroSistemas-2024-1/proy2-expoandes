#################################################################
# User (class) - Proy2 Expoandes: IntroISIS 2024-10
#################################################################


#################################################################
# imports

import AnswerLog

#################################################################
# class definition

class User:
    
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

    def newQuestionSet( this, questions ):
        """Agrega un nuevo set de preguntas al usuario

        Args:
            this (User): this object
            questionsU (dict): preguntas -> { int: str } = { 1:'q1', 2:'q2', ... , n:'qn' }
        """
        this.answerLog.newQuestionSet( questions )
        
    def newAnswerSet( this, answers ):
        """Agrega un nuevo set de respuestas al usuario

        Args:
            this (User): this object
            answersU (dict): respuestas -> { int: str } = { 1:'a1', 2:'a2', ... , n:'an' }
        """
        this.answerLog.newAnswerSet( answers )
        
    def updateAnswer( this, answerID, newAnswer ):
        """Actualiza la respuesta de un usuario a una pregunta específica.
        Si la pregunta no existe, no hace nada.

        Args:
            this (User): this object
            answerID (int): numero de la pregunta
            newAnswer (str): nueva respuesta
        """
        answerSet = this.answerLog.answers
        
        if answerID in answerSet:
            this.answerLog.updateAnswer( answeID, newAnswer )
            
        