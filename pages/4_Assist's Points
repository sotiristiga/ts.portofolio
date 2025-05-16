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
st.sidebar.write("If an error message appears, please refresh the page")
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
    if sit.filter(regex='JB|O|D|TOUT|FTM2FGA|D|ST|3FGM|CM|TO|3FGA|RV||'):
        return 24
    elif sit.filter(regex='O'):
        return 14

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
extra_details=euroleague_2024_2025_playerstats.groupby(['Fixture_Team_Season','Against',"idseason"])['Player'].count().reset_index()
extra_details=extra_details.drop('Player',axis=1)

pbp_data_df2425=pd.read_csv("C:/Users/surve/OneDrive/Desktop/Tiganitas work/EUROLEAGUE/stats/basketnews stats/pbp_data_df2425.csv")

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









pbp_data_2425=pbp_data_df2425[['GAMECODE','Season','Phase','Fixture','PERIOD','MINUTE','MARKERTIME','Team','Player','PLAYTYPE','Against',"SECONDS_diff"]]
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



coach_timeouts_per_period=coachtimeout[['Coach','PERIOD']].value_counts().reset_index()
period_1_timeouts=coach_timeouts_per_period.loc[coach_timeouts_per_period.PERIOD==1][["Coach",'count']].rename(columns={'count':'P1'})
period_2_timeouts=coach_timeouts_per_period.loc[coach_timeouts_per_period.PERIOD==2][["Coach",'count']].rename(columns={'count':'P2'})
period_3_timeouts=coach_timeouts_per_period.loc[coach_timeouts_per_period.PERIOD==3][["Coach",'count']].rename(columns={'count':'P3'})
period_4_timeouts=coach_timeouts_per_period.loc[coach_timeouts_per_period.PERIOD==4][["Coach",'count']].rename(columns={'count':'P4'})
period_ex_timeouts=coach_timeouts_per_period.loc[coach_timeouts_per_period.PERIOD==5][["Coach",'count']].rename(columns={'count':'ET'})

coach_timeouts_per_period_final=pd.merge(period_1_timeouts,period_2_timeouts,on='Coach',how='outer')
coach_timeouts_per_period_final=pd.merge(coach_timeouts_per_period_final,period_3_timeouts,on='Coach',how='outer')
coach_timeouts_per_period_final=pd.merge(coach_timeouts_per_period_final,period_4_timeouts,on='Coach',how='outer')
coach_timeouts_per_period_final=pd.merge(coach_timeouts_per_period_final,period_ex_timeouts,on='Coach',how='outer').fillna(0)

pbp_data_df2425=pbp_data_df2425.reset_index()
pbp_data_df2425.drop('index',axis=1,inplace=True)



total_fixtures=pbp_data_df2425['Fixture'].unique()
for i in pbp_data_df2425.index:
    if i==0:
        pbp_data_df2425.loc[0, 'Timer_new'] = pbp_data_df2425.loc[0, 'MARKERTIME']
    else:
        previous = pbp_data_df2425.loc[i-1,'PLAYTYPE']
        current=   pbp_data_df2425.loc[i,'PLAYTYPE']
        if previous=="2FGM":
            if current=='AS':
                pbp_data_df2425.loc[i, 'Timer_new'] = pbp_data_df2425.loc[i-1, 'MARKERTIME']
            else:
                pbp_data_df2425.loc[i, 'Timer_new'] = pbp_data_df2425.loc[i, 'MARKERTIME']
        elif previous=="3FGM":
            if current=='AS':
                pbp_data_df2425.loc[i, 'Timer_new'] = pbp_data_df2425.loc[i-1, 'MARKERTIME']
            else:
                pbp_data_df2425.loc[i, 'Timer_new'] = pbp_data_df2425.loc[i, 'MARKERTIME']
        elif previous=="FTM":
            if current=='AS':
                pbp_data_df2425.loc[i, 'Timer_new'] = pbp_data_df2425.loc[i-1, 'MARKERTIME']
            else:
                pbp_data_df2425.loc[i, 'Timer_new'] = pbp_data_df2425.loc[i, 'MARKERTIME']
        else:
            pbp_data_df2425.loc[i, 'Timer_new'] = pbp_data_df2425.loc[i, 'MARKERTIME']








