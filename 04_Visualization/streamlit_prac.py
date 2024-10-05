import streamlit as st
from PIL import Image
import pandas as pd


st.set_page_config(layout="wide")

#영역 나누기
empty1,con1,empty2 = st.columns([0.3,0.5,0.3])
empyt1,con2,con3,empty2 = 
empyt1,con4,empty2 = 
empyt1,con5,empty2 = st.columns([0.3,0.5,0.3])

def main():
    with empty1 :
        # 여백부분1
        st.empty()
        
    with con1 :
        #이미지
        st.empty()
        
    with con2 :
        # 셀렉트박스
        # 체크박스
        # markdown
        data = ['appearances','club_games','clubs','competitions',
                'game_events','games','players','player_valuations']
        # game_lineups file 제외
        csv_files = {
            'appearances': 'your_file_path.csv',
            'club_games': 'your_file_path.csv',
            'clubs': 'your_file_path.csv',
            'competitions': 'your_file_path.csv',
            'game_events': 'your_file_path.csv',
            'games': 'your_file_path.csv',
            'players': 'your_file_path.csv',
            'player_valuations': 'your_file_path.csv'
        }
        
        
    with con3 :
        # 데이터프레임
        # 멀티셀렉트박스
        st.empty()

    with con4 :
        # dataframe graph
        st.empty()
        
    with con5 :
        # 동영상
        st.empty()
        
    with empty2 :
        # 여백부분2
        st.empty() 

if __name__ == "__main__":
    main()
