#Создай собственный Шутер!
from pygame import *
window = display.set_mode((1080,720))
display.set_caption('Pin Pong')
clock = time.Clock()
font.init()
font = font.Font(None,20)
background = transform.scale(image.load('sty.jpg'),(1080,720))
class rabotyagi(sprite.Sprite):
    def __init__(self,rabotyaga_image,rabotyaga_x,rabotyaga_y,size_x,size_y,rabotyaga_step):
        super().__init__()
        self.image = transform.scale(image.load(rabotyaga_image),(size_x,size_y))
        self.rect = self.image.get_rect()
        self.rect.x = rabotyaga_x
        self.rect.y = rabotyaga_y
        
        self.step = rabotyaga_step
    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))
class papanya(rabotyagi):
    def control(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_d] and self.rect.y < 720:
            self.rect.y += 10 
        if keys_pressed[K_a] and self.rect.y > 0:
            self.rect.y -= 10
    def control2(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y < 720:
            self.rect.y += 10 
        if keys_pressed[K_s] and self.rect.y > 0:
            self.rect.y -= 10



game = True
finis = False
clock = time.Clock()
pl1 = papanya('artas.jpg',20,300,10,100,15)
pl2 = papanya('artas.jpg',970,300,10,100,15)
ball = papanya('nats.jpg',500,300,40,50,0)
lose_1 = font.render('dayn',True,(255,255,255))
lose_2 = font.render('debil',True,(255,255,255))
ball_speed_x = 6
ball_speed_y = 6
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False  

    if finis == False:
        window.blit(background,(0,0))
        pl1.reset()
        pl2.reset()
        ball.reset()
        pl1.control()
        pl2.control2()
        ball.rect.x -= ball_speed_x
        ball.rect.y += ball_speed_y
        if ball.rect.y < 0 or ball.rect.y > 720:
            ball_speed_y *= -1
        if ball.rect.x < 0:
            finis = True
            background.blit(lose_1,(400,300))
        if ball.rect.x > 1080:
            finis = True
            background.blit(lose_2,(400,300))
        if sprite.collide_rect(pl1,ball) or sprite.collide_rect(pl2,ball):
            ball_speed_y *= 1
            ball_speed_x *= -1
        display.update() 
    clock.tick(60)