#################################################################
# Profesor (class extends User) - Proy2 Expoandes: IntroISIS 2024-10
#################################################################

from src import config as cf

#################################################################
# imports

from src.objects.user import User
from src.objects.answerLog import AnswerLog

assert cf

#################################################################
# class definition

class Profesor(User):
    
    def __init__( self, usernameU, passwordU ):
        
        super().__init__( usernameU, passwordU )
        
    def designAnswerLog():
        pass
        