n=1
for i in pbp_data_df2425.index:
    if i==0:
        pbp_data_df2425.loc[0, 'numberofplay'] =  pbp_data_df2425.loc[0, 'idseason']+"_1"
    else:
        previous = pbp_data_df2425.loc[i - 1, 'Timer_new']
        current = pbp_data_df2425.loc[i, 'Timer_new']
        if previous==current:
            pbp_data_df2425.loc[i, 'numberofplay'] = pbp_data_df2425.loc[i-1, 'numberofplay']
        else:
            n=n+1

            pbp_data_df2425.loc[i, 'numberofplay']= pbp_data_df2425.loc[i, 'idseason'] + "_" + str(n)

st.sidebar.markdown('''
  * ## [Points scored from their assists](#points-scored-from-their-assists)
  * ## [Avg points scored from their assists](#avg-points-scored-from-their-assists)
  * ## [Points per Assist](#points-per-assist)
  * ## [Duos with the most points scored combined](#duos-with-the-most-points-scored-combined)
  * ## [Duos with the most avg points scored combined](#duos-with-the-most-avg-points-scored-combined)
  * ## [Points scored from assists](#points-scored-from-assists)
  * ## [Avg points scored from assists](#avg-points-scored-from-assists)
  * ## [Points scored without assists](#points-scored-without-assists)
  * ## [Avg points scored without assists](#avg-points-scored-without-assists)
''', unsafe_allow_html=True)

madeshots=pbp_data_df2425.loc[pbp_data_df2425.PLAYTYPE.isin(["2FGM","3FGM","FTM"])][['Season',"Phase","idseason","Team","Player","numberofplay","PLAYTYPE"]]
assists=pbp_data_df2425.loc[pbp_data_df2425.PLAYTYPE=="AS"][['Season',"Phase","idseason","Team","Player","numberofplay","PLAYTYPE"]].rename(columns={"Player":"Assist Player","PLAYTYPE":"Assist"})

together=pd.merge(madeshots,assists,how='outer')
together['Points'] = together['PLAYTYPE'].apply(points_scored)
together['Assist Player']=together['Assist Player'].replace(np.nan, "No")
together['Assist']=together['Assist'].replace(np.nan, "No")
together=together.groupby(['Season',"Phase","idseason","Team","Player","numberofplay","PLAYTYPE","Assist Player","Assist"])["Points"].sum().reset_index()

most_points_assists=together.loc[together["Assist Player"]!="No"].groupby(["Assist Player","Team"])["Points"].sum().reset_index().sort_values('Points',ascending=False).reset_index()

most_points_assists.drop('index', axis=1, inplace=True)
most_points_assists = most_points_assists.reset_index()
most_points_assists['No.'] = most_points_assists['index'] + 1
st.header("Points scored from their assists")
interactive_table(
                most_points_assists[["No.","Assist Player","Team","Points"]].head(25),
                paging=True, height=2000, width=2000, showIndex=False,
                classes="display order-column nowrap table_with_monospace_font", searching=True,
                fixedColumns=True, select=True, info=False, scrollCollapse=True,
                scrollX=True, scrollY=2000, fixedHeader=True, scroller=True, filter='bottom',
                columnDefs=[{"className": "dt-center", "targets": "_all"}])
most_points_assists_pg=together.loc[together["Assist Player"]!="No"].groupby(["Assist Player","Team","idseason"])["Points"].sum().reset_index().groupby(["Assist Player","Team"])['Points'].mean().reset_index().sort_values('Points',ascending=False).reset_index()


