import pygame
import math
from Jeux import*
from animaux import Animal
from Bouton import bouton


pygame.init() # charger les composants dans le module pygame

#generer la fenetre 
pygame.display.set_caption("Arche de noé")#display et en rapport avec la fenetre et set_caption permet generer et de donner un titre a la fenetre et rajouter un logo")
surface = pygame.display.set_mode((1080,720))#set_permet de dimensionner le fenetre  en generant une surface 

#importer l'arriere plan du jeu  
Fond_image= pygame.image.load('/Users/nicolascastagni/Desktop/Jeu /Assets /fond mer .jpg')
#charger l'image de depuis un chemin de l'ordi  



image_regle=pygame.image.load('/Users/nicolascastagni/Desktop/Jeu /Assets /fond regle .jpg')
fond_menu=pygame.image.load('/Users/nicolascastagni/Desktop/Jeu /Assets /OIG4.oGOHcLbtLh9DQY_it3RD.jpeg')




def play_screen_starter():
    clock = pygame.time.Clock()
    #generer la fenetre 
    pygame.display.set_caption("Arche de noé")#display et en rapport avec la fenetre et set_caption permet generer et de donner un titre a la fenetre et rajouter un logo")
    surface = pygame.display.set_mode((1280,680))#set_permet de dimensionner le fenetre  en generant une surface 

    #def chemin_image(fichier):#on crée un crossplateform pour les images
        #return os.path.join("images", fichier)

    #importer l'arriere plan du jeu  
    Fond_image = pygame.image.load('/Users/nicolascastagni/Desktop/main fouc /images /image mer.jpg')
    Fond_image = pygame.transform.scale(Fond_image, (1080,680)) 


    #on crée toutes nos images d'animaux et l'arche
    elephant1 = Animal(("/Users/nicolascastagni/Desktop/main fouc /images /elephant1.png"), (116,152), 25, 10)
    elephant2 = Animal(("/Users/nicolascastagni/Desktop/main fouc /images /elephant2.png"), (116,76), 25, 170)
    girafe1 = Animal(("/Users/nicolascastagni/Desktop/main fouc /images /girafe1.png"), (116,152), 25, 260)
    girafe2 = Animal(("/Users/nicolascastagni/Desktop/main fouc /images /girafe2.png"), (58,152), 40, 425)
    hipopo1 = Animal(("/Users/nicolascastagni/Desktop/main fouc /images /hipopotame1.png"), (174,76), 10, 590)
    hipopo2 = Animal(("/Users/nicolascastagni/Desktop/main fouc /images /hipopotame2.png"), (116,76), 1105, 590)
    lion1 = Animal(("/Users/nicolascastagni/Desktop/main fouc /images /lion1.png"), (116,152), 1105, 10)
    lion2 = Animal(("/Users/nicolascastagni/Desktop/main fouc /images /lion2.png"), (116,76), 1105, 170)
    zebre1 = Animal(("/Users/nicolascastagni/Desktop/main fouc /images /zebre1.png"), (58,152), 1120, 260)
    zebre2 = Animal(("/Users/nicolascastagni/Desktop/main fouc /images /zebre2.png"), (116,76), 1105, 425)

    arche  = pygame.image.load('/Users/nicolascastagni/Desktop/main fouc /images /arche.png')
    arche_rect = arche.get_rect(midbottom = (640,570))

    ouvert = True #cette variable permet de definir pour le programme si la fenetre est en court d'éxecution

    #on crée la variable de mouvement de chaque image
    piece_to_move = None

    #on crée une liste contenant les coordonnées x des centres des rectangles de l'arche
    list_center_x = [453, 513, 573, 633, 693, 753, 813]
    #on crée une liste contenant les coordonnées y des centres des rectangles de l'arche
    list_center_y = [225, 305, 385, 465]

    #on crée une liste de tous les rectangles servant à vérifier si les cases sont déjà occupées par un animal
    """ list_test_center = [elephant1.rect1, elephant1.rect2, elephant1.rect4, elephant2.rect2, elephant2.rect4, girafe1.rect2, girafe1.rect3, girafe1.rect4, girafe2.rect1, girafe2.rect2, 
                        lion1.rect1, lion1.rect2, lion1.rect3, lion2.rect2, lion2.rect4, hipopo1.rect2, hipopo1.rect4, hipopo1.rect5, hipopo2.rect2, hipopo2.rect4,
                        zebre1.rect1, zebre1.rect2, zebre2.rect2, zebre2.rect4] """
    list_test_center = [(1,1)]

    #boucle tant que ouvert est vrai pour que le fenêtre reste ouvert 
    while ouvert:

        #appliquer l'arriere plan de notre jeu car pygame.display.set_mode((500,300))genere une surface et pygame.image.load('assets/fond.png.avif') notre fond suffit de mettre le fond sur la surface
        surface.blit(Fond_image, (150,0))#blit permet de mettre notre image sur la surface 

        clock.tick(30)

        barre_droite(surface)
        barre_gauche(surface)

        #appliquer l'arche avant les animaux puisqu'elle est en 'fond'
        surface.blit(arche, arche_rect)

        #appliquer les images d'animaux 
        surface.blit(elephant1.image, elephant1.rect)
        surface.blit(elephant2.image, elephant2.rect)
        surface.blit(girafe1.image, girafe1.rect)
        surface.blit(girafe2.image, girafe2.rect)
        surface.blit(hipopo1.image, hipopo1.rect)
        surface.blit(hipopo2.image, hipopo2.rect)
        surface.blit(lion1.image, lion1.rect)
        surface.blit(lion2.image, lion2.rect)
        surface.blit(zebre1.image, zebre1.rect)
        surface.blit(zebre2.image, zebre2.rect) 


        #mettre à jour notre écran car là c'est fixe
        pygame.display.flip()#flip() permet de mettre à jour l'écran

        pos_souris = pygame.mouse.get_pos()

        for event in pygame.event.get():           
            if event.type == pygame.QUIT:
                ouvert = False
                pygame.quit()


            elif event.type == pygame.MOUSEBUTTONDOWN and pygame.Rect.collidepoint(elephant1.rect, pos_souris):
                elephant1.rect.collidepoint(event.pos)
                piece_to_move = "ele1"
            elif event.type == pygame.MOUSEBUTTONDOWN and pygame.Rect.collidepoint(elephant2.rect, pos_souris):
                elephant2.rect.collidepoint(event.pos)
                piece_to_move = "ele2"
            elif event.type == pygame.MOUSEBUTTONDOWN and pygame.Rect.collidepoint(girafe1.rect, pos_souris):
                girafe1.rect.collidepoint(event.pos)
                piece_to_move = "gir1"
            elif event.type == pygame.MOUSEBUTTONDOWN and pygame.Rect.collidepoint(girafe2.rect, pos_souris):
                girafe2.rect.collidepoint(event.pos)
                piece_to_move = "gir2"
            elif event.type == pygame.MOUSEBUTTONDOWN and pygame.Rect.collidepoint(lion1.rect, pos_souris):
                lion1.rect.collidepoint(event.pos)
                piece_to_move = "lio1"
            elif event.type == pygame.MOUSEBUTTONDOWN and pygame.Rect.collidepoint(lion2.rect, pos_souris):
                lion2.rect.collidepoint(event.pos)
                piece_to_move = "lio2"
            elif event.type == pygame.MOUSEBUTTONDOWN and pygame.Rect.collidepoint(hipopo1.rect, pos_souris):
                hipopo1.rect.collidepoint(event.pos)
                piece_to_move = "hipo1"
            elif event.type == pygame.MOUSEBUTTONDOWN and pygame.Rect.collidepoint(hipopo2.rect, pos_souris):
                hipopo2.rect.collidepoint(event.pos)
                piece_to_move = "hipo2"
            elif event.type == pygame.MOUSEBUTTONDOWN and pygame.Rect.collidepoint(zebre1.rect, pos_souris):
                zebre1.rect.collidepoint(event.pos)
                piece_to_move = "zeb1"
            elif event.type == pygame.MOUSEBUTTONDOWN and pygame.Rect.collidepoint(zebre2.rect, pos_souris):
                zebre2.rect.collidepoint(event.pos)
                piece_to_move = "zeb2"


            elif event.type == pygame.MOUSEMOTION and piece_to_move == "ele1":
                ele1_c1 = elephant1.rect1.center
                ele1_c2 = elephant1.rect2.center
                ele1_c4 = elephant1.rect4.center
                elephant1.rect.move_ip(event.rel)
                elephant1.rect1.move_ip(event.rel)
                elephant1.rect2.move_ip(event.rel)
                elephant1.rect4.move_ip(event.rel)
            elif event.type == pygame.MOUSEMOTION and piece_to_move == "ele2":
                ele2_c2 = elephant2.rect2.center
                ele2_c4 = elephant2.rect4.center
                elephant2.rect.move_ip(event.rel)
                elephant2.rect2.move_ip(event.rel)
                elephant2.rect4.move_ip(event.rel)
            elif event.type == pygame.MOUSEMOTION and piece_to_move == "gir1":
                girafe1.rect.move_ip(event.rel)
                girafe1.rect2.move_ip(event.rel)
                girafe1.rect3.move_ip(event.rel)
                girafe1.rect4.move_ip(event.rel)
            elif event.type == pygame.MOUSEMOTION and piece_to_move == "gir2":
                girafe2.rect.move_ip(event.rel)
                girafe2.rect1.move_ip(event.rel)
                girafe2.rect2.move_ip(event.rel)
            elif event.type == pygame.MOUSEMOTION and piece_to_move == "lio1":
                lion1.rect.move_ip(event.rel)
                lion1.rect1.move_ip(event.rel)
                lion1.rect2.move_ip(event.rel)
                lion1.rect3.move_ip(event.rel)
            elif event.type == pygame.MOUSEMOTION and piece_to_move == "lio2":
                lion2.rect.move_ip(event.rel)
                lion2.rect2.move_ip(event.rel)
                lion2.rect4.move_ip(event.rel)
            elif event.type == pygame.MOUSEMOTION and piece_to_move == "hipo1":
                hipopo1.rect.move_ip(event.rel)
                hipopo1.rect2.move_ip(event.rel)
                hipopo1.rect4.move_ip(event.rel)
                hipopo1.rect5.move_ip(event.rel)
            elif event.type == pygame.MOUSEMOTION and piece_to_move == "hipo2":
                hipopo2.rect.move_ip(event.rel)
                hipopo2.rect2.move_ip(event.rel)
                hipopo2.rect4.move_ip(event.rel)
            elif event.type == pygame.MOUSEMOTION and piece_to_move == "zeb1":
                zebre1.rect.move_ip(event.rel)
                zebre1.rect1.move_ip(event.rel)
                zebre1.rect2.move_ip(event.rel)
            elif event.type == pygame.MOUSEMOTION and piece_to_move == "zeb2":
                zebre2.rect.move_ip(event.rel)
                zebre2.rect2.move_ip(event.rel)
                zebre2.rect4.move_ip(event.rel)

            elif event.type == pygame.MOUSEBUTTONUP:
                match piece_to_move:               
                    case "ele1":
                        t1, i1, j1 = elephant1.test_rect1()
                        if t1:
                            t2, i2, j2 = elephant1.test_rect2()
                            if t2:
                                t4, i4, j4 = elephant1.test_rect4()
                                if t4:
                                    elephant1.rect.centerx = i1+30
                                    elephant1.rect.centery = j1+40
                                    elephant1.rect1.center == (i1,j1)
                                    elephant1.rect2.center == (i2,j2)
                                    elephant1.rect4.center == (i4,j4)
                                    for center in list_test_center:
                                            if center == elephant1.rect1.center or center == elephant1.rect2.center or center == elephant1.rect4.center:
                                                elephant1.rect.x = 25
                                                elephant1.rect.y = 10
                                                elephant1.rect1.center = ele1_c1
                                                elephant1.rect2.center = ele1_c2
                                                elephant1.rect4.center = ele1_c4
                                                print (center)
                                            else:
                                                list_test_center.append((i1,j1))
                                                list_test_center.append((i2,j2))
                                                list_test_center.append((i4,j4))

                    case "ele2":
                        t2, i2, j2 = elephant2.test_rect2()
                        if t2:
                            t4, i4, j4 = elephant2.test_rect4()
                            if t4:
                                elephant2.rect.centerx = i2+90
                                elephant2.rect.centery = j2
                                elephant2.rect2.center == (i2,j2)
                                elephant2.rect4.center == (i4,j4)
                                for center in list_test_center:
                                    if center == elephant2.rect2.center or center == elephant2.rect4.center:
                                        elephant2.rect.x = 25
                                        elephant2.rect.y = 170
                                        elephant2.rect2.center = ele2_c2
                                        elephant2.rect4.center = ele2_c4
                                    else:
                                        list_test_center.append((i2,j2))
                                        list_test_center.append((i4,j4))

                    case "gir1":
                        t2, i2, j2 = girafe1.test_rect2()
                        list_test_center.remove(girafe1.rect2)
                        list_test_center.remove(girafe1.rect3)
                        list_test_center.remove(girafe1.rect4)
                        if t2 and pygame.Rect.collidelist(girafe1.rect2, list_test_center) == -1:
                            t3,_,_ = girafe1.test_rect3()
                            if t3 and pygame.Rect.collidelist(girafe1.rect3, list_test_center) == -1:
                                t4,_,_ = girafe1.test_rect4()
                                if t4 and pygame.Rect.collidelist(girafe1.rect4, list_test_center) == -1:                                
                                    girafe1.rect.centerx = i2+90
                                    girafe1.rect.centery = j2-40
                        else:
                            girafe1.rect.x = 360
                            girafe1.rect.y = 10
                        list_test_center.append(girafe1.rect2)
                        list_test_center.append(girafe1.rect3)
                        list_test_center.append(girafe1.rect4)

                    case "gir2":
                        t1, i1, j1 = girafe2.test_rect1()
                        list_test_center.remove(girafe2.rect1)
                        list_test_center.remove(girafe2.rect2)
                        if t1 and pygame.Rect.collidelist(girafe2.rect1, list_test_center) == -1 :
                            t2,_,_ = girafe2.test_rect2()
                            if t2 and pygame.Rect.collidelist(girafe2.rect2, list_test_center) == -1:
                                girafe2.rect.centerx = i1
                                girafe2.rect.centery = j1+40                   
                        else:
                            girafe2.rect.x = 490
                            girafe2.rect.y = 10
                        list_test_center.append(girafe2.rect1)
                        list_test_center.append(girafe2.rect2)

                    case "lio1":
                        t1, i1, j1 = lion1.test_rect1()
                        list_test_center.remove(lion1.rect1)
                        list_test_center.remove(lion1.rect2)
                        list_test_center.remove(lion1.rect3)
                        if t1 and pygame.Rect.collidelist(lion1.rect1, list_test_center) == -1:
                            t2,_,_ = lion1.test_rect2()
                            if t2 and pygame.Rect.collidelist(lion1.rect2, list_test_center) == -1:
                                t3,_,_ = lion1.test_rect3()
                                if t3 and pygame.Rect.collidelist(lion1.rect3, list_test_center) == -1:
                                    lion1.rect.centerx = i1+90
                                    lion1.rect.centery = j1+120
                        else:
                            lion1.rect.x = 880
                            lion1.rect.y = 10
                        list_test_center.append(lion1.rect1)
                        list_test_center.append(lion1.rect2)
                        list_test_center.append(lion1.rect3)

                    case "lio2":
                        t2, i2, j2 = lion2.test_rect2()
                        list_test_center.remove(lion2.rect2)
                        list_test_center.remove(lion2.rect4)
                        if t2 and pygame.Rect.collidelist(lion2.rect2, list_test_center) == -1:
                            t4,_,_ = lion2.test_rect4()
                            if t4 and pygame.Rect.collidelist(lion2.rect4, list_test_center) == -1:
                                lion2.rect.centerx = i2+90
                                lion2.rect.centery = j2
                        else:
                            lion2.rect.x = 1010
                            lion2.rect.y = 10
                        list_test_center.append(lion2.rect2)
                        list_test_center.append(lion2.rect4)

                    case "hipo1":
                        t2, i2, j2 = hipopo1.test_rect2()
                        if t2:
                            t4,_,_ = hipopo1.test_rect4()
                            if t4:
                                t5,_,_ = hipopo1.test_rect5()
                                if t5:
                                    del list_test_center[0]
                                    del list_test_center[0]
                                    del list_test_center[0]
                                    hipopo1.rect.centerx = i2+60
                                    hipopo1.rect.centery = j2
                                    if hipopo1.rect2.collidelist(list_test_center) == -1 and hipopo1.rect4.collidelist(list_test_center) == -1 and hipopo1.rect5.collidelist(list_test_center) == -1:
                                        pass
                                    else:
                                        hipopo1.rect.x = 620
                                        hipopo1.rect.y = 10
                                    list_test_center.append(hipopo1.rect2)
                                    list_test_center.append(hipopo1.rect4)
                                    list_test_center.append(hipopo1.rect5)
                    case "hipo2":
                        t2, i2, j2 = hipopo2.test_rect2()
                        if t2:
                            t4,_,_ = hipopo2.test_rect4()
                            if t4:
                                del list_test_center[0]
                                del list_test_center[0]
                                hipopo2.rect.centerx = i2+90
                                hipopo2.rect.centery = j2
                                if hipopo2.rect2.collidelist(list_test_center) == -1 and hipopo2.rect4.collidelist(list_test_center) == -1:
                                    pass
                                else:
                                    hipopo2.rect.x = 750
                                    hipopo2.rect.y = 10
                                list_test_center.append(hipopo2.rect2)
                                list_test_center.append(hipopo2.rect4)
                    case "zeb1":
                        t1, i1, j1 = zebre1.test_rect1()
                        if t1:
                            t2,_,_ = zebre1.test_rect2()
                            if t2:
                                del list_test_center[0]
                                del list_test_center[0]
                                zebre1.rect.centerx = i1
                                zebre1.rect.centery = j1+120
                                if zebre1.rect1.collidelist(list_test_center) == -1 and zebre1.rect2.collidelist(list_test_center) == -1:
                                    pass
                                else:
                                    zebre1.rect.x = 460
                                    zebre1.rect.y = 230
                                list_test_center.append(zebre1.rect1)
                                list_test_center.append(zebre1.rect2)
                    case "zeb2":
                        t2, i2, j2 = zebre2.test_rect2()
                        if t2:
                            t4,_,_ = zebre2.test_rect4()
                            if t4:
                                del list_test_center[0]
                                del list_test_center[0]
                                zebre2.rect.centerx = i2+90
                                zebre2.rect.centery = j2
                                if zebre2.rect2.collidelist(list_test_center) == -1 and zebre2.rect4.collidelist(list_test_center) == -1:
                                    pass
                                else:
                                    zebre2.rect.x = 590
                                    zebre2.rect.y = 230
                                list_test_center.append(zebre2.rect2)
                                list_test_center.append(zebre2.rect4)
                piece_to_move = None


        surface.fill((100,100,100))
        #surface.blit(elephant1.image,elephant1.rect)

