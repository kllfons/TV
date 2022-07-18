class Televisão:
    def __init__(self):
        self.on = False
        self.canal= 5
    def power(self):
        if self.on:
            self.on= False
        else :
            self.on = True
    def aumenta_canal(self):
        if self.on:
            self. canal+= 1
    def diminui_canal(self):
        if self.on:
         self. canal -=1

televisão= Televisão()
print ('Televisão está ligada: {}' . format(televisão.on))
print('Canal:{}'. format(televisão.canal))
televisão. power()
print ('Televisão está ligada: {}' . format(televisão.on))
televisão.aumenta_canal()
televisão.aumenta_canal()
print('Canal:{}'. format(televisão.canal))
televisão.diminui_canal()
print('Canal:{}'. format(televisão.canal))