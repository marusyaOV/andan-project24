import pandas as pd

df_spotify = pd.read_excel('Spotify.xlsx')

df_HCI = pd.read_excel('HCI.xlsx')

df_weather = pd.read_html('https://listfist.com/list-of-countries-by-average-temperature', header=None)[0]
df_weather.drop(['Rank', 'Coldest Month (1991-2020) (°C) [source]', 'Flag', 'Hottest Month (1991-2020) (°C) [source]',
         'Variation (1991-2020) (°C)' ], axis=1, inplace=True)

df_osadki = pd.read_html('https://www.indexmundi.com/facts/indicators/AG.LND.PRCP.MM/rankings', header=None)[0]
df_osadki.drop(['Rank', 'Year'], axis=1, inplace=True)

df_density = pd.read_html('https://worldpopulationreview.com/country-rankings/countries-by-density', header=None)[2]
df_density.drop(['Density (/km²)', 'Density (/mi²)'], axis=1, inplace=True)
df_density = pd.DataFrame(df_density)


for i in df_density.index:
    a = str(df_density.loc[i, 'Area (km²)'])
    if '<' in a:
        df_density.loc[i, 'Area (km²)'] = float(a.replace('<', ''))
    elif 'K' in a:
        df_density.loc[i, 'Area (km²)'] = float(a.replace('K', '')) * 1000
    elif 'M' in a:
        df_density.loc[i, 'Area (km²)'] = float(a.replace('M', '')) * 1000000
    else:
        df_density.loc[i, 'Area (km²)'] = float(a)

df_density['Density (км кв.)'] = df_density['Population'] / df_density['Area (km²)']

df_density.drop(['Population', 'Area (km²)'], axis=1, inplace=True)




df_spotify[['Температура', 'Плотность населения', 'Осадки', 'Индекс чел. капитала']] = None

for i in df_spotify.index:
    country = df_spotify.at[i, 'Страны']

    weather_stroka = df_weather[df_weather['Country or Area [source]'] == country]
    if not weather_stroka.empty:
        weather_value = weather_stroka.iloc[0, 1]
        df_spotify.at[i, 'Температура'] = weather_value

    density_stroka = df_density[df_density['Country'] == country]
    if not density_stroka.empty:
        density_value = density_stroka.iloc[0, 1]
        df_spotify.at[i, 'Плотность населения'] = density_value

    osadki_stroka = df_osadki[df_osadki['Country'] == country]
    if not osadki_stroka.empty:
        osadki_value = osadki_stroka.iloc[0, 1]
        df_spotify.at[i, 'Осадки'] = osadki_value

    HCI_stroka = df_HCI[df_HCI['Country Name'] == country]
    if not HCI_stroka.empty:
        HCI_value = HCI_stroka.iloc[0, 2]
        df_spotify.at[i, 'Индекс чел. капитала'] = HCI_value


new_poryadok = ['Страны', 'Температура', 'Плотность населения', 'Осадки', 'Индекс чел. капитала',
                'Трек', 'ID трека', 'Длительность', 'Громкость', 'Энергичность', 'Танцевальность',
                'Акустичность', 'Инструментальность', 'Живость', 'Валентность', 'Речевой контент',
                'Мажорность/минорность', 'Темп']

df_spotify = df_spotify[new_poryadok]

df_spotify.to_excel('DataFrame_Spotify.xlsx', index=False)

