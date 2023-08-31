import streamlit as st
import pandas as pd
import altair as alt

st.header("Das Umweltbewusstsein junger Menschen 2021")
st.subheader("")

source = pd.DataFrame({
        'Anteil(%)': [85, 88, 73, 50, 81],
        'Meinung': ['finden Umwelt- und Klimaschutz sehr oder eher wichtig', 'berichten von Trauer über Umweltzerstörung', 'haben Angst vor den Folgen des Klimawandels', 'berichten, dass die Jugendbewegung für den Klimaschutz ihr eigenes Leben und Verhalten verändert', 'finden, dass die Politik in Klimafragen mehr auf sie hören sollte.']
     })
 
bar_chart = alt.Chart(source).mark_bar().encode(
        y='Anteil(%):Q',
        x='Meinung:O',
    )
st.altair_chart(bar_chart, use_container_width=True)


txt = st.text_area('', '''
    Basis: 1010 Befragte; (14 bis 22 Jahre) in Deutschland; 2021
    ''')
st.text("Klicke an die Balken um die Daten genauer anzuschauen. Du kannst auch die Diagramm vergrößern und ein Bild davon machen")
st.text("Quelle: Umweltbundesamt")