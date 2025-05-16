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

st.set_page_config(layout='wide', page_title="Technical Fouls", page_icon="🏀")


def download_image(url, save_as):
    urllib.request.urlretrieve(url, save_as)


download_image('https://raw.githubusercontent.com/sotiristiga/Euroleague_dash/refs/heads/main/eurologo.png',
               'eurologo.png')
st.image(Image.open("eurologo.png"), width=100)

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


def team_coach(Team, Fixture):
    if Team == 'PAN':
        return 'E. Ataman'
    if Team == 'OLY':
        return 'G. Bartzokas'
    if Team == 'PRB':
        return 'T. Splitter'
    if Team == 'FEN':
        return 'S. Jaskevicius'
    if Team == 'EFE':
        if Fixture <= 19:
            return 'T. Mijatović'
        else:
            return 'L. Bianchi'
    if Team == 'CRV':
        return 'I. Sfairopoulos'
    if Team == 'BAY':
        return 'G. Herbert'
    if Team == 'RMB':
        return 'C. Mateo'
    if Team == 'BAR':
        return 'J. Penarroya'
    if Team == 'ZAL':
        return 'A. Trinkieri'
    if Team == 'MIL':
        return 'E. Messina'
    if Team == 'BAS':
        return 'P. Laso'
    if Team == 'PAR':
        return 'Z. Obradovic'
    if Team == 'VIL':
        return 'P. Poupet'
    if Team == 'MAC':
        return 'O. Kattash'
    if Team == 'BER':
        return 'I. Gonzalez'
    if Team == 'ASM':
        if Fixture <= 11:
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


euroleague_2016_2017_playerstats = pd.read_csv(
    f"https://raw.githubusercontent.com/sotiristiga/euroleague/main/euroleague_2016_2017_playerstats.csv")
euroleague_2016_2017_playerstats['idseason'] = euroleague_2016_2017_playerstats['IDGAME'] + "_" + \
                                               euroleague_2016_2017_playerstats['Season']
euroleague_2016_2017_playerstats[['Fixture', 'Game']] = euroleague_2016_2017_playerstats['IDGAME'].str.split('_', n=1,
                                                                                                             expand=True)
euroleague_2016_2017_playerstats['Fixture'] = pd.to_numeric(euroleague_2016_2017_playerstats['Fixture'])
euroleague_2016_2017_playerstats['Round'] = euroleague_2016_2017_playerstats['Fixture'].apply(fixture_format1)

euroleague_2017_2018_playerstats = pd.read_csv(
    f"https://raw.githubusercontent.com/sotiristiga/euroleague/main/euroleague_2017_2018_playerstats.csv")
euroleague_2017_2018_playerstats['idseason'] = euroleague_2017_2018_playerstats['IDGAME'] + "_" + \
                                               euroleague_2017_2018_playerstats['Season']
euroleague_2017_2018_playerstats[['Fixture', 'Game']] = euroleague_2017_2018_playerstats['IDGAME'].str.split('_', n=1,
                                                                                                             expand=True)
euroleague_2017_2018_playerstats['Fixture'] = pd.to_numeric(euroleague_2017_2018_playerstats['Fixture'])
euroleague_2017_2018_playerstats['Round'] = euroleague_2017_2018_playerstats['Fixture'].apply(fixture_format2)

euroleague_2018_2019_playerstats = pd.read_csv(
    f"https://raw.githubusercontent.com/sotiristiga/euroleague/main/euroleague_2018_2019_playerstats.csv")
euroleague_2018_2019_playerstats['idseason'] = euroleague_2018_2019_playerstats['IDGAME'] + "_" + \
                                               euroleague_2018_2019_playerstats['Season']
euroleague_2018_2019_playerstats[['Fixture', 'Game']] = euroleague_2018_2019_playerstats['IDGAME'].str.split('_', n=1,
                                                                                                             expand=True)
