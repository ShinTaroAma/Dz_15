from abc import ABC, abstractmethod


class Oxygen (ABC):
    freez = 0
    steem = 100
    hot = 30

    @abstractmethod
    def agg_state(self, t):
        pass


class Element (Oxygen):
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

    
b = Element()
print(b.agg_state(30))
