class GameStats():
	"""游戏数据统计"""
	def __init__(self, settings):
		self.settings = settings
		self.reset_stats()
		self.game_active = False

	def reset_stats(self):
		"""初始化在游戏中可能发生变化的统计信息"""
		self.ship_left = self.settings.ship_allowed