euroleague_2018_2019_playerstats['Fixture'] = pd.to_numeric(euroleague_2018_2019_playerstats['Fixture'])
euroleague_2018_2019_playerstats['Round'] = euroleague_2018_2019_playerstats['Fixture'].apply(fixture_format1)

euroleague_2019_2020_playerstats = pd.read_csv(
    f"https://raw.githubusercontent.com/sotiristiga/euroleague/main/euroleague_2019_2020_playerstats.csv")
euroleague_2019_2020_playerstats['idseason'] = euroleague_2019_2020_playerstats['IDGAME'] + "_" + \
                                               euroleague_2019_2020_playerstats['Season']
euroleague_2019_2020_playerstats[['Fixture', 'Game']] = euroleague_2019_2020_playerstats['IDGAME'].str.split('_', n=1,
                                                                                                             expand=True)
euroleague_2019_2020_playerstats['Fixture'] = pd.to_numeric(euroleague_2019_2020_playerstats['Fixture'])
euroleague_2019_2020_playerstats['Round'] = euroleague_2019_2020_playerstats['Fixture'].apply(fixture_format3)

euroleague_2020_2021_playerstats = pd.read_csv(
    f"https://raw.githubusercontent.com/sotiristiga/euroleague/main/euroleague_2020_2021_playerstats.csv")
euroleague_2020_2021_playerstats['idseason'] = euroleague_2020_2021_playerstats['IDGAME'] + "_" + \
                                               euroleague_2020_2021_playerstats['Season']
euroleague_2020_2021_playerstats[['Fixture', 'Game']] = euroleague_2020_2021_playerstats['IDGAME'].str.split('_', n=1,
                                                                                                             expand=True)
euroleague_2020_2021_playerstats['Fixture'] = pd.to_numeric(euroleague_2020_2021_playerstats['Fixture'])
euroleague_2020_2021_playerstats['Round'] = euroleague_2020_2021_playerstats['Fixture'].apply(fixture_format4)

euroleague_2021_2022_playerstats = pd.read_csv(
    f"https://raw.githubusercontent.com/sotiristiga/euroleague/main/euroleague_2021_2022_playerstats.csv")
euroleague_2021_2022_playerstats['idseason'] = euroleague_2021_2022_playerstats['IDGAME'] + "_" + \
                                               euroleague_2021_2022_playerstats['Season']
euroleague_2021_2022_playerstats[['Fixture', 'Game']] = euroleague_2021_2022_playerstats['IDGAME'].str.split('_', n=1,
                                                                                                             expand=True)
euroleague_2021_2022_playerstats['Fixture'] = pd.to_numeric(euroleague_2021_2022_playerstats['Fixture'])
euroleague_2021_2022_playerstats['Round'] = euroleague_2021_2022_playerstats['Fixture'].apply(fixture_format4)

euroleague_2022_2023_playerstats = pd.read_csv(
    f"https://raw.githubusercontent.com/sotiristiga/euroleague/main/euroleague_2022_2023_playerstats.csv")
euroleague_2022_2023_playerstats['idseason'] = euroleague_2022_2023_playerstats['IDGAME'] + "_" + \
                                               euroleague_2022_2023_playerstats['Season']
euroleague_2022_2023_playerstats[['Fixture', 'Game']] = euroleague_2022_2023_playerstats['IDGAME'].str.split('_', n=1,
                                                                                                             expand=True)
euroleague_2022_2023_playerstats['Fixture'] = pd.to_numeric(euroleague_2022_2023_playerstats['Fixture'])
euroleague_2022_2023_playerstats['Round'] = euroleague_2022_2023_playerstats['Fixture'].apply(fixture_format4)

euroleague_2023_2024_playerstats = pd.read_csv(
    f"https://raw.githubusercontent.com/sotiristiga/euroleague/main/euroleague_2023_2024_playerstats.csv")
euroleague_2023_2024_playerstats['idseason'] = euroleague_2023_2024_playerstats['IDGAME'] + "_" + \
                                               euroleague_2023_2024_playerstats['Season']
