class Settings():
	"""设置管理类"""
	def __init__(self):
		self.screen_width = 1200
		self.screen_height = 800
		self.bg_color = 255, 255, 255

		# 设置靶子(气球)
		# 气球移动的方向，为1时方向向右，为-1时方向向左
		self.balloon_direction = 1

		# 设置子弹
		self.bullet_speed_factor = 50.5
		self.bullet_width = 3
		self.bullet_height = 15
		self.bullet_color = 0, 0, 0

		# 设置飞船
		self.ship_speed_factor = 5.5

		# 以什么样的速度加快游戏节奏
		self.speedup_scale = 1.5

		self.initialize_dynamic_settings()

	def initialize_dynamic_settings(self):
		"""初始化随游戏进行而变化的量"""

		# 气球移动速度
		self.target_speed_factor = 1.5

		# 飞船数量
		self.ship_allowed = 3

	def increase_speed(self):
		self.target_speed_factor *= self.speedup_scale

