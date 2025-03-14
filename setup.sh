mkdir -p ~/.streamlit/

echo "\
[server]\n\
headless = true\n\
enableCORS=false\n\
port = $PORT\n\
[theme]\n\
primaryColor = \"#0066cc\"\n\
backgroundColor = \"#f0f2f6\"\n\
secondaryBackgroundColor = \"#ffffff\"\n\
textColor = \"#262730\"\n\
font = \"sans serif\"\n\
" > ~/.streamlit/config.toml
