import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard


def run_game():
    # Inicializa o jogo e cria um objeto para a tela
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load('sounds/background.mp3')
    set_inst = Settings()
    screen = pygame.display.set_mode((set_inst.width, set_inst.height ))
    pygame.display.set_caption("Alien Invasion")
    # Cria o botão Play
    play_button = Button(set_inst, screen, "PLAY")
    #Cria instância para armazenar estatísticas do jogo e cria painel de pontuação
    with open('high_score.text', 'rt') as file:
        high_score = file.readline().strip()
        print(high_score)
    stats = GameStats(set_inst, high_score)
    sb = Scoreboard(set_inst, screen, stats)
    # Cria uma espaçonave, um grupo de projéteis e um grupo de alienígenas
    ship = Ship(set_inst, screen)
    bullets = Group()
    aliens = Group()
    # Cria a frota de alienígenas
    gf.create_fleet(set_inst, screen, ship, aliens)
    # Inicia o laço principal do jogo
    pygame.mixer.music.play(-1)
    while True:
        gf.check_events(set_inst, screen, stats, sb, play_button, ship, aliens, bullets)
        if stats.game_active:
            ship.update()
            gf.update_bullets(set_inst, screen, stats, sb, ship, aliens, bullets)
            gf.update_aliens(set_inst, stats, screen, sb, ship,  aliens, bullets)
        gf.update_screen(set_inst, screen, stats, sb, ship, aliens, bullets, play_button)
run_game()