most_points_assists_pg.drop('index', axis=1, inplace=True)
most_points_assists_pg = most_points_assists_pg.reset_index()
most_points_assists_pg['No.'] = most_points_assists_pg['index'] + 1
st.header("Avg points scored from their assists")
interactive_table(
                most_points_assists_pg[["No.","Assist Player","Team","Points"]].head(25).round(1),
                paging=True, height=2000, width=2000, showIndex=False,
                classes="display order-column nowrap table_with_monospace_font", searching=True,
                fixedColumns=True, select=True, info=False, scrollCollapse=True,
                scrollX=True, scrollY=2000, fixedHeader=True, scroller=True, filter='bottom',
                columnDefs=[{"className": "dt-center", "targets": "_all"}])

st.header("Points per Assist")
filters1=together.loc[together["Assist Player"]!="No"]["Assist Player"].value_counts().reset_index()
filters1=filters1.loc[filters1["count"]>90]["Assist Player"].unique()
pointsperasist=together.loc[together['Assist Player'].isin(filters1)].groupby(['Assist Player',"Team"])["Points"].mean().reset_index().round(1).sort_values('Points',ascending=False).reset_index()
pointsperasist.drop('index', axis=1, inplace=True)
pointsperasist = pointsperasist.reset_index().rename(columns={"Points":"PTS/AS"})
pointsperasist['No.'] = pointsperasist['index'] + 1
interactive_table(
                pointsperasist[["No.","Assist Player","Team","PTS/AS"]],
                paging=True, height=2000, width=2000, showIndex=False,
                classes="display order-column nowrap table_with_monospace_font", searching=True,
                fixedColumns=True, select=True, info=False, scrollCollapse=True,
                scrollX=True, scrollY=2000, fixedHeader=True, scroller=True, filter='bottom',
                columnDefs=[{"className": "dt-center", "targets": "_all"}])
st.header("Duos with the most points scored combined")
most_points_assists=together.loc[together["Assist Player"]!="No"].groupby(["Player","Assist Player","Team"])["Points"].sum().reset_index().sort_values('Points',ascending=False).reset_index()
most_points_assists.drop('index', axis=1, inplace=True)
most_points_assists = most_points_assists.reset_index().rename(columns={"Player":"Player Scored"})
most_points_assists['No.'] = most_points_assists['index'] + 1
interactive_table(
                most_points_assists[["No.","Player Scored","Assist Player","Team","Points"]].head(25).round(1),
                paging=True, height=2000, width=2000, showIndex=False,
                classes="display order-column nowrap table_with_monospace_font", searching=True,
                fixedColumns=True, select=True, info=False, scrollCollapse=True,
                scrollX=True, scrollY=2000, fixedHeader=True, scroller=True, filter='bottom',
                columnDefs=[{"className": "dt-center", "targets": "_all"}])


filters=together.loc[together["Assist Player"]!="No"][["Player","Team","Assist Player"]].value_counts().reset_index()

filters["duo"]=filters["Player"]+"-"+filters["Assist Player"]
filters=filters.loc[filters['count']>30]["duo"].unique()

most_points_assists=together.loc[together["Assist Player"]!="No"].groupby(["idseason","Player","Assist Player","Team"])["Points"].sum().reset_index()
most_points_assists["duo"]=most_points_assists["Player"]+"-"+most_points_assists["Assist Player"]

most_points_assists=most_points_assists.loc[most_points_assists.duo.isin(filters)].groupby(["Player","Assist Player","Team"])['Points'].mean().reset_index().sort_values('Points',ascending=False).reset_index()
most_points_assists.drop('index', axis=1, inplace=True)
most_points_assists = most_points_assists.reset_index().rename(columns={"Player":"Player Scored"})
most_points_assists['No.'] = most_points_assists['index'] + 1
st.header("Duos with the most avg points scored combined")
interactive_table(
                most_points_assists[["No.","Player Scored","Assist Player","Team","Points"]].head(25).round(1),
                paging=True, height=2000, width=2000, showIndex=False,
                classes="display order-column nowrap table_with_monospace_font", searching=True,
                fixedColumns=True, select=True, info=False, scrollCollapse=True,
                scrollX=True, scrollY=2000, fixedHeader=True, scroller=True, filter='bottom',
                columnDefs=[{"className": "dt-center", "targets": "_all"}])

