import streamlit as st
import pandas as pd
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.figure_factory as ff
import plotly.graph_objects as go
import preprocessor
import helper
import os,sys
def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)
df = pd.read_csv(resource_path('athlete_events.csv'))
region_df = pd.read_csv(resource_path('noc_regions.csv'))

df=preprocessor.preprocess(df,region_df)

st.sidebar.title("Olymics Analysis")
st.sidebar.image("olympic-logo.png", caption="Olympic Image", use_column_width=True)
user_menu=st.sidebar.radio(
    'Select an Option',('Medal Tally','Overall Analysis','Country_wise Performance','Athelete Wise Analysis')
)


#Module 1
if user_menu=='Medal Tally':
    
    st.sidebar.header("Medal Tally")
    years,country=helper.country_years_list(df)

    selected_year=st.sidebar.selectbox("Select Year",years)
    selected_conutry=st.sidebar.selectbox("Select Country",country)

    medal_tally=helper.fetch_medal_tally(df,selected_year,selected_conutry)
    if selected_year=='Overall' and selected_conutry=='Overall':
        st.title("Overall Tally")
    if selected_year!='Overall' and selected_conutry=='Overall':
        st.title("Medal Tally in "+ str(selected_year)+" Olympics")
    if selected_year=='Overall' and selected_conutry!='Overall':
        st.title("Overall Medal Tally of "+ selected_conutry)
    if selected_year!='Overall' and selected_conutry!='Overall':
        st.title("Medal Tally of "+ selected_conutry+" in "+ str(selected_year))
    st.table(medal_tally)

#Module 2
if user_menu=='Overall Analysis':
    editions =df['Year'].unique().shape[0]-1
    cities =df['City'].unique().shape[0]
    sports =df['Sport'].unique().shape[0]
    events =df['Event'].unique().shape[0]
    athletes =df['Name'].unique().shape[0]
    nations =df['region'].unique().shape[0]

    st.title("Top Statistics")

    col1,col2,col3=st.columns(3)
    with col1:
        st.header("Editions")
        st.title(editions)
    with col2:
        st.header("Hosts")
        st.title(cities)
    with col3:
        st.header("Sports")
        st.title(sports)

    col1,col2,col3=st.columns(3)
    with col1:
        st.header("Events")
        st.title(events)
    with col2:
        st.header("Regions")
        st.title(nations)
    with col3:
        st.header("Athlete")
        st.title(athletes)
    
    nations_over_time=helper.participating_nations_over_time(df)
    fig1 =px.line(nations_over_time,x="Edition",y="No Of Countries")
    st.title("Participating nation over Year")
    st.plotly_chart(fig1)

    games_over_time=helper.games_over_time(df)
    fig2 =px.line(games_over_time,x="Edition",y="No Of Games")
    st.title("No of Games over Years")
    st.plotly_chart(fig2)

    athelete_over_time=helper.athelete_over_time(df)
    fig2 =px.line(athelete_over_time,x="Edition",y="No Of Atheletes")
    st.title("No of Atheletes participated over Years")
    st.plotly_chart(fig2)

    st.title("No of Events Over time")
    fig,ax=plt.subplots(figsize=(20,20))
    x=df.drop_duplicates(['Year','Sport','Event'])
    ax=sns.heatmap(x.pivot_table(index='Sport',columns='Year',values='Event',aggfunc='count').fillna(0).astype('int'),annot=True)
    st.pyplot(fig)
#     plt.figure(figsize=(25,25))      //.
# sns.heatmap(x.pivot_table(index='Sport',columns='Year',values='Event',aggfunc='count').fillno(0).astype('int'),annot=True)
    
    #to add most sucessfull atheletes
    st.title("Most successful Athletes")

    sport_list = df['Sport'].dropna().unique().tolist()
    sport_list.sort()
    sport_list.insert(0, 'Overall')

    selected_sport = st.selectbox('Select a Sport', sport_list)

    x = helper.most_successful(df, selected_sport)

    st.table(x)


