# -*- coding: utf-8 -*-
"""
/******************************* ASSESSMENT *********************************
*    Questao 02                                                            *
*        Aluno           : Francisco Alves Camello Neto                    *
*        Disciplina      : Fundamentos do Desenvolvimento Python           *
*        Professor       : Thaís do Nascimento Viana                       *
*        Nome do arquivo : questao_02.py                                   *
***************************************************************************/
"""
from validation import Validate


class Questao_02():
    """ This program takes a number from user and return the sum of all even
    numbers from one to user input. """

    def __init__(self):
        """ Constructor. """
        self.input = 0
        self.data = []
        self.num = 0

    def init_class(self):
        """ This function receives the input data from users. """
        self.input = Validate().validate_values(' Digite um número: ')

    def process_data(self):
        """ This function process the input data from init_class. """
        self.init_class()

        for i in range(1, (self.input + 1)):
            if i % 2 == 0:
                self.data.append(i)
            else:
                pass
        self.num = sum(self.data)

    def print_result(self):
        """ This is a printer! It prints. """
        print('===' * 25, 'Questão 02'.center(75), '===' * 25, sep='\n')
        self.process_data()
        print('---' * 25,
              '  A soma dos números pares de 1 a {} é: {}'.format(
                  self.input, self.num),
              '---' * 25, 'Aluno: Francisco Camello'.rjust(75), sep="\n")


Questao_02().print_result()
