import requests
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st
from math import ceil
from datetime import date
from streamlit_dynamic_filters import DynamicFilters
import urllib.request
from PIL import Image
import time
from dplython import (DplyFrame, X, diamonds, select, sift, sample_n, sample_frac, head, arrange, mutate, group_by,
                      summarize, DelayFunction)
from itables.streamlit import interactive_table
from itables import to_html_datatable
from streamlit.components.v1 import html
from plotly.subplots import make_subplots
from euroleague_api.play_by_play_data import PlayByPlay
from datetime import datetime
import pytz

st.set_page_config(layout='wide', page_title="Play by play analysis", page_icon="🏀")
def download_image(url, save_as):
    urllib.request.urlretrieve(url, save_as)

download_image('https://raw.githubusercontent.com/sotiristiga/Euroleague_dash/refs/heads/main/eurologo.png','eurologo.png')
st.image(Image.open("eurologo.png"),width=100)

st.sidebar.write("If an error message appears, please refresh the page")
st.write("## Euroleague stats from 2017 to present")

def fixture_format1(Fixture):
    if Fixture <= 15:
        return "First Round"
    elif Fixture > 15 and Fixture <= 30:
        return "Second Round"
    elif Fixture == 31:
        return "PO 1"
    elif Fixture == 32:
        return "PO 2"
    elif Fixture == 33:
        return "PO 3"
    elif Fixture == 34:
        return "PO 4"
    elif Fixture == 35:
        return "PO 5"
    elif Fixture == 36:
        return "Semi Final"
    elif Fixture == 37:
        return "Third Place"
    elif Fixture == 38:
        return "Final"


def fixture_format2(Fixture):
    if Fixture <= 15:
        return "First Round"
    elif Fixture > 15 and Fixture <= 30:
        return "Second Round"
    elif Fixture == 31:
        return "PO 1"
    elif Fixture == 32:
        return "PO 2"
    elif Fixture == 33:
        return "PO 3"
    elif Fixture == 34:
        return "PO 4"
    elif Fixture == 35:
        return "Semi Final"
    elif Fixture == 36:
        return "Third Place"
    elif Fixture == 37:
        return "Final"


def fixture_format3(Fixture):
    if Fixture <= 17:
        return "First Round"
    elif Fixture > 17 and Fixture <= 34:
        return "Second Round"


def fixture_format4(Fixture):
    if Fixture <= 17:
        return "First Round"
    elif Fixture > 17 and Fixture <= 34:
        return "Second Round"
    elif Fixture == 35:
        return "PO 1"
    elif Fixture == 36:
        return "PO 2"
    elif Fixture == 37:
        return "PO 3"
    elif Fixture == 38:
        return "PO 4"
    elif Fixture == 39:
        return "PO 5"
    elif Fixture == 40:
        return "Semi Final"
    elif Fixture == 41:
        return "Third Place"
    elif Fixture == 42:
        return "Final"


def team_coach(Team,Fixture):
    if Team=='PAN':
        return 'E. Ataman'
    if Team=='OLY':
        return 'G. Bartzokas'
    if Team=='PRB':
        return 'T. Splitter'
    if Team=='FEN':
        return 'S. Jaskevicius'
    if Team=='EFE':
        if Fixture <=19:
            return 'T. Mijatović'
        else:
            return 'L. Bianchi'
    if Team=='CRV':
        return 'I. Sfairopoulos'
    if Team=='BAY':
        return 'G. Herbert'
    if Team=='RMB':
        return 'C. Mateo'
    if Team=='BAR':
        return 'J. Penarroya'
    if Team=='ZAL':
        return 'A. Trinkieri'
    if Team=='MIL':
        return 'E. Messina'
    if Team=='BAS':
        return 'P. Laso'
    if Team=='PAR':
        return 'Z. Obradovic'
    if Team=='VIL':
        return 'P. Poupet'
    if Team=='MAC':
        return 'O. Kattash'
    if Team=='BER':
        return 'I. Gonzalez'
    if Team=='ASM':
        if Fixture<=11:
            return 'S. Obradovic'
        else:
            return 'V. Spanoulis'
    if Team == 'BOL':
        if Fixture <= 14:
            return 'L. Bianchi'
        else:
            return 'D. Ivanovic'





def fixture_format5(Fixture):
    if Fixture <= 17:
        return "First Round"
    elif Fixture > 17 and Fixture <= 34:
        return "Second Round"
    elif Fixture == 35:
        return "PI 1"
    elif Fixture == 36:
        return "PI 2"
    elif Fixture == 37:
        return "PO 1"
    elif Fixture == 38:
        return "PO 2"
    elif Fixture == 39:
        return "PO 3"
    elif Fixture == 40:
        return "PO 4"
    elif Fixture == 41:
        return "PO 5"
    elif Fixture == 42:
        return "Semi Final"
    elif Fixture == 43:
        return "Third Place"
    elif Fixture == 44:
        return "Final"


euroleague_2016_2017_playerstats=pd.read_csv(f"https://raw.githubusercontent.com/sotiristiga/euroleague/main/euroleague_2016_2017_playerstats.csv")
euroleague_2016_2017_playerstats['idseason']=euroleague_2016_2017_playerstats['IDGAME'] + "_" + euroleague_2016_2017_playerstats['Season']
euroleague_2016_2017_playerstats[['Fixture', 'Game']] = euroleague_2016_2017_playerstats['IDGAME'].str.split('_', n=1, expand=True)
euroleague_2016_2017_playerstats['Fixture']=pd.to_numeric(euroleague_2016_2017_playerstats['Fixture'])
euroleague_2016_2017_playerstats['Round']=euroleague_2016_2017_playerstats['Fixture'].apply(fixture_format1)


euroleague_2017_2018_playerstats=pd.read_csv(f"https://raw.githubusercontent.com/sotiristiga/euroleague/main/euroleague_2017_2018_playerstats.csv")
euroleague_2017_2018_playerstats['idseason']=euroleague_2017_2018_playerstats['IDGAME'] + "_" + euroleague_2017_2018_playerstats['Season']
euroleague_2017_2018_playerstats[['Fixture', 'Game']] = euroleague_2017_2018_playerstats['IDGAME'].str.split('_', n=1, expand=True)
euroleague_2017_2018_playerstats['Fixture']=pd.to_numeric(euroleague_2017_2018_playerstats['Fixture'])
euroleague_2017_2018_playerstats['Round']=euroleague_2017_2018_playerstats['Fixture'].apply(fixture_format2)


euroleague_2018_2019_playerstats=pd.read_csv(f"https://raw.githubusercontent.com/sotiristiga/euroleague/main/euroleague_2018_2019_playerstats.csv")
euroleague_2018_2019_playerstats['idseason']=euroleague_2018_2019_playerstats['IDGAME'] + "_" + euroleague_2018_2019_playerstats['Season']
euroleague_2018_2019_playerstats[['Fixture', 'Game']] = euroleague_2018_2019_playerstats['IDGAME'].str.split('_', n=1, expand=True)
euroleague_2018_2019_playerstats['Fixture']=pd.to_numeric(euroleague_2018_2019_playerstats['Fixture'])
euroleague_2018_2019_playerstats['Round']=euroleague_2018_2019_playerstats['Fixture'].apply(fixture_format1)


euroleague_2019_2020_playerstats=pd.read_csv(f"https://raw.githubusercontent.com/sotiristiga/euroleague/main/euroleague_2019_2020_playerstats.csv")
euroleague_2019_2020_playerstats['idseason']=euroleague_2019_2020_playerstats['IDGAME'] + "_" + euroleague_2019_2020_playerstats['Season']
euroleague_2019_2020_playerstats[['Fixture', 'Game']] = euroleague_2019_2020_playerstats['IDGAME'].str.split('_', n=1, expand=True)
euroleague_2019_2020_playerstats['Fixture']=pd.to_numeric(euroleague_2019_2020_playerstats['Fixture'])
euroleague_2019_2020_playerstats['Round']=euroleague_2019_2020_playerstats['Fixture'].apply(fixture_format3)


euroleague_2020_2021_playerstats=pd.read_csv(f"https://raw.githubusercontent.com/sotiristiga/euroleague/main/euroleague_2020_2021_playerstats.csv")
euroleague_2020_2021_playerstats['idseason']=euroleague_2020_2021_playerstats['IDGAME'] + "_" + euroleague_2020_2021_playerstats['Season']
euroleague_2020_2021_playerstats[['Fixture', 'Game']] = euroleague_2020_2021_playerstats['IDGAME'].str.split('_', n=1, expand=True)
euroleague_2020_2021_playerstats['Fixture']=pd.to_numeric(euroleague_2020_2021_playerstats['Fixture'])
euroleague_2020_2021_playerstats['Round']=euroleague_2020_2021_playerstats['Fixture'].apply(fixture_format4)

euroleague_2021_2022_playerstats=pd.read_csv(f"https://raw.githubusercontent.com/sotiristiga/euroleague/main/euroleague_2021_2022_playerstats.csv")
euroleague_2021_2022_playerstats['idseason']=euroleague_2021_2022_playerstats['IDGAME'] + "_" + euroleague_2021_2022_playerstats['Season']
euroleague_2021_2022_playerstats[['Fixture', 'Game']] = euroleague_2021_2022_playerstats['IDGAME'].str.split('_', n=1, expand=True)
euroleague_2021_2022_playerstats['Fixture']=pd.to_numeric(euroleague_2021_2022_playerstats['Fixture'])
euroleague_2021_2022_playerstats['Round']=euroleague_2021_2022_playerstats['Fixture'].apply(fixture_format4)


euroleague_2022_2023_playerstats=pd.read_csv(f"https://raw.githubusercontent.com/sotiristiga/euroleague/main/euroleague_2022_2023_playerstats.csv")
euroleague_2022_2023_playerstats['idseason']=euroleague_2022_2023_playerstats['IDGAME'] + "_" + euroleague_2022_2023_playerstats['Season']
euroleague_2022_2023_playerstats[['Fixture', 'Game']] = euroleague_2022_2023_playerstats['IDGAME'].str.split('_', n=1, expand=True)
euroleague_2022_2023_playerstats['Fixture']=pd.to_numeric(euroleague_2022_2023_playerstats['Fixture'])
euroleague_2022_2023_playerstats['Round']=euroleague_2022_2023_playerstats['Fixture'].apply(fixture_format4)

euroleague_2023_2024_playerstats=pd.read_csv(f"https://raw.githubusercontent.com/sotiristiga/euroleague/main/euroleague_2023_2024_playerstats.csv")
euroleague_2023_2024_playerstats['idseason']=euroleague_2023_2024_playerstats['IDGAME'] + "_" + euroleague_2023_2024_playerstats['Season']
euroleague_2023_2024_playerstats[['Fixture', 'Game']] = euroleague_2023_2024_playerstats['IDGAME'].str.split('_', n=1, expand=True)
euroleague_2023_2024_playerstats['Fixture']=pd.to_numeric(euroleague_2023_2024_playerstats['Fixture'])
euroleague_2023_2024_playerstats['Round']=euroleague_2023_2024_playerstats['Fixture'].apply(fixture_format5)

euroleague_2024_2025_playerstats=pd.read_csv(f"https://raw.githubusercontent.com/sotiristiga/euroleague/main/euroleague_2024_2025_playerstats.csv")
euroleague_2024_2025_playerstats['idseason']=euroleague_2024_2025_playerstats['IDGAME'] + "_" + euroleague_2024_2025_playerstats['Season']
euroleague_2024_2025_playerstats[['Fixture', 'Game']] = euroleague_2024_2025_playerstats['IDGAME'].str.split('_', n=1, expand=True)
euroleague_2024_2025_playerstats['Fixture_Team_Season']=euroleague_2024_2025_playerstats['Fixture']+"_"+euroleague_2024_2025_playerstats['Team']+"_"+euroleague_2024_2025_playerstats['Season']
euroleague_2024_2025_playerstats['Fixture']=pd.to_numeric(euroleague_2024_2025_playerstats['Fixture'])

euroleague_2024_2025_playerstats['Round']=euroleague_2024_2025_playerstats['Fixture'].apply(fixture_format5)



euroleague_2016_2017_results=pd.read_csv(f"https://raw.githubusercontent.com/sotiristiga/euroleague/main/euroleague_2016_2017_results.csv")
euroleague_2016_2017_results['idseason']=euroleague_2016_2017_results['IDGAME'] + "_" + euroleague_2016_2017_results['Season']
euroleague_2016_2017_results[['Fixture', 'Game']] = euroleague_2016_2017_results['IDGAME'].str.split('_', n=1, expand=True)
euroleague_2016_2017_results['Fixture']=pd.to_numeric(euroleague_2016_2017_results['Fixture'])
euroleague_2016_2017_results['Round']=euroleague_2016_2017_results['Fixture'].apply(fixture_format1)


euroleague_2017_2018_results=pd.read_csv(f"https://raw.githubusercontent.com/sotiristiga/euroleague/main/euroleague_2017_2018_results.csv")
euroleague_2017_2018_results['idseason']=euroleague_2017_2018_results['IDGAME'] + "_" + euroleague_2017_2018_results['Season']
euroleague_2017_2018_results[['Fixture', 'Game']] = euroleague_2017_2018_results['IDGAME'].str.split('_', n=1, expand=True)
euroleague_2017_2018_results['Fixture']=pd.to_numeric(euroleague_2017_2018_results['Fixture'])
euroleague_2017_2018_results['Round']=euroleague_2017_2018_results['Fixture'].apply(fixture_format2)


euroleague_2018_2019_results=pd.read_csv(f"https://raw.githubusercontent.com/sotiristiga/euroleague/main/euroleague_2018_2019_results.csv")
euroleague_2018_2019_results['idseason']=euroleague_2018_2019_results['IDGAME'] + "_" + euroleague_2018_2019_results['Season']
euroleague_2018_2019_results[['Fixture', 'Game']] = euroleague_2018_2019_results['IDGAME'].str.split('_', n=1, expand=True)
euroleague_2018_2019_results['Fixture']=pd.to_numeric(euroleague_2018_2019_results['Fixture'])
euroleague_2018_2019_results['Round']=euroleague_2018_2019_results['Fixture'].apply(fixture_format1)


euroleague_2019_2020_results=pd.read_csv(f"https://raw.githubusercontent.com/sotiristiga/euroleague/main/euroleague_2019_2020_results.csv")
euroleague_2019_2020_results['idseason']=euroleague_2019_2020_results['IDGAME'] + "_" + euroleague_2019_2020_results['Season']
euroleague_2019_2020_results[['Fixture', 'Game']] = euroleague_2019_2020_results['IDGAME'].str.split('_', n=1, expand=True)
euroleague_2019_2020_results['Fixture']=pd.to_numeric(euroleague_2019_2020_results['Fixture'])
euroleague_2019_2020_results['Round']=euroleague_2019_2020_results['Fixture'].apply(fixture_format3)


euroleague_2020_2021_results=pd.read_csv(f"https://raw.githubusercontent.com/sotiristiga/euroleague/main/euroleague_2020_2021_results.csv")
euroleague_2020_2021_results['idseason']=euroleague_2020_2021_results['IDGAME'] + "_" + euroleague_2020_2021_results['Season']
euroleague_2020_2021_results[['Fixture', 'Game']] = euroleague_2020_2021_results['IDGAME'].str.split('_', n=1, expand=True)
euroleague_2020_2021_results['Fixture']=pd.to_numeric(euroleague_2020_2021_results['Fixture'])
euroleague_2020_2021_results['Round']=euroleague_2020_2021_results['Fixture'].apply(fixture_format4)

euroleague_2021_2022_results=pd.read_csv(f"https://raw.githubusercontent.com/sotiristiga/euroleague/main/euroleague_2021_2022_results.csv")
euroleague_2021_2022_results['idseason']=euroleague_2021_2022_results['IDGAME'] + "_" + euroleague_2021_2022_results['Season']
euroleague_2021_2022_results[['Fixture', 'Game']] = euroleague_2021_2022_results['IDGAME'].str.split('_', n=1, expand=True)
euroleague_2021_2022_results['Fixture']=pd.to_numeric(euroleague_2021_2022_results['Fixture'])
euroleague_2021_2022_results['Round']=euroleague_2021_2022_results['Fixture'].apply(fixture_format4)


euroleague_2022_2023_results=pd.read_csv(f"https://raw.githubusercontent.com/sotiristiga/euroleague/main/euroleague_2022_2023_results.csv")
euroleague_2022_2023_results['idseason']=euroleague_2022_2023_results['IDGAME'] + "_" + euroleague_2022_2023_results['Season']
euroleague_2022_2023_results[['Fixture', 'Game']] = euroleague_2022_2023_results['IDGAME'].str.split('_', n=1, expand=True)
euroleague_2022_2023_results['Fixture']=pd.to_numeric(euroleague_2022_2023_results['Fixture'])
euroleague_2022_2023_results['Round']=euroleague_2022_2023_results['Fixture'].apply(fixture_format4)

euroleague_2023_2024_results=pd.read_csv(f"https://raw.githubusercontent.com/sotiristiga/euroleague/main/euroleague_2023_2024_results.csv")
euroleague_2023_2024_results['idseason']=euroleague_2023_2024_results['IDGAME'] + "_" + euroleague_2023_2024_results['Season']
euroleague_2023_2024_results[['Fixture', 'Game']] = euroleague_2023_2024_results['IDGAME'].str.split('_', n=1, expand=True)
euroleague_2023_2024_results['Fixture']=pd.to_numeric(euroleague_2023_2024_results['Fixture'])
euroleague_2023_2024_results['Round']=euroleague_2023_2024_results['Fixture'].apply(fixture_format5)

euroleague_2024_2025_results=pd.read_csv(f"https://raw.githubusercontent.com/sotiristiga/euroleague/main/euroleague_2024_2025_results.csv")
euroleague_2024_2025_results['idseason']=euroleague_2024_2025_results['IDGAME'] + "_" + euroleague_2024_2025_results['Season']
euroleague_2024_2025_results[['Fixture', 'Game']] = euroleague_2024_2025_results['IDGAME'].str.split('_', n=1, expand=True)

euroleague_2024_2025_results['Fixture']=pd.to_numeric(euroleague_2024_2025_results['Fixture'])
euroleague_2024_2025_results['Round']=euroleague_2024_2025_results['Fixture'].apply(fixture_format5)



All_Seasons=pd.concat([euroleague_2016_2017_playerstats,euroleague_2017_2018_playerstats,euroleague_2018_2019_playerstats,euroleague_2019_2020_playerstats,euroleague_2020_2021_playerstats,euroleague_2021_2022_playerstats,euroleague_2022_2023_playerstats,euroleague_2023_2024_playerstats,euroleague_2024_2025_playerstats])

All_Seasons_results=pd.concat([euroleague_2016_2017_results,euroleague_2017_2018_results,euroleague_2018_2019_results,euroleague_2019_2020_results,euroleague_2020_2021_results,euroleague_2021_2022_results,euroleague_2022_2023_results,euroleague_2023_2024_results,euroleague_2024_2025_results])



def games_format(HA, Fixture, Season, Team, Against):
    if HA == "H":
        return Fixture + " / " + Season + ' / ' + Team + ' - ' + Against
    elif HA == "A":
        return Fixture + " / " + Season + ' / ' + Against + ' - ' + Team


def result_format(Win):
    if Win == 1:
        return "W"
    elif Win == 0:
        return "L"


def period_win_format(S, C):
    if S > C:
        return 1
    else:
        return 0


def result_format(Win):
    if Win == 1:
        return "W"
    elif Win == 0:
        return "L"


def period_win_res_win_format(S, C, result):
    if S > C and result == "W":
        return 1
    else:
        return 0



def phase_format(ph):
    if ph=="RS":
        return 'Regular Season'
    elif ph=='PI':
        return 'Play In'
    elif ph=='PO':
        return 'Play offs'
    elif ph=='FF':
        return 'Final Four'

def market_format(marker,info):
    if info=="Begin Period":
        return '10:00'
    elif info=="End Period" or info=="End Game":
        return '00:00'
    else:
        return marker
def time_format(timer):
    if timer.startswith("0"):
        return timer.replace("0",'')
    else:
        return timer

def attack_team(team1,team2,sit):
    if sit.filter(regex='JB|O|D|TOUT|'):
        return team1
    elif sit.filter(regex='2FGA|D|ST|3FGM|CM|TO|3FGA|RV|FTM|'):
        return team2

def points_scored(sit):
    if sit=='2FGM':
        return 2
    elif sit=='3FGM':
        return 3
    elif sit=='FTM':
        return 1
    else:
        return 0

home_team=(All_Seasons_results[['Fixture',"Phase","Home","Away","Home_Points","Away_Points",
                                "Q1H","Q2H","Q3H","Q4H",'EXH',"Q1A","Q2A","Q3A","Q4A",'EXA','Season','Round','Home_win','idseason']]
           .rename(columns={"Home":'Team',"Away":'Against',"Home_Points":'Scored',"Away_Points":"Conceed",
                                "Q1H":'P1S',"Q2H":'P2S',"Q3H":'P3S',"Q4H":'P4S','EXH':'EXS',"Q1A":'P1C',
                            "Q2A":'P2C',"Q3A":'P3C',"Q4A":'P4C','EXA':'EXC','Home_win':'Win'}))

home_team['HA']="H"
away_team=(All_Seasons_results[['Fixture',"Phase","Home","Away","Home_Points","Away_Points",
                                "Q1H","Q2H","Q3H","Q4H",'EXH',"Q1A","Q2A","Q3A","Q4A",'EXA','Season','Round','Away_win','idseason']]
           .rename(columns={"Home":'Against',"Away":'Team',"Home_Points":'Conceed',"Away_Points":"Scored",
                                "Q1H":'P1C',"Q2H":'P2C',"Q3H":'P3C',"Q4H":'P4C','EXH':'EXC',"Q1A":'P1S',
                            "Q2A":'P2S',"Q3A":'P3S',"Q4A":'P4S','EXA':'EXS','Away_win':'Win'}))
away_team['HA']="A"

period_points=pd.concat([home_team,away_team])

period_points["FHS"]=period_points["P1S"]+period_points["P2S"]
period_points["FHC"]=period_points["P1C"]+period_points["P2C"]
period_points["SHS"]=period_points["P3S"]+period_points["P4S"]
period_points["SHC"]=period_points["P3C"]+period_points["P4C"]
period_points["results"]=period_points["Win"].apply(result_format)
period_points['EXS'].replace(0, np.nan, inplace=True)
period_points['EXC'].replace(0, np.nan, inplace=True)

total_period_points=period_points.loc[period_points.Season=="2024-2025"].groupby('Team')[['P1S','P2S','P3S','P4S','EXS']].sum().reset_index().rename(columns={'P1S':'p1_PTS',
                                                                                                                       'P2S':'p2_PTS',
                                                                                                                       'P3S':'p3_PTS',
                                                                                                                       'P4S':'p4_PTS',
                                                                                                                       'EXS':'ex_PTS'})
mean_period_points=period_points.loc[period_points.Season=="2024-2025"].groupby('Team')[['P1S','P2S','P3S','P4S']].mean().reset_index().rename(columns={'P1S':'p1_PTS_avg',
                                                                                                                       'P2S':'p2_PTS_avg',
                                                                                                                       'P3S':'p3_PTS_avg',
                                                                                                                       'P4S':'p4_PTS_avg'})

total_period_points_against=period_points.loc[period_points.Season=="2024-2025"].groupby('Team')[['P1C','P2C','P3C','P4C','EXC']].sum().reset_index().rename(columns={'P1C':'p1_PTS',
                                                                                                                       'P2C':'p2_PTS',
                                                                                                                       'P3C':'p3_PTS',
                                                                                                                       'P4C':'p4_PTS',
                                                                                                                       'EXC':'ex_PTS'})
mean_period_points_against=period_points.loc[period_points.Season=="2024-2025"].groupby('Team')[['P1C','P2C','P3C','P4C']].mean().reset_index().rename(columns={'P1C':'p1_PTS_avg',
                                                                                                                       'P2C':'p2_PTS_avg',
                                                                                                                       'P3C':'p3_PTS_avg',
                                                                                                                       'P4C':'p4_PTS_avg'})
team_period_stats=pd.merge(total_period_points,mean_period_points)
team_period_stats_against=pd.merge(total_period_points_against,mean_period_points_against).rename(columns={'Team':'Against'})
extra_details=euroleague_2024_2025_playerstats.groupby(['Fixture_Team_Season','Against'])['Player'].count().reset_index()
extra_details=extra_details.drop('Player',axis=1)

pbp_data_df2425=pd.read_csv(f"https://raw.githubusercontent.com/sotiristiga/ts.portofolio/refs/heads/main/pbp_data_df2425.csv")

pbp_data_df2425=pbp_data_df2425.rename(columns={'Round':'Fixture','CODETEAM':'Team'})
pbp_data_df2425['Fixture']=pd.to_numeric(pbp_data_df2425['Fixture'])
pbp_data_df2425['Season']=pbp_data_df2425['Season'].astype(str)+"-"+(pbp_data_df2425['Season']+1).astype(str)
pbp_data_df2425['Phase']=pbp_data_df2425['Phase'].apply(phase_format)
pbp_data_df2425['Team']=pbp_data_df2425['Team'].str.replace('MCO','ASM')
pbp_data_df2425['Team']=pbp_data_df2425['Team'].str.replace('ASV','VIL')
pbp_data_df2425['Team']=pbp_data_df2425['Team'].str.replace('MAD','RMB')
pbp_data_df2425['Team']=pbp_data_df2425['Team'].str.replace('MUN','BAY')
pbp_data_df2425['Team']=pbp_data_df2425['Team'].str.replace('TEL','MAC')
pbp_data_df2425['Team']=pbp_data_df2425['Team'].str.replace('ULK','FEN')
pbp_data_df2425['Team']=pbp_data_df2425['Team'].str.replace('RED','CRV')
pbp_data_df2425['Team']=pbp_data_df2425['Team'].str.replace('PRS','PRB')
pbp_data_df2425['Team']=pbp_data_df2425['Team'].str.replace('VIR','BOL')
pbp_data_df2425['Team']=pbp_data_df2425['Team'].str.replace('IST','EFE')
pbp_data_df2425['PLAYTYPE']=pbp_data_df2425['PLAYTYPE'].str.replace(' ','')
pbp_data_df2425['GAMECODE']=pbp_data_df2425['Fixture'].astype(str)+"_"+pbp_data_df2425['Gamecode'].astype(str)
pbp_data_df2425[['Last Name', 'First Name']] = pbp_data_df2425['PLAYER'].str.split(', ', expand=True)

