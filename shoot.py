import pygame
import sys
from pygame.sprite import Group

from settings import Settings
from ship import Ship
import functions as f
from button import Button
from game_stats import GameStats
from balloon import Balloon
from bullet import Bullet


def run_game():
	pygame.init()
	settings = Settings()

	# 创建屏幕对象
	screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
	screen_rect = screen.get_rect()
	pygame.display.set_caption('Let\'s shoot')

	# 创建一艘飞船
	ship = Ship(screen, settings)

	# 创建一个气球编组
	balloons = Group()

	# 创建气球并加入编组
	f.create_balloon(screen, settings, balloons)

	# 创建一个子弹编组
	bullets = Group()

	# 创建一个按钮
	button = Button(screen, "Play")

	# 创建游戏统计对象
	stats = GameStats(settings)

	# 开始游戏循环
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()

			elif event.type == pygame.KEYDOWN:
				f.check_key_down_events(event, ship, screen, settings, bullets)
			elif event.type == pygame.KEYUP:
				f.check_key_up_events(event, ship)
			elif event.type == pygame.MOUSEBUTTONDOWN:
				mouse_x, mouse_y = pygame.mouse.get_pos()
				f.check_play_button(stats, button, mouse_x, mouse_y, settings,  bullets, balloons, screen, ship)
		if stats.game_active:
			ship.update()
			f.update_balloon(balloons, screen_rect, settings)
			bullets.update()
			f.update_bullets(bullets, balloons, screen, settings, stats)
		screen.fill(settings.bg_color)
		for bullet in bullets.sprites():
			bullet.draw_bullet()
		ship.blitme()
		for balloon in balloons.copy():
			balloon.blitme()
		# 若游戏处于非活跃状态，则显示Play按钮
		if not stats.game_active:
			button.draw_button()
		pygame.display.flip()


run_game()