euroleague_2023_2024_playerstats[['Fixture', 'Game']] = euroleague_2023_2024_playerstats['IDGAME'].str.split('_', n=1,
                                                                                                             expand=True)
euroleague_2023_2024_playerstats['Fixture'] = pd.to_numeric(euroleague_2023_2024_playerstats['Fixture'])
euroleague_2023_2024_playerstats['Round'] = euroleague_2023_2024_playerstats['Fixture'].apply(fixture_format5)

euroleague_2024_2025_playerstats = pd.read_csv(
    f"https://raw.githubusercontent.com/sotiristiga/euroleague/main/euroleague_2024_2025_playerstats.csv")
euroleague_2024_2025_playerstats['idseason'] = euroleague_2024_2025_playerstats['IDGAME'] + "_" + \
                                               euroleague_2024_2025_playerstats['Season']
euroleague_2024_2025_playerstats[['Fixture', 'Game']] = euroleague_2024_2025_playerstats['IDGAME'].str.split('_', n=1,
                                                                                                             expand=True)
euroleague_2024_2025_playerstats['Fixture_Team_Season'] = euroleague_2024_2025_playerstats['Fixture'] + "_" + \
                                                          euroleague_2024_2025_playerstats['Team'] + "_" + \
                                                          euroleague_2024_2025_playerstats['Season']
euroleague_2024_2025_playerstats['Fixture'] = pd.to_numeric(euroleague_2024_2025_playerstats['Fixture'])

euroleague_2024_2025_playerstats['Round'] = euroleague_2024_2025_playerstats['Fixture'].apply(fixture_format5)

euroleague_2016_2017_results = pd.read_csv(
    f"https://raw.githubusercontent.com/sotiristiga/euroleague/main/euroleague_2016_2017_results.csv")
euroleague_2016_2017_results['idseason'] = euroleague_2016_2017_results['IDGAME'] + "_" + euroleague_2016_2017_results[
    'Season']
euroleague_2016_2017_results[['Fixture', 'Game']] = euroleague_2016_2017_results['IDGAME'].str.split('_', n=1,
                                                                                                     expand=True)
euroleague_2016_2017_results['Fixture'] = pd.to_numeric(euroleague_2016_2017_results['Fixture'])
euroleague_2016_2017_results['Round'] = euroleague_2016_2017_results['Fixture'].apply(fixture_format1)

euroleague_2017_2018_results = pd.read_csv(
    f"https://raw.githubusercontent.com/sotiristiga/euroleague/main/euroleague_2017_2018_results.csv")
euroleague_2017_2018_results['idseason'] = euroleague_2017_2018_results['IDGAME'] + "_" + euroleague_2017_2018_results[
    'Season']
euroleague_2017_2018_results[['Fixture', 'Game']] = euroleague_2017_2018_results['IDGAME'].str.split('_', n=1,
                                                                                                     expand=True)
euroleague_2017_2018_results['Fixture'] = pd.to_numeric(euroleague_2017_2018_results['Fixture'])
euroleague_2017_2018_results['Round'] = euroleague_2017_2018_results['Fixture'].apply(fixture_format2)

euroleague_2018_2019_results = pd.read_csv(
    f"https://raw.githubusercontent.com/sotiristiga/euroleague/main/euroleague_2018_2019_results.csv")
euroleague_2018_2019_results['idseason'] = euroleague_2018_2019_results['IDGAME'] + "_" + euroleague_2018_2019_results[
    'Season']
euroleague_2018_2019_results[['Fixture', 'Game']] = euroleague_2018_2019_results['IDGAME'].str.split('_', n=1,
                                                                                                     expand=True)
euroleague_2018_2019_results['Fixture'] = pd.to_numeric(euroleague_2018_2019_results['Fixture'])
euroleague_2018_2019_results['Round'] = euroleague_2018_2019_results['Fixture'].apply(fixture_format1)

euroleague_2019_2020_results = pd.read_csv(
    f"https://raw.githubusercontent.com/sotiristiga/euroleague/main/euroleague_2019_2020_results.csv")