def niveau():
    ouvert=True 
    while ouvert:
        surface.blit(fond_menu, (0,0))
        
        
        
        bouton_retour =bouton(math.ceil(surface.get_width()/1.3),math.ceil(surface.get_height()/1.2),"RETOUR",(255,255,255),(10,10,10),27,math.ceil(surface.get_width()/1.27),math.ceil(surface.get_height()/1.121))
        niv1= bouton(math.ceil(surface.get_width()/2.5),math.ceil(surface.get_height()/4.5),"STARTER 1-12",(255,255,255),(10,10,10),13,math.ceil(surface.get_width()/2.38),math.ceil(surface.get_height()/3.4))
        niv2= bouton(math.ceil(surface.get_width()/2.5),math.ceil(surface.get_height()/2.5),"MEDIUM 13-24",(255,255,255),(10,10,10),13,math.ceil(surface.get_width()/2.38),math.ceil(surface.get_height()/2.09))
        niv3= bouton(math.ceil(surface.get_width()/2.5),math.ceil(surface.get_height()/1.75),"HARD 25-36",(255,255,255),(10,10,10),13,math.ceil(surface.get_width()/2.31),math.ceil(surface.get_height()/1.54))
        niv4= bouton(math.ceil(surface.get_width()/2.5),math.ceil(surface.get_height()/1.35),"EXTREME 37-48",(255,255,255),(10,10,10),13,math.ceil(surface.get_width()/2.40),math.ceil(surface.get_height()/1.2255))
        for boutton in [bouton_retour,niv1,niv2,niv3,niv4]:
            
            boutton.update(surface)
            boutton.changement_couleur(surface)
        
        pygame.display.flip()
        
        for event in pygame.event.get():
          
            if event.type==pygame.QUIT:
                Ouvert=False 
                pygame.quit()
            elif event.type==pygame.MOUSEBUTTONDOWN:
                if bouton_retour.bouton_rect.collidepoint(event.pos):
                    menu()
                if niv1.bouton_rect.collidepoint(event.pos):
                    play_screen_starter()
                        
                
            