most_points_assists=together.loc[together["Assist Player"]!="No"].groupby(["Player","Team"])["Points"].sum().reset_index().sort_values('Points',ascending=False).reset_index()

most_points_assists.drop('index', axis=1, inplace=True)
most_points_assists = most_points_assists.reset_index()
most_points_assists['No.'] = most_points_assists['index'] + 1
st.header("Points scored from assists")
interactive_table(
                most_points_assists[["No.","Player","Team","Points"]].head(25),
                paging=True, height=2000, width=2000, showIndex=False,
                classes="display order-column nowrap table_with_monospace_font", searching=True,
                fixedColumns=True, select=True, info=False, scrollCollapse=True,
                scrollX=True, scrollY=2000, fixedHeader=True, scroller=True, filter='bottom',
                columnDefs=[{"className": "dt-center", "targets": "_all"}])




most_points_assists_pg=together.loc[together["Assist Player"]!="No"].groupby(["Player","Team","idseason"])["Points"].sum().reset_index().groupby(["Player","Team"])['Points'].mean().reset_index().sort_values('Points',ascending=False).reset_index()


most_points_assists_pg.drop('index', axis=1, inplace=True)
most_points_assists_pg = most_points_assists_pg.reset_index()
most_points_assists_pg['No.'] = most_points_assists_pg['index'] + 1
st.header("Avg points scored from assists")
interactive_table(
                most_points_assists_pg[["No.","Player","Team","Points"]].head(25).round(1),
                paging=True, height=2000, width=2000, showIndex=False,
                classes="display order-column nowrap table_with_monospace_font", searching=True,
                fixedColumns=True, select=True, info=False, scrollCollapse=True,
                scrollX=True, scrollY=2000, fixedHeader=True, scroller=True, filter='bottom',
                columnDefs=[{"className": "dt-center", "targets": "_all"}])




most_points_assists=together.loc[together["Assist Player"]=="No"].groupby(["Player","Team"])["Points"].sum().reset_index().sort_values('Points',ascending=False).reset_index()

most_points_assists.drop('index', axis=1, inplace=True)
most_points_assists = most_points_assists.reset_index()
most_points_assists['No.'] = most_points_assists['index'] + 1
st.header("Points scored without assists")
interactive_table(
                most_points_assists[["No.","Player","Team","Points"]].head(25),
                paging=True, height=2000, width=2000, showIndex=False,
                classes="display order-column nowrap table_with_monospace_font", searching=True,
                fixedColumns=True, select=True, info=False, scrollCollapse=True,
                scrollX=True, scrollY=2000, fixedHeader=True, scroller=True, filter='bottom',
                columnDefs=[{"className": "dt-center", "targets": "_all"}])




most_points_assists_pg=together.loc[together["Assist Player"]=="No"].groupby(["Player","Team","idseason"])["Points"].sum().reset_index().groupby(["Player","Team"])['Points'].mean().reset_index().sort_values('Points',ascending=False).reset_index()


most_points_assists_pg.drop('index', axis=1, inplace=True)
most_points_assists_pg = most_points_assists_pg.reset_index()
most_points_assists_pg['No.'] = most_points_assists_pg['index'] + 1
st.header("Avg points scored without assists")
interactive_table(
                most_points_assists_pg[["No.","Player","Team","Points"]].head(25).round(1),
                paging=True, height=2000, width=2000, showIndex=False,
                classes="display order-column nowrap table_with_monospace_font", searching=True,
                fixedColumns=True, select=True, info=False, scrollCollapse=True,
                scrollX=True, scrollY=2000, fixedHeader=True, scroller=True, filter='bottom',
                columnDefs=[{"className": "dt-center", "targets": "_all"}])
