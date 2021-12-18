import pygame


class Ship:
    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()
        # 加载飞船图像并获取外接矩形
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        # 对于飞船初始化为底部中央
        self.rect.midbottom = self.screen_rect.midbottom

        # 在飞船的属性X中储存小数值
        self.x = float(self.rect.x)
        self.moving_right = False
        self.moving_left = False

    def update(self):

        # 根据位置来移动标志飞船的位置
        # 更新飞船而不是rect对象的X值
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        # 根据self.x来更新rect对象
        self.rect.x = self.x

    def blitme(self):
        # 在指定位置绘制飞船
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        '''让飞船在屏幕底部'''
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect, x)
