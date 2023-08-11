from typing import Any
from random import randint
import pygame


class Button():
	def __init__(self, x:int, y:int, image, scale:int):
		width = image.get_width()
		height = image.get_height()
		self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
		self.rect = self.image.get_rect()
		self.rect.topleft = (x, y)
		self.clicked = False

	def draw(self, surface):
		action = False
		
		pos = pygame.mouse.get_pos()

		#check mouseover and clicked conditions
		if self.rect.collidepoint(pos):
			if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
				self.clicked = True
				action = True

		if pygame.mouse.get_pressed()[0] == 0:
			self.clicked = False

		#draw button on screen
		surface.blit(self.image, (self.rect.x, self.rect.y))

		return action
class image():
	def __init__(self, x:int, y:int, image, scale:int):
		width = image.get_width()
		height = image.get_height()
		self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
		self.rect = self.image.get_rect()
		self.rect.topleft = (x, y)
	def draw(self, surface):

		surface.blit(self.image, (self.rect.x, self.rect.y))

	def draw_multiple(self,surface,amount:int):
		pos_list = [(865, 86), (41, 464), (309, 328), (552, 271), (320, 486), (144, 274), (664, 465), (134, 186), (551, 219), (246, 211), (602, 282), (475, 147), (859, 429), (730, 278), (753, 405), (431, 549), (923, 516), (636, 498)]
		for num in range(amount):
			surface.blit(self.image,pos_list[num])
	def set_vis(self,alpha):
		self.image.set_alpha(alpha)
	def rotate_draw(self, rotation:int):
		self.image = pygame.transform.rotate(self.image,rotation)
class Player():
	def __init__(self,image,x,y,scale,surface,dif_face):
		width = image.get_width()
		height = image.get_height()
		self.x_p = x
		self.y_p = y
		self.image_p = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
		self.width_p = self.image_p.get_width()
		self.height_p = self.image_p.get_height()
		self.rect_p = self.image_p.get_rect()
		self.vel_p = 4
		self.surface_p = surface

		self.dif_face = dif_face
		width = dif_face.get_width()
		height = dif_face.get_height()
		self.x_p = x
		self.y_p = y
		self.dif_face = pygame.transform.scale(dif_face, (int(width * scale), int(height * scale)))
		self.width_dif_face = self.dif_face.get_width()
		self.height_dif_face = self.dif_face.get_height()
		self.rect_dif_face = self.dif_face.get_rect()
		self.spotLight_radius = 200
		self.hunger = False

		self.direction = "none"
		self.spotlight_pos = [self.rect_p.centerx,self.rect_p.centery]
	def Player_input(self,sprint_status):
		keys = pygame.key.get_pressed()
		last_pos = (self.rect_p.centerx,self.rect_p.centery)
		
		if keys[pygame.K_a]:
			# A
			self.rect_p.centerx -= self.vel_p
			self.direction = "a"
		if keys[pygame.K_d]:
			# D
			self.rect_p.centerx += self.vel_p
			self.direction = "d"
		if keys[pygame.K_s]:
			# S
			self.rect_p.centery += self.vel_p
			self.direction = "s"
		if keys[pygame.K_w]:
			# W
			self.rect_p.centery -= self.vel_p
			self.direction = "w"
		

		
		current_pos = (self.rect_p.centerx,self.rect_p.centery)
		if last_pos[0] == current_pos[0] and last_pos[1] == current_pos[1]:
			self.direction = "none"
		
		if keys[pygame.K_LSHIFT] and sprint_status > 0:
			self.vel_p = 10
			return True
		else:
			self.vel_p = 4
			
			return False
	def Player_draw(self):
		
		# drawing the character 
		self.surface_p.blit(self.image_p,self.rect_p)
		# drawing spotlight and darkness
		cover_surf = pygame.Surface((2000, 2000))
		shadow_surf = pygame.Surface((2000,2000))
		cover_surf.fill((21, 1, 38))
		shadow_surf.fill((52, 46, 56))
		cover_surf.set_colorkey((255,255,255))
		shadow_surf.set_colorkey((255,255,255))
		# spotlight drawing logic
		if self.rect_p.centerx != self.spotlight_pos[0] or self.rect_p.centery != self.spotlight_pos[1]:
			
			x_dif = self.rect_p.centerx - self.spotlight_pos[0]
			y_dif = self.rect_p.centery - self.spotlight_pos[1]
			# transion back to the player
			
			if x_dif > 40:
				self.spotlight_pos[0] += 4
			elif x_dif > 20:
				self.spotlight_pos[0] += 1
				print(x_dif)
			if x_dif < -40:
				self.spotlight_pos[0] -= 4
			elif x_dif < -20:
				self.spotlight_pos[0] -= 1
				print(x_dif)
			if y_dif > 40:
				self.spotlight_pos[1] += 4
			elif y_dif > 20:
				# player went down meaning that the dif will be in the +
				self.spotlight_pos[1] += 1
				print(y_dif)
			if y_dif < -40:
				self.spotlight_pos[1] -= 4
			elif y_dif < -20:
				self.spotlight_pos[1] -= 1
				print(y_dif)
				


			
		
		pygame.draw.circle(cover_surf,(255,255,255),self.spotlight_pos,self.spotLight_radius)
		pygame.draw.circle(shadow_surf,(255,255,255),self.spotlight_pos,(self.spotLight_radius - 10))
		darknes_rect = pygame.Rect(0,0,2000,2000)
		# self.surface_p.set_clip(darknes_rect)
		shadow_surf.set_alpha(20)
		self.surface_p.blit(shadow_surf,darknes_rect)
		self.surface_p.blit(cover_surf,darknes_rect)
		# hit box code
		pygame.draw.rect(self.surface_p, (250,0,0),self.rect_p,2)
class Stats():
	def __init__(self,x:int,y:int,image,surface,scale:int,starting_stat:int,Max:int,color):
		width = image.get_width()
		height = image.get_height()
		self.x = x
		self.y = y
		self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
		self.width = self.image.get_width()
		self.height = self.image.get_height()
		self.rect = image.get_rect(midleft = (x,y))
		self.surface = surface
		self.starting_stats = starting_stat
		self.current_stat = starting_stat
		self.Max = Max
		self.color = color
	def stats_draw(self):
		
		pygame.draw.rect(self.surface,self.color,((self.rect.x + 12.5), (self.rect.y + 12.5), self.current_stat, 25))

		self.surface.blit(self.image,self.rect)
class food():
	def __init__(self,x:int,y:int,surface,image,scale:int):
		width = image.get_width()
		height = image.get_height()
		self.surface = surface
		self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
		self.rect = self.image.get_rect()
		self.x = x
		self.y = y
		self.rect.y = y
		self.rect.x = x
		self.eaten = False
	def draw(self):
		if not self.eaten:
			self.surface.blit(self.image,self.rect)
			# hit box code
			pygame.draw.rect(self.surface, (250,0,0),self.rect,2)
		elif self.eaten:
			self.eaten = False
			self.rect.x = randint(100,1100)
			self.rect.y = randint(100,700)
		
