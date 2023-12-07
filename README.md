
# LanguageLens

LanguageLens ist eine Streamlit-WebApp, die Medienschaffenden helfen soll besser über das Thema Partnerschaftsgewalt zu schrieben.  

In der WebApp kam man seinen Artikel zu Partnerschaftsgewalt einfügen und bekommt Feedback ob schädliche oder nützliche Sprache vorkommt bzw. was verbessert werden kann. 

Die WebApp basiert auf einem Bert-Model, welches Paragraphen aufgrund ihrer Ihlate klassifiziert. Trainiert wurde das Model mit Deutschen Zeitungsartikel zum Thema Partnerschaftsgewalt von 2018 bis 2022 analysiert.


## Projekt
Das Projekt ist in die folgenden Schritte untergliedert:
- Daten
    - extra_data.ipynb
- Modelle
    - general_model.ipynb
    - rule_based_model.ipynb
    - nationalities_model.ipynb
- WebApp
    - streamlit

### Daten

Das Projekt basiert auf einem Datensatz von GBI-Genios Deutsche Wirtschaftsdatenbank GmbH mit Zeitungsartikeln und Metadaten aus 257 Zeitungen von 2018-2022.Insgesamt umfasst der Datensatz 60.866.588 Artikel. 

Zusätzlich wurde ein Datensatz der Süddeutschen Zeitung erworben, da dieser nicht in der Genios-Datenbank enthalten war.Insgesamt umfasst der Datensatz der Süddeutschen Zeitung 601.670 Artikel. 

#### extra_data.ipynb
In diesem Notebook werden die Zip-Dateien erxtrahiert, die resultierenden XMLs gelesen und gefiltert.
Das Filtering hat zum Ziel, ausschließlich deutschsprachige Artikel zum Thema Partnerschaftsgewalt zuerhalten.

### Modelle

#### general_model.ipynb
In diesem Notebook werden Bert-Modelle darauf trainiert zu erkennen, ob es in einem Artikel um Partnerschaftsgewalt geht und wenn ja, ob sensationalistische oder verstörende Sprache auftaucht. Es handelt sich um ein Multi-Label Klassifikationsproblem.

#### rule_based_model.ipynb
In diesem Schritt geht es darum, positive Aspekte in Artikelparagraphen zu erkennen: Statistiken und Verweise zu Hilfshotlines oder Links für Betroffene. Das Model verwendet RegEx-Ausdrücke diese in Artikeln zu erkennen. 

#### nationalities_model.ipynb
In diesem Notebook wurde ein separates Model erstellt, dass erkennt, ob in einem Paragraphen die Nationalitäten von Betroffenen/ Täter:innen genannt werden. Dies ist ein binäres Klassifikationsproblem das mithilfe von einem Bert-Model trainiert wird.

### WebApp

Die WebApp wurde mit Hilfe von Streamlit erstellt. Der Order Streamlit umfasst folgende Komponenten:
- zwei trainierte Bert-Modelle
- Homepage (📍Home.py) und weitere Pages (in Order "pages") der Streamlit-WebApp
- modules: Python-Script für das Layout aller Pages
- media: Graphiken, Fotos, Vizuals der WebApp

### Sonstiges
#### scripts
- annotations.py: ein Skript zum Extrahieren der Datenannotationen, erforderlich zum Ausführen von general_model.ipny und nationalities_model.ipynb. 

## Language and Tools
Das Projekt benutzt Python 3.9 und erfordert die folgenden Libraries:
- Streamlit, version 1.25.0
- Pytorch, version 2.1.0
- Transformers, version 4.20.0
- Numpy, version 1.23.5
- Pandas, version  1.5.3
- Tqdm, version  4.66.1
- Google.colab, version  1.0.0
- Datasets, version 2.14.6
- Sklearn, version 1.2.2
