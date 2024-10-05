import streamlit as st
from PIL import Image
import pandas as pd

st.set_page_config(layout="wide")

#영역 나누기
empty1,con1,empty2 = st.columns([0.3,0.5,0.3])
empyt1,con2,con3,empty2 = st.columns([0.3,0.5,0.5,0.3])
empyt1,con4,empty2 = st.columns([0.3,1.0,0.3])
empyt1,con5,empty2 = st.columns([0.3,0.5,0.3])

def main():
    with empty1 :
        # 여백부분1
        st.empty()
        
    with con1 :
        #이미지
        st.title("Soccer Player Data Analysis")
        img = Image.open('player.png')
        st.image(img, caption='Robert Lewandowski No.9')
        
    with con2 :
        # 셀렉트박스
        # 체크박스
        # markdown
        data = ['appearances','club_games','clubs','competitions',
                'game_events','games','players','player_valuations']
        # game_lineups file 제외
        csv_files = {
            'appearances': 'appearances.csv',
            'club_games': 'club_games.csv',
            'clubs': 'clubs.csv',
            'competitions': 'competitions.csv',
            'game_events': 'game_events.csv',
            'games': 'games.csv',
            'players': 'players.csv',
            'player_valuations': 'player_valuations.csv'
        }
        
        choice_data = st.selectbox('Soccer data selection', data)

        show_head = st.checkbox('첫 data를 표시하기')
        show_tail = st.checkbox('마지막 data를 표시하기')
        st.markdown("""
                    - **선택한 data를 보여줍니다!** 
                    - *Check Box를 선택하면 data head 혹은 tail을 보여줍니다!*
                    """)
        
    with con3 :
        # 데이터프레임
        # 멀티셀렉트박스
        df =  pd.read_csv(csv_files[choice_data])
        columns = st.multiselect('필터링할 열 선택', df.columns)
        filtered_df = df[columns]                
        if columns:
            if show_head:
                st.dataframe(filtered_df.head())
            elif show_tail:
                st.dataframe(filtered_df.tail())
            else:
                st.dataframe(filtered_df)
        else:
            if show_head:
                st.dataframe(df.head())
            elif show_tail:
                st.dataframe(df.tail())
            else:
                st.dataframe(df)


    with con4 :
        # dataframe graph
        # button
        st.empty()
        if filtered_df is not None and not filtered_df.empty:
            chart_type = st.selectbox('Select chart type',
                        ['Line', 'Area', 'Bar', 'Scatter'])
            max_rows = len(filtered_df)
            start_row, end_row = st.slider('Select the range of rows',
                    0, max_rows-1, (0, min(1000, max_rows-1)))
            filtered_df = filtered_df.iloc[start_row:end_row,]
            
            if st.button("Draw chart"):
                if chart_type == 'Line':
                    st.line_chart(filtered_df)
                elif chart_type == 'Area':
                    st.area_chart(filtered_df)
                elif chart_type == 'Bar':
                    st.bar_chart(filtered_df)
                elif chart_type == 'Scatter':
                    st.scatter_chart(filtered_df)
          
    with con5 :
        # 동영상
        # st.video('https://www.youtube.com/watch?v=PPMjSS6dEYs')
        from sklearn.datasets import load_iris
        from sklearn.preprocessing import LabelEncoder
        from sklearn.model_selection import train_test_split
        from sklearn.linear_model import LogisticRegression
        import numpy as np
        

        iris_dataset = load_iris()
        df = pd.DataFrame(data=iris_dataset.data,columns= iris_dataset.feature_names)
        # class 0 : setosa / class 1 : versicolor / class 2 : virginica
        df['species']= iris_dataset.target 


        X = df.drop(columns = ['species'])
        y = df['species']
        X_train, X_test, y_train, y_test = train_test_split(X,y,test_size = 0.3)

        model = LogisticRegression()
        model.fit(X_train,y_train)

        col1,col2 = st.columns(2)
        with col1:
            st.subheader("수치를 입력하세요")

            sepal_length = st.select_slider("Sepal Length", options=np.arange(1,11))
            sepal_width = st.select_slider("Sepal Width", options=np.arange(1,11))
            petal_length = st.select_slider("Petal Length", options=np.arange(1,11))
            petal_width = st.select_slider("Petal Width", options=np.arange(1,11))

            sample = [sepal_length,sepal_width,petal_length,petal_width]
            st.write(sample)
            
        with col2:
            st.subheader("모델 결과를 확인해주세요")
            new_df = np.array(sample).reshape(1,-1)
            # st.write(new_df.shape, new_df.ndim)

            prediction = model.predict(new_df)
            pred_prob = model.predict_proba(new_df)
            st.write(prediction)
            st.write(pred_prob)

            if prediction == 0:
                st.success("Setosa 종입니다. ")
                pred_proba_scores = {"Setasa 확률" : pred_prob[0][0] * 100,
                                     "Versicolor 확률": pred_prob[0][1] * 100,
                                     "Virginica 확률":pred_prob[0][2] * 100}
                # 사진첨삭 가능(video 처럼 url로도 가능)
                st.write(pred_proba_scores)
            elif prediction == 1:
                st.success("Versicolor 종입니다. ")
                pred_proba_scores = {"Setasa 확률" : pred_prob[0][0] * 100,
                                     "Versicolor 확률": pred_prob[0][1] * 100,
                                     "Virginica 확률":pred_prob[0][2] * 100}
                # 사진첨삭 가능(video 처럼 url로도 가능)
                st.write(pred_proba_scores)
            elif prediction == 2:
                st.success("Virginica 종입니다. ")
                pred_proba_scores = {"Setasa 확률" : pred_prob[0][0] * 100,
                                     "Versicolor 확률": pred_prob[0][1] * 100,
                                     "Virginica 확률":pred_prob[0][2] * 100}
                # 사진첨삭 가능(video 처럼 url로도 가능)
                st.write(pred_proba_scores)
            else:
                st.warning("판별 불가")
        
    with empty2 :
        # 여백부분2
        st.empty() 

if __name__ == "__main__":
    main()
