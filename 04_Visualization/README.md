## Streamlit 사용법

(로컬 버전)
* Streamlit을 수행하는 경로에 특수 문자를 포함되지 않도록 하세요.
1. Streamlit을 설치하세요.
'''pip install streamlit'''

2. 파이썬 스크립트 파일을 실행하세요. 
'''streamlit run app.py'''

(구글 코랩 버전)
1. 패키지를 설치하세요.
'''!npm install -g localtunnel'''
'''!pip install -q streamlit'''

3. 내 IP를 확인하세요. 
'''!wget -q -O - ipv4.icanhazip.com'''

4. streamlit을 실행하세요.
'''!streamlit run app.py &> logs.txt & npx localtunnel --port 8501'''

5. 결과창에 나와있는 link를 클릭하세요.
![image](https://github.com/awekim/LEC_PythonFootball/assets/56111110/d66acb5b-402c-4c39-8b38-4f4a03e5eac1)

6. Tunnel Password에 IP를 입력하고 "Click to Submit"을 클릭하세요.
![image](https://github.com/awekim/LEC_PythonFootball/assets/56111110/766d80b2-6f30-41a5-9933-c3ea443e66c6)