pbp_data_df2425['First Name']=pbp_data_df2425['First Name'].str.upper().str.title()
pbp_data_df2425['Last Name']=pbp_data_df2425['Last Name'].str.upper().str.title()
pbp_data_df2425['Player']=pbp_data_df2425['First Name']+" "+pbp_data_df2425['Last Name']
pbp_data_df2425['Fixture_Team_Season']=pbp_data_df2425['Fixture'].astype(str)+"_"+pbp_data_df2425['Team']+"_"+pbp_data_df2425['Season']

pbp_data_df2425['MARKERTIME']=pbp_data_df2425.apply(lambda x: market_format(x['MARKERTIME'],x['PLAYINFO']),axis=1)
pbp_data_df2425[['MINUTEN', 'SECONDS1']] = pbp_data_df2425['MARKERTIME'].str.split(':', expand=True)
pbp_data_df2425['SECONDS1']=pbp_data_df2425['SECONDS1'].str.replace(' ','')
pbp_data_df2425['MINUTEN']=pd.to_numeric(pbp_data_df2425['MINUTEN'].apply(time_format))
pbp_data_df2425['SECONDS1']=pd.to_numeric(pbp_data_df2425['SECONDS1'].apply(time_format))
pbp_data_df2425['SECONDS1']=pbp_data_df2425['SECONDS1'].replace(np.nan,0)
pbp_data_df2425['MINUTEN']=pbp_data_df2425['MINUTEN'].replace(np.nan,0)
pbp_data_df2425['PLAYTYPE']=pbp_data_df2425['PLAYTYPE'].replace('CMTI','CM')
pbp_data_df2425['SECONDS']=pbp_data_df2425['MINUTEN']*60+pbp_data_df2425['SECONDS1']
pbp_data_df2425['SECONDS_diff']=-pbp_data_df2425['SECONDS'].diff()

pbp_data_df2425=pd.merge(pbp_data_df2425,extra_details).sort_values(['Fixture','GAMECODE','NUMBEROFPLAY'])


pbp_data_2425=pbp_data_df2425[['GAMECODE','Season','Phase','Fixture','PERIOD','MINUTE','MARKERTIME','Team','Player','PLAYTYPE','Against']]
coachtimeout=pbp_data_2425.loc[(pbp_data_2425['PLAYTYPE']=='TOUT')]
coachtimeout['Coach']=coachtimeout.apply(lambda x: team_coach(x['Team'],x['Fixture']),axis=1)
coachtimeout['Against Coach']=coachtimeout.apply(lambda x: team_coach(x['Against'],x['Fixture']),axis=1)
tfouls=pbp_data_2425.loc[(pbp_data_2425['PLAYTYPE'].isin(['C','B','CMT']))]
tfouls['Coach']=tfouls.apply(lambda x: team_coach(x['Team'],x['Fixture']),axis=1)
team_rebounds=pbp_data_2425.loc[(pbp_data_2425['PLAYTYPE'].isin(['O','D']))]
team_turnovers=pbp_data_2425.loc[(pbp_data_2425['PLAYTYPE']=='TO')]




team_timeouts_pergame=coachtimeout[['Team','Fixture']].value_counts().reset_index().groupby('Team')['count'].mean().reset_index()
coach_timeouts_pergame=coachtimeout[['Coach','Fixture']].value_counts().reset_index().groupby('Coach')['count'].mean().reset_index().round(1)
against_coach_timeouts_pergame=coachtimeout[['Against Coach','Fixture']].value_counts().reset_index().groupby('Against Coach')['count'].mean().reset_index().round(1)
timeouts_perperiod=coachtimeout[['Team','Fixture','PERIOD']].value_counts().reset_index().groupby(['Team','PERIOD'])['count'].mean().reset_index()
team_technical_fouls=tfouls['Team'].value_counts().reset_index()
against_team_technical_fouls=tfouls['Against'].value_counts().reset_index()
st.sidebar.markdown('''
  * ## [Filters](#filters)
  * ## [Average Team Stats](#average-team-stats)
  * ## [Average Opponent Stats](#average-opponent-stats)
  * ## [Player Stats](#player-stats)

''', unsafe_allow_html=True)
st.header("Filters")

col1,col2=st.columns(2)
with col1:
    search_team_team1=st.selectbox("Choose Team:",pbp_data_df2425['Team'].reset_index().sort_values('Team')['Team'].unique())
with col2:
    stat_choose=st.selectbox("Choose Stat:",['PTS','AS',"DR","OR","TR","TO","STL","BLKM","BLKR","DF","OF","TF","UNF","RF"])
timeouts_perminute=coachtimeout[['Team','MINUTE','PERIOD']].value_counts().reset_index().groupby(['Team','PERIOD'])['count'].mean().reset_index()
total_technical=tfouls['Team'].value_counts()
total_technical_bytype=tfouls[['Team','PLAYTYPE']].value_counts()
games=euroleague_2024_2025_playerstats.loc[euroleague_2024_2025_playerstats.Team==search_team_team1][['Player']].value_counts().reset_index().rename(columns={'count':'Games'})
games['Player']=games['Player'].replace("    "," ")
games['Player']=games['Player'].replace("   "," ")
games['Player']=games['Player'].str.replace("  "," ")
games['Player']=games['Player'].str.replace("  "," ")
games['Player']=games['Player'].str.replace("Juan Hernangomez","Juancho Hernangomez")
games['Player']=games['Player'].str.replace("Samontourov","Samodurov")
games['Player']=games['Player'].str.replace("Mouhammadou Jaiteh","Mam Jaiteh")
games['Player']=games['Player'].str.replace("Alejandro Abrines","Alex Abrines")
games['Player']=games['Player'].str.replace("Nikos Rogkavopoulos","Nikolaos Rogkavopoulos")
games['Player']=games['Player'].str.replace("Oscar da Silva","Oscar Da Silva")
games['Player']=games['Player'].str.replace("Yannick Wetzell","Yanni Wetzell")
games['Player']=games['Player'].str.replace("William McDowell-White","Will Mcdowell-White")
games['Player']=games['Player'].str.replace("David McCormack","David Mccormack")
games['Player']=games['Player'].str.replace("David Mc Cormack","David Mccormack")
games['Player']=games['Player'].str.replace("David Mc Cormack","David Mccormack")
games['Player']=games['Player'].str.replace("Yago Mateus dos Santos","Yago Dos Santos")
games['Player']=games['Player'].str.replace("David DeJulius","David De Julius")
games['Player']=games['Player'].str.replace("Will Rayman","William Rayman")
games['Player']=games['Player'].str.replace("Aleksandr Vezenkov","Sasha Vezenkov")
pbp_data_df2425['Player']=pbp_data_df2425['Player'].str.replace("David Mc Cormack","David Mccormack")
pbp_data_df2425['Player']=pbp_data_df2425['Player'].str.replace("Trevion Williams ","Trevion Williams")
pbp_data_df2425['Player']=pbp_data_df2425['Player'].str.replace("John Brown Iii","John Brown III")
pbp_data_df2425['Player']=pbp_data_df2425['Player'].str.replace("Codi Miller-Mcintyre","Codi Miller-McIntyre")
pbp_data_df2425['Player']=pbp_data_df2425['Player'].str.replace("Dan Oturu","Daniel Oturu")
pbp_data_df2425['Player']=pbp_data_df2425['Player'].str.replace("Perry Dozier Jr","P.J. Dozier")
pbp_data_df2425['Player']=pbp_data_df2425['Player'].str.replace("Errick Mccollum","Errick McCollum")
pbp_data_df2425['Player']=pbp_data_df2425['Player'].str.replace("Wade Baldwin Iv","Wade Baldwin IV")
pbp_data_df2425['Player']=pbp_data_df2425['Player'].str.replace("David Dejulius","David De Julius")
pbp_data_df2425['Player']=pbp_data_df2425['Player'].str.replace("Rafi Menco","Rafael Menco")
pbp_data_df2425['Player']=pbp_data_df2425['Player'].str.replace("Neno Dimitrijevic","Nenad Dimitrijevic")
pbp_data_df2425['Player']=pbp_data_df2425['Player'].str.replace("Zach Leday","Zach LeDay")
pbp_data_df2425['Player']=pbp_data_df2425['Player'].str.replace("Shaquielle Mckissic","Shaquielle McKissic")
team_games=(euroleague_2024_2025_playerstats.loc[euroleague_2024_2025_playerstats.Team==search_team_team1][['Team','idseason']]
            .value_counts().reset_index()[['Team','idseason']].value_counts().reset_index()
            .groupby('Team')['count'].sum().reset_index().rename(columns={'count':'Games'}))
st.header("Average Team Stats")
points_compute_total=pbp_data_df2425.loc[pbp_data_df2425.PLAYTYPE.isin(['2FGM','3FGM','FTM'])][['Team','PLAYTYPE','Player','PERIOD']].value_counts().reset_index()
points_compute_total['PTS']=points_compute_total['PLAYTYPE'].apply(points_scored)*points_compute_total['count']
player_points_by_period=points_compute_total.groupby(['Player','PERIOD'])['PTS'].sum().reset_index()



team_period_stats=team_period_stats.loc[team_period_stats.Team==search_team_team1]


team_period_all_Stats=pd.merge(team_period_stats,team_games).round(1)


assists_compute_total=pbp_data_df2425.loc[pbp_data_df2425.PLAYTYPE=='AS'][['Team','PERIOD']].value_counts().reset_index().rename(columns={'count':'AS'}).fillna(0)
sel_team_assists_compute_total=assists_compute_total.loc[assists_compute_total.Team==search_team_team1]
p1_sel_team_assists_compute_total=sel_team_assists_compute_total.loc[sel_team_assists_compute_total.PERIOD==1][['Team','AS']].rename(columns={'AS':'p1_AS'})
p2_sel_team_assists_compute_total=sel_team_assists_compute_total.loc[sel_team_assists_compute_total.PERIOD==2][['Team','AS']].rename(columns={'AS':'p2_AS'})
p3_sel_team_assists_compute_total=sel_team_assists_compute_total.loc[sel_team_assists_compute_total.PERIOD==3][['Team','AS']].rename(columns={'AS':'p3_AS'})
p4_sel_team_assists_compute_total=sel_team_assists_compute_total.loc[sel_team_assists_compute_total.PERIOD==4][['Team','AS']].rename(columns={'AS':'p4_AS'})
p5_sel_team_assists_compute_total=sel_team_assists_compute_total.loc[sel_team_assists_compute_total.PERIOD==5][['Team','AS']].rename(columns={'AS':'ex_AS'})
team_assists_final=pd.merge(p1_sel_team_assists_compute_total,p2_sel_team_assists_compute_total,on='Team',how='outer')
team_assists_final=pd.merge(team_assists_final,p3_sel_team_assists_compute_total,on='Team',how='outer')
team_assists_final=pd.merge(team_assists_final,p4_sel_team_assists_compute_total,on='Team',how='outer')
team_assists_final=pd.merge(team_assists_final,p5_sel_team_assists_compute_total,on='Team',how='outer')
team_period_all_Stats=pd.merge(team_period_all_Stats,team_assists_final).fillna(0)
team_period_all_Stats['p1_AS_avg']=(team_period_all_Stats['p1_AS']/team_period_all_Stats['Games']).round(1)
team_period_all_Stats['p2_AS_avg']=(team_period_all_Stats['p2_AS']/team_period_all_Stats['Games']).round(1)
team_period_all_Stats['p3_AS_avg']=(team_period_all_Stats['p3_AS']/team_period_all_Stats['Games']).round(1)
team_period_all_Stats['p4_AS_avg']=(team_period_all_Stats['p4_AS']/team_period_all_Stats['Games']).round(1)

to_compute_total=pbp_data_df2425.loc[pbp_data_df2425.PLAYTYPE=='TO'][['Team','PERIOD']].value_counts().reset_index().rename(columns={'count':'TO'}).fillna(0)
sel_team_to_compute_total=to_compute_total.loc[to_compute_total.Team==search_team_team1]
p1_sel_team_to_compute_total=sel_team_to_compute_total.loc[sel_team_to_compute_total.PERIOD==1][['Team','TO']].rename(columns={'TO':'p1_TO'})
p2_sel_team_to_compute_total=sel_team_to_compute_total.loc[sel_team_to_compute_total.PERIOD==2][['Team','TO']].rename(columns={'TO':'p2_TO'})
p3_sel_team_to_compute_total=sel_team_to_compute_total.loc[sel_team_to_compute_total.PERIOD==3][['Team','TO']].rename(columns={'TO':'p3_TO'})
p4_sel_team_to_compute_total=sel_team_to_compute_total.loc[sel_team_to_compute_total.PERIOD==4][['Team','TO']].rename(columns={'TO':'p4_TO'})
p5_sel_team_to_compute_total=sel_team_to_compute_total.loc[sel_team_to_compute_total.PERIOD==5][['Team','TO']].rename(columns={'TO':'ex_TO'})
team_to_final=pd.merge(p1_sel_team_to_compute_total,p2_sel_team_to_compute_total,on='Team',how='outer')
team_to_final=pd.merge(team_to_final,p3_sel_team_to_compute_total,on='Team',how='outer')
team_to_final=pd.merge(team_to_final,p4_sel_team_to_compute_total,on='Team',how='outer')
team_to_final=pd.merge(team_to_final,p5_sel_team_to_compute_total,on='Team',how='outer')
team_period_all_Stats=pd.merge(team_period_all_Stats,team_to_final).fillna(0)
team_period_all_Stats['p1_TO_avg']=(team_period_all_Stats['p1_TO']/team_period_all_Stats['Games']).round(1)
team_period_all_Stats['p2_TO_avg']=(team_period_all_Stats['p2_TO']/team_period_all_Stats['Games']).round(1)
team_period_all_Stats['p3_TO_avg']=(team_period_all_Stats['p3_TO']/team_period_all_Stats['Games']).round(1)
team_period_all_Stats['p4_TO_avg']=(team_period_all_Stats['p4_TO']/team_period_all_Stats['Games']).round(1)

dr_compute_total=pbp_data_df2425.loc[pbp_data_df2425.PLAYTYPE=='D'][['Team','PERIOD']].value_counts().reset_index().rename(columns={'count':'DR'}).fillna(0)
sel_team_dr_compute_total=dr_compute_total.loc[dr_compute_total.Team==search_team_team1]
p1_sel_team_dr_compute_total=sel_team_dr_compute_total.loc[sel_team_dr_compute_total.PERIOD==1][['Team','DR']].rename(columns={'DR':'p1_DR'})
p2_sel_team_dr_compute_total=sel_team_dr_compute_total.loc[sel_team_dr_compute_total.PERIOD==2][['Team','DR']].rename(columns={'DR':'p2_DR'})
p3_sel_team_dr_compute_total=sel_team_dr_compute_total.loc[sel_team_dr_compute_total.PERIOD==3][['Team','DR']].rename(columns={'DR':'p3_DR'})
p4_sel_team_dr_compute_total=sel_team_dr_compute_total.loc[sel_team_dr_compute_total.PERIOD==4][['Team','DR']].rename(columns={'DR':'p4_DR'})
p5_sel_team_dr_compute_total=sel_team_dr_compute_total.loc[sel_team_dr_compute_total.PERIOD==5][['Team','DR']].rename(columns={'DR':'ex_DR'})
team_dr_final=pd.merge(p1_sel_team_dr_compute_total,p2_sel_team_dr_compute_total,on='Team',how='outer')
team_dr_final=pd.merge(team_dr_final,p3_sel_team_dr_compute_total,on='Team',how='outer')
team_dr_final=pd.merge(team_dr_final,p4_sel_team_dr_compute_total,on='Team',how='outer')
team_dr_final=pd.merge(team_dr_final,p5_sel_team_dr_compute_total,on='Team',how='outer')
team_period_all_Stats=pd.merge(team_period_all_Stats,team_dr_final).fillna(0)
team_period_all_Stats['p1_DR_avg']=(team_period_all_Stats['p1_DR']/team_period_all_Stats['Games']).round(1)
team_period_all_Stats['p2_DR_avg']=(team_period_all_Stats['p2_DR']/team_period_all_Stats['Games']).round(1)
team_period_all_Stats['p3_DR_avg']=(team_period_all_Stats['p3_DR']/team_period_all_Stats['Games']).round(1)
team_period_all_Stats['p4_DR_avg']=(team_period_all_Stats['p4_DR']/team_period_all_Stats['Games']).round(1)


OR_compute_total=pbp_data_df2425.loc[pbp_data_df2425.PLAYTYPE=='O'][['Team','PERIOD']].value_counts().reset_index().rename(columns={'count':'OR'}).fillna(0)
sel_team_OR_compute_total=OR_compute_total.loc[OR_compute_total.Team==search_team_team1]
p1_sel_team_OR_compute_total=sel_team_OR_compute_total.loc[sel_team_OR_compute_total.PERIOD==1][['Team','OR']].rename(columns={'OR':'p1_OR'})
p2_sel_team_OR_compute_total=sel_team_OR_compute_total.loc[sel_team_OR_compute_total.PERIOD==2][['Team','OR']].rename(columns={'OR':'p2_OR'})
p3_sel_team_OR_compute_total=sel_team_OR_compute_total.loc[sel_team_OR_compute_total.PERIOD==3][['Team','OR']].rename(columns={'OR':'p3_OR'})
p4_sel_team_OR_compute_total=sel_team_OR_compute_total.loc[sel_team_OR_compute_total.PERIOD==4][['Team','OR']].rename(columns={'OR':'p4_OR'})
p5_sel_team_OR_compute_total=sel_team_OR_compute_total.loc[sel_team_OR_compute_total.PERIOD==5][['Team','OR']].rename(columns={'OR':'ex_OR'})
team_OR_final=pd.merge(p1_sel_team_OR_compute_total,p2_sel_team_OR_compute_total,on='Team',how='outer')
team_OR_final=pd.merge(team_OR_final,p3_sel_team_OR_compute_total,on='Team',how='outer')
team_OR_final=pd.merge(team_OR_final,p4_sel_team_OR_compute_total,on='Team',how='outer')
team_OR_final=pd.merge(team_OR_final,p5_sel_team_OR_compute_total,on='Team',how='outer')
team_period_all_Stats=pd.merge(team_period_all_Stats,team_OR_final).fillna(0)
team_period_all_Stats['p1_OR_avg']=(team_period_all_Stats['p1_OR']/team_period_all_Stats['Games']).round(1)
team_period_all_Stats['p2_OR_avg']=(team_period_all_Stats['p2_OR']/team_period_all_Stats['Games']).round(1)
team_period_all_Stats['p3_OR_avg']=(team_period_all_Stats['p3_OR']/team_period_all_Stats['Games']).round(1)
team_period_all_Stats['p4_OR_avg']=(team_period_all_Stats['p4_OR']/team_period_all_Stats['Games']).round(1)
team_period_all_Stats['p1_TR']=team_period_all_Stats['p1_DR']+team_period_all_Stats['p1_OR']
team_period_all_Stats['p2_TR']=team_period_all_Stats['p2_DR']+team_period_all_Stats['p2_OR']
team_period_all_Stats['p3_TR']=team_period_all_Stats['p3_DR']+team_period_all_Stats['p3_OR']
team_period_all_Stats['p4_TR']=team_period_all_Stats['p4_DR']+team_period_all_Stats['p4_OR']
team_period_all_Stats['ex_TR']=team_period_all_Stats['ex_DR']+team_period_all_Stats['ex_OR']
team_period_all_Stats['p1_TR_avg']=(team_period_all_Stats['p1_TR']/team_period_all_Stats['Games']).round(1)
team_period_all_Stats['p2_TR_avg']=(team_period_all_Stats['p2_TR']/team_period_all_Stats['Games']).round(1)
team_period_all_Stats['p3_TR_avg']=(team_period_all_Stats['p3_TR']/team_period_all_Stats['Games']).round(1)
team_period_all_Stats['p4_TR_avg']=(team_period_all_Stats['p4_TR']/team_period_all_Stats['Games']).round(1)

STL_compute_total=pbp_data_df2425.loc[pbp_data_df2425.PLAYTYPE=='ST'][['Team','PERIOD']].value_counts().reset_index().rename(columns={'count':'STL'}).fillna(0)
sel_team_STL_compute_total=STL_compute_total.loc[STL_compute_total.Team==search_team_team1]
p1_sel_team_STL_compute_total=sel_team_STL_compute_total.loc[sel_team_STL_compute_total.PERIOD==1][['Team','STL']].rename(columns={'STL':'p1_STL'})
p2_sel_team_STL_compute_total=sel_team_STL_compute_total.loc[sel_team_STL_compute_total.PERIOD==2][['Team','STL']].rename(columns={'STL':'p2_STL'})
p3_sel_team_STL_compute_total=sel_team_STL_compute_total.loc[sel_team_STL_compute_total.PERIOD==3][['Team','STL']].rename(columns={'STL':'p3_STL'})
p4_sel_team_STL_compute_total=sel_team_STL_compute_total.loc[sel_team_STL_compute_total.PERIOD==4][['Team','STL']].rename(columns={'STL':'p4_STL'})
p5_sel_team_STL_compute_total=sel_team_STL_compute_total.loc[sel_team_STL_compute_total.PERIOD==5][['Team','STL']].rename(columns={'STL':'ex_STL'})
team_STL_final=pd.merge(p1_sel_team_STL_compute_total,p2_sel_team_STL_compute_total,on='Team',how='outer')
team_STL_final=pd.merge(team_STL_final,p3_sel_team_STL_compute_total,on='Team',how='outer')
team_STL_final=pd.merge(team_STL_final,p4_sel_team_STL_compute_total,on='Team',how='outer')
team_STL_final=pd.merge(team_STL_final,p5_sel_team_STL_compute_total,on='Team',how='outer')
team_period_all_Stats=pd.merge(team_period_all_Stats,team_STL_final).fillna(0)
team_period_all_Stats['p1_STL_avg']=(team_period_all_Stats['p1_STL']/team_period_all_Stats['Games']).round(1)
team_period_all_Stats['p2_STL_avg']=(team_period_all_Stats['p2_STL']/team_period_all_Stats['Games']).round(1)
team_period_all_Stats['p3_STL_avg']=(team_period_all_Stats['p3_STL']/team_period_all_Stats['Games']).round(1)
team_period_all_Stats['p4_STL_avg']=(team_period_all_Stats['p4_STL']/team_period_all_Stats['Games']).round(1)

BLKR_compute_total=pbp_data_df2425.loc[pbp_data_df2425.PLAYTYPE=='AG'][['Team','PERIOD']].value_counts().reset_index().rename(columns={'count':'BLKR'}).fillna(0)
sel_team_BLKR_compute_total=BLKR_compute_total.loc[BLKR_compute_total.Team==search_team_team1]
p1_sel_team_BLKR_compute_total=sel_team_BLKR_compute_total.loc[sel_team_BLKR_compute_total.PERIOD==1][['Team','BLKR']].rename(columns={'BLKR':'p1_BLKR'})
p2_sel_team_BLKR_compute_total=sel_team_BLKR_compute_total.loc[sel_team_BLKR_compute_total.PERIOD==2][['Team','BLKR']].rename(columns={'BLKR':'p2_BLKR'})
p3_sel_team_BLKR_compute_total=sel_team_BLKR_compute_total.loc[sel_team_BLKR_compute_total.PERIOD==3][['Team','BLKR']].rename(columns={'BLKR':'p3_BLKR'})
p4_sel_team_BLKR_compute_total=sel_team_BLKR_compute_total.loc[sel_team_BLKR_compute_total.PERIOD==4][['Team','BLKR']].rename(columns={'BLKR':'p4_BLKR'})
p5_sel_team_BLKR_compute_total=sel_team_BLKR_compute_total.loc[sel_team_BLKR_compute_total.PERIOD==5][['Team','BLKR']].rename(columns={'BLKR':'ex_BLKR'})
team_BLKR_final=pd.merge(p1_sel_team_BLKR_compute_total,p2_sel_team_BLKR_compute_total,on='Team',how='outer')
team_BLKR_final=pd.merge(team_BLKR_final,p3_sel_team_BLKR_compute_total,on='Team',how='outer')
team_BLKR_final=pd.merge(team_BLKR_final,p4_sel_team_BLKR_compute_total,on='Team',how='outer')
team_BLKR_final=pd.merge(team_BLKR_final,p5_sel_team_BLKR_compute_total,on='Team',how='outer')
team_period_all_Stats=pd.merge(team_period_all_Stats,team_BLKR_final).fillna(0)
team_period_all_Stats['p1_BLKR_avg']=(team_period_all_Stats['p1_BLKR']/team_period_all_Stats['Games']).round(1)
team_period_all_Stats['p2_BLKR_avg']=(team_period_all_Stats['p2_BLKR']/team_period_all_Stats['Games']).round(1)
team_period_all_Stats['p3_BLKR_avg']=(team_period_all_Stats['p3_BLKR']/team_period_all_Stats['Games']).round(1)
team_period_all_Stats['p4_BLKR_avg']=(team_period_all_Stats['p4_BLKR']/team_period_all_Stats['Games']).round(1)


BLKM_compute_total=pbp_data_df2425.loc[pbp_data_df2425.PLAYTYPE=='FV'][['Team','PERIOD']].value_counts().reset_index().rename(columns={'count':'BLKM'}).fillna(0)
sel_team_BLKM_compute_total=BLKM_compute_total.loc[BLKM_compute_total.Team==search_team_team1]
p1_sel_team_BLKM_compute_total=sel_team_BLKM_compute_total.loc[sel_team_BLKM_compute_total.PERIOD==1][['Team','BLKM']].rename(columns={'BLKM':'p1_BLKM'})
p2_sel_team_BLKM_compute_total=sel_team_BLKM_compute_total.loc[sel_team_BLKM_compute_total.PERIOD==2][['Team','BLKM']].rename(columns={'BLKM':'p2_BLKM'})
p3_sel_team_BLKM_compute_total=sel_team_BLKM_compute_total.loc[sel_team_BLKM_compute_total.PERIOD==3][['Team','BLKM']].rename(columns={'BLKM':'p3_BLKM'})
p4_sel_team_BLKM_compute_total=sel_team_BLKM_compute_total.loc[sel_team_BLKM_compute_total.PERIOD==4][['Team','BLKM']].rename(columns={'BLKM':'p4_BLKM'})
p5_sel_team_BLKM_compute_total=sel_team_BLKM_compute_total.loc[sel_team_BLKM_compute_total.PERIOD==5][['Team','BLKM']].rename(columns={'BLKM':'ex_BLKM'})
team_BLKM_final=pd.merge(p1_sel_team_BLKM_compute_total,p2_sel_team_BLKM_compute_total,on='Team',how='outer')
team_BLKM_final=pd.merge(team_BLKM_final,p3_sel_team_BLKM_compute_total,on='Team',how='outer')
team_BLKM_final=pd.merge(team_BLKM_final,p4_sel_team_BLKM_compute_total,on='Team',how='outer')
team_BLKM_final=pd.merge(team_BLKM_final,p5_sel_team_BLKM_compute_total,on='Team',how='outer')
team_period_all_Stats=pd.merge(team_period_all_Stats,team_BLKM_final).fillna(0)
team_period_all_Stats['p1_BLKM_avg']=(team_period_all_Stats['p1_BLKM']/team_period_all_Stats['Games']).round(1)
team_period_all_Stats['p2_BLKM_avg']=(team_period_all_Stats['p2_BLKM']/team_period_all_Stats['Games']).round(1)
team_period_all_Stats['p3_BLKM_avg']=(team_period_all_Stats['p3_BLKM']/team_period_all_Stats['Games']).round(1)
team_period_all_Stats['p4_BLKM_avg']=(team_period_all_Stats['p4_BLKM']/team_period_all_Stats['Games']).round(1)


