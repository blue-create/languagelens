import streamlit as st
from pathlib import Path
import sys


sys.path.append(str(Path(__file__).resolve().parent.parent))
from modules import __page_setup__

# PAGE SETUP
__page_setup__.page_setup()

# PAGE CONTENT
@st.cache_resource
def findings():
    st.title("🔎 Findings")
    st.write("Die folgende Analyse bespricht die Resultate der trainierten Text-Modelle, wie im Bereich 'Kontext & Guidelines' beschrieben. Artikel wurden zuerst nach Inhalt klassifiziert um die Artikel herauszufiltern, bei denen es um Partnerschaftsgewalt geht. Wenn mindestens 10% der Paragraphen eines Artikels von Partnerschaftgewalt handeln, wird der Text auf schädliche Inhalte überprüft. ")
    st.subheader("Wann und wie häufig wird zu Partnerschaftsgewalt veröffentlicht?")
    st.image("media/elinor.png")
    st.write("Die deutsche Presse berichtet täglich über Partnerschaftsgewalt. Laut unseren Recherchen wurden zwischen 2018 und 2022 insgesamt um die 31.800 Artikel veröffentlicht, in denen mindestens 10% der Absätze explizit von Partnerschaftsgewalt handeln. Das entspricht einem Durchschnitt von **etwas mehr als 17 Artikeln pro Tag.**")
    st.write("Das Volumen der Artikel steigt tendenziell zu zwei Zeitpunkten im Jahr: rund um den Internationalen Frauentag am 8. März und den Internationalen Tag zur Beseitigung von Gewalt gegen Frauen am 25. November. ")

    st.subheader("Welche Zeitungen publizieren zu Partnerschaftsgewalt?")
    st.write("**Der Großteil der Artikel - 70,5 % - wird in regionalen Publikationen veröffentlicht**, die restlichen 29,5 % in überregionalen Zeitungen.")
    st.image("media/elinor.png")
    st.write("Obwohl regionale Zeitungen weitaus häufiger über Partnerschaftsgewalt berichten als überregionale Zeitungen, ist die Häufigkeit, mit der sie potenziell schädliche Formulierungen verwenden oder in ihre Artikel einbauen, etwas geringer.")
    st.image("media/elinor.png")

    st.subheader("Wie groß ist der Anteil an schädlicher Sprache?")
    st.write("Auch wenn das Gesamtvolumen der Artikel über Partnerschaftsgewalt zunimmt, ist der Anteil problematischer Sprache unserer Analyse zufolge von 2018 bis 2020 zurückgegangen.  \n  Die Daten zeigen jedoch, dass sie wieder in Besorgnis erregendem Maße zunimmt. Der prozentuale Anteil der Artikel mit schädlichen Äußerungen ging gegen Ende 2019 deutlich zurück und erreichte Anfang 2020 seinen Tiefststand, was möglicherweise mit einem Anstieg der Meldungen zu Beginn der Coronavirus-Pandemie über ein höheres Vorkommen von Gewalt aufgrund von Lockdowns zusammenhängt. ")
    st.image("media/elinor.png")
    st.write("**Die Daten ab 2020 zeigen jedoch einen Anstieg des Anteils schädlicher Inhalte**, wodurch der Jahresdurchschnitt von 20,6 % im Jahr 2020 auf 26,4 % im Jahr 2022 steigt.")

    st.subheader("Wie häufig kommt schädliche Sprache vor?")
    st.write("In **einem von zehn Artikeln über Partnerschaftsgewalt wird eine sensationsheischende Sprache verwendet.** Dies birgt das Risiko, Gewalttaten als Liebestragödie oder als eifersüchtige Leidenschaftsakt zu verharmlosen oder zu romantisieren.")
    st.write("In **einem von zwölf Berichten wird grafische Sprache verwendet**, die manchmal notwendig ist, um die Schwere der Gewalt zu vermitteln, aber bei übermäßiger Nutzung die Lesenden retraumatisieren und die Würde des Opfers beeinträchtigen kann und **immer von einer Triggergefahr-Warnung begleitet sein sollte.**")
    st.image("media/elinor.png")

    st.subheader("Wie häufig sind nützliche Inhalte in Artikeln zu Partnerschaftsgewalt?")
    st.write("**73,4 % der Artikel enthalten keine Hotline**, die die Opfer anrufen können, wenn sie durch den Inhalt des Artikels betroffen sind - eine grundsätzliche Empfehlung von Experten und Expertinnen des Sektors.")
    st.image("media/elinor.png")
    st.write("**62 % enthalten keine statistischen Angaben**, die ein wesentlicher Bestandteil eines jeden Berichts sind, um zu zeigen, dass der berichtete Vorfall kein Einzelfall ist, sondern Teil eines systemischen Problems.")

findings()




