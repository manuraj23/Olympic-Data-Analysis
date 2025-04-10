import numpy as np

def fetch_medal_tally(df,year,country):
    medal_df=df.drop_duplicates(subset=['Team','NOC','Games','Year','City','Sport','Event','Medal'])
    flag=0
    if year=='Overall' and country=='Overall':
        temp_df=medal_df
    if year=='Overall' and country!='Overall':
        flag=1
        temp_df=medal_df[medal_df['region']==country]
    if year!='Overall' and country=='Overall':
        temp_df=medal_df[medal_df['Year']==int(year)]
    if year!='Overall' and country!='Overall':
        temp_df=medal_df[(medal_df['region']==country) & (medal_df['Year']==int(year))]
    if flag==1:
        x=temp_df.groupby('Year').sum()[['Gold','Silver','Bronze']].sort_values('Year').reset_index()
    else:
        x=temp_df.groupby('region').sum()[['Gold','Silver','Bronze']].sort_values('Gold',ascending=False).reset_index()
    
    x['total']=x['Gold']+x['Silver']+x['Bronze']
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

# Some error in code
def most_sucessful_athelete(df,country):
    df.drop_duplicates(inplace=True)
    table_preview=df.dropna(subset=['Medal'])['Name'].value_counts().reset_index()
    table_preview.columns = ['Name', 'Count']
    table_preview.merge(df, left_on='Name', right_on='Name', how='left')[['Name', 'Count', 'region', 'Sport']].drop_duplicates('Name').head(10)
    # return table_preview


    # table_preview.dropna(subset=['Medal'])['Name'].value_counts().reset_index().merge(df,left_on='index',right_on='Name',how='left')[['index','name_x','region']].drop_duplicates('index').head(10)
    temp_df=table_preview.dropna(subset=['Count'])

    temp_df=temp_df[temp_df['region']==country]

    x=temp_df['Name'].value_counts().reset_index().head(15).merge(df,left_on='Name',right_on='count',how='left')[['Name', 'Count',  'Sport']].drop_duplicates('count')

    # x.rename(columns={'Name':'Name','count':'Medals'},inplace=True)
    return x