def regle():
    Ouvert=True
    panneau_regle=pygame.image.load('/Users/nicolascastagni/Desktop/Jeu /Assets /regle2.png')
    panneau_regle=pygame.transform.scale(panneau_regle,(970,629))
    #generer la fenetre 
    pygame.display.set_caption("Règle")#display et en rapport avec la fenetre et set_caption permet generer et de donner un titre a la fenetre et rajouter un logo")
    while Ouvert:
        surface.blit(image_regle, (0,0))
        surface.blit(panneau_regle,(50,160))
        
        
        bouton_retour =bouton(math.ceil(surface.get_width()/1.3),math.ceil(surface.get_height()/1.2),"RETOUR",(255,255,255),(10,10,10),27,math.ceil(surface.get_width()/1.27),math.ceil(surface.get_height()/1.121))
        for boutton in [bouton_retour]:
            boutton.update(surface)
            boutton.changement_couleur(surface)
            
            
        
        #mettre jour notre ecrans écrans car la c'est fixe
        pygame.display.flip()#flip permet de mettre a jour l'ecrans 
        
        #si le joueur ferme cette fenetre 
        for event in pygame.event.get():#get est une liste d'évenement 
            #l'evenement fermeture de fenetre
            if event.type==pygame.QUIT:
                Ouvert=False  # si le joueur quitte la varriable devient false 
                pygame.quit()
            elif event.type==pygame.MOUSEBUTTONDOWN:
                if bouton_retour.bouton_rect.collidepoint(event.pos):
                    menu()