euroleague_2019_2020_results['idseason'] = euroleague_2019_2020_results['IDGAME'] + "_" + euroleague_2019_2020_results[
    'Season']
euroleague_2019_2020_results[['Fixture', 'Game']] = euroleague_2019_2020_results['IDGAME'].str.split('_', n=1,
                                                                                                     expand=True)
euroleague_2019_2020_results['Fixture'] = pd.to_numeric(euroleague_2019_2020_results['Fixture'])
euroleague_2019_2020_results['Round'] = euroleague_2019_2020_results['Fixture'].apply(fixture_format3)

euroleague_2020_2021_results = pd.read_csv(
    f"https://raw.githubusercontent.com/sotiristiga/euroleague/main/euroleague_2020_2021_results.csv")
euroleague_2020_2021_results['idseason'] = euroleague_2020_2021_results['IDGAME'] + "_" + euroleague_2020_2021_results[
    'Season']
euroleague_2020_2021_results[['Fixture', 'Game']] = euroleague_2020_2021_results['IDGAME'].str.split('_', n=1,
                                                                                                     expand=True)
euroleague_2020_2021_results['Fixture'] = pd.to_numeric(euroleague_2020_2021_results['Fixture'])
euroleague_2020_2021_results['Round'] = euroleague_2020_2021_results['Fixture'].apply(fixture_format4)

euroleague_2021_2022_results = pd.read_csv(
    f"https://raw.githubusercontent.com/sotiristiga/euroleague/main/euroleague_2021_2022_results.csv")
euroleague_2021_2022_results['idseason'] = euroleague_2021_2022_results['IDGAME'] + "_" + euroleague_2021_2022_results[
    'Season']
euroleague_2021_2022_results[['Fixture', 'Game']] = euroleague_2021_2022_results['IDGAME'].str.split('_', n=1,
                                                                                                     expand=True)
euroleague_2021_2022_results['Fixture'] = pd.to_numeric(euroleague_2021_2022_results['Fixture'])
euroleague_2021_2022_results['Round'] = euroleague_2021_2022_results['Fixture'].apply(fixture_format4)

euroleague_2022_2023_results = pd.read_csv(
    f"https://raw.githubusercontent.com/sotiristiga/euroleague/main/euroleague_2022_2023_results.csv")
euroleague_2022_2023_results['idseason'] = euroleague_2022_2023_results['IDGAME'] + "_" + euroleague_2022_2023_results[
    'Season']
euroleague_2022_2023_results[['Fixture', 'Game']] = euroleague_2022_2023_results['IDGAME'].str.split('_', n=1,
                                                                                                     expand=True)
euroleague_2022_2023_results['Fixture'] = pd.to_numeric(euroleague_2022_2023_results['Fixture'])
euroleague_2022_2023_results['Round'] = euroleague_2022_2023_results['Fixture'].apply(fixture_format4)

euroleague_2023_2024_results = pd.read_csv(
    f"https://raw.githubusercontent.com/sotiristiga/euroleague/main/euroleague_2023_2024_results.csv")
euroleague_2023_2024_results['idseason'] = euroleague_2023_2024_results['IDGAME'] + "_" + euroleague_2023_2024_results[
    'Season']
euroleague_2023_2024_results[['Fixture', 'Game']] = euroleague_2023_2024_results['IDGAME'].str.split('_', n=1,
                                                                                                     expand=True)
euroleague_2023_2024_results['Fixture'] = pd.to_numeric(euroleague_2023_2024_results['Fixture'])
euroleague_2023_2024_results['Round'] = euroleague_2023_2024_results['Fixture'].apply(fixture_format5)

euroleague_2024_2025_results = pd.read_csv(
    f"https://raw.githubusercontent.com/sotiristiga/euroleague/main/euroleague_2024_2025_results.csv")
euroleague_2024_2025_results['idseason'] = euroleague_2024_2025_results['IDGAME'] + "_" + euroleague_2024_2025_results[
    'Season']
