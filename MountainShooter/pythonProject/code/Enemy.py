#!/usr/bin/python
# -*- coding: utf-8 -*-
from MountainShooter.pythonProject.code.Const import ENTITY_SPEED, WIN_WIDTH, ENTITY_SHOT_DELAY
from MountainShooter.pythonProject.code.EnemyShot import EnemyShot
from MountainShooter.pythonProject.code.Entity import Entity


class Enemy(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.shot_delay = ENTITY_SHOT_DELAY[self.name]

    def move(self):
         self.rect.centerx -= ENTITY_SPEED[self.name]

     def shoot(self):
         self.shot_delay -= 1
         self.shot_delay = ENTITY_SHOT_DELAY[self.name]
         return EnemyShot(name=f'{self.name}shot', position=(self.rect.centerx, self.rect.centery))
