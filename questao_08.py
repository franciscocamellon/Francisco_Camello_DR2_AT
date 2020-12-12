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
        self.RECT = pygame.Rect(175, 175, 50, 50)
        self.BUTTON = pygame.draw.rect(
            self.SCREEN, (255, 255, 255), self.RECT, border_radius=25)
        self.rect_list = []
        self.color = (randint(0, 255), randint(0, 255), randint(0, 255))
        self.BLACK = (0, 0, 0)
        self.position = (0, 0)
        self.finish = False

    def draw_square(self, surface, color, position):
        """ This functions draws a square """
        rect = Rectangle(color, self.SCREEN_WIDTH,
                         self.SCREEN_HEIGHT)
        return pygame.draw.rect(surface, color, rect)

    def draw_button(self, surface, color):
        """ This functions draws a button """
        button = self.BUTTON
        text = self.FONT.render('Clique', True, (0, 0, 0))
        text_rect = text.get_rect(center=button.center)
        surface.blit(text, text_rect)

    def handle_event(self, event):
        """ This functions handles a mouse click. """
        if event.button == 1:
            position = pygame.mouse.get_pos()

            if self.BUTTON.collidepoint(position):
                rect = self.draw_square(self.SCREEN, self.color, self.position)
                self.rect_list.append(rect)
                self.collision(rect)

    def collision(self, rect_b):
        """ This functions checks the collision. """
        for rect_a in self.rect_list:
            if rect_a is not rect_b and rect_a.colliderect(rect_b):
                self.rect_list.remove(rect_a)
                if rect_b in self.rect_list:
                    self.rect_list.remove(rect_b)

    def init_game(self):
        """ This function starts the game. """
        self.color = (randint(0, 255), randint(0, 255), randint(0, 255))
        self.position = (randint(5, 395), randint(5, 395))
        self.draw_button(self.SCREEN, (255, 255, 255))

        while not self.finish:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.finish = True

                if event.type == pygame.MOUSEBUTTONUP:
                    self.handle_event(event)

            for rect in self.rect_list:
                pygame.draw.rect(self.SCREEN, self.color, rect)

            pygame.display.update()

            self.FPSCLOCK.tick(self.FPS)

        pygame.display.flip()


Questao_08().init_game()
