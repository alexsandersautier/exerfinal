from Contact import Contact

class Schedule:
    
    def __init__(self):
        with open("data/contacts.txt", "w", encoding="utf-8") as file:
            file.write("Lista de contatos")
    
    def add_contact(self, name, phone, email):
        contact = Contact(name,phone,email)
        with open("data/contacts.txt", "a", encoding="utf-8") as file:
            file.write(f"\nNome: {contact.name}, Telefone: {contact.phone}, E-mail: {contact.email}")
    
    def list_contacts(self):
        with open("data/contacts.txt", "r", encoding="utf-8") as file:
            for row in file:
                print(row)
    
    def remove_contacts(self):
        with open("data/contacts.txt", "w", encoding="utf-8") as file:
            file.write("")