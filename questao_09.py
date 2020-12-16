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

    def move_keys(self):
        """ This functions moves a rectangle in place """
        key = pygame.key.get_pressed()

        if self.BUTTON.x > 350:
            self.BUTTON.x = 12.5
            if key[pygame.K_d]:
                self.BUTTON.x += 5
        elif self.BUTTON.x < 12.5:
            self.BUTTON.x = 350
            if key[pygame.K_a]:
                self.BUTTON.x -= 5
        elif self.BUTTON.y > 350:
            self.BUTTON.y = 12.5
            if key[pygame.K_w]:
                self.BUTTON.x += 5
        elif self.BUTTON.y < 12.5:
            self.BUTTON.y = 350
            if key[pygame.K_s]:
                self.BUTTON.x -= 5
        else:
            if key[pygame.K_a]:
                self.BUTTON.x -= 5
            if key[pygame.K_d]:
                self.BUTTON.x += 5
            if key[pygame.K_w]:
                self.BUTTON.y -= 5
            if key[pygame.K_s]:
                self.BUTTON.y += 5

        for rec in self.rect_list:
            if rec.colliderect(self.BUTTON):
                self.rect_list.remove(rec)

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

                # if event.type == pygame.KEYDOWN:
                #     self.move_keys()

            self.SCREEN.fill((0, 0, 0))

            self.draw_button()
            self.move_keys()

            for rect in self.rect_list:
                pygame.draw.rect(self.SCREEN, (255, 197, 1), rect)

            pygame.display.flip()

            self.FPSCLOCK.tick(self.FPS)

        pygame.display.quit()


Questao_09().init_game()
