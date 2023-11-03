import streamlit as st
from pathlib import Path
import sys
    

sys.path.append(str(Path(__file__).resolve().parent.parent))
from modules import __page_setup__

# PAGE SETUP
__page_setup__.page_setup()

# PAGE CONTENT
st.title("🌻 Über uns")
st.write("LanguageLens ist ein Projekt von [Frontline](https://www.frontline100.com/), einer Organisation, die digitale Lösungen gegen Partnerschaftsgewalt entwickelt, und wird vom [Medieninnovationszentrum Babelsberg](https://www.miz-babelsberg.de/foerderung/foerderprojekte-alumni/details/language-lens.html) gefördert.  \n  \nFrontline ist ein Sozialunternehmen mit Sitz in Berlin, das digitale Tools zur Bekämpfung von häuslicher Gewalt entwickelt. Unser Ziel ist es, mithilfe von evidenzbasierter Forschung und moderner Technologie digitale Hilfsmittel für Fachkräfte zu entwickeln, die bei der Bekämpfung von häuslicher Gewalt einen Unterschied machen.  \n  \nNeben LanguageLens entwickeln wir derzeit eine KI-gestützte Risikoanalyse namens “Lizzie”, die Unterstützungsdienste vor Ort wie Polizisten und Polizistinnen, Gesundheitspersonal und Sozialarbeiter*innen dabei helfen sollen, das Risiko wiederholter Gewalt in Fällen von häuslicher Gewalt korrekt einzustufen, um möglichst frühzeitig und effektiv den Gewaltkreislauf zu brechen.")
st.subheader("Das Team")

INTRO_TEXTS=["⭐ [Victoria Waldersee](https://www.linkedin.com/in/victoria-waldersee-73786776/) ist Journalistin bei Reuters, mit Erfahrung in der Berichterstattung über Themen von der Auto- und Modeindustrie über die Corona-Pandemie bis zur Politik. Außerdem war sie für ein Jahr Mitglied des Beirats von Frontline GmbH.",
    "⭐ [Ba Linh Le](https://www.linkedin.com/in/ba-linh-le-/) ist Entwicklungsleiterin von LanguageLens und arbeitet als Social Data Scientist. Sie ist Mitgründerin von Frontline und erforscht digitale Lösungen gegen Partnerschaftsgewalt.",
    "⭐ [Johanna Weiß](https://www.linkedin.com/in/johanna-weiss/) ist Data Scientist bei Frontline und unterstützt die technische Umsetzung von LanguageLens. Sie engagiert sich in Projekten, die soziale Probleme mithilfe technischer und datengetriebener Lösungen angehen.",
    "⭐ Unterstützung bei der Entwicklung unserer Daten bekommen wir zusätzlich von [Katrin Hermann](https://www.linkedin.com/in/katrin-hermann-886255b3/). Als Politikanalystin, die sich für die Schnittstelle zwischen öffentlicher Politik und den Rechten von Frauen und Mädchen interessiert, unterstützt sie uns bei der Entwicklung  Entwicklung der Kategorien und beim Aufbau des Trainingsdatensatzes."
]
PICS=["vic.jpg","balinh.jpg","johanna.jpg","kat.jpg"]

for pic, text in zip(PICS, INTRO_TEXTS):
    im_col,text_col,=st.columns([1,3])
    with im_col:
        st.image("streamlit/media/"+pic)
    with text_col:
        st.write(text)
    
st.subheader("Credits")
st.write("Wir bedanken uns ganz herzlich bei allen Menschen, die dieses Projekt möglich gemacht haben: ")
st.write("- Dem Team beim MIZ Babelsberg")
st.write("- Dem Team und Beirat von Frontline")
st.write("- &effect")
st.write("- Gregor Wiedemann")
st.write("- Rahka Baskaran")
st.write("- Ronny Patz")
st.write("- Sukayna Younger-Khan")
st.write("- Olaya Argüeso")




