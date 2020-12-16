# -*- coding: utf-8 -*-
"""
/******************************* ASSESSMENT *********************************
*    Questao 09                                                            *
*        Aluno           : Francisco Alves Camello Neto                    *
*        Disciplina      : Fundamentos do Desenvolvimento Python           *
*        Professor       : Thaís do Nascimento Viana                       *
*        Nome do arquivo : questao_09.py                                   *
***************************************************************************/
"""
import pygame
import random as rd


class Questao_09():
    """ This function draws a rectangle when the user clicks on button. """

    def __init__(self):
        """ Constructor. """
        pygame.init()
        pygame.font.init()
        self.DISPLAY_NAME = pygame.display.set_caption('Questão 09')
        self.SCREEN = pygame.display.set_mode((400, 400))
        self.FPS = 60
        self.FPSCLOCK = pygame.time.Clock()
        self.FONT = pygame.font.SysFont('Arial', 16)
        self.BUTTON = pygame.Rect(175, 50, 50, 50)
        self.rect_list = []
        self.finish = False

    def draw_square(self):
        """ This functions draws a square """
        x = rd.randint(25, 400 - 25)
        y = rd.randint(25, 400 - 25)
        return pygame.Rect(x, y, 25, 25)

    def draw_button(self):
        """ This functions draws a button """
        pygame.draw.ellipse(self.SCREEN, (255, 255, 255), self.BUTTON)
        text = self.FONT.render('Clique', False, (0, 0, 0))
        text_rect = text.get_rect(center=self.BUTTON.center)
        self.SCREEN.blit(text, text_rect)

    def handle_event(self, event):
        """ This functions handles a mouse click. """
        if event.button == 1:
            position = pygame.mouse.get_pos()

            if self.BUTTON.collidepoint(position):
                rect = self.draw_square()
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
        # self.color = (randint(0, 255), randint(0, 255), randint(0, 255))
        # self.position = (randint(5, 395), randint(5, 395))

        while not self.finish:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.finish = True

                if event.type == pygame.MOUSEBUTTONUP:
                    self.handle_event(event)

            self.SCREEN.fill((0, 0, 0))

            self.draw_button()

            for rect in self.rect_list:
                pygame.draw.rect(self.SCREEN, (255, 197, 1), rect)

            pygame.display.flip()

            self.FPSCLOCK.tick(self.FPS)

        pygame.display.quit()


Questao_09().init_game()
