# -*- coding: utf-8 -*-
"""
/******************************* ASSESSMENT *********************************
*    Questao 07                                                            *
*        Aluno           : Francisco Alves Camello Neto                    *
*        Disciplina      : Fundamentos do Desenvolvimento Python           *
*        Professor       : Thaís do Nascimento Viana                       *
*        Nome do arquivo : questao_07.py                                   *
***************************************************************************/
"""
import pygame
from random import randint


class Questao_07():
    """ This function draws a rectangle where the user clicks. """

    def __init__(self):
        """ Constructor. """
        pygame.init()
        self.DISPLAY_NAME = pygame.display.set_caption('Questão 07')
        self.SCREEN_WIDTH = 400
        self.SCREEN_HEIGHT = 400
        self.SCREEN = pygame.display.set_mode(
            (self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
        self.FPS = 60
        self.FPSCLOCK = pygame.time.Clock()
        self.color = (0, 0, 0)
        self.position = (0, 0)
        self.finish = False

    def draw_square(self, surface, color, position):
        """ This functions draws a square """
        rect = pygame.Rect(position, (50, 50))
        pygame.draw.rect(surface, color, rect)

    def init_game(self):
        """ This function starts the game. """
        while not self.finish:
            self.color = (randint(0, 255), randint(0, 255), randint(0, 255))
            self.position = (randint(5, 395), randint(5, 395))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.finish = True

                elif event.type == pygame.MOUSEBUTTONUP:
                    if event.button == 3:
                        self.draw_square(self.SCREEN, self.color, self.position)
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_SPACE:
                        self.draw_square(self.SCREEN, self.color, self.position)

            pygame.display.update()

            self.FPSCLOCK.tick(self.FPS)

        pygame.display.quit()


Questao_07().init_game()
