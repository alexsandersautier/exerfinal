def validate_email(func):
    def wrapper():
        print("coisa")
        func()
        print("depois")
    return wrapper

class Contact:
    
    def __init__(self, name, phone, email):
        self._name = name
        self._phone = phone
        self._email = email
    
    def __str__(self):
        return self._name
     
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("O nome precisa conter apenas letras")
        self._name = value
    
    @property
    def phone(self):
        return self._phone
    
    @phone.setter
    def phone(self, value):
        if len(value) > 11:
            raise ValueError("O número de telefone não pode conter mais que 11 dígitos")
        self._phone = value
    
    @property
    def email(self):
        return self._email
    
    # @validate_email
    @email.setter
    def email(self, value):
        self._email = value