RF_compute_total=pbp_data_df2425.loc[pbp_data_df2425.PLAYTYPE=='RV'][['Team','PERIOD']].value_counts().reset_index().rename(columns={'count':'RF'}).fillna(0)
sel_team_RF_compute_total=RF_compute_total.loc[RF_compute_total.Team==search_team_team1]
p1_sel_team_RF_compute_total=sel_team_RF_compute_total.loc[sel_team_RF_compute_total.PERIOD==1][['Team','RF']].rename(columns={'RF':'p1_RF'})
p2_sel_team_RF_compute_total=sel_team_RF_compute_total.loc[sel_team_RF_compute_total.PERIOD==2][['Team','RF']].rename(columns={'RF':'p2_RF'})
p3_sel_team_RF_compute_total=sel_team_RF_compute_total.loc[sel_team_RF_compute_total.PERIOD==3][['Team','RF']].rename(columns={'RF':'p3_RF'})
p4_sel_team_RF_compute_total=sel_team_RF_compute_total.loc[sel_team_RF_compute_total.PERIOD==4][['Team','RF']].rename(columns={'RF':'p4_RF'})
p5_sel_team_RF_compute_total=sel_team_RF_compute_total.loc[sel_team_RF_compute_total.PERIOD==5][['Team','RF']].rename(columns={'RF':'ex_RF'})
team_RF_final=pd.merge(p1_sel_team_RF_compute_total,p2_sel_team_RF_compute_total,on='Team',how='outer')
team_RF_final=pd.merge(team_RF_final,p3_sel_team_RF_compute_total,on='Team',how='outer')
team_RF_final=pd.merge(team_RF_final,p4_sel_team_RF_compute_total,on='Team',how='outer')
team_RF_final=pd.merge(team_RF_final,p5_sel_team_RF_compute_total,on='Team',how='outer')
team_period_all_Stats=pd.merge(team_period_all_Stats,team_RF_final).fillna(0)
team_period_all_Stats['p1_RF_avg']=(team_period_all_Stats['p1_RF']/team_period_all_Stats['Games']).round(1)
team_period_all_Stats['p2_RF_avg']=(team_period_all_Stats['p2_RF']/team_period_all_Stats['Games']).round(1)
team_period_all_Stats['p3_RF_avg']=(team_period_all_Stats['p3_RF']/team_period_all_Stats['Games']).round(1)
team_period_all_Stats['p4_RF_avg']=(team_period_all_Stats['p4_RF']/team_period_all_Stats['Games']).round(1)


DF_compute_total=pbp_data_df2425.loc[pbp_data_df2425.PLAYTYPE=='CM'][['Team','PERIOD']].value_counts().reset_index().rename(columns={'count':'DF'}).fillna(0)
sel_team_DF_compute_total=DF_compute_total.loc[DF_compute_total.Team==search_team_team1]
p1_sel_team_DF_compute_total=sel_team_DF_compute_total.loc[sel_team_DF_compute_total.PERIOD==1][['Team','DF']].rename(columns={'DF':'p1_DF'})
p2_sel_team_DF_compute_total=sel_team_DF_compute_total.loc[sel_team_DF_compute_total.PERIOD==2][['Team','DF']].rename(columns={'DF':'p2_DF'})
p3_sel_team_DF_compute_total=sel_team_DF_compute_total.loc[sel_team_DF_compute_total.PERIOD==3][['Team','DF']].rename(columns={'DF':'p3_DF'})
p4_sel_team_DF_compute_total=sel_team_DF_compute_total.loc[sel_team_DF_compute_total.PERIOD==4][['Team','DF']].rename(columns={'DF':'p4_DF'})
p5_sel_team_DF_compute_total=sel_team_DF_compute_total.loc[sel_team_DF_compute_total.PERIOD==5][['Team','DF']].rename(columns={'DF':'ex_DF'})
team_DF_final=pd.merge(p1_sel_team_DF_compute_total,p2_sel_team_DF_compute_total,on='Team',how='outer')
team_DF_final=pd.merge(team_DF_final,p3_sel_team_DF_compute_total,on='Team',how='outer')
team_DF_final=pd.merge(team_DF_final,p4_sel_team_DF_compute_total,on='Team',how='outer')
team_DF_final=pd.merge(team_DF_final,p5_sel_team_DF_compute_total,on='Team',how='outer')
team_period_all_Stats=pd.merge(team_period_all_Stats,team_DF_final).fillna(0)
team_period_all_Stats['p1_DF_avg']=(team_period_all_Stats['p1_DF']/team_period_all_Stats['Games']).round(1)
team_period_all_Stats['p2_DF_avg']=(team_period_all_Stats['p2_DF']/team_period_all_Stats['Games']).round(1)
team_period_all_Stats['p3_DF_avg']=(team_period_all_Stats['p3_DF']/team_period_all_Stats['Games']).round(1)
team_period_all_Stats['p4_DF_avg']=(team_period_all_Stats['p4_DF']/team_period_all_Stats['Games']).round(1)

OF_compute_total=pbp_data_df2425.loc[pbp_data_df2425.PLAYTYPE=='OF'][['Team','PERIOD']].value_counts().reset_index().rename(columns={'count':'OF'}).fillna(0)
sel_team_OF_compute_total=OF_compute_total.loc[OF_compute_total.Team==search_team_team1]
p1_sel_team_OF_compute_total=sel_team_OF_compute_total.loc[sel_team_OF_compute_total.PERIOD==1][['Team','OF']].rename(columns={'OF':'p1_OF'})
p2_sel_team_OF_compute_total=sel_team_OF_compute_total.loc[sel_team_OF_compute_total.PERIOD==2][['Team','OF']].rename(columns={'OF':'p2_OF'})
p3_sel_team_OF_compute_total=sel_team_OF_compute_total.loc[sel_team_OF_compute_total.PERIOD==3][['Team','OF']].rename(columns={'OF':'p3_OF'})
p4_sel_team_OF_compute_total=sel_team_OF_compute_total.loc[sel_team_OF_compute_total.PERIOD==4][['Team','OF']].rename(columns={'OF':'p4_OF'})
p5_sel_team_OF_compute_total=sel_team_OF_compute_total.loc[sel_team_OF_compute_total.PERIOD==5][['Team','OF']].rename(columns={'OF':'ex_OF'})
team_OF_final=pd.merge(p1_sel_team_OF_compute_total,p2_sel_team_OF_compute_total,on='Team',how='outer')
team_OF_final=pd.merge(team_OF_final,p3_sel_team_OF_compute_total,on='Team',how='outer')
team_OF_final=pd.merge(team_OF_final,p4_sel_team_OF_compute_total,on='Team',how='outer')
team_OF_final=pd.merge(team_OF_final,p5_sel_team_OF_compute_total,on='Team',how='outer')
team_period_all_Stats=pd.merge(team_period_all_Stats,team_OF_final).fillna(0)
team_period_all_Stats['p1_OF_avg']=(team_period_all_Stats['p1_OF']/team_period_all_Stats['Games']).round(1)
team_period_all_Stats['p2_OF_avg']=(team_period_all_Stats['p2_OF']/team_period_all_Stats['Games']).round(1)
team_period_all_Stats['p3_OF_avg']=(team_period_all_Stats['p3_OF']/team_period_all_Stats['Games']).round(1)
team_period_all_Stats['p4_OF_avg']=(team_period_all_Stats['p4_OF']/team_period_all_Stats['Games']).round(1)

UNF_compute_total=pbp_data_df2425.loc[pbp_data_df2425.PLAYTYPE.isin(['CMD','CMU'])][['Team','PERIOD']].value_counts().reset_index().rename(columns={'count':'UNF'}).fillna(0)
sel_team_UNF_compute_total=UNF_compute_total.loc[UNF_compute_total.Team==search_team_team1]
p1_sel_team_UNF_compute_total=sel_team_UNF_compute_total.loc[sel_team_UNF_compute_total.PERIOD==1][['Team','UNF']].rename(columns={'UNF':'p1_UNF'})
p2_sel_team_UNF_compute_total=sel_team_UNF_compute_total.loc[sel_team_UNF_compute_total.PERIOD==2][['Team','UNF']].rename(columns={'UNF':'p2_UNF'})
p3_sel_team_UNF_compute_total=sel_team_UNF_compute_total.loc[sel_team_UNF_compute_total.PERIOD==3][['Team','UNF']].rename(columns={'UNF':'p3_UNF'})
p4_sel_team_UNF_compute_total=sel_team_UNF_compute_total.loc[sel_team_UNF_compute_total.PERIOD==4][['Team','UNF']].rename(columns={'UNF':'p4_UNF'})
p5_sel_team_UNF_compute_total=sel_team_UNF_compute_total.loc[sel_team_UNF_compute_total.PERIOD==5][['Team','UNF']].rename(columns={'UNF':'ex_UNF'})
team_UNF_final=pd.merge(p1_sel_team_UNF_compute_total,p2_sel_team_UNF_compute_total,on='Team',how='outer')
team_UNF_final=pd.merge(team_UNF_final,p3_sel_team_UNF_compute_total,on='Team',how='outer')
team_UNF_final=pd.merge(team_UNF_final,p4_sel_team_UNF_compute_total,on='Team',how='outer')
team_UNF_final=pd.merge(team_UNF_final,p5_sel_team_UNF_compute_total,on='Team',how='outer')
team_period_all_Stats=pd.merge(team_period_all_Stats,team_UNF_final).fillna(0)
team_period_all_Stats['p1_UNF_avg']=(team_period_all_Stats['p1_UNF']/team_period_all_Stats['Games']).round(1)
team_period_all_Stats['p2_UNF_avg']=(team_period_all_Stats['p2_UNF']/team_period_all_Stats['Games']).round(1)
team_period_all_Stats['p3_UNF_avg']=(team_period_all_Stats['p3_UNF']/team_period_all_Stats['Games']).round(1)
team_period_all_Stats['p4_UNF_avg']=(team_period_all_Stats['p4_UNF']/team_period_all_Stats['Games']).round(1)



TF_compute_total=pbp_data_df2425.loc[pbp_data_df2425.PLAYTYPE=='CMT'][['Team','PERIOD']].value_counts().reset_index().rename(columns={'count':'TF'}).fillna(0)
sel_team_TF_compute_total=TF_compute_total.loc[TF_compute_total.Team==search_team_team1]
p1_sel_team_TF_compute_total=sel_team_TF_compute_total.loc[sel_team_TF_compute_total.PERIOD==1][['Team','TF']].rename(columns={'TF':'p1_TF'})
p2_sel_team_TF_compute_total=sel_team_TF_compute_total.loc[sel_team_TF_compute_total.PERIOD==2][['Team','TF']].rename(columns={'TF':'p2_TF'})
p3_sel_team_TF_compute_total=sel_team_TF_compute_total.loc[sel_team_TF_compute_total.PERIOD==3][['Team','TF']].rename(columns={'TF':'p3_TF'})
p4_sel_team_TF_compute_total=sel_team_TF_compute_total.loc[sel_team_TF_compute_total.PERIOD==4][['Team','TF']].rename(columns={'TF':'p4_TF'})
p5_sel_team_TF_compute_total=sel_team_TF_compute_total.loc[sel_team_TF_compute_total.PERIOD==5][['Team','TF']].rename(columns={'TF':'ex_TF'})
team_TF_final=pd.merge(p1_sel_team_TF_compute_total,p2_sel_team_TF_compute_total,on='Team',how='outer')
team_TF_final=pd.merge(team_TF_final,p3_sel_team_TF_compute_total,on='Team',how='outer')
team_TF_final=pd.merge(team_TF_final,p4_sel_team_TF_compute_total,on='Team',how='outer')
team_TF_final=pd.merge(team_TF_final,p5_sel_team_TF_compute_total,on='Team',how='outer')
team_period_all_Stats=pd.merge(team_period_all_Stats,team_TF_final).fillna(0)
team_period_all_Stats['p1_TF_avg']=(team_period_all_Stats['p1_TF']/team_period_all_Stats['Games']).round(1)
team_period_all_Stats['p2_TF_avg']=(team_period_all_Stats['p2_TF']/team_period_all_Stats['Games']).round(1)
team_period_all_Stats['p3_TF_avg']=(team_period_all_Stats['p3_TF']/team_period_all_Stats['Games']).round(1)
team_period_all_Stats['p4_TF_avg']=(team_period_all_Stats['p4_TF']/team_period_all_Stats['Games']).round(1)
team_period_all_Stats['p1_PF']=team_period_all_Stats['p1_DF']+team_period_all_Stats['p1_OF']+team_period_all_Stats['p1_UNF']+team_period_all_Stats['p1_TF']
team_period_all_Stats['p2_PF']=team_period_all_Stats['p2_DF']+team_period_all_Stats['p2_OF']+team_period_all_Stats['p2_UNF']+team_period_all_Stats['p2_TF']
team_period_all_Stats['p3_PF']=team_period_all_Stats['p3_DF']+team_period_all_Stats['p3_OF']+team_period_all_Stats['p3_UNF']+team_period_all_Stats['p3_TF']
team_period_all_Stats['p4_PF']=team_period_all_Stats['p4_DF']+team_period_all_Stats['p4_OF']+team_period_all_Stats['p4_UNF']+team_period_all_Stats['p4_TF']
team_period_all_Stats['ex_PF']=team_period_all_Stats['ex_DF']+team_period_all_Stats['ex_OF']+team_period_all_Stats['ex_UNF']+team_period_all_Stats['ex_TF']

team_period_all_Stats['p1_PF_avg']=(team_period_all_Stats['p1_PF']/team_period_all_Stats['Games']).round(1)
team_period_all_Stats['p2_PF_avg']=(team_period_all_Stats['p2_PF']/team_period_all_Stats['Games']).round(1)
team_period_all_Stats['p3_PF_avg']=(team_period_all_Stats['p3_PF']/team_period_all_Stats['Games']).round(1)
team_period_all_Stats['p4_PF_avg']=(team_period_all_Stats['p4_PF']/team_period_all_Stats['Games']).round(1)


P2M_compute_total=pbp_data_df2425.loc[pbp_data_df2425.PLAYTYPE=='2FGM'][['Team','PERIOD']].value_counts().reset_index().rename(columns={'count':'P2M'}).fillna(0)
sel_team_P2M_compute_total=P2M_compute_total.loc[P2M_compute_total.Team==search_team_team1]
p1_sel_team_P2M_compute_total=sel_team_P2M_compute_total.loc[sel_team_P2M_compute_total.PERIOD==1][['Team','P2M']].rename(columns={'P2M':'p1_2PM'})
p2_sel_team_P2M_compute_total=sel_team_P2M_compute_total.loc[sel_team_P2M_compute_total.PERIOD==2][['Team','P2M']].rename(columns={'P2M':'p2_2PM'})
p3_sel_team_P2M_compute_total=sel_team_P2M_compute_total.loc[sel_team_P2M_compute_total.PERIOD==3][['Team','P2M']].rename(columns={'P2M':'p3_2PM'})
p4_sel_team_P2M_compute_total=sel_team_P2M_compute_total.loc[sel_team_P2M_compute_total.PERIOD==4][['Team','P2M']].rename(columns={'P2M':'p4_2PM'})
p5_sel_team_P2M_compute_total=sel_team_P2M_compute_total.loc[sel_team_P2M_compute_total.PERIOD==5][['Team','P2M']].rename(columns={'P2M':'ex_2PM'})
team_P2M_final=pd.merge(p1_sel_team_P2M_compute_total,p2_sel_team_P2M_compute_total,on='Team',how='outer')
team_P2M_final=pd.merge(team_P2M_final,p3_sel_team_P2M_compute_total,on='Team',how='outer')
team_P2M_final=pd.merge(team_P2M_final,p4_sel_team_P2M_compute_total,on='Team',how='outer')
team_P2M_final=pd.merge(team_P2M_final,p5_sel_team_P2M_compute_total,on='Team',how='outer')
team_period_all_Stats=pd.merge(team_period_all_Stats,team_P2M_final).fillna(0)
team_period_all_Stats['p1_2PM_avg']=(team_period_all_Stats['p1_2PM']/team_period_all_Stats['Games']).round(1)
team_period_all_Stats['p2_2PM_avg']=(team_period_all_Stats['p2_2PM']/team_period_all_Stats['Games']).round(1)
team_period_all_Stats['p3_2PM_avg']=(team_period_all_Stats['p3_2PM']/team_period_all_Stats['Games']).round(1)
team_period_all_Stats['p4_2PM_avg']=(team_period_all_Stats['p4_2PM']/team_period_all_Stats['Games']).round(1)


p2a_compute_total=pbp_data_df2425.loc[pbp_data_df2425.PLAYTYPE.isin(['2FGA','2FGM'])].reset_index()[['Team','PERIOD']].value_counts().reset_index().rename(columns={'count':'2PA'}).fillna(0)
sel_team_p2a_compute_total=p2a_compute_total.loc[p2a_compute_total.Team==search_team_team1]
p1_sel_team_p2a_compute_total=sel_team_p2a_compute_total.loc[sel_team_p2a_compute_total.PERIOD==1][['Team','2PA']].rename(columns={'2PA':'p1_2PA'})
p2_sel_team_p2a_compute_total=sel_team_p2a_compute_total.loc[sel_team_p2a_compute_total.PERIOD==2][['Team','2PA']].rename(columns={'2PA':'p2_2PA'})
p3_sel_team_p2a_compute_total=sel_team_p2a_compute_total.loc[sel_team_p2a_compute_total.PERIOD==3][['Team','2PA']].rename(columns={'2PA':'p3_2PA'})
p4_sel_team_p2a_compute_total=sel_team_p2a_compute_total.loc[sel_team_p2a_compute_total.PERIOD==4][['Team','2PA']].rename(columns={'2PA':'p4_2PA'})
p5_sel_team_p2a_compute_total=sel_team_p2a_compute_total.loc[sel_team_p2a_compute_total.PERIOD==5][['Team','2PA']].rename(columns={'2PA':'ex_2PA'})
team_p2a_final=pd.merge(p1_sel_team_p2a_compute_total,p2_sel_team_p2a_compute_total,on='Team',how='outer')
team_p2a_final=pd.merge(team_p2a_final,p3_sel_team_p2a_compute_total,on='Team',how='outer')
team_p2a_final=pd.merge(team_p2a_final,p4_sel_team_p2a_compute_total,on='Team',how='outer')
team_p2a_final=pd.merge(team_p2a_final,p5_sel_team_p2a_compute_total,on='Team',how='outer')

team_period_all_Stats=pd.merge(team_period_all_Stats,team_p2a_final,on='Team',how='outer')
team_period_all_Stats['p1_2PA_avg']=(team_period_all_Stats['p1_2PA']/team_period_all_Stats['Games']).round(1)
team_period_all_Stats['p2_2PA_avg']=(team_period_all_Stats['p2_2PA']/team_period_all_Stats['Games']).round(1)
team_period_all_Stats['p3_2PA_avg']=(team_period_all_Stats['p3_2PA']/team_period_all_Stats['Games']).round(1)
team_period_all_Stats['p4_2PA_avg']=(team_period_all_Stats['p4_2PA']/team_period_all_Stats['Games']).round(1)
team_period_all_Stats['p1_2P(%)']=(100*team_period_all_Stats['p1_2PM']/team_period_all_Stats['p1_2PA']).round(1)
team_period_all_Stats['p2_2P(%)']=(100*team_period_all_Stats['p2_2PM']/team_period_all_Stats['p2_2PA']).round(1)
team_period_all_Stats['p3_2P(%)']=(100*team_period_all_Stats['p3_2PM']/team_period_all_Stats['p3_2PA']).round(1)
team_period_all_Stats['p4_2P(%)']=(100*team_period_all_Stats['p4_2PM']/team_period_all_Stats['p4_2PA']).round(1)
team_period_all_Stats['ex_2P(%)']=(100*team_period_all_Stats['ex_2PM']/team_period_all_Stats['ex_2PA']).round(1)



P3M_compute_total=pbp_data_df2425.loc[pbp_data_df2425.PLAYTYPE=='3FGM'][['Team','PERIOD']].value_counts().reset_index().rename(columns={'count':'P3M'}).fillna(0)
sel_team_P3M_compute_total=P3M_compute_total.loc[P3M_compute_total.Team==search_team_team1]
p1_sel_team_P3M_compute_total=sel_team_P3M_compute_total.loc[sel_team_P3M_compute_total.PERIOD==1][['Team','P3M']].rename(columns={'P3M':'p1_3PM'})
p2_sel_team_P3M_compute_total=sel_team_P3M_compute_total.loc[sel_team_P3M_compute_total.PERIOD==2][['Team','P3M']].rename(columns={'P3M':'p2_3PM'})
p3_sel_team_P3M_compute_total=sel_team_P3M_compute_total.loc[sel_team_P3M_compute_total.PERIOD==3][['Team','P3M']].rename(columns={'P3M':'p3_3PM'})
p4_sel_team_P3M_compute_total=sel_team_P3M_compute_total.loc[sel_team_P3M_compute_total.PERIOD==4][['Team','P3M']].rename(columns={'P3M':'p4_3PM'})
p5_sel_team_P3M_compute_total=sel_team_P3M_compute_total.loc[sel_team_P3M_compute_total.PERIOD==5][['Team','P3M']].rename(columns={'P3M':'ex_3PM'})
team_P3M_final=pd.merge(p1_sel_team_P3M_compute_total,p2_sel_team_P3M_compute_total,on='Team',how='outer')
team_P3M_final=pd.merge(team_P3M_final,p3_sel_team_P3M_compute_total,on='Team',how='outer')
team_P3M_final=pd.merge(team_P3M_final,p4_sel_team_P3M_compute_total,on='Team',how='outer')
team_P3M_final=pd.merge(team_P3M_final,p5_sel_team_P3M_compute_total,on='Team',how='outer')
team_period_all_Stats=pd.merge(team_period_all_Stats,team_P3M_final).fillna(0)
team_period_all_Stats['p1_3PM_avg']=(team_period_all_Stats['p1_3PM']/team_period_all_Stats['Games']).round(1)
team_period_all_Stats['p2_3PM_avg']=(team_period_all_Stats['p2_3PM']/team_period_all_Stats['Games']).round(1)
team_period_all_Stats['p3_3PM_avg']=(team_period_all_Stats['p3_3PM']/team_period_all_Stats['Games']).round(1)
team_period_all_Stats['p4_3PM_avg']=(team_period_all_Stats['p4_3PM']/team_period_all_Stats['Games']).round(1)



p3a_compute_total=pbp_data_df2425.loc[pbp_data_df2425.PLAYTYPE.isin(['3FGA','3FGM'])].reset_index()[['Team','PERIOD']].value_counts().reset_index().rename(columns={'count':'3PA'}).fillna(0)
sel_team_p3a_compute_total=p3a_compute_total.loc[p3a_compute_total.Team==search_team_team1]
p1_sel_team_p3a_compute_total=sel_team_p3a_compute_total.loc[sel_team_p3a_compute_total.PERIOD==1][['Team','3PA']].rename(columns={'3PA':'p1_3PA'})
p2_sel_team_p3a_compute_total=sel_team_p3a_compute_total.loc[sel_team_p3a_compute_total.PERIOD==2][['Team','3PA']].rename(columns={'3PA':'p2_3PA'})
p3_sel_team_p3a_compute_total=sel_team_p3a_compute_total.loc[sel_team_p3a_compute_total.PERIOD==3][['Team','3PA']].rename(columns={'3PA':'p3_3PA'})
p4_sel_team_p3a_compute_total=sel_team_p3a_compute_total.loc[sel_team_p3a_compute_total.PERIOD==4][['Team','3PA']].rename(columns={'3PA':'p4_3PA'})
p5_sel_team_p3a_compute_total=sel_team_p3a_compute_total.loc[sel_team_p3a_compute_total.PERIOD==5][['Team','3PA']].rename(columns={'3PA':'ex_3PA'})
team_p3a_final=pd.merge(p1_sel_team_p3a_compute_total,p2_sel_team_p3a_compute_total,on='Team',how='outer')
team_p3a_final=pd.merge(team_p3a_final,p3_sel_team_p3a_compute_total,on='Team',how='outer')
team_p3a_final=pd.merge(team_p3a_final,p4_sel_team_p3a_compute_total,on='Team',how='outer')
team_p3a_final=pd.merge(team_p3a_final,p5_sel_team_p3a_compute_total,on='Team',how='outer')

team_period_all_Stats=pd.merge(team_period_all_Stats,team_p3a_final,on='Team',how='outer').fillna(0)
team_period_all_Stats['p1_3PA_avg']=(team_period_all_Stats['p1_3PA']/team_period_all_Stats['Games']).round(1)
team_period_all_Stats['p2_3PA_avg']=(team_period_all_Stats['p2_3PA']/team_period_all_Stats['Games']).round(1)
team_period_all_Stats['p3_3PA_avg']=(team_period_all_Stats['p3_3PA']/team_period_all_Stats['Games']).round(1)
team_period_all_Stats['p4_3PA_avg']=(team_period_all_Stats['p4_3PA']/team_period_all_Stats['Games']).round(1)
team_period_all_Stats['p1_3P(%)']=(100*team_period_all_Stats['p1_3PM']/team_period_all_Stats['p1_3PA']).round(1)
team_period_all_Stats['p2_3P(%)']=(100*team_period_all_Stats['p2_3PM']/team_period_all_Stats['p2_3PA']).round(1)
team_period_all_Stats['p3_3P(%)']=(100*team_period_all_Stats['p3_3PM']/team_period_all_Stats['p3_3PA']).round(1)
team_period_all_Stats['p4_3P(%)']=(100*team_period_all_Stats['p4_3PM']/team_period_all_Stats['p4_3PA']).round(1)
team_period_all_Stats['ex_3P(%)']=(100*team_period_all_Stats['ex_3PM']/team_period_all_Stats['ex_3PA']).round(1)