euroleague_2024_2025_results[['Fixture', 'Game']] = euroleague_2024_2025_results['IDGAME'].str.split('_', n=1,
                                                                                                     expand=True)

euroleague_2024_2025_results['Fixture'] = pd.to_numeric(euroleague_2024_2025_results['Fixture'])
euroleague_2024_2025_results['Round'] = euroleague_2024_2025_results['Fixture'].apply(fixture_format5)

All_Seasons = pd.concat(
    [euroleague_2016_2017_playerstats, euroleague_2017_2018_playerstats, euroleague_2018_2019_playerstats,
     euroleague_2019_2020_playerstats, euroleague_2020_2021_playerstats, euroleague_2021_2022_playerstats,
     euroleague_2022_2023_playerstats, euroleague_2023_2024_playerstats, euroleague_2024_2025_playerstats])

All_Seasons_results = pd.concat(
    [euroleague_2016_2017_results, euroleague_2017_2018_results, euroleague_2018_2019_results,
     euroleague_2019_2020_results, euroleague_2020_2021_results, euroleague_2021_2022_results,
     euroleague_2022_2023_results, euroleague_2023_2024_results, euroleague_2024_2025_results])


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
    if ph == "RS":
        return 'Regular Season'
    elif ph == 'PI':
        return 'Play In'
    elif ph == 'PO':
        return 'Play offs'
    elif ph == 'FF':
        return 'Final Four'


def market_format(marker, info):
    if info == "Begin Period":
        return '10:00'
    elif info == "End Period" or info == "End Game":
        return '00:00'
    else:
        return marker


def time_format(timer):
    if timer.startswith("0"):
        return timer.replace("0", '')
    else:
        return timer


def attack_team(team1, team2, sit):
    if sit.filter(regex='JB|O|D|TOUT|'):
        return team1
    elif sit.filter(regex='2FGA|D|ST|3FGM|CM|TO|3FGA|RV|FTM|'):
        return team2


def points_scored(sit):
    if sit == '2FGM':
        return 2
    elif sit == '3FGM':
        return 3
    elif sit == 'FTM':
        return 1
    else:
        return 0


extra_details = euroleague_2024_2025_playerstats.groupby(['Fixture_Team_Season', 'Against'])[
    'Player'].count().reset_index()
extra_details = extra_details.drop('Player', axis=1)

pbp_data_df2425 = pd.read_csv(
    f"https://raw.githubusercontent.com/sotiristiga/ts.portofolio/refs/heads/main/pbp_data_df2425.csv")

pbp_data_df2425 = pbp_data_df2425.rename(columns={'Round': 'Fixture', 'CODETEAM': 'Team'})
pbp_data_df2425['Fixture'] = pd.to_numeric(pbp_data_df2425['Fixture'])
pbp_data_df2425['Season'] = pbp_data_df2425['Season'].astype(str) + "-" + (pbp_data_df2425['Season'] + 1).astype(str)
pbp_data_df2425['Phase'] = pbp_data_df2425['Phase'].apply(phase_format)
pbp_data_df2425['Team'] = pbp_data_df2425['Team'].str.replace('MCO', 'ASM')
pbp_data_df2425['Team'] = pbp_data_df2425['Team'].str.replace('ASV', 'VIL')
pbp_data_df2425['Team'] = pbp_data_df2425['Team'].str.replace('MAD', 'RMB')
pbp_data_df2425['Team'] = pbp_data_df2425['Team'].str.replace('MUN', 'BAY')
pbp_data_df2425['Team'] = pbp_data_df2425['Team'].str.replace('TEL', 'MAC')
pbp_data_df2425['Team'] = pbp_data_df2425['Team'].str.replace('ULK', 'FEN')
pbp_data_df2425['Team'] = pbp_data_df2425['Team'].str.replace('RED', 'CRV')
pbp_data_df2425['Team'] = pbp_data_df2425['Team'].str.replace('PRS', 'PRB')
pbp_data_df2425['Team'] = pbp_data_df2425['Team'].str.replace('VIR', 'BOL')
pbp_data_df2425['Team'] = pbp_data_df2425['Team'].str.replace('IST', 'EFE')
pbp_data_df2425['PLAYTYPE'] = pbp_data_df2425['PLAYTYPE'].str.replace(' ', '')
pbp_data_df2425['GAMECODE'] = pbp_data_df2425['Fixture'].astype(str) + "_" + pbp_data_df2425['Gamecode'].astype(str)
pbp_data_df2425[['Last Name', 'First Name']] = pbp_data_df2425['PLAYER'].str.split(', ', expand=True)

