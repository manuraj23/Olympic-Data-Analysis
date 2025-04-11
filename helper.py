import numpy as np

def fetch_medal_tally(df, year, country):
    medal_df = df.drop_duplicates(subset=['Team','NOC','Games','Year','City','Sport','Event','Medal'])
    flag = 0
    if year == 'Overall' and country == 'Overall':
        temp_df = medal_df
    if year == 'Overall' and country != 'Overall':
        flag = 1
        temp_df = medal_df[medal_df['region'] == country]
    if year != 'Overall' and country == 'Overall':
        temp_df = medal_df[medal_df['Year'] == int(year)]
    if year != 'Overall' and country != 'Overall':
        temp_df = medal_df[(medal_df['region'] == country) & (medal_df['Year'] == int(year))]
    
    if flag == 1:
        x = temp_df.groupby('Year').sum()[['Gold','Silver','Bronze']].sort_values('Year').reset_index()
    else:
        x = temp_df.groupby('region').sum()[['Gold','Silver','Bronze']].sort_values('Gold', ascending=False).reset_index()
    x['total'] = x['Gold'] + x['Silver'] + x['Bronze']
    x.index = np.arange(1, len(x)+1)
    return x

def medal_tally(df):

    medal_tally=df.drop_duplicates(subset=['Team','NOC','Games','Year','City','Sport','Event','Medal'])

    medal_tally=medal_tally.groupby('region').sum()[['Gold','Silver','Bronze']].sort_values('Gold',ascending=False).reset_index()

    medal_tally['total']=medal_tally['Gold']+medal_tally['Silver']+medal_tally['Bronze']

    return medal_tally

def country_years_list(df):
    years=df['Year'].unique().tolist()
    years.sort()
    years.insert(0,'Overall')
    country=np.unique(df['region'].dropna().values).tolist()
    country.sort()
    country.insert(0,'Overall')
    return years,country

def participating_nations_over_time(df):
    nation_over_time=df.drop_duplicates(['Year', 'region'])['Year'].value_counts().reset_index().sort_values('Year')
    nation_over_time.rename(columns={'Year':'Edition', 'count':'No Of Countries'}, inplace=True)
    return nation_over_time

def games_over_time(df):
    games_over_time=df.drop_duplicates(['Year', 'Event'])['Year'].value_counts().reset_index().sort_values('Year')
    games_over_time.rename(columns={'Year':'Edition', 'count':'No Of Games'}, inplace=True)
    return games_over_time

def athelete_over_time(df):
    athelete_over_time=df.drop_duplicates(['Year', 'Name'])['Year'].value_counts().reset_index().sort_values('Year')
    athelete_over_time.rename(columns={'Year':'Edition', 'count':'No Of Atheletes'}, inplace=True)
    return athelete_over_time

def yearwise_medal_tally(df,country):
    temp_df=df.dropna(subset=['Medal'])
    temp_df.drop_duplicates(subset=['Team','NOC','Games','Year','City','Sport','Event','Medal'],inplace=True)
    new_df=temp_df[temp_df['region']==country]
    final_df=new_df.groupby('Year').count()['Medal'].reset_index()
    return final_df

def country_event_heatmap(df,country):
    temp_df=df.dropna(subset=['Medal'])
    temp_df.drop_duplicates(subset=['Team','NOC','Games','Year','City','Sport','Event','Medal'],inplace=True)
    new_df=temp_df[temp_df['region']==country]
    pt=new_df.pivot_table(index='Sport',columns='Year',values='Event',aggfunc='count').fillna(0)
    return pt

def most_successful(df, sport):
    df.drop_duplicates(inplace=True)
    table_preview = df.dropna(subset=['Medal'])['Name'].value_counts().reset_index()
    table_preview.columns = ['Name', 'Count']
    table_preview = table_preview.merge(df, on='Name', how='left')[['Name', 'Count', 'region', 'Sport']].drop_duplicates('Name')
    
    if sport != 'Overall':
        table_preview = table_preview[table_preview['Sport'] == sport]
    return table_preview.head(10)

def most_successful_countrywise(df, country):
    temp_df = df.dropna(subset=['Medal'])
    temp_df = temp_df[temp_df['region'] == country]
    medal_count = temp_df.pivot_table(index='Name', columns='Medal', values='Event', aggfunc='count', fill_value=0)
    medal_count['Total'] = medal_count.sum(axis=1)
    sport_info = temp_df[['Name', 'Sport']].drop_duplicates(subset=['Name'])
    medal_count = medal_count.merge(sport_info, on='Name', how='left')
    medal_count = medal_count.rename(columns={
        'Gold': 'Gold',
        'Silver': 'Silver',
        'Bronze': 'Bronze'
    })
    for medal in ['Gold', 'Silver', 'Bronze']:
        if medal not in medal_count.columns:
            medal_count[medal] = 0
    medal_count = medal_count.sort_values(by=['Gold', 'Silver', 'Bronze'], ascending=False).reset_index()
    return medal_count[['Name', 'Gold', 'Silver', 'Bronze', 'Total', 'Sport']].head(10)

def weight_v_height(df,sport):
    athlete_df = df.drop_duplicates(subset=['Name', 'region'])
    athlete_df['Medal'].fillna('No Medal', inplace=True)
    if sport != 'Overall':
        temp_df = athlete_df[athlete_df['Sport'] == sport]
        return temp_df
    else:
        return athlete_df
# future scope Pandas version 3.0
# def weight_v_height(df, sport):
#     athlete_df = df.drop_duplicates(subset=['Name', 'region'])
#     athlete_df['Medal'] = athlete_df['Medal'].fillna('No Medal')
    
#     if sport != 'Overall':
#         temp_df = athlete_df[athlete_df['Sport'] == sport]
#         return temp_df
#     else:
#         return athlete_df

def men_vs_women(df):
    athlete_df = df.drop_duplicates(subset=['Name', 'region'])
    men = athlete_df[athlete_df['Sex'] == 'M'].groupby('Year').count()['Name'].reset_index()
    women = athlete_df[athlete_df['Sex'] == 'F'].groupby('Year').count()['Name'].reset_index()
    final = men.merge(women, on='Year', how='left')
    final.rename(columns={'Name_x': 'Male', 'Name_y': 'Female'}, inplace=True)
    final.fillna(0, inplace=True)
    return final
