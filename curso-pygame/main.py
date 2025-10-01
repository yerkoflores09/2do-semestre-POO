import pygame as pg

#se inicializa pygame
pg.init()

#color de fondo (variable)
background = (0,0,0) #negro
yellow = (255,255,0) #amarillo
light_blue = (0,76,255) #azul
light_green = (7,255,0) #verdecito
light_red = (255,0,0) #rojito

#seteo de la ventana 
window = pg.display.set_mode((800, 600))
pg.display.set_caption('conceptos basicos') #titulo de la ventana

running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    window.fill(background)

    #dibujando figuras
    pg.draw.circle(window, yellow, (400,300), 50)
    pg.draw.rect(window, light_blue, (150, 400, 150, 50))
    pg.draw.line(window, light_green, (100,383), (700,100), 5)
    
    #vertices de triangulos
    vertices = [(400,110), (350,200), (450,200)]
    pg.draw.polygon(window, light_red, vertices)

    pg.display.update()

pg.quit()