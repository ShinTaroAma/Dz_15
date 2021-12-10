import random
class Oxygen (object):
    freez = 0
    steem = 100
    hot = 30
    def agg_state(self, t):
        temp = ""
        if t == self.freez or t < self.freez :
            temp += "Ice"
        elif t == self.steem or t > self.steem :
            temp += "Пара"
        elif t == self.hot :
            temp += "Жарко"
        kalvin = float(t)-273.16
        far = (float(t)-32)*(5/9)
        return temp, kalvin, far
a = Oxygen()
print(a.agg_state(30))
class Element (Oxygen):
    pass

    
b = Oxygen()
print(b.agg_state(30))
a = 10
