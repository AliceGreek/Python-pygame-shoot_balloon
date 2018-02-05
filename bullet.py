import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
	"""子弹类"""
	def __init__(self, screen, settings, ship):
		super().__init__()
		self.screen = screen
		self.settings = settings

		# 在（0，0）处创建子弹的矩形，再确定矩形的具体位置
		self.rect = pygame.Rect(0, 0, settings.bullet_width, settings.bullet_height)
		self.rect.centerx = ship.rect.centerx
		self.rect.top = ship.rect.top

		# 用小数存储子弹的精确位置
		self.y = float(self.rect.y)

		self.color = settings.bullet_color
		self.speed_factor = settings.bullet_speed_factor

	def update(self):
		self.y -= self.speed_factor
		self.rect.y = self.y

	def draw_bullet(self):
		"""在屏幕上绘制子弹"""
		pygame.draw.rect(self.screen, self.color, self.rect)

