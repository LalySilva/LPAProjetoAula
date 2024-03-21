from abc import ABC

from MountainShooter.pythonProject.code.Const import ENTITY_SPEED
from MountainShooter.pythonProject.code.EnemyShot import EnemyShot
from MountainShooter.pythonProject.code.Entity import Entity


class PlayerShot(Entity, ABC):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)

    def move(self):
        self.rect.centerx += ENTITY_SPEED[self.name]

    def shoot(self):
        return EnemyShot(name=f'{self.name}shot', position=(self.rect.centerx, self.rect.centery))
