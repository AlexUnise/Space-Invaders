#Classe qui gere les projectiles des ennemis et du joueur
class Projectile:
    def __init__(self,canvas,wind,entity,backImg,blockAlien,shooter,player,specialAlien):
        self.__height=10
        self.__width=4
        self.__dy=20
        self.__canvas=canvas
        self.__wind=wind
        self.__entity=entity
        self.__backImg=backImg
        self.__blockAlien=blockAlien
        self.__player=player
        self.__origin=shooter
        self.__specialAlien=specialAlien
    #Methode qui permet de placer un projectiler devant l'alien ou le joueur
    def place_projectile(self):
        (x0,y0)=self.__canvas.coords(self.__entity.rect)
        if self.__origin=="player":
            color="yellow"
            signe=-1
        elif self.__origin=="alien":
            color="red"
            signe=1
        self.projectile=self.__canvas.create_rectangle(x0,y0+signe*(self.__entity.height+2),x0+self.__width,y0+signe*(self.__entity.height+2+self.__height),fill=color)
        
    #Methode qui fait bouger verticalement le projectile, et qui gere les collisions entre le projectile et les differents objets du canvas
    def fire_projectile(self):
        if self.projectile in self.__canvas.find_all():
            (x_proj0,y_proj0,x_proj1,y_proj1)=self.__canvas.coords(self.projectile)
            liste_objet=self.__canvas.find_overlapping(x_proj0,y_proj0,x_proj1,y_proj1)
            
            if len(liste_objet)>2:
                
                for objet in liste_objet:
                    if objet!=self.__backImg and objet!=self.projectile and self.__origin=="player":
                        if objet==self.__specialAlien.rect:
                            self.__canvas.delete(self.projectile)
                            self.__canvas.delete(objet)
                            self.__player.score+=self.__specialAlien.bonusScore
                            self.__blockAlien.score_counter.set('Score: ' + str(self.__player.score))
                        else:
                            self.__blockAlien.add_aliens_hit(objet)
                            self.__canvas.delete(self.projectile)

                    elif objet!=self.__backImg and objet!=self.projectile and self.__origin=="alien":
                        
                        if objet==self.__player.rect:
                            self.__player.player_hit()
                            self.__canvas.delete(self.projectile)   
                        else:
                            if y_proj1>int(self.__canvas.cget('height'))-250:
                                self.__canvas.delete(self.projectile)  
                                self.__canvas.delete(objet)
        


            if y_proj0<0 or y_proj1>int(self.__canvas.cget('height')):
                self.__canvas.delete(self.projectile)



            else:
                if self.__origin=="player":
                    self.__canvas.move(self.projectile,0,-self.__dy)
                elif self.__origin=="alien":
                    self.__canvas.move(self.projectile,0,self.__dy) 
                self.__wind.after(20,self.fire_projectile)