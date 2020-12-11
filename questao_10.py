# -*- coding: utf-8 -*-
"""
/******************************* ASSESSMENT *********************************
*    Questao 10                                                            *
*        Aluno           : Francisco Alves Camello Neto                    *
*        Disciplina      : Fundamentos do Desenvolvimento Python           *
*        Professor       : Thaís do Nascimento Viana                       *
*        Nome do arquivo : questao_10.py                                   *
***************************************************************************/
"""
import csv
import requests
# import pandas as pd


class Questao_10():
    """ This function draws a square with side size given by the user. """

    def __init__(self):
        """ Constructor. """
        self.url = 'https://sites.google.com/site/dr2fundamentospython/arquivos/Winter_Olympics_Medals.csv'
        self.gold_medal = []
        self.total_medal = {}

    def init_class(self):
        """ This function receives the input data from users. """

        self.csv = requests.get(self.url).text
        self.csv_lines = self.csv.splitlines()

        for line in self.csv_lines:
            coluna = line.split(',')
            if coluna[0] != 'Year' and int(coluna[0]) >= 2001:
                if coluna[4] == 'SWE' or coluna[4] == 'DEN' or coluna[4] == 'NOR':
                    if coluna[2] == 'Curling' or coluna[2] == 'Skating' or coluna[2] == 'Skiing' or coluna[2] == 'Ice Hockey':
                        if coluna[7] == 'Gold':
                            self.gold_medal.append(coluna)

    def process_data(self):
        """ This function process the input data from init_class. """
        self.init_class()

        country_gold_medal = {'SWE': 0, 'DEN': 0, 'NOR': 0}
        for country in self.gold_medal:
            if country[4] == 'SWE':
                country_gold_medal['SWE'] += 1
            if country[4] == 'DEN':
                country_gold_medal['DEN'] += 1
            if country[4] == 'NOR':
                country_gold_medal['NOR'] += 1
        self.total_medal = country_gold_medal

    def print_result(self):
        """
        This is a printer! It prints.
        """
        print('===' * 25, 'Questão 10'.center(75), '===' * 25, sep='\n')
        self.process_data()
        print('---' * 25,
              'O país com mais medalhas de ouro no século 21 nas modalidades Skiing,',
              'Curling, Skating, Ice Hockey foi a Noruega com {} medalhas.'.format(
                  self.total_medal['NOR']),
              '---' * 25, 'Aluno: Francisco Camello'.rjust(75), sep="\n")


Questao_10().print_result()
