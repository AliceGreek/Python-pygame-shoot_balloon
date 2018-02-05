import pygame
import sys
from time import sleep

from bullet import Bullet
from balloon import Balloon


def check_key_down_events(event, ship, screen, settings, bullets):
	if event.key == pygame.K_LEFT:
		ship.moving_left = True
	elif event.key == pygame.K_RIGHT:
		ship.moving_right = True
	elif event.key == pygame.K_q:
		sys.exit()
	elif event.key == pygame.K_SPACE:
		"""按空格键发射子弹"""
		if len(bullets) == 0:
			new_bullet = Bullet(screen, settings, ship)
			bullets.add(new_bullet)


def check_play_button(stats, button, mouse_x, mouse_y, settings,  bullets, balloons, screen, ship):
	button_clicked = button.rect.collidepoint(mouse_x, mouse_y)
	if button_clicked and not stats.game_active:
		start_game(settings, stats, bullets, balloons, screen, ship)


def start_game(settings, stats, bullets, balloons, screen, ship):
	# 重置游戏设置
	settings.initialize_dynamic_settings()

	# 重置游戏统计设置
	stats.reset_stats()
	stats.game_active = True

	# 清空子弹列表和气球列表
	bullets.empty()
	balloons.empty()

	# 创建新的气球并使得飞船居中
	balloon = Balloon(screen, settings)
	balloons.add(balloon)
	ship.ship_center()


def update_bullets(bullets, balloons, screen, ai_settings, stats):
	"""若子弹越过屏幕顶部或者子弹与气球碰撞则删除子弹"""
	for bullet in bullets.copy():
		if bullet.rect.bottom < 0:
			bullets.remove(bullet)
			if ai_settings.ship_allowed > 0:
				ai_settings.ship_allowed -= 1
			else:
				stats.game_active = False
				sleep(0.5)


	check_collison_balloon_and_bullet(balloons, bullets, screen, ai_settings)


def check_collison_balloon_and_bullet(balloons, bullets, screen, ai_settings):
	"""子弹和气球碰撞，则删除碰撞的子弹和气球，并创建新的气球"""
	collisions = pygame.sprite.groupcollide(balloons, bullets, True, True)
	if collisions:
		ai_settings.increase_speed()
		# print(ai_settings.target_speed_factor)
		create_balloon(screen, ai_settings, balloons)


def check_key_up_events(event, ship):
	if event.key == pygame.K_LEFT:
		ship.moving_left = False
	elif event.key == pygame.K_RIGHT:
		ship.moving_right = False


def check_balloon_edge(balloons, screen_rect, ai_settings):
	for balloon in balloons.sprites():
		if balloon.rect.right >= screen_rect.right or balloon.rect.left <= screen_rect.left:
			ai_settings.balloon_direction *= -1
			break


def update_balloon(balloons, screen_rect, ai_settings):
	check_balloon_edge(balloons, screen_rect, ai_settings)
	balloons.update()


def create_balloon(screen, ai_settings, balloons):
	new_balloon = Balloon(screen, ai_settings)
	balloons.add(new_balloon)
