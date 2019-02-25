class Pet():
    
    allowed = ['Cat','Dog','Fish','Rat']

    def __init__(self,name,species):
        if species not in Pet.allowed:  
            raise ValueError(f'You cannot have a {species} pet')

        self.name = name
        self.species = species

    def set_species(self,species):
        if species not in Pet.allowed:
            raise ValueError(f'You cannot have a {species} pet')

        self.species = species

cat = Pet('Blue','Cat')
dog = Pet('Wyatt','Dog')
