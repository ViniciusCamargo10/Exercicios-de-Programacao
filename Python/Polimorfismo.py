class Passaro:
    def voar(self):
        pass
    
class Pardal(Passaro):
    def voar(self):
        print("Pardal voa")
        
class Avestruz(Passaro):
    def voar(self):
        print("Nao voa")
        
def planoDeVoo(passaro):
    passaro.voar()
    
planoDeVoo(Pardal())
planoDeVoo(Avestruz())