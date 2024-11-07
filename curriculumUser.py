from dataclasses import dataclass
from enum import Enum, auto

#Temp
class Roles(Enum):
    TEACHER = auto()
    ADMIN = auto()


@dataclass
class CurriculumUser:
    username: str
    password: str # Will be encrypted
    accessLevel: Roles

    @staticmethod
    def updateDatabase(function):
        # Encrypt and Update database here
        def executedFunction(*args, **kwargs):
            function(*args, **kwargs) # Calls changePassword
            print(f"Database Updated, new password: {args[-1]}")
        return executedFunction

    @updateDatabase
    def changePassword(self, newPassword):
        self.password = newPassword

teacher = CurriculumUser("Testteacher", "1234", Roles.TEACHER)
teacher.changePassword("Newpassword123")
print(teacher.password)