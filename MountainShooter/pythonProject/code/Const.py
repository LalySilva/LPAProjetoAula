# CONSTANTE PARA COR.
import pygame

COLOR_ORANGE = (255, 128, 0)
COLOR_YELLOW = (255, 255, 128)
COLOR_WHITE = (255, 255, 255)

# MENU DE OPÇÕES.

MENU_OPTION = ('NEW GAME 1P',
               'NEW GAME 2P - COOPERATIVE',
               'NEW GAME 2P - COMPETITIVE',
               'EXIT')
# CONSTANTE PARA O TAMANHO DA JANELA
WIN_WIDTH = 576
WIN_HEIGHT = 324

EVENT_ENEMY = pygame.USEREVENT + 1

# VÁRIAVEL IMAGEM LEVEL
# IMAGEM_LEVEL = {'Level1bg': 7}

# VARIAVEL PARA VELOCIDADE

ENTITY_SPEED = {'Level1bg0': 0,
                'Level1bg1': 1,
                'Level1bg2': 2,
                'Level1bg3': 3,
                'Level1bg4': 4,
                'Level1bg5': 5,
                'Level1bg6': 6,
                'Player1': 3,
                'Player2': 3,
                'Enemy1': 2,
                'Enemy2': 1,
                }

PLAYER_KEY_UP = {'Player1': pygame.K_UP,
                 'Player2': pygame.K_w}

PLAYER_KEY_DOWN = {'Player1': pygame.K_DOWN,
                   'Player2': pygame.K_s}

PLAYER_KEY_LEFT = {'Player1': pygame.K_LEFT,
                   'Player2': pygame.K_a}

PLAYER_KEY_RIGHT = {'Player1': pygame.K_RIGHT,
                    'Player2': pygame.K_d}