FTM_compute_total=pbp_data_df2425.loc[pbp_data_df2425.PLAYTYPE=='FTM'][['Team','PERIOD']].value_counts().reset_index().rename(columns={'count':'FTM'}).fillna(0)
sel_team_FTM_compute_total=FTM_compute_total.loc[FTM_compute_total.Team==search_team_team1]
p1_sel_team_FTM_compute_total=sel_team_FTM_compute_total.loc[sel_team_FTM_compute_total.PERIOD==1][['Team','FTM']].rename(columns={'FTM':'p1_FTM'})
p2_sel_team_FTM_compute_total=sel_team_FTM_compute_total.loc[sel_team_FTM_compute_total.PERIOD==2][['Team','FTM']].rename(columns={'FTM':'p2_FTM'})
p3_sel_team_FTM_compute_total=sel_team_FTM_compute_total.loc[sel_team_FTM_compute_total.PERIOD==3][['Team','FTM']].rename(columns={'FTM':'p3_FTM'})
p4_sel_team_FTM_compute_total=sel_team_FTM_compute_total.loc[sel_team_FTM_compute_total.PERIOD==4][['Team','FTM']].rename(columns={'FTM':'p4_FTM'})
p5_sel_team_FTM_compute_total=sel_team_FTM_compute_total.loc[sel_team_FTM_compute_total.PERIOD==5][['Team','FTM']].rename(columns={'FTM':'ex_FTM'})
team_FTM_final=pd.merge(p1_sel_team_FTM_compute_total,p2_sel_team_FTM_compute_total,on='Team',how='outer')
team_FTM_final=pd.merge(team_FTM_final,p3_sel_team_FTM_compute_total,on='Team',how='outer')
team_FTM_final=pd.merge(team_FTM_final,p4_sel_team_FTM_compute_total,on='Team',how='outer')
team_FTM_final=pd.merge(team_FTM_final,p5_sel_team_FTM_compute_total,on='Team',how='outer')
team_period_all_Stats=pd.merge(team_period_all_Stats,team_FTM_final).fillna(0)
team_period_all_Stats['p1_FTM_avg']=(team_period_all_Stats['p1_FTM']/team_period_all_Stats['Games']).round(1)
team_period_all_Stats['p2_FTM_avg']=(team_period_all_Stats['p2_FTM']/team_period_all_Stats['Games']).round(1)
team_period_all_Stats['p3_FTM_avg']=(team_period_all_Stats['p3_FTM']/team_period_all_Stats['Games']).round(1)
team_period_all_Stats['p4_FTM_avg']=(team_period_all_Stats['p4_FTM']/team_period_all_Stats['Games']).round(1)



p3a_compute_total=pbp_data_df2425.loc[pbp_data_df2425.PLAYTYPE.isin(['FTA','FTM'])].reset_index()[['Team','PERIOD']].value_counts().reset_index().rename(columns={'count':'FTA'}).fillna(0)
sel_team_p3a_compute_total=p3a_compute_total.loc[p3a_compute_total.Team==search_team_team1]
p1_sel_team_p3a_compute_total=sel_team_p3a_compute_total.loc[sel_team_p3a_compute_total.PERIOD==1][['Team','FTA']].rename(columns={'FTA':'p1_FTA'})
p2_sel_team_p3a_compute_total=sel_team_p3a_compute_total.loc[sel_team_p3a_compute_total.PERIOD==2][['Team','FTA']].rename(columns={'FTA':'p2_FTA'})
p3_sel_team_p3a_compute_total=sel_team_p3a_compute_total.loc[sel_team_p3a_compute_total.PERIOD==3][['Team','FTA']].rename(columns={'FTA':'p3_FTA'})
p4_sel_team_p3a_compute_total=sel_team_p3a_compute_total.loc[sel_team_p3a_compute_total.PERIOD==4][['Team','FTA']].rename(columns={'FTA':'p4_FTA'})
p5_sel_team_p3a_compute_total=sel_team_p3a_compute_total.loc[sel_team_p3a_compute_total.PERIOD==5][['Team','FTA']].rename(columns={'FTA':'ex_FTA'})
team_p3a_final=pd.merge(p1_sel_team_p3a_compute_total,p2_sel_team_p3a_compute_total,on='Team',how='outer')
team_p3a_final=pd.merge(team_p3a_final,p3_sel_team_p3a_compute_total,on='Team',how='outer')
team_p3a_final=pd.merge(team_p3a_final,p4_sel_team_p3a_compute_total,on='Team',how='outer')
team_p3a_final=pd.merge(team_p3a_final,p5_sel_team_p3a_compute_total,on='Team',how='outer')

team_period_all_Stats=pd.merge(team_period_all_Stats,team_p3a_final,on='Team',how='outer').fillna(0)
team_period_all_Stats['p1_FTA_avg']=(team_period_all_Stats['p1_FTA']/team_period_all_Stats['Games']).round(1)
team_period_all_Stats['p2_FTA_avg']=(team_period_all_Stats['p2_FTA']/team_period_all_Stats['Games']).round(1)
team_period_all_Stats['p3_FTA_avg']=(team_period_all_Stats['p3_FTA']/team_period_all_Stats['Games']).round(1)
team_period_all_Stats['p4_FTA_avg']=(team_period_all_Stats['p4_FTA']/team_period_all_Stats['Games']).round(1)
team_period_all_Stats['p1_FT(%)']=(100*team_period_all_Stats['p1_FTM']/team_period_all_Stats['p1_FTA']).round(1)
team_period_all_Stats['p2_FT(%)']=(100*team_period_all_Stats['p2_FTM']/team_period_all_Stats['p2_FTA']).round(1)
team_period_all_Stats['p3_FT(%)']=(100*team_period_all_Stats['p3_FTM']/team_period_all_Stats['p3_FTA']).round(1)
team_period_all_Stats['p4_FT(%)']=(100*team_period_all_Stats['p4_FTM']/team_period_all_Stats['p4_FTA']).round(1)
team_period_all_Stats['ex_FT(%)']=(100*team_period_all_Stats['ex_FTM']/team_period_all_Stats['ex_FTA']).round(1)
team_period_all_Stats["p1_PIR"] = (team_period_all_Stats["p1_PTS"].fillna(0) +
                                           team_period_all_Stats["p1_AS"].fillna(0) +
                                           team_period_all_Stats["p1_TR"].fillna(0) -
                                           team_period_all_Stats["p1_TO"].fillna(0) +
                                           team_period_all_Stats["p1_STL"].fillna(0) +
                                           team_period_all_Stats["p1_BLKM"].fillna(0) -
                                           team_period_all_Stats["p1_BLKR"].fillna(0) -
                                           team_period_all_Stats["p1_PF"].fillna(0) +
                                           team_period_all_Stats["p1_2PM"].fillna(0) + team_period_all_Stats[
                                               "p1_3PM"].fillna(0) + team_period_all_Stats["p1_FTM"].fillna(0) -
                                           team_period_all_Stats["p1_2PA"].fillna(0) - team_period_all_Stats[
                                               "p1_3PA"].fillna(0) + team_period_all_Stats["p1_FTA"].fillna(0))
team_period_all_Stats["p2_PIR"] = (team_period_all_Stats["p2_PTS"].fillna(0) +
                                           team_period_all_Stats["p2_AS"].fillna(0) +
                                           team_period_all_Stats["p2_TR"].fillna(0) -
                                           team_period_all_Stats["p2_TO"].fillna(0) +
                                           team_period_all_Stats["p2_STL"].fillna(0) +
                                           team_period_all_Stats["p2_BLKM"].fillna(0) -
                                           team_period_all_Stats["p2_BLKR"].fillna(0) -
                                           team_period_all_Stats["p2_PF"].fillna(0) +
                                           team_period_all_Stats["p2_2PM"].fillna(0) + team_period_all_Stats[
                                               "p2_3PM"].fillna(0) + team_period_all_Stats["p2_FTM"].fillna(0) -
                                           team_period_all_Stats["p3_2PA"].fillna(0) - team_period_all_Stats[
                                               "p2_3PA"].fillna(0) + team_period_all_Stats["p2_FTA"].fillna(0))
team_period_all_Stats["p3_PIR"] = (team_period_all_Stats["p3_PTS"].fillna(0) +
                                           team_period_all_Stats["p3_AS"].fillna(0) +
                                           team_period_all_Stats["p3_TR"].fillna(0) -
                                           team_period_all_Stats["p3_TO"].fillna(0) +
                                           team_period_all_Stats["p3_STL"].fillna(0)+
                                           team_period_all_Stats["p3_BLKM"].fillna(0) -
                                           team_period_all_Stats["p3_BLKR"].fillna(0) -
                                           team_period_all_Stats["p3_PF"].fillna(0) +
                                           team_period_all_Stats["p3_2PM"].fillna(0) + team_period_all_Stats[
                                               "p3_3PM"].fillna(0) + team_period_all_Stats["p3_FTM"].fillna(0) -
                                           team_period_all_Stats["p3_2PA"].fillna(0) - team_period_all_Stats[
                                               "p3_3PA"].fillna(0) + team_period_all_Stats["p3_FTA"].fillna(0))

team_period_all_Stats["p4_PIR"] = (team_period_all_Stats["p4_PTS"].fillna(0) +
                                           team_period_all_Stats["p4_AS"].fillna(0) +
                                           team_period_all_Stats["p4_TR"].fillna(0) -
                                           team_period_all_Stats["p4_TO"].fillna(0) +
                                           team_period_all_Stats["p4_STL"].fillna(0) +
                                           team_period_all_Stats["p4_BLKM"].fillna(0) -
                                           team_period_all_Stats["p4_BLKR"].fillna(0) -
                                           team_period_all_Stats["p4_PF"].fillna(0) +
                                           team_period_all_Stats["p4_2PM"].fillna(0) + team_period_all_Stats[
                                               "p4_3PM"].fillna(0) + team_period_all_Stats["p4_FTM"].fillna(0) -
                                           team_period_all_Stats["p4_2PA"].fillna(0) - team_period_all_Stats[
                                               "p4_3PA"].fillna(0) + team_period_all_Stats["p4_FTA"].fillna(0))

team_period_all_Stats["ex_PIR"] = (team_period_all_Stats["ex_PTS"].fillna(0) +
                                           team_period_all_Stats["ex_AS"].fillna(0) +
                                           team_period_all_Stats["ex_TR"].fillna(0) -
                                           team_period_all_Stats["ex_TO"].fillna(0) +
                                           team_period_all_Stats["ex_STL"].fillna(0) +
                                           team_period_all_Stats["ex_BLKM"].fillna(0) -
                                           team_period_all_Stats["ex_BLKR"].fillna(0) -
                                           team_period_all_Stats["ex_PF"].fillna(0) +
                                           team_period_all_Stats["ex_2PM"].fillna(0) + team_period_all_Stats[
                                               "ex_3PM"].fillna(0) + team_period_all_Stats["ex_FTM"].fillna(0) -
                                           team_period_all_Stats["ex_2PA"].fillna(0) - team_period_all_Stats[
                                               "ex_3PA"].fillna(0) + team_period_all_Stats["ex_FTA"].fillna(0))
team_period_all_Stats['p1_PIR_avg'] = (
        team_period_all_Stats['p1_PIR'] / team_period_all_Stats['Games']).round(1)
team_period_all_Stats['p2_PIR_avg'] = (
        team_period_all_Stats['p2_PIR'] / team_period_all_Stats['Games']).round(1)
team_period_all_Stats['p3_PIR_avg'] = (
        team_period_all_Stats['p3_PIR'] / team_period_all_Stats['Games']).round(1)
team_period_all_Stats['p4_PIR_avg'] = (
        team_period_all_Stats['p4_PIR'] / team_period_all_Stats['Games']).round(1)
regex1 = "Team|" + stat_choose
interactive_table(
    team_period_all_Stats.set_index('Team').filter(regex=regex1),
    paging=False, height=900, width=2000, showIndex=True,
    classes="display order-column nowrap table_with_monospace_font", searching=False,
    fixedColumns=True, select=True, info=False, scrollCollapse=True,
    scrollX=True, scrollY=1000, fixedHeader=True, scroller=True, filter='bottom',
    columnDefs=[{"className": "dt-center", "targets": "_all"}])


st.header('Average Opponent Stats')

team_against_period_all_Stats=pd.merge(team_period_stats_against,team_games.rename(columns={'Team':"Against"})).round(1)
assists_compute_total=pbp_data_df2425.loc[pbp_data_df2425.PLAYTYPE=='AS'][['Against','PERIOD']].value_counts().reset_index().rename(columns={'count':'AS'})
sel_team_against_assists_compute_total=assists_compute_total.loc[assists_compute_total.Against==search_team_team1]
p1_sel_team_against_assists_compute_total=sel_team_against_assists_compute_total.loc[sel_team_against_assists_compute_total.PERIOD==1][['Against','AS']].rename(columns={'AS':'p1_AS'})
p2_sel_team_against_assists_compute_total=sel_team_against_assists_compute_total.loc[sel_team_against_assists_compute_total.PERIOD==2][['Against','AS']].rename(columns={'AS':'p2_AS'})
p3_sel_team_against_assists_compute_total=sel_team_against_assists_compute_total.loc[sel_team_against_assists_compute_total.PERIOD==3][['Against','AS']].rename(columns={'AS':'p3_AS'})
p4_sel_team_against_assists_compute_total=sel_team_against_assists_compute_total.loc[sel_team_against_assists_compute_total.PERIOD==4][['Against','AS']].rename(columns={'AS':'p4_AS'})
p5_sel_team_against_assists_compute_total=sel_team_against_assists_compute_total.loc[sel_team_against_assists_compute_total.PERIOD==5][['Against','AS']].rename(columns={'AS':'ex_AS'})
team_against_assists_final=pd.merge(p1_sel_team_against_assists_compute_total,p2_sel_team_against_assists_compute_total,on='Against',how='outer')
team_against_assists_final=pd.merge(team_against_assists_final,p3_sel_team_against_assists_compute_total,on='Against',how='outer')
team_against_assists_final=pd.merge(team_against_assists_final,p4_sel_team_against_assists_compute_total,on='Against',how='outer')
team_against_assists_final=pd.merge(team_against_assists_final,p5_sel_team_against_assists_compute_total,on='Against',how='outer')
team_against_period_all_Stats=pd.merge(team_against_period_all_Stats,team_against_assists_final).fillna(0)
team_against_period_all_Stats['p1_AS_avg']=(team_against_period_all_Stats['p1_AS']/team_against_period_all_Stats['Games']).round(1)
team_against_period_all_Stats['p2_AS_avg']=(team_against_period_all_Stats['p2_AS']/team_against_period_all_Stats['Games']).round(1)
team_against_period_all_Stats['p3_AS_avg']=(team_against_period_all_Stats['p3_AS']/team_against_period_all_Stats['Games']).round(1)
team_against_period_all_Stats['p4_AS_avg']=(team_against_period_all_Stats['p4_AS']/team_against_period_all_Stats['Games']).round(1)

to_compute_total=pbp_data_df2425.loc[pbp_data_df2425.PLAYTYPE=='TO'][['Against','PERIOD']].value_counts().reset_index().rename(columns={'count':'TO'})
sel_team_to_compute_total=to_compute_total.loc[to_compute_total.Against==search_team_team1]
p1_sel_team_to_compute_total=sel_team_to_compute_total.loc[sel_team_to_compute_total.PERIOD==1][['Against','TO']].rename(columns={'TO':'p1_TO'})
p2_sel_team_to_compute_total=sel_team_to_compute_total.loc[sel_team_to_compute_total.PERIOD==2][['Against','TO']].rename(columns={'TO':'p2_TO'})
p3_sel_team_to_compute_total=sel_team_to_compute_total.loc[sel_team_to_compute_total.PERIOD==3][['Against','TO']].rename(columns={'TO':'p3_TO'})
p4_sel_team_to_compute_total=sel_team_to_compute_total.loc[sel_team_to_compute_total.PERIOD==4][['Against','TO']].rename(columns={'TO':'p4_TO'})
p5_sel_team_to_compute_total=sel_team_to_compute_total.loc[sel_team_to_compute_total.PERIOD==5][['Against','TO']].rename(columns={'TO':'ex_TO'})
team_to_final=pd.merge(p1_sel_team_to_compute_total,p2_sel_team_to_compute_total,on='Against',how='outer')
team_to_final=pd.merge(team_to_final,p3_sel_team_to_compute_total,on='Against',how='outer')
team_to_final=pd.merge(team_to_final,p4_sel_team_to_compute_total,on='Against',how='outer')
team_to_final=pd.merge(team_to_final,p5_sel_team_to_compute_total,on='Against',how='outer')
team_against_period_all_Stats=pd.merge(team_against_period_all_Stats,team_to_final).fillna(0)
team_against_period_all_Stats['p1_TO_avg']=(team_against_period_all_Stats['p1_TO']/team_against_period_all_Stats['Games']).round(1)
team_against_period_all_Stats['p2_TO_avg']=(team_against_period_all_Stats['p2_TO']/team_against_period_all_Stats['Games']).round(1)
team_against_period_all_Stats['p3_TO_avg']=(team_against_period_all_Stats['p3_TO']/team_against_period_all_Stats['Games']).round(1)
team_against_period_all_Stats['p4_TO_avg']=(team_against_period_all_Stats['p4_TO']/team_against_period_all_Stats['Games']).round(1)

dr_compute_total=pbp_data_df2425.loc[pbp_data_df2425.PLAYTYPE=='D'][['Against','PERIOD']].value_counts().reset_index().rename(columns={'count':'DR'}).fillna(0)
sel_team_dr_compute_total=dr_compute_total.loc[dr_compute_total.Against==search_team_team1]
p1_sel_team_dr_compute_total=sel_team_dr_compute_total.loc[sel_team_dr_compute_total.PERIOD==1][['Against','DR']].rename(columns={'DR':'p1_DR'})
p2_sel_team_dr_compute_total=sel_team_dr_compute_total.loc[sel_team_dr_compute_total.PERIOD==2][['Against','DR']].rename(columns={'DR':'p2_DR'})
p3_sel_team_dr_compute_total=sel_team_dr_compute_total.loc[sel_team_dr_compute_total.PERIOD==3][['Against','DR']].rename(columns={'DR':'p3_DR'})
p4_sel_team_dr_compute_total=sel_team_dr_compute_total.loc[sel_team_dr_compute_total.PERIOD==4][['Against','DR']].rename(columns={'DR':'p4_DR'})
p5_sel_team_dr_compute_total=sel_team_dr_compute_total.loc[sel_team_dr_compute_total.PERIOD==5][['Against','DR']].rename(columns={'DR':'ex_DR'})
team_dr_final=pd.merge(p1_sel_team_dr_compute_total,p2_sel_team_dr_compute_total,on='Against',how='outer')
team_dr_final=pd.merge(team_dr_final,p3_sel_team_dr_compute_total,on='Against',how='outer')
team_dr_final=pd.merge(team_dr_final,p4_sel_team_dr_compute_total,on='Against',how='outer')
team_dr_final=pd.merge(team_dr_final,p5_sel_team_dr_compute_total,on='Against',how='outer')
team_against_period_all_Stats=pd.merge(team_against_period_all_Stats,team_dr_final).fillna(0)
team_against_period_all_Stats['p1_DR_avg']=(team_against_period_all_Stats['p1_DR']/team_against_period_all_Stats['Games']).round(1)
team_against_period_all_Stats['p2_DR_avg']=(team_against_period_all_Stats['p2_DR']/team_against_period_all_Stats['Games']).round(1)
team_against_period_all_Stats['p3_DR_avg']=(team_against_period_all_Stats['p3_DR']/team_against_period_all_Stats['Games']).round(1)
team_against_period_all_Stats['p4_DR_avg']=(team_against_period_all_Stats['p4_DR']/team_against_period_all_Stats['Games']).round(1)


OR_compute_total=pbp_data_df2425.loc[pbp_data_df2425.PLAYTYPE=='O'][['Against','PERIOD']].value_counts().reset_index().rename(columns={'count':'OR'}).fillna(0)
sel_team_OR_compute_total=OR_compute_total.loc[OR_compute_total.Against==search_team_team1]
p1_sel_team_OR_compute_total=sel_team_OR_compute_total.loc[sel_team_OR_compute_total.PERIOD==1][['Against','OR']].rename(columns={'OR':'p1_OR'})
p2_sel_team_OR_compute_total=sel_team_OR_compute_total.loc[sel_team_OR_compute_total.PERIOD==2][['Against','OR']].rename(columns={'OR':'p2_OR'})
p3_sel_team_OR_compute_total=sel_team_OR_compute_total.loc[sel_team_OR_compute_total.PERIOD==3][['Against','OR']].rename(columns={'OR':'p3_OR'})
p4_sel_team_OR_compute_total=sel_team_OR_compute_total.loc[sel_team_OR_compute_total.PERIOD==4][['Against','OR']].rename(columns={'OR':'p4_OR'})
p5_sel_team_OR_compute_total=sel_team_OR_compute_total.loc[sel_team_OR_compute_total.PERIOD==5][['Against','OR']].rename(columns={'OR':'ex_OR'})
team_OR_final=pd.merge(p1_sel_team_OR_compute_total,p2_sel_team_OR_compute_total,on='Against',how='outer')
team_OR_final=pd.merge(team_OR_final,p3_sel_team_OR_compute_total,on='Against',how='outer')
team_OR_final=pd.merge(team_OR_final,p4_sel_team_OR_compute_total,on='Against',how='outer')
team_OR_final=pd.merge(team_OR_final,p5_sel_team_OR_compute_total,on='Against',how='outer')
team_against_period_all_Stats=pd.merge(team_against_period_all_Stats,team_OR_final).fillna(0)
team_against_period_all_Stats['p1_OR_avg']=(team_against_period_all_Stats['p1_OR']/team_against_period_all_Stats['Games']).round(1)
team_against_period_all_Stats['p2_OR_avg']=(team_against_period_all_Stats['p2_OR']/team_against_period_all_Stats['Games']).round(1)
team_against_period_all_Stats['p3_OR_avg']=(team_against_period_all_Stats['p3_OR']/team_against_period_all_Stats['Games']).round(1)
team_against_period_all_Stats['p4_OR_avg']=(team_against_period_all_Stats['p4_OR']/team_against_period_all_Stats['Games']).round(1)
team_against_period_all_Stats['p1_TR']=team_against_period_all_Stats['p1_DR']+team_against_period_all_Stats['p1_OR']
team_against_period_all_Stats['p2_TR']=team_against_period_all_Stats['p2_DR']+team_against_period_all_Stats['p2_OR']
team_against_period_all_Stats['p3_TR']=team_against_period_all_Stats['p3_DR']+team_against_period_all_Stats['p3_OR']
team_against_period_all_Stats['p4_TR']=team_against_period_all_Stats['p4_DR']+team_against_period_all_Stats['p4_OR']
team_against_period_all_Stats['ex_TR']=team_against_period_all_Stats['ex_DR']+team_against_period_all_Stats['ex_OR']
team_against_period_all_Stats['p1_TR_avg']=(team_against_period_all_Stats['p1_TR']/team_against_period_all_Stats['Games']).round(1)
team_against_period_all_Stats['p2_TR_avg']=(team_against_period_all_Stats['p2_TR']/team_against_period_all_Stats['Games']).round(1)
team_against_period_all_Stats['p3_TR_avg']=(team_against_period_all_Stats['p3_TR']/team_against_period_all_Stats['Games']).round(1)
team_against_period_all_Stats['p4_TR_avg']=(team_against_period_all_Stats['p4_TR']/team_against_period_all_Stats['Games']).round(1)

STL_compute_total=pbp_data_df2425.loc[pbp_data_df2425.PLAYTYPE=='ST'][['Against','PERIOD']].value_counts().reset_index().rename(columns={'count':'STL'}).fillna(0)
sel_team_STL_compute_total=STL_compute_total.loc[STL_compute_total.Against==search_team_team1]
p1_sel_team_STL_compute_total=sel_team_STL_compute_total.loc[sel_team_STL_compute_total.PERIOD==1][['Against','STL']].rename(columns={'STL':'p1_STL'})
p2_sel_team_STL_compute_total=sel_team_STL_compute_total.loc[sel_team_STL_compute_total.PERIOD==2][['Against','STL']].rename(columns={'STL':'p2_STL'})
p3_sel_team_STL_compute_total=sel_team_STL_compute_total.loc[sel_team_STL_compute_total.PERIOD==3][['Against','STL']].rename(columns={'STL':'p3_STL'})
p4_sel_team_STL_compute_total=sel_team_STL_compute_total.loc[sel_team_STL_compute_total.PERIOD==4][['Against','STL']].rename(columns={'STL':'p4_STL'})
p5_sel_team_STL_compute_total=sel_team_STL_compute_total.loc[sel_team_STL_compute_total.PERIOD==5][['Against','STL']].rename(columns={'STL':'ex_STL'})
team_STL_final=pd.merge(p1_sel_team_STL_compute_total,p2_sel_team_STL_compute_total,on='Against',how='outer')
team_STL_final=pd.merge(team_STL_final,p3_sel_team_STL_compute_total,on='Against',how='outer')
team_STL_final=pd.merge(team_STL_final,p4_sel_team_STL_compute_total,on='Against',how='outer')
team_STL_final=pd.merge(team_STL_final,p5_sel_team_STL_compute_total,on='Against',how='outer')
team_against_period_all_Stats=pd.merge(team_against_period_all_Stats,team_STL_final).fillna(0)
team_against_period_all_Stats['p1_STL_avg']=(team_against_period_all_Stats['p1_STL']/team_against_period_all_Stats['Games']).round(1)
team_against_period_all_Stats['p2_STL_avg']=(team_against_period_all_Stats['p2_STL']/team_against_period_all_Stats['Games']).round(1)
team_against_period_all_Stats['p3_STL_avg']=(team_against_period_all_Stats['p3_STL']/team_against_period_all_Stats['Games']).round(1)
team_against_period_all_Stats['p4_STL_avg']=(team_against_period_all_Stats['p4_STL']/team_against_period_all_Stats['Games']).round(1)

