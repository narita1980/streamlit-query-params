import streamlit as st

st.title('Streamlitでクエリパラメータを取得するサンプル')

params = st.experimental_get_query_params()
st.write('experimental_get_query_params() の実行結果')
st.write(params)
