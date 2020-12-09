# -*- coding: utf-8 -*-
"""
/******************************* ASSESSMENT *********************************
*    Questao 08                                                            *
*        Aluno           : Francisco Alves Camello Neto                    *
*        Disciplina      : Fundamentos do Desenvolvimento Python           *
*        Professor       : Thaís do Nascimento Viana                       *
*        Nome do arquivo : questao_08.py                                   *
***************************************************************************/
"""
import pygame
from random import randint
from components import Rectangle


class Questao_08():
    """ This function draws a rectangle when the user clicks on button. """

    def __init__(self):
        """ Constructor. """
        pygame.init()
        self.DISPLAY_NAME = pygame.display.set_caption('Questão 08')
        self.SCREEN_WIDTH = 400
        self.SCREEN_HEIGHT = 400
        self.SCREEN = pygame.display.set_mode(
            (self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
        self.FPS = 60
        self.FPSCLOCK = pygame.time.Clock()
        self.FONTSIZE = 16
        self.FONT = pygame.font.SysFont('Arial', self.FONTSIZE)
        self.color = (0, 0, 0)
        self.position = (0, 0)
        self.finish = False

    def draw_square(self, surface, color, position):
        """ This functions draws a square """
        rect = Rectangle(self.color, self.SCREEN_WIDTH,
                         self.SCREEN_HEIGHT)
        return pygame.draw.rect(surface, color, rect)

    def draw_button(self, surface, color):
        """ This functions draws a button """
        # text = self.FONT.render('Clique', True, (255,255,255))
        # surface.blit(text, (50, 50))

        rect = pygame.Rect(175, 175, 50, 50)

        button = pygame.draw.rect(
            surface, (255, 255, 255), rect, border_radius=25)
        return button

    def init_game(self):
        """ This function starts the game. """
        button = self.draw_button(self.SCREEN, self.color)
        rect_list = []

        while not self.finish:
            self.color = (randint(0, 255), randint(0, 255), randint(0, 255))
            self.position = (randint(5, 395), randint(5, 395))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.finish = True

                if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                    mouse_pos = event.pos
                    rect = self.draw_square(
                        self.SCREEN, self.color, self.position)

                    if button.collidepoint(mouse_pos):
                        for rect in rect_list:
                            if rect.collidepoint(button):
                                rect_list.remove(rect)
                            else:
                                rect = self.draw_square(
                                    self.SCREEN, self.color, self.position)
                                rect_list.append(rect)


            pygame.display.update()

            self.FPSCLOCK.tick(self.FPS)

        pygame.display.quit()


Questao_08().init_game()
