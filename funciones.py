# -*- coding: utf-8 -*-
"""
Created on 07/10/2023
@author: Sergio Dominguez

"""
import pandas as pd
import numpy as np


def probabilidad_pertenecer_a_continente(df, nombre_continente):
    """
    genera print con % de probabilidad de pertenecer a un continente

    Args:
        dataframe (pd.DataFrame): DataFrame a consultar.
        nombre_continente (str): Nombre del continente.
        
    Returns:
        None

    formulas
    df['continent'].value_counts()[nombre_continente]
    df['continent'].value_counts().sum()
    """
        
    print(f"La probabilidad de pertenecer a {nombre_continente} equivale a: \
    {round((df['continent'].value_counts()[nombre_continente] / df['continent'].value_counts().sum()) *100,2)}%")
    
def probabilidad_continente_y_segundaronda(df, nombre_continente):
    """
    genera print con % de probabilidad de pertenecer a un continente y pasar a segunda ronda

    Args:
        dataframe (pd.DataFrame): DataFrame a consultar.
        nombre_continente (str): Nombre del continente.
        
    Returns:
        None

    Reglas de negocios
    condicion1 = df["continent"] == 'africa' -->  pertenecer a africa
    condicion2 = df['clasificado'] == 1      -->  clasificar a segunda ronda (1=si, 0=no)
    df.shape[0]    --> total de registros
    (condicion1 & condicion2).sum()/ df.shape[0]
    """
    condicion1 = df["continent"] == nombre_continente  # -->  pertenecer a continente
    condicion2 = df['clasificado'] == 1     #  -->  clasificar a segunda ronda (1=si, 0=no)
    probabilidad = (condicion1 & condicion2).sum()/df.shape[0] 

    print(f"La probabilidad de pertenecer a {nombre_continente} y pasar a segunda ronda equivale a: \
    {round(probabilidad * 100, 2)}%")  

def probabilidad_continente_o_segundaronda(df, nombre_continente):
    """
    genera print con % de probabilidad de pertenecer a un continente y pasar a segunda ronda

    Args:
        dataframe (pd.DataFrame): DataFrame a consultar.
        nombre_continente (str): Nombre del continente.
        
    Returns:
        None

    Reglas de negocios
    condicion1 = df["continent"] == 'africa' -->  pertenecer a africa
    condicion2 = df['clasificado'] == 1      -->  clasificar a segunda ronda (1=si, 0=no)
    df.shape[0]    --> total de registros
    (condicion1 & condicion2).sum()/ df.shape[0]
    """
    condicion1 = df["continent"] == nombre_continente  # -->  pertenecer a continente
    condicion2 = df['clasificado'] == 1     #  -->  clasificar a segunda ronda (1=si, 0=no)
    probabilidad = (condicion1 | condicion2).sum()/df.shape[0] 

    print(f"La probabilidad de pertenecer a {nombre_continente} o pasar a segunda ronda equivale a: \
    {round(probabilidad * 100, 2)}%")  


def probabilidad_continente_y_ganaralmenosunpartido(df, nombre_continente):
    """
    genera print con % de probabilidad de pertenecer a un continente y haber ganado al menos un partido

    Args:
        dataframe (pd.DataFrame): DataFrame a consultar.
        nombre_continente (str): Nombre del continente.
        
    Returns:
        None

    Reglas de negocios
    df["continent"] == nombre_continente  # -->  pertenecer a continente
    df['juegos_ganados'] > 0     #  -->  ganar al menos un partido
    df.shape[0]  --> total de registros
    probabilidad = (condicion1 & condicion2).sum()/df.shape[0] 
    
    """
    condicion1 = df["continent"] == nombre_continente  # -->  pertenecer a continente
    condicion2 = df['juegos_ganados'] > 0     #  -->  ganar al menos un partido
    probabilidad = (condicion1 & condicion2).sum()/df.shape[0] 

    print(f"La probabilidad de pertenecer a {nombre_continente} y haber ganado al menos un partido equivale a: \
    {round(probabilidad * 100, 2)}%")   


def probabilidad_AyB_probabilidad_B(condicion_A, condicion_B, total,descripcion):
    """
    genera print con % de probabilidad de pertenecer a un continente, si se sabe que clasificó

    Args:
        condicion_A: Pandas.Serie primera condicion para calcular la probabilidad
        condicion_B: Pandas.Serie segunda condicion para calcular la probabilidad
        total: pandas.serie con la cantidad total de registros.
        descripcion: se requiere para informar en el print, descripcion de la probabilidad calculada
        
    Returns:
        None

    
    """
        
    # probabilidades
    probabilidad_AyB=(condicion_A & condicion_B).sum() / total
    probabilidad_B=condicion_B.sum() / total
    # print con probabilidad final
    print(f"{descripcion}  \
    {round((probabilidad_AyB / probabilidad_B)*100, 2)}%")