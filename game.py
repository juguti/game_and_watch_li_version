import pyxel


class App:
    def __init__(self):
        pyxel.init(128,128)
        pyxel.load("my_resource.pyxres")
        self.player = Player()
        self.mobs = [Mob(pyxel.rndi(0,5))]
        self.supprimer_tours_apres = []
        self.scorre = 0
        self.vie = 3
        self.menu = True
        pyxel.run(self.update,self.draw)

    def update(self):
        self.event()
        if not self.menu:

            if self.vie <= 0:
                self.menu = True



            self.player.u = 0
            # ajouter un nouveau mobs
            b = 70-self.scorre//40 if 70-self.scorre//40 > 30 else 30
            if pyxel.rndi(0,80-self.scorre//100) == 1:
                self.mobs.append(Mob(pyxel.rndi(0, 5)))
            elif len(self.mobs) == 0:
                self.mobs.append(Mob(pyxel.rndi(0, 5)))



            a_sup = []
            a_sup2 = []


            i= 0
            for mob in self.mobs:
                mob.update()
                if mob.arrive:
                    if mob.numero == self.player.numero or mob.numero == self.player.numero+1:
                        if i not in self.supprimer_tours_apres:
                            mob.u = 16
                            a_sup.append(i)
                            self.scorre += 10
                    else:
                        if i not in self.supprimer_tours_apres:
                            if mob.frame + 30 < pyxel.frame_count:
                                self.vie -= 1
                                a_sup2.append(i)

                i+=1
            for i in self.supprimer_tours_apres[::-1]:
                self.player.u = 16
                self.mobs.pop(i)
            for i in a_sup2[::-1]:self.mobs.pop(i)

            self.supprimer_tours_apres = a_sup.copy()
    def event(self):
        if not self.menu:
            if pyxel.btnp(pyxel.KEY_LEFT) or pyxel.btnp(pyxel.GAMEPAD1_BUTTON_DPAD_LEFT):
                self.player.move(-1)
            if pyxel.btnp(pyxel.KEY_RIGHT) or pyxel.btnp(pyxel.GAMEPAD1_BUTTON_DPAD_RIGHT):
                self.player.move(1)
        else:
            if pyxel.btnp(pyxel.KEY_SPACE) or pyxel.btnp(pyxel.GAMEPAD1_BUTTON_Y)or pyxel.btnp(pyxel.GAMEPAD1_BUTTON_X) or pyxel.btnp(pyxel.GAMEPAD1_BUTTON_A) or pyxel.btnp(pyxel.GAMEPAD1_BUTTON_B):
                self.menu = False
                self.scorre = 0
                self.vie = 3
    def draw(self):
        if not  self.menu:
            pyxel.bltm(0,0,0,0,0,128,128)
            pyxel.text(4,4,str(self.scorre),0)
            pyxel.text(100, 4, "Vie: "+str(self.vie), 0)
            self.player.draw()
            for mob in self.mobs:
                mob.draw()
        else:
            pyxel.cls(6)
            pyxel.text(50,60,"Press Space",0)


class Player:
    def __init__(self):
        self.u = 0
        self.v = 0
        self.size = 16
        self.x = (pyxel.width-8)//5*2 + 8
        self.y = 32
        self.speed = (pyxel.width-8)//5
        self.numero = 2

    def draw(self):
        pyxel.blt(self.x,self.y,0,self.u,self.v,self.size,self.size,colkey=0)

    def move(self,dir):
        if 0 < self.x + self.speed*dir < 120:
            self.x += self.speed * dir
            self.numero += 1 * dir
            print(self.numero)

class Mob:
    def __init__(self,n):
        self.x = (pyxel.width-8)//5 * n
        self.y = pyxel.height
        self.numero = n
        self.speed = pyxel.rndi(75,150)/100
        self.u = 0
        self.v = 16
        self.size = 8
        self.arrive = False

    def update(self):
        if self.y > 46:
            self.y -= self.speed
        elif not self.arrive:
            self.u = 8
            self.arrive = True
            self.frame = pyxel.frame_count


    def draw(self):
        pyxel.blt(self.x,self.y,0,self.u,self.v,self.size,self.size,colkey=0)

App()
