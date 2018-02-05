import pygame
import os


class Ship():
	"""飞船类"""
	def __init__(self, screen, settings):
		self.screen = screen
		self.settings = settings

		# 加载飞船图片并获得边距
		self.image = pygame.image.load(os.path.join('images', 'airplane.bmp'))
		self.rect = self.image.get_rect()
		self.screen_rect = self.screen.get_rect()

		# 设置飞船的位置
		self.rect.x = self.screen_rect.centerx
		self.rect.bottom = self.screen_rect.bottom

		# 用小数存储飞船的精确位置
		self.x = self.rect.centerx

		# 移动状态
		self.moving_left = False
		self.moving_right = False

	def blitme(self):
		"""将飞船画在屏幕上"""
		self.screen.blit(self.image, self.rect)

	def update(self):
		"""更新飞船的位置"""
		if self.moving_left and self.rect.left > 0:
			self.x -= self.settings.ship_speed_factor
		elif self.moving_right and self.rect.right < self.screen_rect.right:
			self.x += self.settings.ship_speed_factor
		self.rect.centerx = self.x

	def ship_center(self):
		self.x = self.screen_rect.centerx
		print('hi,ship center')