BLKR_compute_total=pbp_data_df2425.loc[pbp_data_df2425.PLAYTYPE=='AG'][['Against','PERIOD']].value_counts().reset_index().rename(columns={'count':'BLKR'}).fillna(0)
sel_team_BLKR_compute_total=BLKR_compute_total.loc[BLKR_compute_total.Against==search_team_team1]
p1_sel_team_BLKR_compute_total=sel_team_BLKR_compute_total.loc[sel_team_BLKR_compute_total.PERIOD==1][['Against','BLKR']].rename(columns={'BLKR':'p1_BLKR'})
p2_sel_team_BLKR_compute_total=sel_team_BLKR_compute_total.loc[sel_team_BLKR_compute_total.PERIOD==2][['Against','BLKR']].rename(columns={'BLKR':'p2_BLKR'})
p3_sel_team_BLKR_compute_total=sel_team_BLKR_compute_total.loc[sel_team_BLKR_compute_total.PERIOD==3][['Against','BLKR']].rename(columns={'BLKR':'p3_BLKR'})
p4_sel_team_BLKR_compute_total=sel_team_BLKR_compute_total.loc[sel_team_BLKR_compute_total.PERIOD==4][['Against','BLKR']].rename(columns={'BLKR':'p4_BLKR'})
p5_sel_team_BLKR_compute_total=sel_team_BLKR_compute_total.loc[sel_team_BLKR_compute_total.PERIOD==5][['Against','BLKR']].rename(columns={'BLKR':'ex_BLKR'})
team_BLKR_final=pd.merge(p1_sel_team_BLKR_compute_total,p2_sel_team_BLKR_compute_total,on='Against',how='outer')
team_BLKR_final=pd.merge(team_BLKR_final,p3_sel_team_BLKR_compute_total,on='Against',how='outer')
team_BLKR_final=pd.merge(team_BLKR_final,p4_sel_team_BLKR_compute_total,on='Against',how='outer')
team_BLKR_final=pd.merge(team_BLKR_final,p5_sel_team_BLKR_compute_total,on='Against',how='outer')
team_against_period_all_Stats=pd.merge(team_against_period_all_Stats,team_BLKR_final).fillna(0)
team_against_period_all_Stats['p1_BLKR_avg']=(team_against_period_all_Stats['p1_BLKR']/team_against_period_all_Stats['Games']).round(1)
team_against_period_all_Stats['p2_BLKR_avg']=(team_against_period_all_Stats['p2_BLKR']/team_against_period_all_Stats['Games']).round(1)
team_against_period_all_Stats['p3_BLKR_avg']=(team_against_period_all_Stats['p3_BLKR']/team_against_period_all_Stats['Games']).round(1)
team_against_period_all_Stats['p4_BLKR_avg']=(team_against_period_all_Stats['p4_BLKR']/team_against_period_all_Stats['Games']).round(1)


BLKM_compute_total=pbp_data_df2425.loc[pbp_data_df2425.PLAYTYPE=='FV'][['Against','PERIOD']].value_counts().reset_index().rename(columns={'count':'BLKM'}).fillna(0)
sel_team_BLKM_compute_total=BLKM_compute_total.loc[BLKM_compute_total.Against==search_team_team1]
p1_sel_team_BLKM_compute_total=sel_team_BLKM_compute_total.loc[sel_team_BLKM_compute_total.PERIOD==1][['Against','BLKM']].rename(columns={'BLKM':'p1_BLKM'})
p2_sel_team_BLKM_compute_total=sel_team_BLKM_compute_total.loc[sel_team_BLKM_compute_total.PERIOD==2][['Against','BLKM']].rename(columns={'BLKM':'p2_BLKM'})
p3_sel_team_BLKM_compute_total=sel_team_BLKM_compute_total.loc[sel_team_BLKM_compute_total.PERIOD==3][['Against','BLKM']].rename(columns={'BLKM':'p3_BLKM'})
p4_sel_team_BLKM_compute_total=sel_team_BLKM_compute_total.loc[sel_team_BLKM_compute_total.PERIOD==4][['Against','BLKM']].rename(columns={'BLKM':'p4_BLKM'})
p5_sel_team_BLKM_compute_total=sel_team_BLKM_compute_total.loc[sel_team_BLKM_compute_total.PERIOD==5][['Against','BLKM']].rename(columns={'BLKM':'ex_BLKM'})
team_BLKM_final=pd.merge(p1_sel_team_BLKM_compute_total,p2_sel_team_BLKM_compute_total,on='Against',how='outer')
team_BLKM_final=pd.merge(team_BLKM_final,p3_sel_team_BLKM_compute_total,on='Against',how='outer')
team_BLKM_final=pd.merge(team_BLKM_final,p4_sel_team_BLKM_compute_total,on='Against',how='outer')
team_BLKM_final=pd.merge(team_BLKM_final,p5_sel_team_BLKM_compute_total,on='Against',how='outer')
team_against_period_all_Stats=pd.merge(team_against_period_all_Stats,team_BLKM_final).fillna(0)
team_against_period_all_Stats['p1_BLKM_avg']=(team_against_period_all_Stats['p1_BLKM']/team_against_period_all_Stats['Games']).round(1)
team_against_period_all_Stats['p2_BLKM_avg']=(team_against_period_all_Stats['p2_BLKM']/team_against_period_all_Stats['Games']).round(1)
team_against_period_all_Stats['p3_BLKM_avg']=(team_against_period_all_Stats['p3_BLKM']/team_against_period_all_Stats['Games']).round(1)
team_against_period_all_Stats['p4_BLKM_avg']=(team_against_period_all_Stats['p4_BLKM']/team_against_period_all_Stats['Games']).round(1)


RF_compute_total=pbp_data_df2425.loc[pbp_data_df2425.PLAYTYPE=='RV'][['Against','PERIOD']].value_counts().reset_index().rename(columns={'count':'RF'}).fillna(0)
sel_team_RF_compute_total=RF_compute_total.loc[RF_compute_total.Against==search_team_team1]
p1_sel_team_RF_compute_total=sel_team_RF_compute_total.loc[sel_team_RF_compute_total.PERIOD==1][['Against','RF']].rename(columns={'RF':'p1_RF'})
p2_sel_team_RF_compute_total=sel_team_RF_compute_total.loc[sel_team_RF_compute_total.PERIOD==2][['Against','RF']].rename(columns={'RF':'p2_RF'})
p3_sel_team_RF_compute_total=sel_team_RF_compute_total.loc[sel_team_RF_compute_total.PERIOD==3][['Against','RF']].rename(columns={'RF':'p3_RF'})
p4_sel_team_RF_compute_total=sel_team_RF_compute_total.loc[sel_team_RF_compute_total.PERIOD==4][['Against','RF']].rename(columns={'RF':'p4_RF'})
p5_sel_team_RF_compute_total=sel_team_RF_compute_total.loc[sel_team_RF_compute_total.PERIOD==5][['Against','RF']].rename(columns={'RF':'ex_RF'})
team_RF_final=pd.merge(p1_sel_team_RF_compute_total,p2_sel_team_RF_compute_total,on='Against',how='outer')
team_RF_final=pd.merge(team_RF_final,p3_sel_team_RF_compute_total,on='Against',how='outer')
team_RF_final=pd.merge(team_RF_final,p4_sel_team_RF_compute_total,on='Against',how='outer')
team_RF_final=pd.merge(team_RF_final,p5_sel_team_RF_compute_total,on='Against',how='outer')
team_against_period_all_Stats=pd.merge(team_against_period_all_Stats,team_RF_final).fillna(0)
team_against_period_all_Stats['p1_RF_avg']=(team_against_period_all_Stats['p1_RF']/team_against_period_all_Stats['Games']).round(1)
team_against_period_all_Stats['p2_RF_avg']=(team_against_period_all_Stats['p2_RF']/team_against_period_all_Stats['Games']).round(1)
team_against_period_all_Stats['p3_RF_avg']=(team_against_period_all_Stats['p3_RF']/team_against_period_all_Stats['Games']).round(1)
team_against_period_all_Stats['p4_RF_avg']=(team_against_period_all_Stats['p4_RF']/team_against_period_all_Stats['Games']).round(1)


DF_compute_total=pbp_data_df2425.loc[pbp_data_df2425.PLAYTYPE=='CM'][['Against','PERIOD']].value_counts().reset_index().rename(columns={'count':'DF'}).fillna(0)
sel_team_DF_compute_total=DF_compute_total.loc[DF_compute_total.Against==search_team_team1]
p1_sel_team_DF_compute_total=sel_team_DF_compute_total.loc[sel_team_DF_compute_total.PERIOD==1][['Against','DF']].rename(columns={'DF':'p1_DF'})
p2_sel_team_DF_compute_total=sel_team_DF_compute_total.loc[sel_team_DF_compute_total.PERIOD==2][['Against','DF']].rename(columns={'DF':'p2_DF'})
p3_sel_team_DF_compute_total=sel_team_DF_compute_total.loc[sel_team_DF_compute_total.PERIOD==3][['Against','DF']].rename(columns={'DF':'p3_DF'})
p4_sel_team_DF_compute_total=sel_team_DF_compute_total.loc[sel_team_DF_compute_total.PERIOD==4][['Against','DF']].rename(columns={'DF':'p4_DF'})
p5_sel_team_DF_compute_total=sel_team_DF_compute_total.loc[sel_team_DF_compute_total.PERIOD==5][['Against','DF']].rename(columns={'DF':'ex_DF'})
team_DF_final=pd.merge(p1_sel_team_DF_compute_total,p2_sel_team_DF_compute_total,on='Against',how='outer')
team_DF_final=pd.merge(team_DF_final,p3_sel_team_DF_compute_total,on='Against',how='outer')
team_DF_final=pd.merge(team_DF_final,p4_sel_team_DF_compute_total,on='Against',how='outer')
team_DF_final=pd.merge(team_DF_final,p5_sel_team_DF_compute_total,on='Against',how='outer')
team_against_period_all_Stats=pd.merge(team_against_period_all_Stats,team_DF_final).fillna(0)
team_against_period_all_Stats['p1_DF_avg']=(team_against_period_all_Stats['p1_DF']/team_against_period_all_Stats['Games']).round(1)
team_against_period_all_Stats['p2_DF_avg']=(team_against_period_all_Stats['p2_DF']/team_against_period_all_Stats['Games']).round(1)
team_against_period_all_Stats['p3_DF_avg']=(team_against_period_all_Stats['p3_DF']/team_against_period_all_Stats['Games']).round(1)
team_against_period_all_Stats['p4_DF_avg']=(team_against_period_all_Stats['p4_DF']/team_against_period_all_Stats['Games']).round(1)

OF_compute_total=pbp_data_df2425.loc[pbp_data_df2425.PLAYTYPE=='OF'][['Against','PERIOD']].value_counts().reset_index().rename(columns={'count':'OF'}).fillna(0)
sel_team_OF_compute_total=OF_compute_total.loc[OF_compute_total.Against==search_team_team1]
p1_sel_team_OF_compute_total=sel_team_OF_compute_total.loc[sel_team_OF_compute_total.PERIOD==1][['Against','OF']].rename(columns={'OF':'p1_OF'})
p2_sel_team_OF_compute_total=sel_team_OF_compute_total.loc[sel_team_OF_compute_total.PERIOD==2][['Against','OF']].rename(columns={'OF':'p2_OF'})
p3_sel_team_OF_compute_total=sel_team_OF_compute_total.loc[sel_team_OF_compute_total.PERIOD==3][['Against','OF']].rename(columns={'OF':'p3_OF'})
p4_sel_team_OF_compute_total=sel_team_OF_compute_total.loc[sel_team_OF_compute_total.PERIOD==4][['Against','OF']].rename(columns={'OF':'p4_OF'})
p5_sel_team_OF_compute_total=sel_team_OF_compute_total.loc[sel_team_OF_compute_total.PERIOD==5][['Against','OF']].rename(columns={'OF':'ex_OF'})
team_OF_final=pd.merge(p1_sel_team_OF_compute_total,p2_sel_team_OF_compute_total,on='Against',how='outer')
team_OF_final=pd.merge(team_OF_final,p3_sel_team_OF_compute_total,on='Against',how='outer')
team_OF_final=pd.merge(team_OF_final,p4_sel_team_OF_compute_total,on='Against',how='outer')
team_OF_final=pd.merge(team_OF_final,p5_sel_team_OF_compute_total,on='Against',how='outer')
team_against_period_all_Stats=pd.merge(team_against_period_all_Stats,team_OF_final).fillna(0)
team_against_period_all_Stats['p1_OF_avg']=(team_against_period_all_Stats['p1_OF']/team_against_period_all_Stats['Games']).round(1)
team_against_period_all_Stats['p2_OF_avg']=(team_against_period_all_Stats['p2_OF']/team_against_period_all_Stats['Games']).round(1)
team_against_period_all_Stats['p3_OF_avg']=(team_against_period_all_Stats['p3_OF']/team_against_period_all_Stats['Games']).round(1)
team_against_period_all_Stats['p4_OF_avg']=(team_against_period_all_Stats['p4_OF']/team_against_period_all_Stats['Games']).round(1)

UNF_compute_total=pbp_data_df2425.loc[pbp_data_df2425.PLAYTYPE.isin(['CMD','CMU'])][['Against','PERIOD']].value_counts().reset_index().rename(columns={'count':'UNF'}).fillna(0)
sel_team_UNF_compute_total=UNF_compute_total.loc[UNF_compute_total.Against==search_team_team1]
p1_sel_team_UNF_compute_total=sel_team_UNF_compute_total.loc[sel_team_UNF_compute_total.PERIOD==1][['Against','UNF']].rename(columns={'UNF':'p1_UNF'})
p2_sel_team_UNF_compute_total=sel_team_UNF_compute_total.loc[sel_team_UNF_compute_total.PERIOD==2][['Against','UNF']].rename(columns={'UNF':'p2_UNF'})
p3_sel_team_UNF_compute_total=sel_team_UNF_compute_total.loc[sel_team_UNF_compute_total.PERIOD==3][['Against','UNF']].rename(columns={'UNF':'p3_UNF'})
p4_sel_team_UNF_compute_total=sel_team_UNF_compute_total.loc[sel_team_UNF_compute_total.PERIOD==4][['Against','UNF']].rename(columns={'UNF':'p4_UNF'})
p5_sel_team_UNF_compute_total=sel_team_UNF_compute_total.loc[sel_team_UNF_compute_total.PERIOD==5][['Against','UNF']].rename(columns={'UNF':'ex_UNF'})
team_UNF_final=pd.merge(p1_sel_team_UNF_compute_total,p2_sel_team_UNF_compute_total,on='Against',how='outer')
team_UNF_final=pd.merge(team_UNF_final,p3_sel_team_UNF_compute_total,on='Against',how='outer')
team_UNF_final=pd.merge(team_UNF_final,p4_sel_team_UNF_compute_total,on='Against',how='outer')
team_UNF_final=pd.merge(team_UNF_final,p5_sel_team_UNF_compute_total,on='Against',how='outer')
team_against_period_all_Stats=pd.merge(team_against_period_all_Stats,team_UNF_final).fillna(0)
team_against_period_all_Stats['p1_UNF_avg']=(team_against_period_all_Stats['p1_UNF']/team_against_period_all_Stats['Games']).round(1)
team_against_period_all_Stats['p2_UNF_avg']=(team_against_period_all_Stats['p2_UNF']/team_against_period_all_Stats['Games']).round(1)
team_against_period_all_Stats['p3_UNF_avg']=(team_against_period_all_Stats['p3_UNF']/team_against_period_all_Stats['Games']).round(1)
team_against_period_all_Stats['p4_UNF_avg']=(team_against_period_all_Stats['p4_UNF']/team_against_period_all_Stats['Games']).round(1)



TF_compute_total=pbp_data_df2425.loc[pbp_data_df2425.PLAYTYPE=='CMT'][['Against','PERIOD']].value_counts().reset_index().rename(columns={'count':'TF'}).fillna(0)
sel_team_TF_compute_total=TF_compute_total.loc[TF_compute_total.Against==search_team_team1]
p1_sel_team_TF_compute_total=sel_team_TF_compute_total.loc[sel_team_TF_compute_total.PERIOD==1][['Against','TF']].rename(columns={'TF':'p1_TF'})
p2_sel_team_TF_compute_total=sel_team_TF_compute_total.loc[sel_team_TF_compute_total.PERIOD==2][['Against','TF']].rename(columns={'TF':'p2_TF'})
p3_sel_team_TF_compute_total=sel_team_TF_compute_total.loc[sel_team_TF_compute_total.PERIOD==3][['Against','TF']].rename(columns={'TF':'p3_TF'})
p4_sel_team_TF_compute_total=sel_team_TF_compute_total.loc[sel_team_TF_compute_total.PERIOD==4][['Against','TF']].rename(columns={'TF':'p4_TF'})
p5_sel_team_TF_compute_total=sel_team_TF_compute_total.loc[sel_team_TF_compute_total.PERIOD==5][['Against','TF']].rename(columns={'TF':'ex_TF'})
team_TF_final=pd.merge(p1_sel_team_TF_compute_total,p2_sel_team_TF_compute_total,on='Against',how='outer')
team_TF_final=pd.merge(team_TF_final,p3_sel_team_TF_compute_total,on='Against',how='outer')
team_TF_final=pd.merge(team_TF_final,p4_sel_team_TF_compute_total,on='Against',how='outer')
team_TF_final=pd.merge(team_TF_final,p5_sel_team_TF_compute_total,on='Against',how='outer')
team_against_period_all_Stats=pd.merge(team_against_period_all_Stats,team_TF_final).fillna(0)
team_against_period_all_Stats['p1_TF_avg']=(team_against_period_all_Stats['p1_TF']/team_against_period_all_Stats['Games']).round(1)
team_against_period_all_Stats['p2_TF_avg']=(team_against_period_all_Stats['p2_TF']/team_against_period_all_Stats['Games']).round(1)
team_against_period_all_Stats['p3_TF_avg']=(team_against_period_all_Stats['p3_TF']/team_against_period_all_Stats['Games']).round(1)
team_against_period_all_Stats['p4_TF_avg']=(team_against_period_all_Stats['p4_TF']/team_against_period_all_Stats['Games']).round(1)
team_against_period_all_Stats['p1_PF']=team_against_period_all_Stats['p1_DF']+team_against_period_all_Stats['p1_OF']+team_against_period_all_Stats['p1_UNF']+team_against_period_all_Stats['p1_TF']
team_against_period_all_Stats['p2_PF']=team_against_period_all_Stats['p2_DF']+team_against_period_all_Stats['p2_OF']+team_against_period_all_Stats['p2_UNF']+team_against_period_all_Stats['p2_TF']
team_against_period_all_Stats['p3_PF']=team_against_period_all_Stats['p3_DF']+team_against_period_all_Stats['p3_OF']+team_against_period_all_Stats['p3_UNF']+team_against_period_all_Stats['p3_TF']
team_against_period_all_Stats['p4_PF']=team_against_period_all_Stats['p4_DF']+team_against_period_all_Stats['p4_OF']+team_against_period_all_Stats['p4_UNF']+team_against_period_all_Stats['p4_TF']
team_against_period_all_Stats['ex_PF']=team_against_period_all_Stats['ex_DF']+team_against_period_all_Stats['ex_OF']+team_against_period_all_Stats['ex_UNF']+team_against_period_all_Stats['ex_TF']

team_against_period_all_Stats['p1_PF_avg']=(team_against_period_all_Stats['p1_PF']/team_against_period_all_Stats['Games']).round(1)
team_against_period_all_Stats['p2_PF_avg']=(team_against_period_all_Stats['p2_PF']/team_against_period_all_Stats['Games']).round(1)
team_against_period_all_Stats['p3_PF_avg']=(team_against_period_all_Stats['p3_PF']/team_against_period_all_Stats['Games']).round(1)
team_against_period_all_Stats['p4_PF_avg']=(team_against_period_all_Stats['p4_PF']/team_against_period_all_Stats['Games']).round(1)


P2M_compute_total=pbp_data_df2425.loc[pbp_data_df2425.PLAYTYPE=='2FGM'][['Against','PERIOD']].value_counts().reset_index().rename(columns={'count':'P2M'}).fillna(0)
sel_team_P2M_compute_total=P2M_compute_total.loc[P2M_compute_total.Against==search_team_team1]
p1_sel_team_P2M_compute_total=sel_team_P2M_compute_total.loc[sel_team_P2M_compute_total.PERIOD==1][['Against','P2M']].rename(columns={'P2M':'p1_2PM'})
p2_sel_team_P2M_compute_total=sel_team_P2M_compute_total.loc[sel_team_P2M_compute_total.PERIOD==2][['Against','P2M']].rename(columns={'P2M':'p2_2PM'})
p3_sel_team_P2M_compute_total=sel_team_P2M_compute_total.loc[sel_team_P2M_compute_total.PERIOD==3][['Against','P2M']].rename(columns={'P2M':'p3_2PM'})
p4_sel_team_P2M_compute_total=sel_team_P2M_compute_total.loc[sel_team_P2M_compute_total.PERIOD==4][['Against','P2M']].rename(columns={'P2M':'p4_2PM'})
p5_sel_team_P2M_compute_total=sel_team_P2M_compute_total.loc[sel_team_P2M_compute_total.PERIOD==5][['Against','P2M']].rename(columns={'P2M':'ex_2PM'})
team_P2M_final=pd.merge(p1_sel_team_P2M_compute_total,p2_sel_team_P2M_compute_total,on='Against',how='outer')
team_P2M_final=pd.merge(team_P2M_final,p3_sel_team_P2M_compute_total,on='Against',how='outer')
team_P2M_final=pd.merge(team_P2M_final,p4_sel_team_P2M_compute_total,on='Against',how='outer')
team_P2M_final=pd.merge(team_P2M_final,p5_sel_team_P2M_compute_total,on='Against',how='outer')
team_against_period_all_Stats=pd.merge(team_against_period_all_Stats,team_P2M_final).fillna(0)
team_against_period_all_Stats['p1_2PM_avg']=(team_against_period_all_Stats['p1_2PM']/team_against_period_all_Stats['Games']).round(1)
team_against_period_all_Stats['p2_2PM_avg']=(team_against_period_all_Stats['p2_2PM']/team_against_period_all_Stats['Games']).round(1)
team_against_period_all_Stats['p3_2PM_avg']=(team_against_period_all_Stats['p3_2PM']/team_against_period_all_Stats['Games']).round(1)
team_against_period_all_Stats['p4_2PM_avg']=(team_against_period_all_Stats['p4_2PM']/team_against_period_all_Stats['Games']).round(1)


p2a_compute_total=pbp_data_df2425.loc[pbp_data_df2425.PLAYTYPE.isin(['2FGA','2FGM'])].reset_index()[['Against','PERIOD']].value_counts().reset_index().rename(columns={'count':'2PA'}).fillna(0)
sel_team_p2a_compute_total=p2a_compute_total.loc[p2a_compute_total.Against==search_team_team1]
p1_sel_team_p2a_compute_total=sel_team_p2a_compute_total.loc[sel_team_p2a_compute_total.PERIOD==1][['Against','2PA']].rename(columns={'2PA':'p1_2PA'})
p2_sel_team_p2a_compute_total=sel_team_p2a_compute_total.loc[sel_team_p2a_compute_total.PERIOD==2][['Against','2PA']].rename(columns={'2PA':'p2_2PA'})
p3_sel_team_p2a_compute_total=sel_team_p2a_compute_total.loc[sel_team_p2a_compute_total.PERIOD==3][['Against','2PA']].rename(columns={'2PA':'p3_2PA'})
p4_sel_team_p2a_compute_total=sel_team_p2a_compute_total.loc[sel_team_p2a_compute_total.PERIOD==4][['Against','2PA']].rename(columns={'2PA':'p4_2PA'})
p5_sel_team_p2a_compute_total=sel_team_p2a_compute_total.loc[sel_team_p2a_compute_total.PERIOD==5][['Against','2PA']].rename(columns={'2PA':'ex_2PA'})
team_p2a_final=pd.merge(p1_sel_team_p2a_compute_total,p2_sel_team_p2a_compute_total,on='Against',how='outer')
team_p2a_final=pd.merge(team_p2a_final,p3_sel_team_p2a_compute_total,on='Against',how='outer')
team_p2a_final=pd.merge(team_p2a_final,p4_sel_team_p2a_compute_total,on='Against',how='outer')
team_p2a_final=pd.merge(team_p2a_final,p5_sel_team_p2a_compute_total,on='Against',how='outer')

team_against_period_all_Stats=pd.merge(team_against_period_all_Stats,team_p2a_final,on='Against',how='outer').fillna(0)
team_against_period_all_Stats['p1_2PA_avg']=(team_against_period_all_Stats['p1_2PA']/team_against_period_all_Stats['Games']).round(1)
team_against_period_all_Stats['p2_2PA_avg']=(team_against_period_all_Stats['p2_2PA']/team_against_period_all_Stats['Games']).round(1)
team_against_period_all_Stats['p3_2PA_avg']=(team_against_period_all_Stats['p3_2PA']/team_against_period_all_Stats['Games']).round(1)
team_against_period_all_Stats['p4_2PA_avg']=(team_against_period_all_Stats['p4_2PA']/team_against_period_all_Stats['Games']).round(1)
team_against_period_all_Stats['p1_2P(%)']=(100*team_against_period_all_Stats['p1_2PM']/team_against_period_all_Stats['p1_2PA']).round(1)
team_against_period_all_Stats['p2_2P(%)']=(100*team_against_period_all_Stats['p2_2PM']/team_against_period_all_Stats['p2_2PA']).round(1)
team_against_period_all_Stats['p3_2P(%)']=(100*team_against_period_all_Stats['p3_2PM']/team_against_period_all_Stats['p3_2PA']).round(1)
team_against_period_all_Stats['p4_2P(%)']=(100*team_against_period_all_Stats['p4_2PM']/team_against_period_all_Stats['p4_2PA']).round(1)
team_against_period_all_Stats['ex_2P(%)']=(100*team_against_period_all_Stats['ex_2PM']/team_against_period_all_Stats['ex_2PA']).round(1)



