import pygame


def check():
	event = pygame.event.poll()
	if event.type == pygame.QUIT:
		return 0
	if event.type == pygame.KEYDOWN and event.key == "K_ESC":
		return 0