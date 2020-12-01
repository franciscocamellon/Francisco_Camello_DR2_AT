# -*- coding: utf-8 -*-
"""
/******************************* ASSESMENT *********************************
*    Questao 01                                                            *
*        Aluno           : Francisco Alves Camello Neto                    *
*        Disciplina      : Fundamentos do Desenvolvimento Python           *
*        Professor       : Thaís do Nascimento Viana                       *
*        Nome do arquivo : questao_01.py                                   *
***************************************************************************/
"""


class Questao_01():
    """
    This program takes a tuple and prints your elements in ascending order.
    """

    def __init__(self):
        """ Constructor """
        self.data = (55, 9, 22)

    def init_class(self):
        """ This function receives the input data from users. """
        print('Tupla original: {}'.format(self.data))

    def process_data(self):
        """ This function process the input data from init_class. """
        self.init_class()
        _list = list(self.data)
        _list.sort()
        return tuple(_list)

    def print_result(self):
        """ This is a printer! It prints. """

        print('===' * 25, 'Questão 01'.center(75), '===' * 25, sep='\n')
        print('---' * 25,
              'Tupla em ordem crescente: {}'.format(self.process_data()),
              '---' * 25, 'Aluno: Francisco Camello'.rjust(75), sep="\n")


Questao_01().print_result()
