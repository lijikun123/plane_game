class Settings:
    # 存储游戏的设置类
    def __init__(self):
        '''初始化游戏设置,屏幕设置'''
        self.screen_width = 1200
        self.screen_height = 600
        self.bg_color = (230, 230, 230)

        self.ship_speed = 0.5
        self.ship_limit = 3

        self.bullet_speed = 1.5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullet_allowed = 3

        self.alien_speed = 0.5
        self.fleet_drop_speed = 5
        # fleet.direction 为1表示向右移,为-1表示向左移
        self.fleet_direction = 1
        # 子弹设置