P3M_compute_total=pbp_data_df2425.loc[pbp_data_df2425.PLAYTYPE=='3FGM'][['Against','PERIOD']].value_counts().reset_index().rename(columns={'count':'P3M'}).fillna(0)
sel_team_P3M_compute_total=P3M_compute_total.loc[P3M_compute_total.Against==search_team_team1]
p1_sel_team_P3M_compute_total=sel_team_P3M_compute_total.loc[sel_team_P3M_compute_total.PERIOD==1][['Against','P3M']].rename(columns={'P3M':'p1_3PM'})
p2_sel_team_P3M_compute_total=sel_team_P3M_compute_total.loc[sel_team_P3M_compute_total.PERIOD==2][['Against','P3M']].rename(columns={'P3M':'p2_3PM'})
p3_sel_team_P3M_compute_total=sel_team_P3M_compute_total.loc[sel_team_P3M_compute_total.PERIOD==3][['Against','P3M']].rename(columns={'P3M':'p3_3PM'})
p4_sel_team_P3M_compute_total=sel_team_P3M_compute_total.loc[sel_team_P3M_compute_total.PERIOD==4][['Against','P3M']].rename(columns={'P3M':'p4_3PM'})
p5_sel_team_P3M_compute_total=sel_team_P3M_compute_total.loc[sel_team_P3M_compute_total.PERIOD==5][['Against','P3M']].rename(columns={'P3M':'ex_3PM'})
team_P3M_final=pd.merge(p1_sel_team_P3M_compute_total,p2_sel_team_P3M_compute_total,on='Against',how='outer')
team_P3M_final=pd.merge(team_P3M_final,p3_sel_team_P3M_compute_total,on='Against',how='outer')
team_P3M_final=pd.merge(team_P3M_final,p4_sel_team_P3M_compute_total,on='Against',how='outer')
team_P3M_final=pd.merge(team_P3M_final,p5_sel_team_P3M_compute_total,on='Against',how='outer')
team_against_period_all_Stats=pd.merge(team_against_period_all_Stats,team_P3M_final).fillna(0)
team_against_period_all_Stats['p1_3PM_avg']=(team_against_period_all_Stats['p1_3PM']/team_against_period_all_Stats['Games']).round(1)
team_against_period_all_Stats['p2_3PM_avg']=(team_against_period_all_Stats['p2_3PM']/team_against_period_all_Stats['Games']).round(1)
team_against_period_all_Stats['p3_3PM_avg']=(team_against_period_all_Stats['p3_3PM']/team_against_period_all_Stats['Games']).round(1)
team_against_period_all_Stats['p4_3PM_avg']=(team_against_period_all_Stats['p4_3PM']/team_against_period_all_Stats['Games']).round(1)



p3a_compute_total=pbp_data_df2425.loc[pbp_data_df2425.PLAYTYPE.isin(['3FGA','3FGM'])].reset_index()[['Against','PERIOD']].value_counts().reset_index().rename(columns={'count':'3PA'}).fillna(0)
sel_team_p3a_compute_total=p3a_compute_total.loc[p3a_compute_total.Against==search_team_team1]
p1_sel_team_p3a_compute_total=sel_team_p3a_compute_total.loc[sel_team_p3a_compute_total.PERIOD==1][['Against','3PA']].rename(columns={'3PA':'p1_3PA'})
p2_sel_team_p3a_compute_total=sel_team_p3a_compute_total.loc[sel_team_p3a_compute_total.PERIOD==2][['Against','3PA']].rename(columns={'3PA':'p2_3PA'})
p3_sel_team_p3a_compute_total=sel_team_p3a_compute_total.loc[sel_team_p3a_compute_total.PERIOD==3][['Against','3PA']].rename(columns={'3PA':'p3_3PA'})
p4_sel_team_p3a_compute_total=sel_team_p3a_compute_total.loc[sel_team_p3a_compute_total.PERIOD==4][['Against','3PA']].rename(columns={'3PA':'p4_3PA'})
p5_sel_team_p3a_compute_total=sel_team_p3a_compute_total.loc[sel_team_p3a_compute_total.PERIOD==5][['Against','3PA']].rename(columns={'3PA':'ex_3PA'})
team_p3a_final=pd.merge(p1_sel_team_p3a_compute_total,p2_sel_team_p3a_compute_total,on='Against',how='outer')
team_p3a_final=pd.merge(team_p3a_final,p3_sel_team_p3a_compute_total,on='Against',how='outer')
team_p3a_final=pd.merge(team_p3a_final,p4_sel_team_p3a_compute_total,on='Against',how='outer')
team_p3a_final=pd.merge(team_p3a_final,p5_sel_team_p3a_compute_total,on='Against',how='outer')

team_against_period_all_Stats=pd.merge(team_against_period_all_Stats,team_p3a_final,on='Against',how='outer').fillna(0)
team_against_period_all_Stats['p1_3PA_avg']=(team_against_period_all_Stats['p1_3PA']/team_against_period_all_Stats['Games']).round(1)
team_against_period_all_Stats['p2_3PA_avg']=(team_against_period_all_Stats['p2_3PA']/team_against_period_all_Stats['Games']).round(1)
team_against_period_all_Stats['p3_3PA_avg']=(team_against_period_all_Stats['p3_3PA']/team_against_period_all_Stats['Games']).round(1)
team_against_period_all_Stats['p4_3PA_avg']=(team_against_period_all_Stats['p4_3PA']/team_against_period_all_Stats['Games']).round(1)
team_against_period_all_Stats['p1_3P(%)']=(100*team_against_period_all_Stats['p1_3PM']/team_against_period_all_Stats['p1_3PA']).round(1)
team_against_period_all_Stats['p2_3P(%)']=(100*team_against_period_all_Stats['p2_3PM']/team_against_period_all_Stats['p2_3PA']).round(1)
team_against_period_all_Stats['p3_3P(%)']=(100*team_against_period_all_Stats['p3_3PM']/team_against_period_all_Stats['p3_3PA']).round(1)
team_against_period_all_Stats['p4_3P(%)']=(100*team_against_period_all_Stats['p4_3PM']/team_against_period_all_Stats['p4_3PA']).round(1)
team_against_period_all_Stats['ex_3P(%)']=(100*team_against_period_all_Stats['ex_3PM']/team_against_period_all_Stats['ex_3PA']).round(1)



FTM_compute_total=pbp_data_df2425.loc[pbp_data_df2425.PLAYTYPE=='FTM'][['Against','PERIOD']].value_counts().reset_index().rename(columns={'count':'FTM'}).fillna(0)
sel_team_FTM_compute_total=FTM_compute_total.loc[FTM_compute_total.Against==search_team_team1]
p1_sel_team_FTM_compute_total=sel_team_FTM_compute_total.loc[sel_team_FTM_compute_total.PERIOD==1][['Against','FTM']].rename(columns={'FTM':'p1_FTM'})
p2_sel_team_FTM_compute_total=sel_team_FTM_compute_total.loc[sel_team_FTM_compute_total.PERIOD==2][['Against','FTM']].rename(columns={'FTM':'p2_FTM'})
p3_sel_team_FTM_compute_total=sel_team_FTM_compute_total.loc[sel_team_FTM_compute_total.PERIOD==3][['Against','FTM']].rename(columns={'FTM':'p3_FTM'})
p4_sel_team_FTM_compute_total=sel_team_FTM_compute_total.loc[sel_team_FTM_compute_total.PERIOD==4][['Against','FTM']].rename(columns={'FTM':'p4_FTM'})
p5_sel_team_FTM_compute_total=sel_team_FTM_compute_total.loc[sel_team_FTM_compute_total.PERIOD==5][['Against','FTM']].rename(columns={'FTM':'ex_FTM'})
team_FTM_final=pd.merge(p1_sel_team_FTM_compute_total,p2_sel_team_FTM_compute_total,on='Against',how='outer')
team_FTM_final=pd.merge(team_FTM_final,p3_sel_team_FTM_compute_total,on='Against',how='outer')
team_FTM_final=pd.merge(team_FTM_final,p4_sel_team_FTM_compute_total,on='Against',how='outer')
team_FTM_final=pd.merge(team_FTM_final,p5_sel_team_FTM_compute_total,on='Against',how='outer')
team_against_period_all_Stats=pd.merge(team_against_period_all_Stats,team_FTM_final).fillna(0)
team_against_period_all_Stats['p1_FTM_avg']=(team_against_period_all_Stats['p1_FTM']/team_against_period_all_Stats['Games']).round(1)
team_against_period_all_Stats['p2_FTM_avg']=(team_against_period_all_Stats['p2_FTM']/team_against_period_all_Stats['Games']).round(1)
team_against_period_all_Stats['p3_FTM_avg']=(team_against_period_all_Stats['p3_FTM']/team_against_period_all_Stats['Games']).round(1)
team_against_period_all_Stats['p4_FTM_avg']=(team_against_period_all_Stats['p4_FTM']/team_against_period_all_Stats['Games']).round(1)



p3a_compute_total=pbp_data_df2425.loc[pbp_data_df2425.PLAYTYPE.isin(['FTA','FTM'])].reset_index()[['Against','PERIOD']].value_counts().reset_index().rename(columns={'count':'FTA'}).fillna(0)
sel_team_p3a_compute_total=p3a_compute_total.loc[p3a_compute_total.Against==search_team_team1]
p1_sel_team_p3a_compute_total=sel_team_p3a_compute_total.loc[sel_team_p3a_compute_total.PERIOD==1][['Against','FTA']].rename(columns={'FTA':'p1_FTA'})
p2_sel_team_p3a_compute_total=sel_team_p3a_compute_total.loc[sel_team_p3a_compute_total.PERIOD==2][['Against','FTA']].rename(columns={'FTA':'p2_FTA'})
p3_sel_team_p3a_compute_total=sel_team_p3a_compute_total.loc[sel_team_p3a_compute_total.PERIOD==3][['Against','FTA']].rename(columns={'FTA':'p3_FTA'})
p4_sel_team_p3a_compute_total=sel_team_p3a_compute_total.loc[sel_team_p3a_compute_total.PERIOD==4][['Against','FTA']].rename(columns={'FTA':'p4_FTA'})
p5_sel_team_p3a_compute_total=sel_team_p3a_compute_total.loc[sel_team_p3a_compute_total.PERIOD==5][['Against','FTA']].rename(columns={'FTA':'ex_FTA'})
team_p3a_final=pd.merge(p1_sel_team_p3a_compute_total,p2_sel_team_p3a_compute_total,on='Against',how='outer')
team_p3a_final=pd.merge(team_p3a_final,p3_sel_team_p3a_compute_total,on='Against',how='outer')
team_p3a_final=pd.merge(team_p3a_final,p4_sel_team_p3a_compute_total,on='Against',how='outer')
team_p3a_final=pd.merge(team_p3a_final,p5_sel_team_p3a_compute_total,on='Against',how='outer')

team_against_period_all_Stats=pd.merge(team_against_period_all_Stats,team_p3a_final,on='Against',how='outer').fillna(0)
team_against_period_all_Stats['p1_FTA_avg']=(team_against_period_all_Stats['p1_FTA']/team_against_period_all_Stats['Games']).round(1)
team_against_period_all_Stats['p2_FTA_avg']=(team_against_period_all_Stats['p2_FTA']/team_against_period_all_Stats['Games']).round(1)
team_against_period_all_Stats['p3_FTA_avg']=(team_against_period_all_Stats['p3_FTA']/team_against_period_all_Stats['Games']).round(1)
team_against_period_all_Stats['p4_FTA_avg']=(team_against_period_all_Stats['p4_FTA']/team_against_period_all_Stats['Games']).round(1)
team_against_period_all_Stats['p1_FT(%)']=(100*team_against_period_all_Stats['p1_FTM']/team_against_period_all_Stats['p1_FTA']).round(1)
team_against_period_all_Stats['p2_FT(%)']=(100*team_against_period_all_Stats['p2_FTM']/team_against_period_all_Stats['p2_FTA']).round(1)
team_against_period_all_Stats['p3_FT(%)']=(100*team_against_period_all_Stats['p3_FTM']/team_against_period_all_Stats['p3_FTA']).round(1)
team_against_period_all_Stats['p4_FT(%)']=(100*team_against_period_all_Stats['p4_FTM']/team_against_period_all_Stats['p4_FTA']).round(1)
team_against_period_all_Stats['ex_FT(%)']=(100*team_against_period_all_Stats['ex_FTM']/team_against_period_all_Stats['ex_FTA']).round(1)
team_against_period_all_Stats["p1_PIR"]=(team_against_period_all_Stats["p1_PTS"].fillna(0)+
                                         team_against_period_all_Stats["p1_AS"].fillna(0)+
                                         team_against_period_all_Stats["p1_TR"].fillna(0)-
                                         team_against_period_all_Stats["p1_TO"].fillna(0)+
                                         team_against_period_all_Stats["p1_STL"].fillna(0)+
                                         team_against_period_all_Stats["p1_BLKM"].fillna(0)-
                                         team_against_period_all_Stats["p1_BLKR"].fillna(0)-
                                         team_against_period_all_Stats["p1_PF"].fillna(0)+
                                         team_against_period_all_Stats["p1_2PM"].fillna(0)+team_against_period_all_Stats["p1_3PM"].fillna(0)+team_against_period_all_Stats["p1_FTM"].fillna(0)-
                                         team_against_period_all_Stats["p1_2PA"].fillna(0)-team_against_period_all_Stats["p1_3PA"].fillna(0)+team_against_period_all_Stats["p1_FTA"].fillna(0))
team_against_period_all_Stats["p2_PIR"] = (team_against_period_all_Stats["p2_PTS"].fillna(0) +
                                           team_against_period_all_Stats["p2_AS"].fillna(0) +
                                           team_against_period_all_Stats["p2_TR"].fillna(0) -
                                           team_against_period_all_Stats["p2_TO"].fillna(0) +
                                           team_against_period_all_Stats["p2_STL"].fillna(0) +
                                           team_against_period_all_Stats["p2_BLKM"].fillna(0) -
                                           team_against_period_all_Stats["p2_BLKR"].fillna(0) -
                                           team_against_period_all_Stats["p2_PF"].fillna(0) +
                                           team_against_period_all_Stats["p2_2PM"].fillna(0) + team_against_period_all_Stats[
                                               "p2_3PM"].fillna(0) + team_against_period_all_Stats["p2_FTM"].fillna(0) -
                                           team_against_period_all_Stats["p3_2PA"].fillna(0) - team_against_period_all_Stats[
                                               "p2_3PA"].fillna(0) + team_against_period_all_Stats["p2_FTA"].fillna(0))
team_against_period_all_Stats["p3_PIR"] = (team_against_period_all_Stats["p3_PTS"].fillna(0) +
                                           team_against_period_all_Stats["p3_AS"].fillna(0) +
                                           team_against_period_all_Stats["p3_TR"].fillna(0) -
                                           team_against_period_all_Stats["p3_TO"].fillna(0) +
                                           team_against_period_all_Stats["p3_STL"].fillna(0) +
                                           team_against_period_all_Stats["p3_BLKM"].fillna(0) -
                                           team_against_period_all_Stats["p3_BLKR"].fillna(0) -
                                           team_against_period_all_Stats["p3_PF"].fillna(0) +
                                           team_against_period_all_Stats["p3_2PM"].fillna(0) + team_against_period_all_Stats[
                                               "p3_3PM"].fillna(0) + team_against_period_all_Stats["p3_FTM"].fillna(0) -
                                           team_against_period_all_Stats["p3_2PA"].fillna(0) - team_against_period_all_Stats[
                                               "p3_3PA"].fillna(0) + team_against_period_all_Stats["p3_FTA"].fillna(0))

team_against_period_all_Stats["p4_PIR"] = (team_against_period_all_Stats["p4_PTS"] +
                                           team_against_period_all_Stats["p4_AS"] +
                                           team_against_period_all_Stats["p4_TR"] -
                                           team_against_period_all_Stats["p4_TO"] +
                                           team_against_period_all_Stats["p4_STL"] +
                                           team_against_period_all_Stats["p4_BLKM"] -
                                           team_against_period_all_Stats["p4_BLKR"] -
                                           team_against_period_all_Stats["p4_PF"] +
                                           team_against_period_all_Stats["p4_2PM"] + team_against_period_all_Stats[
                                               "p4_3PM"] + team_against_period_all_Stats["p4_FTM"] -
                                           team_against_period_all_Stats["p4_2PA"] - team_against_period_all_Stats[
                                               "p4_3PA"] + team_against_period_all_Stats["p4_FTA"])

team_against_period_all_Stats["ex_PIR"] = (team_against_period_all_Stats["ex_PTS"].fillna(0) +
                                           team_against_period_all_Stats["ex_AS"].fillna(0) +
                                           team_against_period_all_Stats["ex_TR"].fillna(0) -
                                           team_against_period_all_Stats["ex_TO"].fillna(0) +
                                           team_against_period_all_Stats["ex_STL"].fillna(0) +
                                           team_against_period_all_Stats["ex_BLKM"].fillna(0) -
                                           team_against_period_all_Stats["ex_BLKR"].fillna(0) -
                                           team_against_period_all_Stats["ex_PF"].fillna(0) +
                                           team_against_period_all_Stats["ex_2PM"].fillna(0) + team_against_period_all_Stats[
                                               "ex_3PM"].fillna(0) + team_against_period_all_Stats["ex_FTM"].fillna(0) -
                                           team_against_period_all_Stats["ex_2PA"].fillna(0) - team_against_period_all_Stats[
                                               "ex_3PA"].fillna(0) + team_against_period_all_Stats["ex_FTA"].fillna(0))
team_against_period_all_Stats['p1_PIR_avg'] = (
            team_against_period_all_Stats['p1_PIR'] / team_against_period_all_Stats['Games']).round(1)
team_against_period_all_Stats['p2_PIR_avg'] = (
            team_against_period_all_Stats['p2_PIR'] / team_against_period_all_Stats['Games']).round(1)
team_against_period_all_Stats['p3_PIR_avg'] = (
            team_against_period_all_Stats['p3_PIR'] / team_against_period_all_Stats['Games']).round(1)
team_against_period_all_Stats['p4_PIR_avg'] = (
            team_against_period_all_Stats['p4_PIR'] / team_against_period_all_Stats['Games']).round(1)

regex1 = "Against|" + stat_choose
interactive_table(
    team_against_period_all_Stats.set_index('Against').filter(regex=regex1),
    paging=False, height=900, width=2000, showIndex=True,
    classes="display order-column nowrap table_with_monospace_font", searching=False,
    fixedColumns=True, select=True, info=False, scrollCollapse=True,
    scrollX=True, scrollY=1000, fixedHeader=True, scroller=True, filter='bottom',
    columnDefs=[{"className": "dt-center", "targets": "_all"}])


points_compute_total=pbp_data_df2425.loc[pbp_data_df2425.PLAYTYPE.isin(['2FGM','3FGM','FTM'])][['Team','PLAYTYPE','Player','PERIOD']].value_counts().reset_index()
points_compute_total['PTS']=points_compute_total['PLAYTYPE'].apply(points_scored)*points_compute_total['count']
player_points_by_period=points_compute_total.groupby(['Player','PERIOD'])['PTS'].sum().reset_index()



st.header('Player Stats')
sel_team_points_compute_total=points_compute_total.loc[points_compute_total.Team==search_team_team1].groupby(['Player','PLAYTYPE','PERIOD'])['PTS'].sum().reset_index().groupby(['Player','PERIOD'])['PTS'].sum().reset_index().fillna(0)

p1_sel_team_points_compute_total=sel_team_points_compute_total.loc[sel_team_points_compute_total.PERIOD==1][['Player','PTS']].rename(columns={'PTS':'p1_PTS'})
p2_sel_team_points_compute_total=sel_team_points_compute_total.loc[sel_team_points_compute_total.PERIOD==2][['Player','PTS']].rename(columns={'PTS':'p2_PTS'})
p3_sel_team_points_compute_total=sel_team_points_compute_total.loc[sel_team_points_compute_total.PERIOD==3][['Player','PTS']].rename(columns={'PTS':'p3_PTS'})
p4_sel_team_points_compute_total=sel_team_points_compute_total.loc[sel_team_points_compute_total.PERIOD==4][['Player','PTS']].rename(columns={'PTS':'p4_PTS'})
p5_sel_team_points_compute_total=sel_team_points_compute_total.loc[sel_team_points_compute_total.PERIOD==5][['Player','PTS']].rename(columns={'PTS':'ex_PTS'})
team_points_final=pd.merge(games,p1_sel_team_points_compute_total,on='Player',how='outer')
team_points_final=pd.merge(team_points_final,p2_sel_team_points_compute_total,on='Player',how='outer')
team_points_final=pd.merge(team_points_final,p3_sel_team_points_compute_total,on='Player',how='outer')
team_points_final=pd.merge(team_points_final,p4_sel_team_points_compute_total,on='Player',how='outer')
team_points_final=pd.merge(team_points_final,p5_sel_team_points_compute_total,on='Player',how='outer')
team_points_final['p1_PTS_avg']=(team_points_final['p1_PTS']/team_points_final['Games']).round(1)
team_points_final['p2_PTS_avg']=(team_points_final['p2_PTS']/team_points_final['Games']).round(1)
team_points_final['p3_PTS_avg']=(team_points_final['p3_PTS']/team_points_final['Games']).round(1)
team_points_final['p4_PTS_avg']=(team_points_final['p4_PTS']/team_points_final['Games']).round(1)
team_points_final['ex_PTS_avg']=(team_points_final['ex_PTS']/team_points_final['Games']).round(1)



assists_compute_total=pbp_data_df2425.loc[pbp_data_df2425.PLAYTYPE=='AS'][['Team','PLAYTYPE','Player','PERIOD']].value_counts().reset_index().rename(columns={'count':'AS'}).fillna(0)
sel_team_assists_compute_total=assists_compute_total.loc[assists_compute_total.Team==search_team_team1]
p1_sel_team_assists_compute_total=sel_team_assists_compute_total.loc[sel_team_assists_compute_total.PERIOD==1][['Player','AS']].rename(columns={'AS':'p1_AS'})
p2_sel_team_assists_compute_total=sel_team_assists_compute_total.loc[sel_team_assists_compute_total.PERIOD==2][['Player','AS']].rename(columns={'AS':'p2_AS'})
p3_sel_team_assists_compute_total=sel_team_assists_compute_total.loc[sel_team_assists_compute_total.PERIOD==3][['Player','AS']].rename(columns={'AS':'p3_AS'})
p4_sel_team_assists_compute_total=sel_team_assists_compute_total.loc[sel_team_assists_compute_total.PERIOD==4][['Player','AS']].rename(columns={'AS':'p4_AS'})
p5_sel_team_assists_compute_total=sel_team_assists_compute_total.loc[sel_team_assists_compute_total.PERIOD==5][['Player','AS']].rename(columns={'AS':'ex_AS'})
team_assists_final=pd.merge(p1_sel_team_assists_compute_total,p2_sel_team_assists_compute_total,on='Player',how='outer')
team_assists_final=pd.merge(team_assists_final,p3_sel_team_assists_compute_total,on='Player',how='outer')
team_assists_final=pd.merge(team_assists_final,p4_sel_team_assists_compute_total,on='Player',how='outer')
team_assists_final=pd.merge(team_assists_final,p5_sel_team_assists_compute_total,on='Player',how='outer')
player_quarter_stats=pd.merge(team_points_final,team_assists_final,on='Player',how='outer').fillna(0)
player_quarter_stats['p1_AS_avg']=(player_quarter_stats['p1_AS']/player_quarter_stats['Games']).round(1)
player_quarter_stats['p2_AS_avg']=(player_quarter_stats['p2_AS']/player_quarter_stats['Games']).round(1)
player_quarter_stats['p3_AS_avg']=(player_quarter_stats['p3_AS']/player_quarter_stats['Games']).round(1)
player_quarter_stats['p4_AS_avg']=(player_quarter_stats['p4_AS']/player_quarter_stats['Games']).round(1)
player_quarter_stats['ex_AS_avg']=(player_quarter_stats['ex_AS']/player_quarter_stats['Games']).round(1)




def_reb_compute_total=pbp_data_df2425.loc[pbp_data_df2425.PLAYTYPE=='D'][['Team','PLAYTYPE','Player','PERIOD']].value_counts().reset_index().rename(columns={'count':'D'}).fillna(0)
sel_team_def_reb_compute_total=def_reb_compute_total.loc[def_reb_compute_total.Team==search_team_team1]
p1_sel_team_def_reb_compute_total=sel_team_def_reb_compute_total.loc[sel_team_def_reb_compute_total.PERIOD==1][['Player','D']].rename(columns={'D':'p1_DR'})
p2_sel_team_def_reb_compute_total=sel_team_def_reb_compute_total.loc[sel_team_def_reb_compute_total.PERIOD==2][['Player','D']].rename(columns={'D':'p2_DR'})
p3_sel_team_def_reb_compute_total=sel_team_def_reb_compute_total.loc[sel_team_def_reb_compute_total.PERIOD==3][['Player','D']].rename(columns={'D':'p3_DR'})
p4_sel_team_def_reb_compute_total=sel_team_def_reb_compute_total.loc[sel_team_def_reb_compute_total.PERIOD==4][['Player','D']].rename(columns={'D':'p4_DR'})
p5_sel_team_def_reb_compute_total=sel_team_def_reb_compute_total.loc[sel_team_def_reb_compute_total.PERIOD==5][['Player','D']].rename(columns={'D':'ex_DR'})
team_def_reb_final=pd.merge(p1_sel_team_def_reb_compute_total,p2_sel_team_def_reb_compute_total,on='Player',how='outer')
team_def_reb_final=pd.merge(team_def_reb_final,p3_sel_team_def_reb_compute_total,on='Player',how='outer')
team_def_reb_final=pd.merge(team_def_reb_final,p4_sel_team_def_reb_compute_total,on='Player',how='outer')
team_def_reb_final=pd.merge(team_def_reb_final,p5_sel_team_def_reb_compute_total,on='Player',how='outer')

player_quarter_stats=pd.merge(player_quarter_stats,team_def_reb_final,on='Player',how='outer').fillna(0)
player_quarter_stats['p1_DR_avg']=(player_quarter_stats['p1_DR']/player_quarter_stats['Games']).round(1)
player_quarter_stats['p2_DR_avg']=(player_quarter_stats['p2_DR']/player_quarter_stats['Games']).round(1)
player_quarter_stats['p3_DR_avg']=(player_quarter_stats['p3_DR']/player_quarter_stats['Games']).round(1)
player_quarter_stats['p4_DR_avg']=(player_quarter_stats['p4_DR']/player_quarter_stats['Games']).round(1)
player_quarter_stats['ex_DR_avg']=(player_quarter_stats['ex_DR']/player_quarter_stats['Games']).round(1)

or_reb_compute_total=pbp_data_df2425.loc[pbp_data_df2425.PLAYTYPE=='O'][['Team','PLAYTYPE','Player','PERIOD']].value_counts().reset_index().rename(columns={'count':'OR'}).fillna(0)
sel_team_or_reb_compute_total=or_reb_compute_total.loc[or_reb_compute_total.Team==search_team_team1]
p1_sel_team_or_reb_compute_total=sel_team_or_reb_compute_total.loc[sel_team_or_reb_compute_total.PERIOD==1][['Player','OR']].rename(columns={'OR':'p1_OR'})
p2_sel_team_or_reb_compute_total=sel_team_or_reb_compute_total.loc[sel_team_or_reb_compute_total.PERIOD==2][['Player','OR']].rename(columns={'OR':'p2_OR'})
p3_sel_team_or_reb_compute_total=sel_team_or_reb_compute_total.loc[sel_team_or_reb_compute_total.PERIOD==3][['Player','OR']].rename(columns={'OR':'p3_OR'})
p4_sel_team_or_reb_compute_total=sel_team_or_reb_compute_total.loc[sel_team_or_reb_compute_total.PERIOD==4][['Player','OR']].rename(columns={'OR':'p4_OR'})
p5_sel_team_or_reb_compute_total=sel_team_or_reb_compute_total.loc[sel_team_or_reb_compute_total.PERIOD==5][['Player','OR']].rename(columns={'OR':'ex_OR'})
team_or_reb_final=pd.merge(p1_sel_team_or_reb_compute_total,p2_sel_team_or_reb_compute_total,on='Player',how='outer')
team_or_reb_final=pd.merge(team_or_reb_final,p3_sel_team_or_reb_compute_total,on='Player',how='outer')
team_or_reb_final=pd.merge(team_or_reb_final,p4_sel_team_or_reb_compute_total,on='Player',how='outer')
team_or_reb_final=pd.merge(team_or_reb_final,p5_sel_team_or_reb_compute_total,on='Player',how='outer')

