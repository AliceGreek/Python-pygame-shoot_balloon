import pygame
from random import randint
from pygame.sprite import Sprite


class Balloon(Sprite):
	"""热气球类"""
	def __init__(self, screen, ai_settings):
		super().__init__()
		self.screen = screen
		self.ai_settings = ai_settings

		# 加载热气球图片
		self.image = pygame.image.load('images/balloon.bmp')
		self.rect = self.image.get_rect()
		self.screen_rect = self.screen.get_rect()

		# 将热气球放在确定位置
		self.rect.centerx = randint(0+self.rect.width, int(self.ai_settings.screen_width - self.rect.width))
		self.rect.top = self.screen_rect.top

		# 用小数存储气球所在的精确位置
		self.x = self.rect.centerx

	def blitme(self):
		self.screen.blit(self.image, self.rect)
		self.screen.blit(self.image, self.rect)

	def update(self):
		self.x += self.ai_settings.target_speed_factor * self.ai_settings.balloon_direction
		self.rect.centerx = self.x
