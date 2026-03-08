#!/usr/bin/env python3
"""Shutdown countdown screen displayed before system halt."""

import sys
import time

try:
    import pygame
except ImportError:
    sys.exit(0)

COUNTDOWN = 30


def main():
    pygame.init()
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    pygame.display.set_caption("Extinction")
    pygame.mouse.set_visible(False)

    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    GREY = (85, 85, 85)

    width, height = screen.get_size()

    font_title = pygame.font.SysFont("helvetica", 52, bold=True)
    font_countdown = pygame.font.SysFont("helvetica", 120, bold=True)
    font_sub = pygame.font.SysFont("helvetica", 28)

    clock = pygame.time.Clock()
    start = time.time()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)

        elapsed = int(time.time() - start)
        remaining = COUNTDOWN - elapsed

        if remaining <= 0:
            break

        screen.fill(WHITE)

        title = font_title.render("Extinction de la borne", True, BLACK)
        screen.blit(title, (width // 2 - title.get_width() // 2, height // 2 - 120))

        countdown = font_countdown.render(str(remaining), True, BLACK)
        screen.blit(countdown, (width // 2 - countdown.get_width() // 2, height // 2 - 30))

        sub = font_sub.render("secondes", True, GREY)
        screen.blit(sub, (width // 2 - sub.get_width() // 2, height // 2 + 100))

        pygame.display.flip()
        clock.tick(10)

    pygame.quit()


if __name__ == "__main__":
    main()