player_quarter_stats=pd.merge(player_quarter_stats,team_or_reb_final,on='Player',how='outer').fillna(0)
player_quarter_stats['p1_OR_avg']=(player_quarter_stats['p1_OR']/player_quarter_stats['Games']).round(1)
player_quarter_stats['p2_OR_avg']=(player_quarter_stats['p2_OR']/player_quarter_stats['Games']).round(1)
player_quarter_stats['p3_OR_avg']=(player_quarter_stats['p3_OR']/player_quarter_stats['Games']).round(1)
player_quarter_stats['p4_OR_avg']=(player_quarter_stats['p4_OR']/player_quarter_stats['Games']).round(1)
player_quarter_stats['ex_OR_avg']=(player_quarter_stats['ex_OR']/player_quarter_stats['Games']).round(1)
player_quarter_stats['p1_TR']=player_quarter_stats['p1_DR']+player_quarter_stats['p1_OR']
player_quarter_stats['p2_TR']=player_quarter_stats['p2_DR']+player_quarter_stats['p2_OR']
player_quarter_stats['p3_TR']=player_quarter_stats['p3_DR']+player_quarter_stats['p3_OR']
player_quarter_stats['p4_TR']=player_quarter_stats['p4_DR']+player_quarter_stats['p4_OR']
player_quarter_stats['ex_TR']=player_quarter_stats['ex_DR']+player_quarter_stats['ex_OR']
player_quarter_stats['p1_TR_avg']=(player_quarter_stats['p1_TR']/player_quarter_stats['Games']).round(1)
player_quarter_stats['p2_TR_avg']=(player_quarter_stats['p2_TR']/player_quarter_stats['Games']).round(1)
player_quarter_stats['p3_TR_avg']=(player_quarter_stats['p3_TR']/player_quarter_stats['Games']).round(1)
player_quarter_stats['p4_TR_avg']=(player_quarter_stats['p4_TR']/player_quarter_stats['Games']).round(1)
player_quarter_stats['ex_TR_avg']=(player_quarter_stats['ex_TR']/player_quarter_stats['Games']).round(1)

to_reb_compute_total=pbp_data_df2425.loc[pbp_data_df2425.PLAYTYPE=='TO'][['Team','PLAYTYPE','Player','PERIOD']].value_counts().reset_index().rename(columns={'count':'TO'}).fillna(0)
sel_team_to_reb_compute_total=to_reb_compute_total.loc[to_reb_compute_total.Team==search_team_team1]
p1_sel_team_to_reb_compute_total=sel_team_to_reb_compute_total.loc[sel_team_to_reb_compute_total.PERIOD==1][['Player','TO']].rename(columns={'TO':'p1_TO'})
p2_sel_team_to_reb_compute_total=sel_team_to_reb_compute_total.loc[sel_team_to_reb_compute_total.PERIOD==2][['Player','TO']].rename(columns={'TO':'p2_TO'})
p3_sel_team_to_reb_compute_total=sel_team_to_reb_compute_total.loc[sel_team_to_reb_compute_total.PERIOD==3][['Player','TO']].rename(columns={'TO':'p3_TO'})
p4_sel_team_to_reb_compute_total=sel_team_to_reb_compute_total.loc[sel_team_to_reb_compute_total.PERIOD==4][['Player','TO']].rename(columns={'TO':'p4_TO'})
p5_sel_team_to_reb_compute_total=sel_team_to_reb_compute_total.loc[sel_team_to_reb_compute_total.PERIOD==5][['Player','TO']].rename(columns={'TO':'ex_TO'})
team_to_reb_final=pd.merge(p1_sel_team_to_reb_compute_total,p2_sel_team_to_reb_compute_total,on='Player',how='outer')
team_to_reb_final=pd.merge(team_to_reb_final,p3_sel_team_to_reb_compute_total,on='Player',how='outer')
team_to_reb_final=pd.merge(team_to_reb_final,p4_sel_team_to_reb_compute_total,on='Player',how='outer')
team_to_reb_final=pd.merge(team_to_reb_final,p5_sel_team_to_reb_compute_total,on='Player',how='outer')

player_quarter_stats=pd.merge(player_quarter_stats,team_to_reb_final,on='Player',how='outer').fillna(0)
player_quarter_stats['p1_TO_avg']=(player_quarter_stats['p1_TO']/player_quarter_stats['Games']).round(1)
player_quarter_stats['p2_TO_avg']=(player_quarter_stats['p2_TO']/player_quarter_stats['Games']).round(1)
player_quarter_stats['p3_TO_avg']=(player_quarter_stats['p3_TO']/player_quarter_stats['Games']).round(1)
player_quarter_stats['p4_TO_avg']=(player_quarter_stats['p4_TO']/player_quarter_stats['Games']).round(1)
player_quarter_stats['ex_TO_avg']=(player_quarter_stats['ex_TO']/player_quarter_stats['Games']).round(1)

stl_compute_total=pbp_data_df2425.loc[pbp_data_df2425.PLAYTYPE=='ST'][['Team','PLAYTYPE','Player','PERIOD']].value_counts().reset_index().rename(columns={'count':'STL'}).fillna(0)
sel_team_stl_compute_total=stl_compute_total.loc[stl_compute_total.Team==search_team_team1]
p1_sel_team_stl_compute_total=sel_team_stl_compute_total.loc[sel_team_stl_compute_total.PERIOD==1][['Player','STL']].rename(columns={'STL':'p1_STL'})
p2_sel_team_stl_compute_total=sel_team_stl_compute_total.loc[sel_team_stl_compute_total.PERIOD==2][['Player','STL']].rename(columns={'STL':'p2_STL'})
p3_sel_team_stl_compute_total=sel_team_stl_compute_total.loc[sel_team_stl_compute_total.PERIOD==3][['Player','STL']].rename(columns={'STL':'p3_STL'})
p4_sel_team_stl_compute_total=sel_team_stl_compute_total.loc[sel_team_stl_compute_total.PERIOD==4][['Player','STL']].rename(columns={'STL':'p4_STL'})
p5_sel_team_stl_compute_total=sel_team_stl_compute_total.loc[sel_team_stl_compute_total.PERIOD==5][['Player','STL']].rename(columns={'STL':'ex_STL'})
team_stl_final=pd.merge(p1_sel_team_stl_compute_total,p2_sel_team_stl_compute_total,on='Player',how='outer')
team_stl_final=pd.merge(team_stl_final,p3_sel_team_stl_compute_total,on='Player',how='outer')
team_stl_final=pd.merge(team_stl_final,p4_sel_team_stl_compute_total,on='Player',how='outer')
team_stl_final=pd.merge(team_stl_final,p5_sel_team_stl_compute_total,on='Player',how='outer')
player_quarter_stats=pd.merge(player_quarter_stats,team_stl_final,on='Player',how='outer').fillna(0)
player_quarter_stats['p1_STL_avg']=(player_quarter_stats['p1_STL']/player_quarter_stats['Games']).round(1)
player_quarter_stats['p2_STL_avg']=(player_quarter_stats['p2_STL']/player_quarter_stats['Games']).round(1)
player_quarter_stats['p3_STL_avg']=(player_quarter_stats['p3_STL']/player_quarter_stats['Games']).round(1)
player_quarter_stats['p4_STL_avg']=(player_quarter_stats['p4_STL']/player_quarter_stats['Games']).round(1)
player_quarter_stats['ex_STL_avg']=(player_quarter_stats['ex_STL']/player_quarter_stats['Games']).round(1)

blkr_compute_total=pbp_data_df2425.loc[pbp_data_df2425.PLAYTYPE=='AG'][['Team','PLAYTYPE','Player','PERIOD']].value_counts().reset_index().rename(columns={'count':'BLKR'}).fillna(0)
sel_team_blkr_compute_total=blkr_compute_total.loc[blkr_compute_total.Team==search_team_team1]
p1_sel_team_blkr_compute_total=sel_team_blkr_compute_total.loc[sel_team_blkr_compute_total.PERIOD==1][['Player','BLKR']].rename(columns={'BLKR':'p1_BLKR'})
p2_sel_team_blkr_compute_total=sel_team_blkr_compute_total.loc[sel_team_blkr_compute_total.PERIOD==2][['Player','BLKR']].rename(columns={'BLKR':'p2_BLKR'})
p3_sel_team_blkr_compute_total=sel_team_blkr_compute_total.loc[sel_team_blkr_compute_total.PERIOD==3][['Player','BLKR']].rename(columns={'BLKR':'p3_BLKR'})
p4_sel_team_blkr_compute_total=sel_team_blkr_compute_total.loc[sel_team_blkr_compute_total.PERIOD==4][['Player','BLKR']].rename(columns={'BLKR':'p4_BLKR'})
p5_sel_team_blkr_compute_total=sel_team_blkr_compute_total.loc[sel_team_blkr_compute_total.PERIOD==5][['Player','BLKR']].rename(columns={'BLKR':'ex_BLKR'})
team_blkr_final=pd.merge(p1_sel_team_blkr_compute_total,p2_sel_team_blkr_compute_total,on='Player',how='outer')
team_blkr_final=pd.merge(team_blkr_final,p3_sel_team_blkr_compute_total,on='Player',how='outer')
team_blkr_final=pd.merge(team_blkr_final,p4_sel_team_blkr_compute_total,on='Player',how='outer')
team_blkr_final=pd.merge(team_blkr_final,p5_sel_team_blkr_compute_total,on='Player',how='outer')

player_quarter_stats=pd.merge(player_quarter_stats,team_blkr_final,on='Player',how='outer').fillna(0)
player_quarter_stats['p1_BLKR_avg']=(player_quarter_stats['p1_BLKR']/player_quarter_stats['Games']).round(1)
player_quarter_stats['p2_BLKR_avg']=(player_quarter_stats['p2_BLKR']/player_quarter_stats['Games']).round(1)
player_quarter_stats['p3_BLKR_avg']=(player_quarter_stats['p3_BLKR']/player_quarter_stats['Games']).round(1)
player_quarter_stats['p4_BLKR_avg']=(player_quarter_stats['p4_BLKR']/player_quarter_stats['Games']).round(1)
player_quarter_stats['ex_BLKR_avg']=(player_quarter_stats['ex_BLKR']/player_quarter_stats['Games']).round(1)

blk_compute_total=pbp_data_df2425.loc[pbp_data_df2425.PLAYTYPE=='FV'][['Team','PLAYTYPE','Player','PERIOD']].value_counts().reset_index().rename(columns={'count':'BLKM'}).fillna(0)
sel_team_blk_compute_total=blk_compute_total.loc[blk_compute_total.Team==search_team_team1]
p1_sel_team_blk_compute_total=sel_team_blk_compute_total.loc[sel_team_blk_compute_total.PERIOD==1][['Player','BLKM']].rename(columns={'BLKM':'p1_BLKM'})
p2_sel_team_blk_compute_total=sel_team_blk_compute_total.loc[sel_team_blk_compute_total.PERIOD==2][['Player','BLKM']].rename(columns={'BLKM':'p2_BLKM'})
p3_sel_team_blk_compute_total=sel_team_blk_compute_total.loc[sel_team_blk_compute_total.PERIOD==3][['Player','BLKM']].rename(columns={'BLKM':'p3_BLKM'})
p4_sel_team_blk_compute_total=sel_team_blk_compute_total.loc[sel_team_blk_compute_total.PERIOD==4][['Player','BLKM']].rename(columns={'BLKM':'p4_BLKM'})
p5_sel_team_blk_compute_total=sel_team_blk_compute_total.loc[sel_team_blk_compute_total.PERIOD==5][['Player','BLKM']].rename(columns={'BLKM':'ex_BLKM'})
team_blk_final=pd.merge(p1_sel_team_blk_compute_total,p2_sel_team_blk_compute_total,on='Player',how='outer')
team_blk_final=pd.merge(team_blk_final,p3_sel_team_blk_compute_total,on='Player',how='outer')
team_blk_final=pd.merge(team_blk_final,p4_sel_team_blk_compute_total,on='Player',how='outer')
team_blk_final=pd.merge(team_blk_final,p5_sel_team_blk_compute_total,on='Player',how='outer')

player_quarter_stats=pd.merge(player_quarter_stats,team_blk_final,on='Player',how='outer').fillna(0)
player_quarter_stats['p1_BLKM_avg']=(player_quarter_stats['p1_BLKM']/player_quarter_stats['Games']).round(1)
player_quarter_stats['p2_BLKM_avg']=(player_quarter_stats['p2_BLKM']/player_quarter_stats['Games']).round(1)
player_quarter_stats['p3_BLKM_avg']=(player_quarter_stats['p3_BLKM']/player_quarter_stats['Games']).round(1)
player_quarter_stats['p4_BLKM_avg']=(player_quarter_stats['p4_BLKM']/player_quarter_stats['Games']).round(1)
player_quarter_stats['ex_BLKM_avg']=(player_quarter_stats['ex_BLKM']/player_quarter_stats['Games']).round(1)


rf_compute_total=pbp_data_df2425.loc[pbp_data_df2425.PLAYTYPE=='RV'][['Team','PLAYTYPE','Player','PERIOD']].value_counts().reset_index().rename(columns={'count':'RF'}).fillna(0)
sel_team_rf_compute_total=rf_compute_total.loc[rf_compute_total.Team==search_team_team1]
p1_sel_team_rf_compute_total=sel_team_rf_compute_total.loc[sel_team_rf_compute_total.PERIOD==1][['Player','RF']].rename(columns={'RF':'p1_RF'})
p2_sel_team_rf_compute_total=sel_team_rf_compute_total.loc[sel_team_rf_compute_total.PERIOD==2][['Player','RF']].rename(columns={'RF':'p2_RF'})
p3_sel_team_rf_compute_total=sel_team_rf_compute_total.loc[sel_team_rf_compute_total.PERIOD==3][['Player','RF']].rename(columns={'RF':'p3_RF'})
p4_sel_team_rf_compute_total=sel_team_rf_compute_total.loc[sel_team_rf_compute_total.PERIOD==4][['Player','RF']].rename(columns={'RF':'p4_RF'})
p5_sel_team_rf_compute_total=sel_team_rf_compute_total.loc[sel_team_rf_compute_total.PERIOD==5][['Player','RF']].rename(columns={'RF':'ex_RF'})
team_rf_final=pd.merge(p1_sel_team_rf_compute_total,p2_sel_team_rf_compute_total,on='Player',how='outer')
team_rf_final=pd.merge(team_rf_final,p3_sel_team_rf_compute_total,on='Player',how='outer')
team_rf_final=pd.merge(team_rf_final,p4_sel_team_rf_compute_total,on='Player',how='outer')
team_rf_final=pd.merge(team_rf_final,p5_sel_team_rf_compute_total,on='Player',how='outer')

player_quarter_stats=pd.merge(player_quarter_stats,team_rf_final,on='Player',how='outer').fillna(0)
player_quarter_stats['p1_RF_avg']=(player_quarter_stats['p1_RF']/player_quarter_stats['Games']).round(1)
player_quarter_stats['p2_RF_avg']=(player_quarter_stats['p2_RF']/player_quarter_stats['Games']).round(1)
player_quarter_stats['p3_RF_avg']=(player_quarter_stats['p3_RF']/player_quarter_stats['Games']).round(1)
player_quarter_stats['p4_RF_avg']=(player_quarter_stats['p4_RF']/player_quarter_stats['Games']).round(1)
player_quarter_stats['ex_RF_avg']=(player_quarter_stats['ex_RF']/player_quarter_stats['Games']).round(1)

df_compute_total=pbp_data_df2425.loc[pbp_data_df2425.PLAYTYPE=='CM'][['Team','PLAYTYPE','Player','PERIOD']].value_counts().reset_index().rename(columns={'count':'DF'}).fillna(0)
sel_team_df_compute_total=df_compute_total.loc[df_compute_total.Team==search_team_team1]
p1_sel_team_df_compute_total=sel_team_df_compute_total.loc[sel_team_df_compute_total.PERIOD==1][['Player','DF']].rename(columns={'DF':'p1_DF'})
p2_sel_team_df_compute_total=sel_team_df_compute_total.loc[sel_team_df_compute_total.PERIOD==2][['Player','DF']].rename(columns={'DF':'p2_DF'})
p3_sel_team_df_compute_total=sel_team_df_compute_total.loc[sel_team_df_compute_total.PERIOD==3][['Player','DF']].rename(columns={'DF':'p3_DF'})
p4_sel_team_df_compute_total=sel_team_df_compute_total.loc[sel_team_df_compute_total.PERIOD==4][['Player','DF']].rename(columns={'DF':'p4_DF'})
p5_sel_team_df_compute_total=sel_team_df_compute_total.loc[sel_team_df_compute_total.PERIOD==5][['Player','DF']].rename(columns={'DF':'ex_DF'})
team_df_final=pd.merge(p1_sel_team_df_compute_total,p2_sel_team_df_compute_total,on='Player',how='outer')
team_df_final=pd.merge(team_df_final,p3_sel_team_df_compute_total,on='Player',how='outer')
team_df_final=pd.merge(team_df_final,p4_sel_team_df_compute_total,on='Player',how='outer')
team_df_final=pd.merge(team_df_final,p5_sel_team_df_compute_total,on='Player',how='outer')
player_quarter_stats=pd.merge(player_quarter_stats,team_df_final,on='Player',how='outer').fillna(0)
player_quarter_stats['p1_DF_avg']=(player_quarter_stats['p1_DF']/player_quarter_stats['Games']).round(1)
player_quarter_stats['p2_DF_avg']=(player_quarter_stats['p2_DF']/player_quarter_stats['Games']).round(1)
player_quarter_stats['p3_DF_avg']=(player_quarter_stats['p3_DF']/player_quarter_stats['Games']).round(1)
player_quarter_stats['p4_DF_avg']=(player_quarter_stats['p4_DF']/player_quarter_stats['Games']).round(1)
player_quarter_stats['ex_DF_avg']=(player_quarter_stats['ex_DF']/player_quarter_stats['Games']).round(1)

of_compute_total=pbp_data_df2425.loc[pbp_data_df2425.PLAYTYPE=='OF'][['Team','PLAYTYPE','Player','PERIOD']].value_counts().reset_index().rename(columns={'count':'OF'}).fillna(0)
sel_team_of_compute_total=of_compute_total.loc[of_compute_total.Team==search_team_team1]
p1_sel_team_of_compute_total=sel_team_of_compute_total.loc[sel_team_of_compute_total.PERIOD==1][['Player','OF']].rename(columns={'OF':'p1_OF'})
p2_sel_team_of_compute_total=sel_team_of_compute_total.loc[sel_team_of_compute_total.PERIOD==2][['Player','OF']].rename(columns={'OF':'p2_OF'})
p3_sel_team_of_compute_total=sel_team_of_compute_total.loc[sel_team_of_compute_total.PERIOD==3][['Player','OF']].rename(columns={'OF':'p3_OF'})
p4_sel_team_of_compute_total=sel_team_of_compute_total.loc[sel_team_of_compute_total.PERIOD==4][['Player','OF']].rename(columns={'OF':'p4_OF'})
p5_sel_team_of_compute_total=sel_team_of_compute_total.loc[sel_team_of_compute_total.PERIOD==5][['Player','OF']].rename(columns={'OF':'ex_OF'})
team_of_final=pd.merge(p1_sel_team_of_compute_total,p2_sel_team_of_compute_total,on='Player',how='outer')
team_of_final=pd.merge(team_of_final,p3_sel_team_of_compute_total,on='Player',how='outer')
team_of_final=pd.merge(team_of_final,p4_sel_team_of_compute_total,on='Player',how='outer')
team_of_final=pd.merge(team_of_final,p5_sel_team_of_compute_total,on='Player',how='outer')
player_quarter_stats=pd.merge(player_quarter_stats,team_of_final,on='Player',how='outer').fillna(0)
player_quarter_stats['p1_OF_avg']=(player_quarter_stats['p1_OF']/player_quarter_stats['Games']).round(1)
player_quarter_stats['p2_OF_avg']=(player_quarter_stats['p2_OF']/player_quarter_stats['Games']).round(1)
player_quarter_stats['p3_OF_avg']=(player_quarter_stats['p3_OF']/player_quarter_stats['Games']).round(1)
player_quarter_stats['p4_OF_avg']=(player_quarter_stats['p4_OF']/player_quarter_stats['Games']).round(1)
player_quarter_stats['ex_OF_avg']=(player_quarter_stats['ex_OF']/player_quarter_stats['Games']).round(1)



unf_compute_total=pbp_data_df2425.loc[pbp_data_df2425.PLAYTYPE.isin(['CMD','CMU'])][['Team','PLAYTYPE','Player','PERIOD']].value_counts().reset_index().groupby(['Team','Player','PERIOD'])['count'].sum().reset_index().rename(columns={'count':'UNF'}).fillna(0)
sel_team_unf_compute_total=unf_compute_total.loc[unf_compute_total.Team==search_team_team1]
p1_sel_team_unf_compute_total=sel_team_unf_compute_total.loc[sel_team_unf_compute_total.PERIOD==1][['Player','UNF']].rename(columns={'UNF':'p1_UNF'})
p2_sel_team_unf_compute_total=sel_team_unf_compute_total.loc[sel_team_unf_compute_total.PERIOD==2][['Player','UNF']].rename(columns={'UNF':'p2_UNF'})
p3_sel_team_unf_compute_total=sel_team_unf_compute_total.loc[sel_team_unf_compute_total.PERIOD==3][['Player','UNF']].rename(columns={'UNF':'p3_UNF'})
p4_sel_team_unf_compute_total=sel_team_unf_compute_total.loc[sel_team_unf_compute_total.PERIOD==4][['Player','UNF']].rename(columns={'UNF':'p4_UNF'})
p5_sel_team_unf_compute_total=sel_team_unf_compute_total.loc[sel_team_unf_compute_total.PERIOD==5][['Player','UNF']].rename(columns={'UNF':'ex_UNF'})
team_unf_final=pd.merge(p1_sel_team_unf_compute_total,p2_sel_team_unf_compute_total,on='Player',how='outer')
team_unf_final=pd.merge(team_unf_final,p3_sel_team_unf_compute_total,on='Player',how='outer')
team_unf_final=pd.merge(team_unf_final,p4_sel_team_unf_compute_total,on='Player',how='outer')
team_unf_final=pd.merge(team_unf_final,p5_sel_team_unf_compute_total,on='Player',how='outer')



player_quarter_stats=pd.merge(player_quarter_stats,team_unf_final,on='Player',how='outer').fillna(0)
player_quarter_stats['p1_UNF_avg']=(player_quarter_stats['p1_UNF']/player_quarter_stats['Games']).round(1)
player_quarter_stats['p2_UNF_avg']=(player_quarter_stats['p2_UNF']/player_quarter_stats['Games']).round(1)
player_quarter_stats['p3_UNF_avg']=(player_quarter_stats['p3_UNF']/player_quarter_stats['Games']).round(1)
player_quarter_stats['p4_UNF_avg']=(player_quarter_stats['p4_UNF']/player_quarter_stats['Games']).round(1)
player_quarter_stats['ex_UNF_avg']=(player_quarter_stats['ex_UNF']/player_quarter_stats['Games']).round(1)

tf_compute_total=pbp_data_df2425.loc[pbp_data_df2425.PLAYTYPE=='CMT'][['Team','PLAYTYPE','Player','PERIOD']].value_counts().reset_index().rename(columns={'count':'TF'}).fillna(0)
sel_team_tf_compute_total=tf_compute_total.loc[tf_compute_total.Team==search_team_team1]
p1_sel_team_tf_compute_total=sel_team_tf_compute_total.loc[sel_team_tf_compute_total.PERIOD==1][['Player','TF']].rename(columns={'TF':'p1_TF'})
p2_sel_team_tf_compute_total=sel_team_tf_compute_total.loc[sel_team_tf_compute_total.PERIOD==2][['Player','TF']].rename(columns={'TF':'p2_TF'})
p3_sel_team_tf_compute_total=sel_team_tf_compute_total.loc[sel_team_tf_compute_total.PERIOD==3][['Player','TF']].rename(columns={'TF':'p3_TF'})
p4_sel_team_tf_compute_total=sel_team_tf_compute_total.loc[sel_team_tf_compute_total.PERIOD==4][['Player','TF']].rename(columns={'TF':'p4_TF'})
p5_sel_team_tf_compute_total=sel_team_tf_compute_total.loc[sel_team_tf_compute_total.PERIOD==5][['Player','TF']].rename(columns={'TF':'ex_TF'})
team_tf_final=pd.merge(p1_sel_team_tf_compute_total,p2_sel_team_tf_compute_total,on='Player',how='outer')
team_tf_final=pd.merge(team_tf_final,p3_sel_team_tf_compute_total,on='Player',how='outer')
team_tf_final=pd.merge(team_tf_final,p4_sel_team_tf_compute_total,on='Player',how='outer')
team_tf_final=pd.merge(team_tf_final,p5_sel_team_tf_compute_total,on='Player',how='outer')

player_quarter_stats=pd.merge(player_quarter_stats,team_tf_final,on='Player',how='outer').fillna(0)
player_quarter_stats['p1_TF_avg']=(player_quarter_stats['p1_TF']/player_quarter_stats['Games']).round(1)
player_quarter_stats['p2_TF_avg']=(player_quarter_stats['p2_TF']/player_quarter_stats['Games']).round(1)
player_quarter_stats['p3_TF_avg']=(player_quarter_stats['p3_TF']/player_quarter_stats['Games']).round(1)
player_quarter_stats['p4_TF_avg']=(player_quarter_stats['p4_TF']/player_quarter_stats['Games']).round(1)
player_quarter_stats['ex_TF_avg']=(player_quarter_stats['ex_TF']/player_quarter_stats['Games']).round(1)

