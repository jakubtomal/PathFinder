from termcolor import colored

class labirynt():
    def __init__(self,nazwa):
        self.nazwa=nazwa
        self.mapa=[]
        self.start=[1,1]
        self.meta=[1,1]
        self.kgora=[self.start[0]-1,self.start[1]]
        self.kdol=[self.start[0]+1,self.start[1]]
        self.kprawo=[self.start[0],self.start[1]+1]
        self.klewo=[self.start[0],self.start[1]-1]
        self.gora=None
        self.dol=None
        self.prawo=None
        self.lewo=None

    def stworz(self):
        self.start=[]
        self.meta=[]
        plik=open(self.nazwa,'r')
        c=0
        w=''
        h=''
        tmp=[]

        for i in plik.readline():

            if i == '\n':
                break;

            if i == ' ':
                c=1

            if c == 0:
                h+=i

            if c == 1:
                w+=i
            if i == ' ':
                c=1

        for i in range(0,int(float(h))):
            linia=plik.readline()
            for k in range(0,int(float(w))):
                tmp.append(linia[k]);
            self.mapa.append(tmp)
            tmp=[]

        plik.close()

        w=0
        h=0

        for i in self.mapa:
            for k in i:
                if k == '$':
                    self.meta.append(h)
                    self.meta.append(w)

                if k == '@':
                    self.start.append(h)
                    self.start.append(w)


                w+=1
            h+=1
            w=0

    def Gora(self):
        self.mapa[self.start[0]][self.start[1]]=colored('.','red')
        self.start=[self.start[0]-1,self.start[1]]
        self.kierunki()

    def Dol(self):
        self.mapa[self.start[0]][self.start[1]]=colored('.','red')
        self.start=[self.start[0]+1,self.start[1]]
        self.kierunki()

    def Lewo(self):
        self.mapa[self.start[0]][self.start[1]]=colored('.','red')
        self.start=[self.start[0],self.start[1]-1]
        self.kierunki()

    def Prawo(self):
        self.mapa[self.start[0]][self.start[1]]=colored('.','red')
        self.start=[self.start[0],self.start[1]+1]
        self.kierunki()

    def kierunki(self):
        self.gora=self.mapa[self.start[0]-1][self.start[1]]
        self.dol=self.mapa[self.start[0]+1][self.start[1]]
        self.lewo=self.mapa[self.start[0]][self.start[1]-1]
        self.prawo=self.mapa[self.start[0]][self.start[1]+1]

    def koordy(self):
        self.kgora=[self.start[0]-1,self.start[1]]
        self.kdol=[self.start[0]+1,self.start[1]]
        self.kprawo=[self.start[0],self.start[1]+1]
        self.klewo=[self.start[0],self.start[1]-1]

    def Start(self):
        return self.mapa[self.start[0]][self.start[1]]


    def graf(self):
        tmp = self.start
        self.koordy()
        kolejka=[]
        kolejka.append(self.start)
        i=1
        self.mapa[self.start[0]][self.start[1]]=i


        while kolejka:

            self.start=kolejka[0]
            kolejka=kolejka[1:]
            self.koordy()
            self.kierunki()
            i=int( self.mapa[self.start[0]][self.start[1]] )

            if self.gora == ' ' or self.gora == "$":
                kolejka.append(self.kgora)
                self.mapa[self.start[0]-1][self.start[1]] = i + 1

            if self.dol == ' ' or self.dol == '$':
                kolejka.append(self.kdol)
                self.mapa[self.start[0]+1][self.start[1]] = i + 1

            if self.prawo == ' ' or self.prawo == '$':
                kolejka.append(self.kprawo)
                self.mapa[self.start[0]][self.start[1]+1] = i + 1

            if self.lewo == ' ' or self.lewo == '$':
                kolejka.append(self.klewo)
                self.mapa[self.start[0]][self.start[1]-1] = i + 1

        self.start = tmp

    def znajdz(self):

        tmp = self.start
        self.mapa[self.start[0]][self.start[1]] = '@'
        self.start = self.meta
        self.kierunki()

        while self.Start() != 2:

            if self.lewo == self.Start()-1:
                self.Lewo()

            elif self.dol == self.Start()-1:
                self.Dol()

            elif self.gora == self.Start()-1:
                self.Gora()

            elif self.prawo == self.Start()-1:
                self.Prawo()


        self.mapa[self.start[0]][self.start[1]] = colored('.','red')
        self.mapa[self.meta[0]][self.meta[1]] = '$'
        self.start = tmp

        for i in range(0,len(self.mapa)):
            for k in range(0,len(self.mapa[1])):
                if self.mapa[i][k] != '#' and self.mapa[i][k] != colored('.','red') and self.mapa[i][k] != '$' and self.mapa[i][k] != '@':
                    self.mapa[i][k] = ' '

    def drukuj(self):
        d=''
        for i in a.mapa:
            for k in i:
                d=d+str(k)
            print(d)
            d=''

    def drukuj2(self):
        d=''
        for i in a.mapa:
            for k in i:
                if len(str(k))<2:
                    d=d+str(k)+'  '
                else:
                    d=d+str(k)+' '
            print(d+'\n')
            d=''


a=labirynt('labirynt0.txt')
a.stworz()
a.drukuj()
a.graf()
a.drukuj2()
a.znajdz()
a.drukuj()
