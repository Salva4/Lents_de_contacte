import pygame, time, sys
import datetime as dt

t0 = time.time()

pygame.init()

AMPLADA_FINESTRA, ALÇADA_FINESTRA = 640, 480
AMPLADA_IMATGE, ALÇADA_IMATGE = 300, 300
POSICIO_IMATGE = (AMPLADA_FINESTRA - AMPLADA_IMATGE)*.5, (ALÇADA_FINESTRA - ALÇADA_IMATGE)*.7

screen = pygame.display.set_mode((640,480))
screen.fill((255,255,255))

adreça_registre = "resources/registre.txt"
f = open(adreça_registre, 'r')
t = f.read()
f.close()
l = t.split()
n = int(l[0])
data = [int(i) for i in l[1].split(',')]
ultim_dia = dt.date(data[2], data[1], data[0])

avui = dt.date.today()

# TEXT
pygame.font.init()
myfont = pygame.font.SysFont('Comic Sans MS', 27)
mesos_romans = dict(zip(list(range(1, 13)), ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X', 'XI', 'XII']))


def modifica_registre():
	f = open(adreça_registre, 'w')
	f.write(str(n+1) + ' ' + ','.join([str(avui.day), str(avui.month), str(avui.year)]))
	f.close()
	ultim_dia = dt.date(avui.year, avui.month, avui.day)
	return n+1, ultim_dia

while 1:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		if event.type == pygame.MOUSEBUTTONUP:
				x,y = pygame.mouse.get_pos()
				if ultim_dia != avui and \
				   POSICIO_IMATGE[0] <= x <= POSICIO_IMATGE[0] + AMPLADA_IMATGE and \
				   POSICIO_IMATGE[1] <= y <= POSICIO_IMATGE[1] + ALÇADA_IMATGE:
				   n, ultim_dia = modifica_registre()

	if ultim_dia != avui:
		image = pygame.image.load("resources/Pendent.png")
		image = pygame.transform.scale(image, (AMPLADA_IMATGE, ALÇADA_IMATGE))
	else:
		image = pygame.image.load("resources/tick.png")
		image = pygame.transform.scale(image, (AMPLADA_IMATGE, ALÇADA_IMATGE))

	textsurface = myfont.render(f'Recompte de dies: {n}   -   Últim dia: {ultim_dia.day}-{mesos_romans[ultim_dia.month]}-{ultim_dia.year}', False, (0, 0, 0))

	screen.fill((255,255,255))
	screen.blit(textsurface,(40,40))
	screen.blit(image, POSICIO_IMATGE)
	pygame.display.flip()