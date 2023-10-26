import streamlit as st
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))
from modules import __page_setup__


# PAGE SETUP

__page_setup__.page_setup()

@st.cache_data
def load_kontext():
    st.title("📖 Kontext & Guidelines")
    st.subheader("Warum ist die Berichterstattung über Partnerschaftsgewalt so wichtig?")
    st.write("Medienberichterstattung hat einen bewiesenen Einfluss darauf, wie wir als Gesellschaft über ein Thema denken. Insbesondere bei sensiblen Themen wie Partnerschaftsgewalt macht die Sprache und das Framing eines Geschehens einen großen Unterschied. 'Framing' bezeichnet die Art und Weise, wie Informationen präsentiert werden, um die Sichtweise und Reaktion der Menschen zu beeinflussen. Dabei werden bestimmte Aspekte hervorgehoben, um eine bestimmte Perspektive zu fördern.")
    st.write("Genauere Einblicke dazu gibt zum Beispiel die Studie [Rezeption medialer Frames in der Berichterstattung über Gewalt gegen Frauen](https://www.lfsh.de/files/Materialien/Rezeption%20medialer%20Frames.pdf) von M. L. Teichgräber und L. Mußlick. In der Studie untersuchen die Autor*innen , wie bestimmte Blickwinkel und Schwerpunkte in den Berichten - das Framing - beeinflussen können, wie die Menschen über Gewalt gegen Frauen denken. Das Framing betont verschiedene Aspekte, wie zum Beispiel, wer schuld ist oder wie man das Problem lösen kann. Die Studie zeigt, dass die Art, wie die Medien über Gewalt berichten, die Meinung der Öffentlichkeit und sogar politische Reaktionen beeinflussen kann. Manche Frames können dazu führen, dass Gewalt als individuelles Problem gesehen wird, während andere auf gesellschaftliche Ursachen hinweisen.")
    st.write("Die Studie macht sehr deutlich, wie wichtig die Wortwahl, Schwerpunkte und Framing in Berichterstattung zur Partnerschaftsgewalt sind. ")
    st.subheader("Worauf muss man in der Berichterstattung zu Partnerschaftsgewalt achten? ")
    st.markdown("<br>", unsafe_allow_html=True)
    st.write("**⚠️ Sensationalismus**")
    st.write("Sensationalismus kann dazu führen, dass die Ernsthaftigkeit und Relevanz von Partnerschaftsgewalt heruntergespielt wird. Opfer von Partnerschaftsgewalt könnten dadurch das Gefühl haben, dass ihre Erfahrungen nicht angemessen wahrgenommen werden.")
    st.markdown('''
<div style="border: 2px solid #E6E6E6;background-color:#E6E6E6; border-radius: 5px; padding: 10px 30px 10px 10px; margin:10px 30px 30px 10px; text-align: center;">
    <blockquote style="font-style: italic;">
        Familientragödie klingt nach Schicksal, etwas, was von außen gekommen und nicht zu ändern ist...Femizide sind gezielt, geplant, überlegt, und von Macht und Dominanz geprägt, aber Zeitungen sprechen von reinem Beziehungsdrama... Solche Begrifflichkeiten verfälschen die Tatsachen.
    </blockquote>
    <p style="text-align: right;font-size:small;">Tanja Bourges, Leiterin der Beratungsstellen des Frauen- und Mädchennotrufs Rosenheim e.V.</p>
</div>
''', unsafe_allow_html=True)
    st.write("  \n  \nAußerdem kann sensationalistische Berichterstattung stereotype Bilder von Opfern und Tätern verstärken, die der Realität nicht gerecht werden. Dies kann die öffentliche Wahrnehmung von Partnerschaftsgewalt beeinflussen und die Vorstellung verstärken, dass bestimmte Faktoren oder Charakteristika Gewalt rechtfertigen könnten.  \n  \nSensationalistische Berichterstattung kann das Bewusstsein für komplexe psychologische, emotionale und soziale Dynamiken, die mit Partnerschaftsgewalt verbunden sind, beeinträchtigen. Dies erschwert die Fähigkeit, das Problem in seiner ganzen Tiefe zu verstehen.")
    st.markdown("<br>", unsafe_allow_html=True)
    st.write("**⚠️ Verstörende Sprache**")
    st.write("Opfer von Partnerschaftsgewalt könnten sich durch reißerische Berichterstattung und detaillierte Beschreibungen von Gewalt erneut traumatisiert fühlen. Sensationelle Beschreibungen ihrer Erfahrungen könnten ihre psychische Belastung verschlimmern.  \n  \nBeachte: Graphische/ Detaillierte Sprache kann von Relevanz sein, um deutlich zu machen, was Opfern passiert und klarzustellen, wie aggressiv und gewalttätig häusliche Gewalt sein kann. Allerdings muss unterschieden werden, was journalistisch wichtig ist, um die Situation genau zu beschreiben und was eine unnötige Detaillierung wäre, die die Würde des Opfers verletzt und/oder einen Versuch darstellt, eine emotionale Reaktion des Lesers zu provozieren.")
    st.markdown('''
<div style="border: 2px solid #E6E6E6;background-color:#E6E6E6; border-radius: 5px; padding: 10px 30px 10px 10px; margin:10px 30px 30px 10px; text-align: center;">
    <blockquote style="font-style: italic;">Es muss erzählt werden, was Menschen erleiden müssen und wie schlimm es wirklich ist - aber die Sprache soll sachlich und nüchtern sein, nicht reißerisch wie in einem Krimi.
    </blockquote>
    <p style="text-align: right;font-size:small;">Birte, Überlebende von häuslicher Gewalt</p>
</div>
''', unsafe_allow_html=True)
    st.write("\n  \nWenn Du eine grafische Beschreibung für journalistisch relevant und angebracht hältst, überlege Dir, eine Triggerwarnung auszusprechen. ")
    st.markdown("<br>", unsafe_allow_html=True)
    st.write("**⚠️ Schilderung der Verantwortung**")
    st.write("Die Schilderung der Verantwortung des Opfers deutet an, dass Opfer für die Gewalt zum Teil mitverantwortlich sind oder dass sie die Situation selbst provoziert haben. Dies führt zu einer Schuldumkehr.")

    st.markdown('''
<div style="border: 2px solid #E6E6E6;background-color:#E6E6E6; border-radius: 5px; padding: 10px 30px 10px 10px; margin:10px 30px 30px 10px; text-align: center;">
    <blockquote style="font-style: italic;">
Es bedarf überlegten und sehr klaren Formulierungen mit eindeutiger Positionierung, wer die Verantwortung für die ausgeübte Gewalt trägt. Viele Artikeln implizieren eine Mitschuld der Betroffenen und geben ihr zwischen den Zeilen eine Mitverantwortung für das Geschehene. Das ist fatal für betroffene Frauen, die solche Artikel lesen, und realitätsverzerrend für den gesellschaftliche Blick auf von Gewalt Betroffene.                
    </blockquote>
    <p style="text-align: right;font-size:small;">Tanja Bourges, Leiterin der Beratungsstellen des Frauen- und Mädchennotrufs Rosenheim e.V.</p>
</div>
''', unsafe_allow_html=True)
    st.write("\n  \nIndem die Schuld den Opfern zugeschrieben wird, wird die Verantwortung der Täter für ihr gewalttätiges Verhalten verharmlost. Infolgedessen besteht die Gefahr, dass Täter weniger zur Rechenschaft gezogen werden und die eigentlichen Ursachen der Gewalt vernachlässigt werden.  \n  \nOpfer könnten sich aufgrund von Schuldgefühlen und Stigmatisierung davor scheuen, Hilfe oder Unterstützung zu suchen. Dies kann ihre Möglichkeiten, aus der Gewaltsituation herauszukommen, stark einschränken.")
    st.markdown("<br>", unsafe_allow_html=True)
   
    st.write("**⚠️ Nennung von Nationalitäten**")
    st.write("Wenn Nationalitäten genannt werden, lenkt dies oft von den eigentlichen strukturellen und sozialen Ursachen von Partnerschaftsgewalt ab. Diese komplexen Ursachen können durch eine vereinfachte Betonung auf Nationalitäten nicht angemessen vermittelt werden.  \n  \nDie Nennung von Nationalitäten kann rassistische und diskriminierende Haltungen verstärken, indem sie die Idee unterstützt, dass Gewalt von bestimmten ethnischen oder kulturellen Gruppen häufiger begangen wird.")
    st.markdown("<br>", unsafe_allow_html=True)
    st.write("**✅ Statistiken**")
    st.write("Statistiken liefern objektive und faktenbasierte Informationen über das Ausmaß und die Prävalenz von Partnerschaftsgewalt. Sie helfen dabei, ein genaueres Bild der Realität zu vermitteln. Durch die Nennung von Statistiken kann deutlich werden, dass Partnerschaftsgewaltein weit verbreitetes gesellschaftliches Problem ist und nicht isolierte Einzelfälle betrifft.")
    st.markdown('''
<div style="border: 2px solid #E6E6E6;background-color:#E6E6E6; border-radius: 5px; padding: 10px 30px 10px 10px; margin:10px 30px 30px 10px; text-align: center;">
    <blockquote style="font-style: italic;">Gewalt ist ein gesellschaftliches, strukturelles Problem. In Artikeln wird das so fast nie gesagt.
    </blockquote>
    <p style="text-align: right;font-size:small;">Tanja Bourges, Leiterin der Beratungsstellen des Frauen- und Mädchennotrufs Rosenheim e.V.</p>
</div>
''', unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    st.write("**✅ Opferunterstützung**")
    st.write("Verweise auf Opferschutz und Hilfsangebote bieten konkrete Informationen und Ressourcen für Menschen, die von Partnerschaftsgewalt betroffen sind. Dies kann Opfern helfen, Unterstützung zu finden und ihnen gleichzeitig das Gefühl zu vermitteln, dass sie nicht alleine in ihrer Situation sind.  \n  \nWenn Medien auf Opferschutz und Hilfsangebote hinweisen, kann dies dazu beitragen, das Bewusstsein für Partnerschaftsgewalt zu schärfen und Menschen dazu zu ermutigen, Hilfe zu suchen oder verdächtige Situationen zu melden. Verweise auf Hilfsangebote können auch Menschen in der Umgebung von Opfern helfen, angemessen zu reagieren und Unterstützung anzubieten")
    st.markdown('''
<div style="border: 2px solid #E6E6E6;background-color:#E6E6E6; border-radius: 5px; padding: 10px 30px 10px 10px; margin:10px 30px 30px 10px; text-align: center;">
    <blockquote style="font-style: italic;">„Man ist soweit unten, dass man nicht mehr glaubt, jemand würde einen helfen. Man schämt sich.... Medien müssen klarstellen, dass es jedem passieren kann, und man nicht selber Schuld ist. <br>
Authentisch und ehrlich zu schreiben kann wirklich jemanden helfen und was bewirken.
    </blockquote>
    <p style="text-align: right;font-size:small;">Birte, Überlebende von häuslicher Gewalt</p>
</div>
''', unsafe_allow_html=True)
    st.subheader("📚 Weitere Guidelines und Tipps")
    st.write("Hier findest Du weitere Resources zum Thema wie man besser über Partnerschaftsgewalt berichten kann:")
    st.write("- [Kein Familiendrama](https://www.journalist.de/startseite/detail/article/kein-familiendrama-berichterstattung-ueber-femizide-und-der-umgang-mit-ueberlebenden-und-angehoerigen): Berichterstattung über Femizide und der Umgang mit Überlebenden und Angehörigen (www.journalist.de) ")
    st.write("- [Leitlinien für Medienschaffende](https://www.big-berlin.info/sites/default/files/uploads/2207_FEM-UnitED_Leitlinien-Medienschaffende_7-2022.pdf): Beitrag zur Prävention von Gewalt gegen Frauen und Mädchen (Fem-United)")
    st.write("- [Dignity for Dead Women](https://www.welevelup.org/wp-content/uploads/2022/06/Media-Guidelines-V2-1.pdf): Media guidelines for reporting domestic abuse deaths (We Level Up)")
    st.write("- [Guidelines for Reporting on Violence Against Women in the News Media](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2832441). Australian Journalism Review 38(1): 5-17. Georgina Sutherland, Angus McCormack, Patricia Easteal, Kate Holland and Jane Pirkis (2016) ")
    st.write("- Mapping the Nexus Between Media Reporting and Violence Against Girls [UN Women](https://www.unwomen.org/sites/default/files/2022-08/Evidence-review-Mapping-the-nexus-between-media-reporting-of-violence-against-girls-en.pdf)")
load_kontext()