player_quarter_stats['p1_PF']=player_quarter_stats['p1_DF'].fillna(0)+player_quarter_stats['p1_OF'].fillna(0)+player_quarter_stats['p1_UNF'].fillna(0)+player_quarter_stats['p1_TF'].fillna(0)
player_quarter_stats['p2_PF']=player_quarter_stats['p2_DF'].fillna(0)+player_quarter_stats['p2_OF'].fillna(0)+player_quarter_stats['p2_UNF'].fillna(0)+player_quarter_stats['p2_TF'].fillna(0)
player_quarter_stats['p3_PF']=player_quarter_stats['p3_DF'].fillna(0)+player_quarter_stats['p3_OF'].fillna(0)+player_quarter_stats['p3_UNF'].fillna(0)+player_quarter_stats['p3_TF'].fillna(0)
player_quarter_stats['p4_PF']=player_quarter_stats['p4_DF'].fillna(0)+player_quarter_stats['p4_OF'].fillna(0)+player_quarter_stats['p4_UNF'].fillna(0)+player_quarter_stats['p4_TF'].fillna(0)
player_quarter_stats['ex_PF']=player_quarter_stats['ex_DF'].fillna(0)+player_quarter_stats['ex_OF'].fillna(0)+player_quarter_stats['ex_UNF'].fillna(0)+player_quarter_stats['ex_TF'].fillna(0)

player_quarter_stats['p1_PF_avg']=(player_quarter_stats['p1_PF']/player_quarter_stats['Games']).round(1)
player_quarter_stats['p2_PF_avg']=(player_quarter_stats['p2_PF']/player_quarter_stats['Games']).round(1)
player_quarter_stats['p3_PF_avg']=(player_quarter_stats['p3_PF']/player_quarter_stats['Games']).round(1)
player_quarter_stats['p4_PF_avg']=(player_quarter_stats['p4_PF']/player_quarter_stats['Games']).round(1)
player_quarter_stats['ex_PF_avg']=(player_quarter_stats['ex_PF']/player_quarter_stats['Games']).round(1)


p2m_compute_total=pbp_data_df2425.loc[pbp_data_df2425.PLAYTYPE=='2FGM'][['Team','PLAYTYPE','Player','PERIOD']].value_counts().reset_index().rename(columns={'count':'2PM'}).fillna(0)
sel_team_p2m_compute_total=p2m_compute_total.loc[p2m_compute_total.Team==search_team_team1]
p1_sel_team_p2m_compute_total=sel_team_p2m_compute_total.loc[sel_team_p2m_compute_total.PERIOD==1][['Player','2PM']].rename(columns={'2PM':'p1_2PM'})
p2_sel_team_p2m_compute_total=sel_team_p2m_compute_total.loc[sel_team_p2m_compute_total.PERIOD==2][['Player','2PM']].rename(columns={'2PM':'p2_2PM'})
p3_sel_team_p2m_compute_total=sel_team_p2m_compute_total.loc[sel_team_p2m_compute_total.PERIOD==3][['Player','2PM']].rename(columns={'2PM':'p3_2PM'})
p4_sel_team_p2m_compute_total=sel_team_p2m_compute_total.loc[sel_team_p2m_compute_total.PERIOD==4][['Player','2PM']].rename(columns={'2PM':'p4_2PM'})
p5_sel_team_p2m_compute_total=sel_team_p2m_compute_total.loc[sel_team_p2m_compute_total.PERIOD==5][['Player','2PM']].rename(columns={'2PM':'ex_2PM'})
team_p2m_final=pd.merge(p1_sel_team_p2m_compute_total,p2_sel_team_p2m_compute_total,on='Player',how='outer')
team_p2m_final=pd.merge(team_p2m_final,p3_sel_team_p2m_compute_total,on='Player',how='outer')
team_p2m_final=pd.merge(team_p2m_final,p4_sel_team_p2m_compute_total,on='Player',how='outer')
team_p2m_final=pd.merge(team_p2m_final,p5_sel_team_p2m_compute_total,on='Player',how='outer')

player_quarter_stats=pd.merge(player_quarter_stats,team_p2m_final,on='Player',how='outer').fillna(0)

player_quarter_stats['p1_2PM_avg']=(player_quarter_stats['p1_2PM']/player_quarter_stats['Games']).round(1)
player_quarter_stats['p2_2PM_avg']=(player_quarter_stats['p2_2PM']/player_quarter_stats['Games']).round(1)
player_quarter_stats['p3_2PM_avg']=(player_quarter_stats['p3_2PM']/player_quarter_stats['Games']).round(1)
player_quarter_stats['p4_2PM_avg']=(player_quarter_stats['p4_2PM']/player_quarter_stats['Games']).round(1)
player_quarter_stats['ex_2PM_avg']=(player_quarter_stats['ex_2PM']/player_quarter_stats['Games']).round(1)

p2a_compute_total=pbp_data_df2425.loc[pbp_data_df2425.PLAYTYPE.isin(['2FGA','2FGM'])].reset_index()[['Team','PLAYTYPE','Player','PERIOD']].value_counts().reset_index().groupby(['Team','Player','PERIOD'])['count'].sum().reset_index().rename(columns={'count':'2PA'}).fillna(0)
sel_team_p2a_compute_total=p2a_compute_total.loc[p2a_compute_total.Team==search_team_team1]
p1_sel_team_p2a_compute_total=sel_team_p2a_compute_total.loc[sel_team_p2a_compute_total.PERIOD==1][['Player','2PA']].rename(columns={'2PA':'p1_2PA'})
p2_sel_team_p2a_compute_total=sel_team_p2a_compute_total.loc[sel_team_p2a_compute_total.PERIOD==2][['Player','2PA']].rename(columns={'2PA':'p2_2PA'})
p3_sel_team_p2a_compute_total=sel_team_p2a_compute_total.loc[sel_team_p2a_compute_total.PERIOD==3][['Player','2PA']].rename(columns={'2PA':'p3_2PA'})
p4_sel_team_p2a_compute_total=sel_team_p2a_compute_total.loc[sel_team_p2a_compute_total.PERIOD==4][['Player','2PA']].rename(columns={'2PA':'p4_2PA'})
p5_sel_team_p2a_compute_total=sel_team_p2a_compute_total.loc[sel_team_p2a_compute_total.PERIOD==5][['Player','2PA']].rename(columns={'2PA':'ex_2PA'})
team_p2a_final=pd.merge(p1_sel_team_p2a_compute_total,p2_sel_team_p2a_compute_total,on='Player',how='outer')
team_p2a_final=pd.merge(team_p2a_final,p3_sel_team_p2a_compute_total,on='Player',how='outer')
team_p2a_final=pd.merge(team_p2a_final,p4_sel_team_p2a_compute_total,on='Player',how='outer')
team_p2a_final=pd.merge(team_p2a_final,p5_sel_team_p2a_compute_total,on='Player',how='outer')

player_quarter_stats=pd.merge(player_quarter_stats,team_p2a_final,on='Player',how='outer').fillna(0)
player_quarter_stats['p1_2PA_avg']=(player_quarter_stats['p1_2PA']/player_quarter_stats['Games']).round(1)
player_quarter_stats['p2_2PA_avg']=(player_quarter_stats['p2_2PA']/player_quarter_stats['Games']).round(1)
player_quarter_stats['p3_2PA_avg']=(player_quarter_stats['p3_2PA']/player_quarter_stats['Games']).round(1)
player_quarter_stats['p4_2PA_avg']=(player_quarter_stats['p4_2PA']/player_quarter_stats['Games']).round(1)
player_quarter_stats['ex_2PA_avg']=(player_quarter_stats['ex_2PA']/player_quarter_stats['Games']).round(1)
player_quarter_stats['p1_2P(%)']=(100*player_quarter_stats['p1_2PM']/player_quarter_stats['p1_2PA']).round(1)
player_quarter_stats['p2_2P(%)']=(100*player_quarter_stats['p2_2PM']/player_quarter_stats['p2_2PA']).round(1)
player_quarter_stats['p3_2P(%)']=(100*player_quarter_stats['p3_2PM']/player_quarter_stats['p3_2PA']).round(1)
player_quarter_stats['p4_2P(%)']=(100*player_quarter_stats['p4_2PM']/player_quarter_stats['p4_2PA']).round(1)
player_quarter_stats['ex_2P(%)']=(100*player_quarter_stats['ex_2PM']/player_quarter_stats['ex_2PA']).round(1)


p3m_compute_total=pbp_data_df2425.loc[pbp_data_df2425.PLAYTYPE=='3FGM'][['Team','PLAYTYPE','Player','PERIOD']].value_counts().reset_index().rename(columns={'count':'3PM'}).fillna(0)
sel_team_p3m_compute_total=p3m_compute_total.loc[p3m_compute_total.Team==search_team_team1]
p1_sel_team_p3m_compute_total=sel_team_p3m_compute_total.loc[sel_team_p3m_compute_total.PERIOD==1][['Player','3PM']].rename(columns={'3PM':'p1_3PM'})
p2_sel_team_p3m_compute_total=sel_team_p3m_compute_total.loc[sel_team_p3m_compute_total.PERIOD==2][['Player','3PM']].rename(columns={'3PM':'p2_3PM'})
p3_sel_team_p3m_compute_total=sel_team_p3m_compute_total.loc[sel_team_p3m_compute_total.PERIOD==3][['Player','3PM']].rename(columns={'3PM':'p3_3PM'})
p4_sel_team_p3m_compute_total=sel_team_p3m_compute_total.loc[sel_team_p3m_compute_total.PERIOD==4][['Player','3PM']].rename(columns={'3PM':'p4_3PM'})
p5_sel_team_p3m_compute_total=sel_team_p3m_compute_total.loc[sel_team_p3m_compute_total.PERIOD==5][['Player','3PM']].rename(columns={'3PM':'ex_3PM'})
team_p3m_final=pd.merge(p1_sel_team_p3m_compute_total,p2_sel_team_p3m_compute_total,on='Player',how='outer')
team_p3m_final=pd.merge(team_p3m_final,p3_sel_team_p3m_compute_total,on='Player',how='outer')
team_p3m_final=pd.merge(team_p3m_final,p4_sel_team_p3m_compute_total,on='Player',how='outer')
team_p3m_final=pd.merge(team_p3m_final,p5_sel_team_p3m_compute_total,on='Player',how='outer')

player_quarter_stats=pd.merge(player_quarter_stats,team_p3m_final,on='Player',how='outer').fillna(0)
player_quarter_stats['p1_3PM_avg']=(player_quarter_stats['p1_3PM']/player_quarter_stats['Games']).round(1)
player_quarter_stats['p2_3PM_avg']=(player_quarter_stats['p2_3PM']/player_quarter_stats['Games']).round(1)
player_quarter_stats['p3_3PM_avg']=(player_quarter_stats['p3_3PM']/player_quarter_stats['Games']).round(1)
player_quarter_stats['p4_3PM_avg']=(player_quarter_stats['p4_3PM']/player_quarter_stats['Games']).round(1)
player_quarter_stats['ex_3PM_avg']=(player_quarter_stats['ex_3PM']/player_quarter_stats['Games']).round(1)
p3a_compute_total=pbp_data_df2425.loc[pbp_data_df2425.PLAYTYPE.isin(['3FGA','3FGM'])][['Team','PLAYTYPE','Player','PERIOD']].value_counts().reset_index().groupby(['Team','Player','PERIOD'])['count'].sum().reset_index().rename(columns={'count':'3PA'}).fillna(0)
sel_team_p3a_compute_total=p3a_compute_total.loc[p3a_compute_total.Team==search_team_team1]
p1_sel_team_p3a_compute_total=sel_team_p3a_compute_total.loc[sel_team_p3a_compute_total.PERIOD==1][['Player','3PA']].rename(columns={'3PA':'p1_3PA'})
p2_sel_team_p3a_compute_total=sel_team_p3a_compute_total.loc[sel_team_p3a_compute_total.PERIOD==2][['Player','3PA']].rename(columns={'3PA':'p2_3PA'})
p3_sel_team_p3a_compute_total=sel_team_p3a_compute_total.loc[sel_team_p3a_compute_total.PERIOD==3][['Player','3PA']].rename(columns={'3PA':'p3_3PA'})
p4_sel_team_p3a_compute_total=sel_team_p3a_compute_total.loc[sel_team_p3a_compute_total.PERIOD==4][['Player','3PA']].rename(columns={'3PA':'p4_3PA'})
p5_sel_team_p3a_compute_total=sel_team_p3a_compute_total.loc[sel_team_p3a_compute_total.PERIOD==5][['Player','3PA']].rename(columns={'3PA':'ex_3PA'})
team_p3a_final=pd.merge(p1_sel_team_p3a_compute_total,p2_sel_team_p3a_compute_total,on='Player',how='outer')
team_p3a_final=pd.merge(team_p3a_final,p3_sel_team_p3a_compute_total,on='Player',how='outer')
team_p3a_final=pd.merge(team_p3a_final,p4_sel_team_p3a_compute_total,on='Player',how='outer')
team_p3a_final=pd.merge(team_p3a_final,p5_sel_team_p3a_compute_total,on='Player',how='outer')

player_quarter_stats=pd.merge(player_quarter_stats,team_p3a_final,on='Player',how='outer').fillna(0)
player_quarter_stats['p1_3PA_avg']=(player_quarter_stats['p1_3PA']/player_quarter_stats['Games']).round(1)
player_quarter_stats['p2_3PA_avg']=(player_quarter_stats['p2_3PA']/player_quarter_stats['Games']).round(1)
player_quarter_stats['p3_3PA_avg']=(player_quarter_stats['p3_3PA']/player_quarter_stats['Games']).round(1)
player_quarter_stats['p4_3PA_avg']=(player_quarter_stats['p4_3PA']/player_quarter_stats['Games']).round(1)
player_quarter_stats['ex_3PA_avg']=(player_quarter_stats['ex_3PA']/player_quarter_stats['Games']).round(1)
player_quarter_stats['p1_3P(%)']=(100*player_quarter_stats['p1_3PM']/player_quarter_stats['p1_3PA']).round(1)
player_quarter_stats['p2_3P(%)']=(100*player_quarter_stats['p2_3PM']/player_quarter_stats['p2_3PA']).round(1)
player_quarter_stats['p3_3P(%)']=(100*player_quarter_stats['p3_3PM']/player_quarter_stats['p3_3PA']).round(1)
player_quarter_stats['p4_3P(%)']=(100*player_quarter_stats['p4_3PM']/player_quarter_stats['p4_3PA']).round(1)
player_quarter_stats['ex_3P(%)']=(100*player_quarter_stats['ex_3PM']/player_quarter_stats['ex_3PA']).round(1)


ftm_compute_total=pbp_data_df2425.loc[pbp_data_df2425.PLAYTYPE=='FTM'][['Team','PLAYTYPE','Player','PERIOD']].value_counts().reset_index().groupby(['Team','Player','PERIOD'])['count'].sum().reset_index().rename(columns={'count':'FTM'}).fillna(0)
sel_team_ftm_compute_total=ftm_compute_total.loc[ftm_compute_total.Team==search_team_team1]
p1_sel_team_ftm_compute_total=sel_team_ftm_compute_total.loc[sel_team_ftm_compute_total.PERIOD==1][['Player','FTM']].rename(columns={'FTM':'p1_FTM'})
p2_sel_team_ftm_compute_total=sel_team_ftm_compute_total.loc[sel_team_ftm_compute_total.PERIOD==2][['Player','FTM']].rename(columns={'FTM':'p2_FTM'})
p3_sel_team_ftm_compute_total=sel_team_ftm_compute_total.loc[sel_team_ftm_compute_total.PERIOD==3][['Player','FTM']].rename(columns={'FTM':'p3_FTM'})
p4_sel_team_ftm_compute_total=sel_team_ftm_compute_total.loc[sel_team_ftm_compute_total.PERIOD==4][['Player','FTM']].rename(columns={'FTM':'p4_FTM'})
p5_sel_team_ftm_compute_total=sel_team_ftm_compute_total.loc[sel_team_ftm_compute_total.PERIOD==5][['Player','FTM']].rename(columns={'FTM':'ex_FTM'})
team_ftm_final=pd.merge(p1_sel_team_ftm_compute_total,p2_sel_team_ftm_compute_total,on='Player',how='outer')
team_ftm_final=pd.merge(team_ftm_final,p3_sel_team_ftm_compute_total,on='Player',how='outer')
team_ftm_final=pd.merge(team_ftm_final,p4_sel_team_ftm_compute_total,on='Player',how='outer')
team_ftm_final=pd.merge(team_ftm_final,p5_sel_team_ftm_compute_total,on='Player',how='outer')

player_quarter_stats=pd.merge(player_quarter_stats,team_ftm_final,on='Player',how='outer').fillna(0)
player_quarter_stats['p1_FTM_avg']=(player_quarter_stats['p1_FTM']/player_quarter_stats['Games']).round(1)
player_quarter_stats['p2_FTM_avg']=(player_quarter_stats['p2_FTM']/player_quarter_stats['Games']).round(1)
player_quarter_stats['p3_FTM_avg']=(player_quarter_stats['p3_FTM']/player_quarter_stats['Games']).round(1)
player_quarter_stats['p4_FTM_avg']=(player_quarter_stats['p4_FTM']/player_quarter_stats['Games']).round(1)
player_quarter_stats['ex_FTM_avg']=(player_quarter_stats['ex_FTM']/player_quarter_stats['Games']).round(1)


fta_compute_total=pbp_data_df2425.loc[pbp_data_df2425.PLAYTYPE.isin(['FTM','FTA'])][['Team','PLAYTYPE','Player','PERIOD']].value_counts().reset_index().groupby(['Team','Player','PERIOD'])['count'].sum().reset_index().rename(columns={'count':'FTA'}).fillna(0)
sel_team_fta_compute_total=fta_compute_total.loc[fta_compute_total.Team==search_team_team1]
p1_sel_team_fta_compute_total=sel_team_fta_compute_total.loc[sel_team_fta_compute_total.PERIOD==1][['Player','FTA']].rename(columns={'FTA':'p1_FTA'})
p2_sel_team_fta_compute_total=sel_team_fta_compute_total.loc[sel_team_fta_compute_total.PERIOD==2][['Player','FTA']].rename(columns={'FTA':'p2_FTA'})
p3_sel_team_fta_compute_total=sel_team_fta_compute_total.loc[sel_team_fta_compute_total.PERIOD==3][['Player','FTA']].rename(columns={'FTA':'p3_FTA'})
p4_sel_team_fta_compute_total=sel_team_fta_compute_total.loc[sel_team_fta_compute_total.PERIOD==4][['Player','FTA']].rename(columns={'FTA':'p4_FTA'})
p5_sel_team_fta_compute_total=sel_team_fta_compute_total.loc[sel_team_fta_compute_total.PERIOD==5][['Player','FTA']].rename(columns={'FTA':'ex_FTA'})
team_fta_final=pd.merge(p1_sel_team_fta_compute_total,p2_sel_team_fta_compute_total,on='Player',how='outer')
team_fta_final=pd.merge(team_fta_final,p3_sel_team_fta_compute_total,on='Player',how='outer')
team_fta_final=pd.merge(team_fta_final,p4_sel_team_fta_compute_total,on='Player',how='outer')
team_fta_final=pd.merge(team_fta_final,p5_sel_team_fta_compute_total,on='Player',how='outer')

player_quarter_stats=pd.merge(player_quarter_stats,team_fta_final,on='Player',how='outer').fillna(0)
player_quarter_stats['p1_FTA_avg']=(player_quarter_stats['p1_FTA']/player_quarter_stats['Games']).round(1)
player_quarter_stats['p2_FTA_avg']=(player_quarter_stats['p2_FTA']/player_quarter_stats['Games']).round(1)
player_quarter_stats['p3_FTA_avg']=(player_quarter_stats['p3_FTA']/player_quarter_stats['Games']).round(1)
player_quarter_stats['p4_FTA_avg']=(player_quarter_stats['p4_FTA']/player_quarter_stats['Games']).round(1)
player_quarter_stats['ex_FTA_avg']=(player_quarter_stats['ex_FTA']/player_quarter_stats['Games']).round(1)
player_quarter_stats['p1_FT(%)']=(100*player_quarter_stats['p1_FTM']/player_quarter_stats['p1_FTA']).round(1)
player_quarter_stats['p2_FT(%)']=(100*player_quarter_stats['p2_FTM']/player_quarter_stats['p2_FTA']).round(1)
player_quarter_stats['p3_FT(%)']=(100*player_quarter_stats['p3_FTM']/player_quarter_stats['p3_FTA']).round(1)
player_quarter_stats['p4_FT(%)']=(100*player_quarter_stats['p4_FTM']/player_quarter_stats['p4_FTA']).round(1)
player_quarter_stats['ex_FT(%)']=(100*player_quarter_stats['ex_FTM']/player_quarter_stats['ex_FTA']).round(1)
player_quarter_stats["p1_PIR"]=(player_quarter_stats["p1_PTS"].fillna(0)+
                                             player_quarter_stats["p1_AS"].fillna(0)+
                                             player_quarter_stats["p1_TR"].fillna(0)-
                                             player_quarter_stats["p1_TO"].fillna(0)+
                                             player_quarter_stats["p1_STL"].fillna(0)+
                                             player_quarter_stats["p1_BLKM"].fillna(0)-
                                             player_quarter_stats["p1_BLKR"].fillna(0)-
                                             player_quarter_stats["p1_PF"].fillna(0)+
                                             player_quarter_stats["p1_2PM"].fillna(0)+player_quarter_stats["p1_3PM"].fillna(0)+player_quarter_stats["p1_FTM"].fillna(0)-
                                             player_quarter_stats["p1_2PA"].fillna(0)-player_quarter_stats["p1_3PA"].fillna(0)+player_quarter_stats["p1_FTA"].fillna(0))
player_quarter_stats["p2_PIR"] = (player_quarter_stats["p2_PTS"].fillna(0) +
                                           player_quarter_stats["p2_AS"].fillna(0) +
                                           player_quarter_stats["p2_TR"].fillna(0) -
                                           player_quarter_stats["p2_TO"].fillna(0) +
                                           player_quarter_stats["p2_STL"].fillna(0) +
                                           player_quarter_stats["p2_BLKM"].fillna(0) -
                                           player_quarter_stats["p2_BLKR"].fillna(0) -
                                           player_quarter_stats["p2_PF"].fillna(0) +
                                           player_quarter_stats["p2_2PM"].fillna(0) + player_quarter_stats[
                                               "p2_3PM"].fillna(0) + player_quarter_stats["p2_FTM"].fillna(0) -
                                           player_quarter_stats["p3_2PA"].fillna(0) - player_quarter_stats[
                                               "p2_3PA"].fillna(0) + player_quarter_stats["p2_FTA"].fillna(0))
player_quarter_stats["p3_PIR"] = (player_quarter_stats["p3_PTS"].fillna(0) +
                                           player_quarter_stats["p3_AS"].fillna(0) +
                                           player_quarter_stats["p3_TR"].fillna(0) -
                                           player_quarter_stats["p3_TO"].fillna(0) +
                                           player_quarter_stats["p3_STL"].fillna(0) +
                                           player_quarter_stats["p3_BLKM"].fillna(0) -
                                           player_quarter_stats["p3_BLKR"].fillna(0) -
                                           player_quarter_stats["p3_PF"].fillna(0) +
                                           player_quarter_stats["p3_2PM"].fillna(0) + player_quarter_stats[
                                               "p3_3PM"].fillna(0) + player_quarter_stats["p3_FTM"].fillna(0) -
                                           player_quarter_stats["p3_2PA"].fillna(0) - player_quarter_stats[
                                               "p3_3PA"].fillna(0) + player_quarter_stats["p3_FTA"].fillna(0))

player_quarter_stats["p4_PIR"] = (player_quarter_stats["p4_PTS"].fillna(0) +
                                           player_quarter_stats["p4_AS"].fillna(0) +
                                           player_quarter_stats["p4_TR"].fillna(0) -
                                           player_quarter_stats["p4_TO"].fillna(0) +
                                           player_quarter_stats["p4_STL"].fillna(0) +
                                           player_quarter_stats["p4_BLKM"].fillna(0) -
                                           player_quarter_stats["p4_BLKR"].fillna(0) -
                                           player_quarter_stats["p4_PF"].fillna(0) +
                                           player_quarter_stats["p4_2PM"].fillna(0) + player_quarter_stats[
                                               "p4_3PM"].fillna(0) + player_quarter_stats["p4_FTM"] -
                                           player_quarter_stats["p4_2PA"].fillna(0) - player_quarter_stats[
                                               "p4_3PA"].fillna(0) + player_quarter_stats["p4_FTA"].fillna(0))

player_quarter_stats["ex_PIR"] = (player_quarter_stats["ex_PTS"].fillna(0) +
                                           player_quarter_stats["ex_AS"].fillna(0) +
                                           player_quarter_stats["ex_TR"].fillna(0) -
                                           player_quarter_stats["ex_TO"].fillna(0) +
                                           player_quarter_stats["ex_STL"].fillna(0) +
                                           player_quarter_stats["ex_BLKM"].fillna(0) -
                                           player_quarter_stats["ex_BLKR"].fillna(0) -
                                           player_quarter_stats["ex_PF"].fillna(0) +
                                           player_quarter_stats["ex_2PM"].fillna(0) + player_quarter_stats[
                                               "ex_3PM"].fillna(0) + player_quarter_stats["ex_FTM"].fillna(0) -
                                           player_quarter_stats["ex_2PA"].fillna(0) - player_quarter_stats[
                                               "ex_3PA"].fillna(0) + player_quarter_stats["ex_FTA"].fillna(0))
player_quarter_stats['p1_PIR_avg'] = (
            player_quarter_stats['p1_PIR'] / player_quarter_stats['Games']).round(1)
player_quarter_stats['p2_PIR_avg'] = (
            player_quarter_stats['p2_PIR'] / player_quarter_stats['Games']).round(1)
player_quarter_stats['p3_PIR_avg'] = (
            player_quarter_stats['p3_PIR'] / player_quarter_stats['Games']).round(1)
player_quarter_stats['p4_PIR_avg'] = (
            player_quarter_stats['p4_PIR'] / player_quarter_stats['Games']).round(1)

player_quarter_stats['ex_PIR_avg'] = (
            player_quarter_stats['ex_PIR'] / player_quarter_stats['Games']).round(1)
regex1="Player|"+stat_choose
interactive_table(
                player_quarter_stats.set_index('Player').filter(regex=regex1),
                paging=False, height=900, width=2000, showIndex=True,
                classes="display order-column nowrap table_with_monospace_font", searching=False,
                fixedColumns=True, select=True, info=False, scrollCollapse=True,
                scrollX=True, scrollY=1000, fixedHeader=True, scroller=True, filter='bottom',
                columnDefs=[{"className": "dt-center", "targets": "_all"}])
