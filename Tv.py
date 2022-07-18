class Tv:
    def __init__(self):
        self.on = False
        self.channel= 5
    def power(self):
        if self.on:
            self.on= False
        else :
            self.on = True
    def increase_channel(self):
        if self.on:
            self. channel+= 1
    def decrease_channel(self):
        if self.on:
         self. channel -=1

tv= Tv()
print ('Tv is on: {}' . format(tv.on))
print('channel:{}'. format(tv.channel))
tv. power()
print ('Tv is on: {}' . format(tv.on))
tv.increase_channel()
tv.increase_channel()
print('channel:{}'. format(tv.channel))
tv.decrease_channel()
print('channel:{}'. format(tv.channel))
