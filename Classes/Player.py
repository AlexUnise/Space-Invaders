from PIL import Image,ImageTk
import os

class Player:
    #Classe Joueur
    #Un joueur peut se déplacer uniquement sur l'axe x. Le programmeur définit sa coordonnée y. 
    #dx réprésente la vitesse de déplacement sur l'axe, définie par le programmeur.
    #La fonction draw déssine pour la première fois le player sur le canvas
    #Les fonctions moveRight et moveLeft permettent de déplacer le joueur sur le canvas.
    
    def __init__(self,x,y,dx,width,height,life_counter,canvas,wind):
        self.__name=""
        self.lives = 3
        self.score = 0
        self.__positionx = x
        self.__positiony = y
        self.dx = dx
        self.width = width
        self.height = height
        self.__canvas=canvas
        self.__wind=wind
        self.__file=[]
        self.__life_counter = life_counter
        
        
    def place_player(self):
        scriptDir = os.path.dirname(__file__)
        imgpath = os.path.join(scriptDir, '../Assets/space_invaders_player.png')
        img= Image.open(imgpath)
        self.__canvas_img = ImageTk.PhotoImage(img)
        self.rect=self.__canvas.create_image(self.__positionx,self.__positiony, image=self.__canvas_img)  

    
    def moveLeft(self,canvas):
        canvas.move(self.rect,-self.dx, 0)
    def moveRight(self,canvas):
        canvas.move(self.rect,self.dx, 0)


    def player_hit(self):
        self.lives-=1
        self.__life_counter.set('Lives: ' + str(self.lives) )

        if self.lives==0:
            #On efface tout dans le canvas
            self.__canvas.delete('all')
            #Affichage du titre gameover 
            self.__canvas.create_text(int(int(self.__canvas.cget('width'))/2),int(int(self.__canvas.cget('height'))/2), text='Vous avez perdu !', fill="#fff", font=('Helvetica','30','bold'))
            #On désactive l'écoute des évenements clavier 
            self.__canvas.unbind('<Key>', self.__keyboard_event_id)
            # #On désactive l'exécution de la fonction alien_fire 
            # self.__canvas.after_cancel(self.__alienFireAfter)
    
    def set_keyboard_id(self,id):
        self.__keyboard_event_id = id

    # def set_alienFireAfter(self, id):
    #     self.__alienFireAfter = id