pbp_data_df2425['First Name'] = pbp_data_df2425['First Name'].str.upper().str.title()
pbp_data_df2425['Last Name'] = pbp_data_df2425['Last Name'].str.upper().str.title()
pbp_data_df2425['Player'] = pbp_data_df2425['First Name'] + " " + pbp_data_df2425['Last Name']
pbp_data_df2425['Fixture_Team_Season'] = pbp_data_df2425['Fixture'].astype(str) + "_" + pbp_data_df2425['Team'] + "_" + \
                                         pbp_data_df2425['Season']

pbp_data_df2425['MARKERTIME'] = pbp_data_df2425.apply(lambda x: market_format(x['MARKERTIME'], x['PLAYINFO']), axis=1)
pbp_data_df2425[['MINUTEN', 'SECONDS1']] = pbp_data_df2425['MARKERTIME'].str.split(':', expand=True)
pbp_data_df2425['SECONDS1'] = pbp_data_df2425['SECONDS1'].str.replace(' ', '')
pbp_data_df2425['MINUTEN'] = pd.to_numeric(pbp_data_df2425['MINUTEN'].apply(time_format))
pbp_data_df2425['SECONDS1'] = pd.to_numeric(pbp_data_df2425['SECONDS1'].apply(time_format))
pbp_data_df2425['SECONDS1'] = pbp_data_df2425['SECONDS1'].replace(np.nan, 0)
pbp_data_df2425['MINUTEN'] = pbp_data_df2425['MINUTEN'].replace(np.nan, 0)
pbp_data_df2425['PLAYTYPE'] = pbp_data_df2425['PLAYTYPE'].replace('CMTI', 'CM')
pbp_data_df2425['SECONDS'] = pbp_data_df2425['MINUTEN'] * 60 + pbp_data_df2425['SECONDS1']
pbp_data_df2425['SECONDS_diff'] = -pbp_data_df2425['SECONDS'].diff()

pbp_data_df2425 = pd.merge(pbp_data_df2425, extra_details).sort_values(['Fixture', 'GAMECODE', 'NUMBEROFPLAY'])

pbp_data_2425 = pbp_data_df2425[
    ['GAMECODE', 'Season', 'Phase', 'Fixture', 'PERIOD', 'MINUTE', 'MARKERTIME', 'Team', 'Player', 'PLAYTYPE',
     'Against']]
coachtimeout = pbp_data_2425.loc[(pbp_data_2425['PLAYTYPE'] == 'TOUT')]
coachtimeout['Coach'] = coachtimeout.apply(lambda x: team_coach(x['Team'], x['Fixture']), axis=1)
coachtimeout['Against Coach'] = coachtimeout.apply(lambda x: team_coach(x['Against'], x['Fixture']), axis=1)
tfouls = pbp_data_2425.loc[(pbp_data_2425['PLAYTYPE'].isin(['C', 'B', 'CMT']))]
tfouls['Coach'] = tfouls.apply(lambda x: team_coach(x['Team'], x['Fixture']), axis=1)
team_rebounds = pbp_data_2425.loc[(pbp_data_2425['PLAYTYPE'].isin(['O', 'D']))]
team_turnovers = pbp_data_2425.loc[(pbp_data_2425['PLAYTYPE'] == 'TO')]

