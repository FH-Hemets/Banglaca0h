import streamlit as st
import pandas as pd


def init_game(players_in_game):
    st.session_state['players_in_game'] = players_in_game
    st.session_state['df'] = pd.DataFrame(columns=players_in_game)


st.header("Emma Treibn")

players_available = [
    'Mario',
    'Richi',
    'Joe',
    'Chris',
    'Stefan E.',
    'Geri',
    'Hias',
    'Maxi',
    'Phil',
    'Stefan H.'
]
btn_new_game = st.button("Neues Spiel starten")

if btn_new_game:
    with st.form('start_game_form'):
        players = st.multiselect("Mitspieler", options=players_available, default=players_available, disabled=not btn_new_game)
        
        submitted = st.form_submit_button("Start 💣")
        if submitted:
            btn_new_game=False

# Initialization
if 'df' not in st.session_state:
    init_game(players_available)

if st.session_state.players_in_game != players_available:
    st.warning('Neues Spiel muss gestartet werden um Spieler zu ändern!')


st.subheader('Spielstatus')
st.dataframe(st.session_state.df)




with st.form("one_round_form"):
   st.write("Neue Runde:")

   # Every form must have a submit button.
   submitted = st.form_submit_button("Punkte aktualisieren")
   if submitted:
        st.session_state.df = st.session_state.df.append(st.session_state['players_in_game'])





