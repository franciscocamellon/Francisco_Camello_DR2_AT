# -*- coding: utf-8 -*-
"""
/******************************* ASSESSMENT *********************************
*    Questao 11                                                            *
*        Aluno           : Francisco Alves Camello Neto                    *
*        Disciplina      : Fundamentos do Desenvolvimento Python           *
*        Professor       : Thaís do Nascimento Viana                       *
*        Nome do arquivo : questao_11.py                                   *
***************************************************************************/
"""

import pandas


class Questao_11():
    """ This function gets data about games from a CSV file given by a URL. """

    def __init__(self):
        """ Constructor. """
        self.url = 'https://sites.google.com/site/dr2fundamentospython/arquivos/Video_Games_Sales_as_at_22_Dec_2016.csv'
        self.dataframe = pandas.read_csv(self.url, sep=',')

    def init_class(self):
        """ This function receives the input data from users. """
        self.game_genre = self.dataframe[(self.dataframe['Genre'] == 'Action') | (
            self.dataframe['Genre'] == 'Shooter') | (self.dataframe['Genre'] == 'Platform')]
        self.biggest_sellers = self.dataframe.groupby(
            ['Publisher'])['Global_Sales'].sum().sort_values(ascending=False)
        self.japan_action = self.dataframe[(self.dataframe['Year_of_Release'] >= 2010) & (
            self.dataframe['Genre'] == 'Action')]
        self.japan_shooter = self.dataframe[(self.dataframe['Year_of_Release'] >= 2010) & (
            self.dataframe['Genre'] == 'Shooter')]
        self.japan_platform = self.dataframe[(self.dataframe['Year_of_Release'] >= 2010) & (
            self.dataframe['Genre'] == 'Platform')]
        self.sales_japan_action = self.dataframe[(
            self.dataframe['Year_of_Release'] >= 2010) & (self.dataframe['Genre'] == 'Action')]
        self.sales_japan_shooter = self.dataframe[(
            self.dataframe['Year_of_Release'] >= 2010) & (self.dataframe['Genre'] == 'Shooter')]
        self.sales_japan_platform = self.dataframe[(
            self.dataframe['Year_of_Release'] >= 2010) & (self.dataframe['Genre'] == 'Platform')]

    def process_data(self):
        """ This function process the input data from init_class. """
        self.init_class()

        self.game_genre_report = self.game_genre.groupby(
            ['Publisher'])['Publisher'].count().sort_values(ascending=False).head(3)

        self.biggest_sellers_report = self.biggest_sellers.head(3)

        self.ja_publisher = self.japan_action.groupby(
            ['Publisher'])['Publisher'].count().sort_values(ascending=False)

        self.js_publisher = self.japan_shooter.groupby(
            ['Publisher'])['Publisher'].count().sort_values(ascending=False)

        self.jp_publisher = self.japan_platform.groupby(
            ['Publisher'])['Publisher'].count().sort_values(ascending=False)

        self.ja_seller = self.sales_japan_action.groupby(
            ['Publisher'])['JP_Sales'].sum().sort_values(ascending=False)

        self.js_seller = self.sales_japan_shooter.groupby(
            ['Publisher'])['JP_Sales'].sum().sort_values(ascending=False)

        self.jp_seller = self.sales_japan_platform.groupby(
            ['Publisher'])['JP_Sales'].sum().sort_values(ascending=False)

    def print_result(self):
        """ This is a printer! It prints. """
        print('===' * 25, 'Questão 11'.center(75), '===' * 25, sep='\n')
        self.process_data()
        print(
            'Informações sobre jogos do gênero de ação (Action), tiro (Shooter) e \nplataforma (Platform)',
            'Marcas que mais publicaram jogos:\n{}'.format(
                self.game_genre_report),
            '---' * 25,
            'Três maiores vendedores de jogos:\n{}'.format(
                self.biggest_sellers_report),
            '---' * 25,
            'Marca com mais publicações no gênero action:\n{}'.format(
                self.ja_publisher.head(1)),
            '---' * 25,
            'Marca com mais publicações no gênero shooter:\n{}'.format(
                self.js_publisher.head(1)),
            '---' * 25,
            'Marca com mais publicações no gênero platform:\n{}'.format(
                self.jp_publisher.head(1)),
            '---' * 25,
            'Marca que mais vendeu no gênero action nos ultimos 10 anos:\n{}'.format(
                self.ja_seller.head(1)),
            '---' * 25,
            'Marca que mais vendeu no gênero shooter nos ultimos 10 anos:\n{}'.format(
                self.js_seller.head(1)),
            '---' * 25,
            'Marca que mais vendeu no gênero platform nos ultimos 10 anos:\n{}'.format(
                self.jp_seller.head(1)),
            '---' * 25, sep="\n")


Questao_11().print_result()