against_coach_timeouts_pergame = \
coachtimeout[['Against Coach', 'Fixture']].value_counts().reset_index().groupby('Against Coach')[
    'count'].mean().reset_index().round(1)
timeouts_perperiod = \
coachtimeout[['Team', 'Fixture', 'PERIOD']].value_counts().reset_index().groupby(['Team', 'PERIOD'])[
    'count'].mean().reset_index()
unf = pbp_data_2425.loc[(pbp_data_2425['PLAYTYPE'].isin(['CMU', "CMD"]))]


st.sidebar.markdown('''
  * ## [By Team](#by-team)
  * ## [By Coach](#by-coach)
  * ## [By Player](#by-player)

''', unsafe_allow_html=True)
st.header('By Team')
tec1,tec2=st.columns(2)
with tec1:
    st.write("#### Against")
    team_technical_fouls = tfouls['Team'].value_counts().reset_index().reset_index()
    team_technical_fouls['Rank'] = team_technical_fouls['index'] + 1
    team_technical_fouls.drop('index', axis=1, inplace=True)
    interactive_table(
        team_technical_fouls.set_index('Rank').rename(columns={'count': 'Technical Fouls'}),
        paging=False, height=2000, width=2000, showIndex=True,
        classes="display order-column nowrap table_with_monospace_font", searching=True,
        fixedColumns=True, select=True, info=False, scrollCollapse=True,
        scrollX=True, scrollY=1000, fixedHeader=True, scroller=True, filter='bottom',
        columnDefs=[{"className": "dt-center", "targets": "_all"}])
with tec2:
    st.write("#### Favor")
    against_team_technical_fouls = tfouls['Against'].value_counts().reset_index().reset_index()

    against_team_technical_fouls['Rank'] = against_team_technical_fouls['index'] + 1
    against_team_technical_fouls.drop('index', axis=1, inplace=True)
    interactive_table(
        against_team_technical_fouls.set_index('Rank').rename(columns={'count': 'Technical Fouls'}),
        paging=False, height=2000, width=2000, showIndex=True,
        classes="display order-column nowrap table_with_monospace_font", searching=True,
        fixedColumns=True, select=True, info=False, scrollCollapse=True,
        scrollX=True, scrollY=1000, fixedHeader=True, scroller=True, filter='bottom',
        columnDefs=[{"className": "dt-center", "targets": "_all"}])



st.header("By Coach")
coach_technicals_fouls = tfouls['Coach'].loc[tfouls.PLAYTYPE == 'C'].value_counts().reset_index().reset_index()
coach_technicals_fouls['Rank'] = coach_technicals_fouls['index'] + 1
coach_technicals_fouls.drop('index', axis=1, inplace=True)
interactive_table(
    coach_technicals_fouls.set_index('Rank').rename(columns={'count': 'Technical Fouls'}),
    paging=False, height=2000, width=2000, showIndex=True,
    classes="display order-column nowrap table_with_monospace_font", searching=True,
    fixedColumns=True, select=True, info=False, scrollCollapse=True,
    scrollX=True, scrollY=1000, fixedHeader=True, scroller=True, filter='bottom',
    columnDefs=[{"className": "dt-center", "targets": "_all"}])


st.header("By Player")
player_technicals_fouls = tfouls['Player'].loc[
    tfouls.PLAYTYPE == 'CMT'].value_counts().reset_index().reset_index()
player_technicals_fouls['Rank'] = player_technicals_fouls['index'] + 1
player_technicals_fouls.drop('index', axis=1, inplace=True)
interactive_table(
    player_technicals_fouls.set_index('Rank').rename(columns={'count': 'Technical Fouls'}),
    paging=False, height=2000, width=2000, showIndex=True,
    classes="display order-column nowrap table_with_monospace_font", searching=True,
    fixedColumns=True, select=True, info=False, scrollCollapse=True,
    scrollX=True, scrollY=1000, fixedHeader=True, scroller=True, filter='bottom',
    columnDefs=[{"className": "dt-center", "targets": "_all"}])
