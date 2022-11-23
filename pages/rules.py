import streamlit as st

st.header("Spielregeln:")
st.markdown("- Alle Karten werden ausgeteilt. Können Karten nicht aufgeteilt werden werden sie aus dem Spiel entfernt.")
st.markdown("- Ziel ist es keine Punkte zu schreiben")
st.markdown("- Wer zuerst 200 Punkte erreicht zahlt 5€ in die Stammtischkasse und das Spiel endet")
st.markdown("- Wer in den letzen 5 Runden keine 30 Punkte erreicht, zahlt 5€ in die Stammtischkasse und die 30 Punkte Rechnung wird zurückgesetzt")
st.markdown("- **[Full House]** Einer hat alle Punkte (90) in den Karten =  er wird verschont und alle anderen schreiben 30 Punkte")
st.markdown("- **[Jackpot]** Einer sticht alles = alle anderen zahlen 5€ in die Stammtischkassa und der Spielstand beginnt von 0")

st.subheader("Punkte:")
st.markdown("30 Punkte Grün Ober (Emma)")
st.markdown("20 Punkte Herz Sau")
st.markdown("5 Punkte alle restlichen Herz")