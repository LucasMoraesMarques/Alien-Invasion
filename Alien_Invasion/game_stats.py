class GameStats():
    """Armazena dados estatísticos da Invasão Alienígena."""
    def __init__(self, ai_settings, high_score):
        """Inicializa os dados estatísticos."""
        # A pontuação máxima jamais deverá ser reiniciada
        self.high_score = int(high_score)
        self.level = 1
        self.ai_settings = ai_settings
        self.reset_stats()
        # Inicia a Invasão Alienígena em um estado inativo
        self.game_active = False

    def reset_stats(self):
        """Inicializa os dados estatísticos que podem mudar durante o
        jogo."""
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0