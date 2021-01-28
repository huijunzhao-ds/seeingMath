mkdir -p ~/.streamlit/
echo "[general]
email = \"huijunzhao.ds@gmail.com\"\
“ > ~/.streamlit/credentials.toml
echo “[server]\
headless = true\
enableCORS=false\
port = $PORT\
“ > ~/.streamlit/config.toml