import streamlit as st
from PIL import Image
import pandas as pd

# 화면을 넓게!!!
st.set_page_config(layout="wide")

# 화면 UI 구역 정의
empty1,con1,empty2 = st.columns([0.3,0.5,0.3])
empyt1,con2,con3,empty2 = st.columns([0.3,0.5,0.5,0.3])
empyt1,con4,empty2 = st.columns([0.3,1.0,0.3])
empyt1,con5,empty2 = st.columns([0.3,0.5,0.3])

def main():
    
    with empty1:
        st.empty()

    with con1: ## section 1
        # simple streamlit Example
        img = Image.open('Player.png')
        st.image(img)

        st.title('Hello Steramlit Project!!!')

        name = 'Hong Gil Dong'
        st.text('안녕하세요 저는 {}입니다.'.format(name))
        st.header('안녕하세요')
        st.subheader('Handong Global University')
        st.info('예시 프로그램입니다')
        st.success('성공했다면 success')
        st.error('실패했다면 error')
        st.warning('경고한다면 warning')

    with con2: ## section 2

        #Define the selectbox
        st.selectbox(
            'Select Options', #설명 Label
            ['Option1', 'Option2', 'Option3'], #선택 옵션
            index = 1, #기본 선택값 (ex : 1은 두번째 항목)
            #format_func=lambda x :f"formatted {x}", #항목을 문자열로 변환
            help='Choose Option!'#도움말 옵션
        )

        #define the checkbox
        agree = st.checkbox('동의합니다', value=True, help='해당 항목을 동의하십니까?')

        # When click the check box, write the comment
        if agree:
            st.write('Great!')

        # Example markdown
        st.markdown("""
            # This is a title
            ## This is a header
            **Bold text**
            _Italic text_
            - List item 1
            - List item 2
            > Blockquotes
            [Link to Streamlit](https://streamlit.io/components)
            """, unsafe_allow_html=True)

    with con3: ## section 3
        # Example Dataframe
        df = pd.DataFrame({
            'Column1' : [1.5, 2.5, 3.5, 4.5],
            'Column2' : [10, 20, 30, 40]
        })

        # write Dataframe
        st.dataframe(df, width = 700, height = 500, use_container_width=True)

        options = ['Option 1', 'Option 2', 'Option 3', 'Option 4']
        
        # define the multiselect box
        selected_options = st.multiselect(
            'Select multiple options',
            options,
            default=['Option 2', 'Option 3'],
            help='You can select multiple options here'
        )
        # write the selected options
        st.write('You selected:', selected_options)


    with con4: ## section 4
        # Example DataFrame
        # X : 1~100 / Y : 1^2 ~ 100^2(제곱)
        df = pd.DataFrame({
            'x': range(1, 101),
            'y': [i**2 for i in range(1, 101)]
        })

        # Slider to select range of rows
        max_rows = len(df)
        row_range = st.slider('Select the range of rows', 0, max_rows-1, (0, min(1000, max_rows-1)))
        # select the drawing data range
        filtered_df = df.iloc[row_range[0]:row_range[1]+1]

        # Multiselect to filter DataFrame columns
        selected_columns = st.multiselect('Select columns to display', df.columns, default=df.columns.tolist())

        # Display DataFrame with selected columns and range
        st.dataframe(filtered_df[selected_columns])

        # Select chart type
        chart_type = st.selectbox('Select chart type', ['line', 'area', 'bar'])

        # Draw chart button
        if st.button('Draw chart'):
            if chart_type == 'line':
                st.line_chart(filtered_df[selected_columns])
            elif chart_type == 'area':
                st.area_chart(filtered_df[selected_columns])
            elif chart_type == 'bar':
                st.bar_chart(filtered_df[selected_columns])

    with con5 : ## section 5
        # define the streamlit video
        # st.video('your video link')
        # st.audio('your audio link')
        st.empty()

    with empty2:
        st.empty()

if __name__ == "__main__":
    main()