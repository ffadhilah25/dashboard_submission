import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
sns.set(style='dark')

yr_season_df = pd.read_csv("yr_season_data.csv")
yr1_weather_df = pd.read_csv("2012_weather_data.csv")

st.title("BIKE SHARING DATASET")

st.header("Data Analysis Project")

tab1, tab2 = st.tabs(["Question 1", "Question 2"])
with tab1:
    st.header("""
    Question 1
    The highest bike sharing occurs during which season?
    """)

    st.subheader("Total Bike Sharing on Each Season (2011 - 2012)")
    fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(24, 6))

    colors1 = ["#D3D3D3", "#D3D3D3", "#72BCD4", "#D3D3D3"]
    sns.barplot(x="season", y="cnt", data=yr_season_df.head(4), palette=colors1, ax=ax[0])
    ax[0].set_ylabel("Total Bike Sharing")
    ax[0].set_xlabel("Season")
    ax[0].set_title("Years 2011", loc="center", fontsize=15)
    ax[0].tick_params(axis = 'y', labelsize=12)
    ax[0].legend([
        "1 = Spring",
        "2 = Summer",
        "3 = Fall",
        "4 = Winter" 
    ])

    colors2 = ["#D3D3D3", "#D3D3D3", "#72BCD4", "#D3D3D3"]
    sns.barplot(x="season", y="cnt", data=yr_season_df.sort_values(by="yr", ascending=False).head(4), palette=colors2, ax=ax[1])
    ax[1].set_ylabel("Total Bike Sharing")
    ax[1].set_xlabel("Season")
    ax[1].set_title("Years 2012", loc="center", fontsize=15)
    ax[1].tick_params(axis = 'y', labelsize=12)
    ax[1].legend([
        "1 = Spring",
        "2 = Summer",
        "3 = Fall",
        "4 = Winter" 
    ])

    st.pyplot(fig)

    st.text("""
        Conclusion:
        In both 2011 and 2012, the highest number of bike sharing occurred during the Fall
        season.
        """)
 
with tab2:
    st.header("""
    Question 2
    What kind of weather conditions lead to a drastic decrease in bike sharing?
    """)

    st.subheader("Casual vs Registered Users by Weather (2012)")
    fig2 = plt.figure(figsize=(8, 6))
    plt.plot(yr1_weather_df['weather'], yr1_weather_df['casual'], marker='o', label='Casual')
    plt.plot(yr1_weather_df['weather'], yr1_weather_df['registered'], marker='o', label='Registered')

    plt.xlabel('Weather')
    plt.ylabel('Total Bike Sharing')
    plt.xticks(yr1_weather_df['weather'])
    plt.legend()

    st.pyplot(fig2)

    st.text("""
        Conclusion:
        Based on the data in 2012, there was a drastic decrease in bike sharing during
        weather condition 3, which includes:
            - 'Light Snow', 'Light Rain + Thunderstorm + Scattered clouds', and
            - 'Light Rain + Scattered clouds',
        for both casual and registered users.
        """)    


st.caption("Made by itspadpar || Farah Fadhilah Widiaputri (2023)")