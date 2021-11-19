class Amigo:
    def __init__(self, nome):
        self.nome = nome
        self.acordar = False
        self.esc_dentes = False
        self.cafe = False
        self.tomei_cafe = False
        self.atv_fisicas = False
        self.banho = False
        self.trabalhar = False
        self.almocar = False
        self.almocei = False
        self.tabalhei = False
        self.voltar_casa = False
        self.ver_TV = False
        self.dormir = False

    def Acordar(self):
        self.acordar = True
        print(f'{self.nome} - Bom dia, Obrigado por me acordar, tive uma ótima noite de sono. ')
        return

    def Dentes(self):
        if self.acordar:
            print(f"{self.nome} - Está bem, Estou indo escovar os dentes.")
            return
        else:
            print(f"{self.nome} - Zzzzzzz  Zzzzzzz Zzzzzzz")
            return