#Module 3
if user_menu=='Country_wise Performance':

    st.sidebar.title('Country-wise Analysis')

    country_list=df['region'].dropna().unique().tolist()
    country_list.sort()

    selected_conutry=st.sidebar.selectbox('Select a country',country_list)

    country_df=helper.yearwise_medal_tally(df,selected_conutry)
    fig =px.line(country_df,x="Year",y="Medal")
    st.title(selected_conutry+"'s medal tally over Years")
    st.plotly_chart(fig)

    st.title(selected_conutry+" excels in the following sports: ")
    pt=helper.country_event_heatmap(df,selected_conutry)
    fig,ax=plt.subplots(figsize=(20,20))
    ax=sns.heatmap(pt,annot=True)
    st.pyplot(fig)
    
    st.title("Top 10 Athletes of " + selected_conutry)
    top10_df = helper.most_successful_countrywise(df, selected_conutry)
    st.table(top10_df.set_index(pd.Index(range(1, len(top10_df)+1))))




#Module 4
if user_menu == 'Athelete Wise Analysis':
    st.title('Distribution of Age')

    athelete_df = df.copy()
    athelete_df = athelete_df.dropna(subset=['Age'])

    x1 = athelete_df['Age']
    x2 = athelete_df[athelete_df['Medal'] == 'Gold']['Age']
    x3 = athelete_df[athelete_df['Medal'] == 'Silver']['Age']
    x4 = athelete_df[athelete_df['Medal'] == 'Bronze']['Age']

    fig = ff.create_distplot([x1, x2, x3, x4],
                             ['Overall Age', 'Gold Medalist', 'Silver Medalist', 'Bronze Medalist'],
                             show_hist=False, show_rug=False)
    fig.update_layout(autosize=False, width=800, height=500)
    st.plotly_chart(fig)

    # -------------------- SPORT-WISE GOLD AGE DISTRIBUTION --------------------

    famous_sports = ['Basketball', 'Judo', 'Football', 'Tug-Of-War', 'Athletics',
                     'Swimming', 'Badminton', 'Sailing', 'Gymnastics',
                     'Art Competitions', 'Handball', 'Weightlifting', 'Wrestling',
                     'Water Polo', 'Hockey', 'Rowing', 'Fencing',
                     'Shooting', 'Boxing', 'Taekwondo', 'Cycling', 'Diving', 'Canoeing',
                     'Tennis', 'Golf', 'Softball', 'Archery',
                     'Volleyball', 'Synchronized Swimming', 'Table Tennis', 'Baseball',
                     'Rhythmic Gymnastics', 'Rugby Sevens',
                     'Beach Volleyball', 'Triathlon', 'Rugby', 'Polo', 'Ice Hockey']

    x = []
    name = []

    for sport in famous_sports:
        temp_df = athelete_df[athelete_df['Sport'] == sport]
        gold_ages = temp_df[temp_df['Medal'] == 'Gold']['Age'].dropna()
        if len(gold_ages) > 0:
            x.append(gold_ages)
            name.append(sport)

    fig2 = ff.create_distplot(x, name, show_hist=False, show_rug=False)
    fig2.update_layout(autosize=False, width=1000, height=600)
    st.title("Distribution of Age wrt Sports (Gold Medalists)")
    st.plotly_chart(fig2)

    sport_list = df['Sport'].unique().tolist()
    sport_list.sort()
    sport_list.insert(0, 'Overall')

    st.title('Height Vs Weight')
    selected_sport = st.selectbox('Select a Sport', sport_list)
    temp_df = helper.weight_v_height(df, selected_sport)

    fig, ax = plt.subplots()
    ax = sns.scatterplot(x=temp_df['Weight'], y=temp_df['Height'], hue=temp_df['Medal'], style=temp_df['Sex'], s=60)
    st.pyplot(fig)

    st.title("Men Vs Women Participation Over the Years")
    final = helper.men_vs_women(df)
    fig = px.line(final, x="Year", y=["Male", "Female"])
    fig.update_layout(autosize=False, width=1000, height=600)
    st.plotly_chart(fig)
    

