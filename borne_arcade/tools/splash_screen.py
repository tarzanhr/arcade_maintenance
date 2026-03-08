#!/usr/bin/env python3
"""Splash screen displayed during arcade cabinet startup."""

import sys
import os

try:
    import pygame
except ImportError:
    sys.exit(0)

STATUS_FILE = "/tmp/arcade_status"


def main():
    pygame.init()
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    pygame.display.set_caption("IUT Arcade")
    pygame.mouse.set_visible(False)

    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    GREY = (85, 85, 85)

    width, height = screen.get_size()

    font_title = pygame.font.SysFont("helvetica", 72, bold=True)
    font_status = pygame.font.SysFont("helvetica", 32)

    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)

        status = "Chargement..."
        if os.path.exists(STATUS_FILE):
            try:
                with open(STATUS_FILE) as f:
                    msg = f.read().strip()
                if msg == "READY":
                    break
                if msg:
                    status = msg
            except OSError:
                pass

        screen.fill(WHITE)

        title = font_title.render("IUT Arcade", True, BLACK)
        screen.blit(title, (width // 2 - title.get_width() // 2, height // 2 - 60))

        status_text = font_status.render(status, True, GREY)
        screen.blit(status_text, (width // 2 - status_text.get_width() // 2, height // 2 + 40))

        pygame.display.flip()
        clock.tick(10)

    pygame.quit()


if __name__ == "__main__":
    main()
