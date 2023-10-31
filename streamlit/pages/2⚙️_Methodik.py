import streamlit as st
import sys
from pathlib import Path
import pandas as pd

sys.path.append(str(Path(__file__).resolve().parent.parent))
from modules import __page_setup__
__page_setup__.page_setup()


#indent for lists
@st.cache_data
def load_meth():
    st.title("⚙️ Methodik")
    st.subheader("1.Die Idee")
    st.write("LanguageLens nimmt den Gebrauch von Sprache in der Berichterstattung über häusliche Gewalt genauer unter die Lupe, um sie im Einklang mit Leitlinien von Experten und Betroffenen zu verbessern.")
    st.write("Das bedeutet:  \n- die Beseitigung von sensationalistische oder bagatellisierende Sprache;  \n- die Vermeidung unnötig verstörende Beschreibungen von Gewalt;  \n- das Bewusstsein für andere Vorurteile, die die Berichterstattung beeinflussen, wie z. B. die Nennung der Nationalität der beteiligten Akteure in Fällen, in denen dies nicht unbedingt relevant ist;  \n- die Verwendung von Statistiken, um den systemischen Charakter häuslicher Gewalt zu verdeutlichen;  \n- und die Angabe einer Hotline für den Fall, dass Betroffene Deine Geschichte lesen und meinen, Unterstützung zu benötigen  \n")
    st.write("Unsere Lösung: Ein Check-Up Tool, das durch die Verwendung eines NLP-basierten Modells Zeitungsartikel über Partnerschaftsgewalt analysiert und zu jedem Absatz ein kurzes Feedback gibt, ob der Text die von Experten ausgewiesenen Kriterien erfüllt.")
    st.image("streamlit/media/Projektvorgehen.png","Projektvorgehen")
    st.markdown("Mehr Informationen zur Frage, warum die Berichterstattung zu Partnerschaftsgewalt wichtig ist und worauf man achten soll, erfährst Du [hier](Kontext_&_Guidelines).")
    st.subheader("2.Daten")
    st.write("**Woher kommen die Daten?**")
    st.write("Die Daten, die für das Projekt LanguageLens benutzt werden, stammen hauptsächlich aus der Zeitungsdatenbank von [Genios](https://www.genios.de/). Die Datenbank umfasst sämtliche Zeitungsartikel von 257 deutschsprachigen Zeitungen im Zeitraum 2018 - 2022. Neben dem Artikeltext enthält der Datensatz Metadaten zu jeder Veröffentlichung, unter anderem: den Namen der Zeitung, die zeitungsinterne Artikel ID, das Veröffentlichungsdatum, den Namen des Autors, Titel und Untertitel des Artikels, das Ressort, indem der Artikel veröffentlicht wurde. Insgesamt umfasst der Datensatz  60'866'588 Artikel. ")
    st.write("Zusätzlich wurde ein Datensatz der Süddeutschen Zeitung dazu genommen, da dieser nicht in der Genios-Datenbank enthalten ist. Die Daten der Süddeutschen Zeitung enthalten die gleichen Metadaten über den gleichen Zeitraum. Insgesamt umfasst der Datensatz 601'670 Artikel.")
    st.write("**Geltungsbereich der Daten**")
    st.write("Das Projekt richtet sich an die Medienberichterstattung in Deutschland und in deutschen Zeitungen. Aus diesem Grund sind alle nicht deutschen und nicht deutsch-sprachigen Zeitungen von der Analyse ausgeschlossen. ")
    st.write("**Auswahl der Daten**")
    st.write("Da die Datensätze Artikel zu allen Themen beinhalten, führten wir eine initiale Filterung durch, um hauptsächlich Artikel zum Thema Partnerschaftsgewalt zu erhalten. Für die Filterung nutzen wir folgende Ansätze: ")
    st.markdown("- Iterative Keyword-Suche mit Schlagwörtern und Wortkombinationen im Text  \n- Iterative Keyword-Suche mit Schlagwörtern und Wortkombinationen im Titel, Untertitel und Ressort \n- Aufbau eines Ausschluss-Wörterbuches (Bspw.: Ticker, Leserbrief, etc.)  \n- Iterative Keyword-Suche und RegEx-Filtern auf Paragraphen-Ebene ")
    st.write("Obwohl die Filterung einen Großteil der nicht relevanten Artikel aussortieren konnte, sind nach diesem Schritt noch ca. 60% der gefilterten Artikel nicht ausschließlich zum Thema Partnerschaftsgewalt. Das sind beispielsweise Artikel, die das Thema nur streifen oder am Rand erwähnen.")
    st.write("Am Anfang mussten wir diese Artikel als Teil der Annotationsarbeit aussortieren. Später verwendeten wir  für diesen Schritt ein trainiertes binäres Klassifizierungsmodell. Dazu mehr im Kapitel “Modelling”.")
    st.write("**Bearbeitung der Daten**")
    st.write("Da die Klassifizierung der Artikel für jeden einzelnen Paragraphen erfolgt, werden die Artikel in Paragraphen aufgespalten. Duplikate werden ignoriert. ")
    st.write("Anfänglich wurden die Paragraphen auch mit mehreren Preprocessing-Schritten bearbeitet, um z.B. Stoppwörter, Sonderzeichen und Ähnliches zu entfernen. Nach der Modellierung hat sich jedoch herausgestellt, dass die Modelle ausnahmslos besser funktionieren, wenn das Preprocessing der Texte ausgelassen wird. ")
    st.subheader("3. Annotationen")
    st.write("Für den Aufbau des Trainingsdatensatzes haben wir uns für die folgenden Annotationskategorien entschieden: ")
    st.write("- **Partnerschaftsgewalt**: Der Text handelt von Partnerschaftsgewalt, beinhaltet aber keine schädliche Sprache  \n- **Sensationalismus**: Der Text enthält hetzerische, aufmerksamkeitserregende, dramaturgische oder rührselige Sprache, die Clickbait ähnlich kommt.  \n- **Verstörend**: Der Text beschreibt Partnerschaftsgewalt und Missbrauch im Detail, so dass es potenziell verstörend auf Leser*innen sein könnte. Diese Kategorie wird weit gefasst und schließt alle Details ein, die über einen allgemeinen Tatbestand, also Verletzung, Mord/Totschlag, hinausgehen.  \n- **Nennung von Nationalität der Opfer / Täter:innen:** Der Text nennt die Herkunft/ Nationalität von Tätern oder Opfern, obwohl es für die Berichterstattung nicht von Relevanz ist.  \n- **Schilderung der Verantwortung**: Der Text deutet eine Schuld beim Opfer an ")
    st.markdown("Inwiefern diese Kategorien schädlich sein können und wie sie unsere Sicht auf das Thema beeinflussen, erfährst Du [hier](Kontext_&_Guidelines).")

    st.write("Für die Annotation der Daten wurde das Tool elinor verwendet. Mit elinor können Texte annotiert, Ontologien erstellt und in Experimenten getestet werden")
    st.image("streamlit/media/elinor.png")
    st.subheader("4. Modelling")
    st.write("Für die Entwicklung eines KI-Modells, das Artikel zu Partnerschaftsgewalt automatisch annotieren kann, gibt es zwei Ansätze: NLP-basierte und regelbasierte Modelle. ")
    st.write("**Regelbasierte Modellierung**")
    st.write("Der Regelbasierte Ansatz besteht  - ähnlich wie die initiale Filterung - aus ReEx-Ausdrücken und Schlagwörtern für verschiedene Kategorien, auf deren Basis die Paragraphen klassifiziert werden.  \nBei der initialen Annotierung haben wir festgestellt, dass bestimmte Kategorien einem gewissen Schema folgen, z.B. die Angabe von Telefonnummern / Emailadressen bei Hinweisen zu Unterstützungsdiensten. Diese Sammlung an Regeln nutzen wir, um folgende Kategorien zu finden:  \n- Statistiken zu Partnerschaftsgewalt  \n- Verweise zu Hilfsorganisationen, Hilfstelefonen, etc.  \n  \nDiese werden zusätzlich zu den Annotationskategorien in Texten klassifiziert. ")
    st.markdown("Warum es wichtig ist, Artikel zur Partnerschaftsgewalt mit Statistiken und Verweisen zur Opferhilfe zu versehen, erfährst Du [hier](Kontext_&_Guidelines)")
    st.write("**NLP-basierte Modellierung**") 
    st.write("Der Kern dieses Projekts sind mehrere NLP-Modelle, die darauf trainiert werden, schädliche Sprache in dem annotierten Trainingssatz zu verstehen und in einem neuen, nicht-annotierten Datensatz zu erkennen. ")
    right, left=st.columns(2)
    with left:
        st.image("streamlit/media/bert_structure.png", width=300, caption="Structure of Transformer, taken from 'Attention Is All You Need' (https://arxiv.org/abs/1706.03762)", output_format="PNG")
    with right:
        st.write("Für die Entwicklung des Modells wurden mehrere vor-trainierte Modelle aus der BERT-Familie getestet, darunter BERT, DistilBert, Bloom Modelle. Bei den vor-trainierten Modellen wurde darauf geachtet, dass sie möglichst auf deutschen Textkorpora basieren und beim Trainieren einen ähnlichen Schwerpunkt wie dieses Projekt haben. ")
        st.write("Außerdem wurde als Vergleich ein Tfidf-Modell getestet, welches aber erwartungsgemäß weitaus schlechter performte. Ein Tfidf-Modell ist eine Methode zur Einschätzung der Wichtigkeit eines Wortes in einem Textauschnitt im Verhältnis zu einem gesamten Korpus. Das Modell berechnet und kombiniert die Häufigkeit des Wortes im Text mit der Seltenheit des Wortes im Korpus.")
    st.write("Für das Laden und Trainieren der Modelle wurde Huggingface verwendet. Je nach Art des Modells musste die Form der Daten angepasst werden. ")
    st.write("**Schrittweise vs. allgemeine Modelle**")
    st.write("Für die Klassifizierung der Texte wurden zwei verschiedene Vorgehensweisen ausprobiert.  \n 1. Das erste ist ein allgemeines Modell, das zwischen problematischen Kategorien und allgemeinen Texten zu Partnerschaftsgewalt unterscheidet. ")
    st.write("2. Der andere Ansatz ist eine schrittweise Modellierung. Der schrittweise Ansatz berücksichtigt den Mengenunterschied in den Trainingsdaten für jede Kategorie.  \nDie Klassifizierung erfolgt demnach auf drei Ebenen. In der ersten wird ausschließlich unterschieden, ob es bei dem Text um Partnerschaftsgewalt geht. In der zweiten Ebene wird mithilfe von einem binären Modell festgestellt, ob der Text zu Partnerschaftsgewalt schädliche Sprache enthält.  \nDas dritte und letzte Modell benutzt dann die Texte mit schädlicher Sprache als Input und lernt, zwischen den Annotationskategorien 'Sensationalismus' und 'Verstörende Sprache' zu unterscheiden. Die Analyse und Modellierung der Kategorie 'Schilderung der Verantowrtung' überstieg die Rahmenbedingungen dieses Projekts.")
    st.image("streamlit/media/Modelstruktur.png", width=600)
    st.write("Der Vorteil eines schrittweisen Vorgehens ist, dass der Output der ersten bzw. zweiten Ebene, neben RegEx und Keywords, als zusätzlicher Filter der Zeitungsartikel für die Annotationsarbeit dienen kann. So kann die Annotierung auf die wesentlichen Artikel beschränkt werden. ")
    st.write("Die Kassifizierung der Kategorie 'Nennung von Nationalitäten' wurde in einem separaten, binären Model trainiert und ist demnach unabhängig von der beiden Ansätzen ")
    st.write("**Details zu Modellentwicklung**")
    st.write("Die Modellierung wurde größtenteils mit den folgenden Parametern bzw. Einstellungen definiert. In einigen Fällen weichen diese jedoch ab, um eine bessere Modell-Performance zu erzielen.  \n  \n80% der Daten wurden zum Trainieren der Modelle verwendet, und je 10% für die Validierung bzw. die Evaluation des Modells. ")
    st.write("Um ungleiche Klassen in den Daten zu vermeiden, wurden die Daten der überrepräsentierten Gruppe heruntergerechnet, so dass sie maximal 1,5 mal der Größe der bzw. aller anderen Kategorien entspricht. Zusätzlich wurde der Fokus der Modelle mit Hilfe unterschiedlicher Gewichtungen der Verlustfunktion auf die relevanten Kategorien gerichtet.   \n  \nDie Texte werden vor der Tokenisierung nicht angepasst oder vorverarbeitet. Aus Performance-Gründen werden die Paragraphen in der Trainingsphase teilweise gekürzt. Die maximale Länge aller Texte, die durch Bert-Modelle analysiert werden können, sind 512 Tokens. Ein Token kann ein Wort, ein Satzzeichen oder ein Wortteil sein. Diese Kürzung betrifft allerdings <5% der Paragraphen und sollte daher keinen negativen Effekt auf das Training haben. Jeder Paragraph wird als Teil der Tokenisierung 'gepaddet', das heißt, jeder Text wird künstlich mit Hilfe von dafür definierten Tokens auf die maximale Länge verlängert, so dass alle Paragraphen die gleiche Länge haben.  \n  \nDie Hyperparameter der verschiedenen Modelle wurden basierend auf der Modell-Performance und der Größe des Datensatzes individuell angepasst.")
    st.subheader("5. Evaluation und Selektion der Modelle")
    st.write("Zur Evaluation der Modelle wurde die F1-Score verwendet, da sie sowohl Präzision als auch Recall berücksichtigt. Präzision ist das Maß für die Genauigkeit eines Modells, definiert als der Anteil der korrekten positiven Vorhersagen an der Gesamtanzahl der positiven Vorhersagen. Recall hingegen misst die Vollständigkeit und wird als der Anteil der korrekten positiven Vorhersagen an der Gesamtanzahl der tatsächlich positiven Fälle berechnet.")
    _,mid,_=st.columns([1,3,1])
    df=pd.read_csv("streamlit/media/model_performances.csv", index_col=0)
    with mid:
        st.dataframe(df)
    st.write("Für die Selektion des finalen Modells wurden Performance als auch die Komplexität bzw. Größe des Modells berücksichtigt werden. Da die schrittweisen Modelle zwischen weniger Kategorien unterscheiden, sind sie einfacher zu trainieren und sagen neue Artikel besser vorher. Allerdings gibt es zwei Probleme mit dem schrittweisen Vorgehen. Einerseits sind es mehrere Modelle die nacheinander klassifizieren und länger für die Vorhersage brauchen. Andererseits bauen sie aufeinander auf, so dass die allgemeine Fehlerquote sich mit jeder Modellebene vergrößert. Aus diesen Gründen, haben wir uns für die Klassifizierung durch das allgemeine Modell entschieden")

load_meth()