def menu():
    Ouvert=True
    #generer la fenetre 
    pygame.display.set_caption("Menu")#display et en rapport avec la fenetre et set_caption permet generer et de donner un titre a la fenetre et rajouter un logo")
    
    # importer image du bouton
    play_boutton= pygame.image.load('/Users/nicolascastagni/Desktop/Jeu /Assets /test4.png')
    play_boutton=pygame.transform.scale(play_boutton,(200,115))
    
    regle_bouton=pygame.image.load('/Users/nicolascastagni/Desktop/Jeu /Assets /test4.png')
    regle_bouton=pygame.transform.scale(regle_bouton,(200,115))
    #bouton jouer 
    play_boutton_rect = play_boutton.get_rect()
    play_boutton_rect.x=math.ceil(surface.get_width()/2.5)
    play_boutton_rect.y=math.ceil(surface.get_height()/4.5 )
    
    #bouton règle 
    regle_boutton_rect = regle_bouton.get_rect()
    regle_boutton_rect.x=math.ceil(surface.get_width()/2.5)
    regle_boutton_rect.y=math.ceil(surface.get_height()/1.2)
    
    
    #importer police d'écriture 
    police_ecriture_play_bouton=pygame.font.Font('/Users/nicolascastagni/Desktop/Jeu /Assets /font.ttf',33)#creer la police d'écriture et la taille 
   
    police_ecriture_regle_bouton=pygame.font.Font('/Users/nicolascastagni/Desktop/Jeu /Assets /font.ttf',24)#creer la police d'écriture et la taille 
   
   #écriture de jouer 
    text_jouer_bouton=police_ecriture_play_bouton.render("JOUER",True,(255, 255, 255))#creer le texte qu'on veut 
    text_jouer_bouton_rect= text_jouer_bouton.get_rect()
    text_jouer_bouton_rect.x=math.ceil(surface.get_width()/2.4)
    text_jouer_bouton_rect.y=math.ceil(surface.get_height()/3.5 )
   
    # écriture de regle 
    text_regle_bouton= police_ecriture_regle_bouton.render("REGLE",True,(255,255,255))
    text_regle_bouton_rect=text_regle_bouton.get_rect()
    text_regle_bouton_rect.x= math.ceil(surface.get_width()/2.4)
    text_regle_bouton_rect.y=math.ceil(surface.get_height()/1.112)
    
    while Ouvert:
        surface.blit(fond_menu, (0,0))
        
        surface.blit(play_boutton,play_boutton_rect)
        surface.blit(text_jouer_bouton,text_jouer_bouton_rect)
        
        
        surface.blit(regle_bouton,regle_boutton_rect)
        surface.blit(text_regle_bouton,text_regle_bouton_rect)
        
       
        
        if regle_boutton_rect.collidepoint(pygame.mouse.get_pos()):
            text_regle_bouton= police_ecriture_regle_bouton.render("QUITTER",True,(10,10,10))
        else:
            text_regle_bouton=police_ecriture_regle_bouton.render("QUITTER",True,(255,255,255))
            
        
        if play_boutton_rect.collidepoint(pygame.mouse.get_pos()):
            text_jouer_bouton=police_ecriture_play_bouton.render("JOUER",True,(10,10,10))
        else:
            text_jouer_bouton=police_ecriture_play_bouton.render("JOUER",True,(255, 255, 255))#creer le texte qu'on veut
            
             
        bouton_regle=bouton(math.ceil(surface.get_width()/2.5),math.ceil(surface.get_height()/1.6),"REGLE",(255,255,255),(10,10,10),26,math.ceil(surface.get_width()/2.3),math.ceil(surface.get_height()/1.45))
        
        for boutton in [bouton_regle]:
            boutton.update(surface)
            boutton.changement_couleur(surface)
            
        
        #mettre jour notre ecrans écrans car la c'est fixe
        pygame.display.flip()#flip permet de mettre a jour l'ecrans 
        

        
        
        #si le joueur ferme cette fenetre 
        for event in pygame.event.get():#get est une liste d'évenement 
            #l'evenement fermeture de fenetre
            if event.type==pygame.QUIT:
                Ouvert=False  # si le joueur quitte la varriable devient false 
                pygame.quit()
            elif event.type==pygame.MOUSEBUTTONDOWN and play_boutton_rect.collidepoint(event.pos):
                    niveau()
            elif event.type==pygame.MOUSEBUTTONDOWN and regle_boutton_rect.collidepoint(event.pos):
                pygame.quit()
            elif event.type==pygame.MOUSEBUTTONDOWN and bouton_regle.bouton_rect.collidepoint(event.pos):
                regle()
                
        
        
menu()
