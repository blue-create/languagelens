import streamlit as st
import torch
import numpy as np
from pathlib import Path
import sys
from transformers import AutoTokenizer, AutoModelForSequenceClassification
from itertools import compress
import re


sys.path.append(str(Path(__file__).resolve().parent.parent))
from modules import __page_setup__

# PAGE SETUP
__page_setup__.page_setup("wide")
st.title("Willkommen bei LanguageLens!")
st.subheader("Überprüfe Deinen Artikel zu Partnerschaftsgewalt.")

#CONSTANTS
labels_nat=["","Nationality"]
labels_gen=['Domestic Violence','Graphisch','Sensationalistisch','Statement of responsibility']

FEEDBACK={"Domestic Violence":"Keine problematische Sprache gefunden!",
          "":"Keine problematische Sprache gefunden!",
          "Graphisch": "**Verstörende Sprache** Detaillierte Beschreibungen von Gewalt können auf Leser traumatisierend wirken. Überlege dir, ob es journalistisch wichtig ist, die Situation genau zu beschreiben und gegebenenfalls eine Triggerwarnung auszusprechen.",
          "Sensationalistisch":"**Senationalistische Sprache** kann durch den Fokus auf spektakuläre Aspekte von den eigentlichen Ursachen und der Problematik von häuslicher Gewalt ablenken",
          "Support Service":"**Hilfsangebote**  bieten konkrete Informationen und Ressourcen für Menschen, die von häuslicher Gewalt betroffen sind. Dies kann Opfern helfen, Unterstützung zu finden und aus gefährlichen Situationen herauszukommen.",
          "Statistic":"**Statistiken** liefern objektive und faktenbasierte Informationen über das Ausmaß und die Prävalenz von häuslicher Gewalt. Sie helfen dabei, ein genaues Bild der Realität zu vermitteln.",
          "Nationality":"**Die Erwähnung von Nationlitäten** kann die öffentliche Wahrnehmung verzerren und zur Verstärkung rassistischer Stereotypen führen. "
          }

@st.cache_resource
def load_tokenizer():
    return AutoTokenizer.from_pretrained("bert-base-german-cased")
@st.cache_resource
def load_gen_model():
    return AutoModelForSequenceClassification.from_pretrained("streamlit/best_model_general",num_labels=len(labels_gen),id2label={idx:label for idx, label in enumerate(labels_gen)},label2id= {label:idx for idx, label in enumerate(labels_gen)})
@st.cache_resource 
def load_nat_model():
    return AutoModelForSequenceClassification.from_pretrained("streamlit/best_model_nationalities",num_labels=2,id2label={idx:label for idx, label in enumerate(labels_nat)},label2id= {label:idx for idx, label in enumerate(labels_nat)})

tokenizer = load_tokenizer()
trainer_nat = load_nat_model()
trainer_gen = load_gen_model()

sigmoid = torch.nn.Sigmoid()

STATS=["\d*([\.,]\d*)?[ ](Prozent|%)",
       "\d+ (Fälle|Opfer|Frauen|Kinder|Personen|Betroffene|Morde|Plätze)\W",
       "Bundeskriminalamt",
       "Kriminalstatistik",
       "statistisches Amt",
       "offizielle Zahlen",
       "jeder? (zweiter?|dritter?|vierter?|fünfter?|sechster?|siebenter?) (mann|frau|kind)",
       "(eine|zwei|drei|vier|fünf) von (zwei|drei|vier|fünf) Frauen",
       "\Wbka\W"]
SUPPORT=[
         "(www\.)\S+\.\S+",
         "Beratungsstelle",
         "Notrufdienst",
         "Hotline",
        #EMAIL ADDRESS
        "[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}",
        "([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+"
        #PHONE NUMBERS
         "\d{2,4}\s?\(?\d{1,5}\)?[-.\s]?(\d{1,8}[-.\s]?){1,5}\d{1,8}"
         ]
GRAPHIC=["vergewaltigt","vergewaltigung","sexuell missbraucht"]
SENSATIONALIST =["Ehetragödie",
       "verschmähter? Liebhaber(in)?",
       "rachsüchtige Hexe",
       "Eifersuchtstat",
       "Beziehungsdramas?",
       "Rosenkrieg",
       "Frauenschläger",
       "tödliches?m? Drama",
       "tränenerstickter? Stimme",
       "blutüberströmt",
       "tödlichen? Eskalation",
       "ehedrama",
       "bluttat",
       "schicksalsgebeutelt",
       "Alptraum"]

# METHODS
def start_analysis(article):
    paragraphs=article.split("\n")
    overall_fb=[]
    for para in paragraphs:
        if len(para)>0:
            (neg_fb, pos_fb, all_lab)=analyse_paragraph(para)
            overall_fb.append(all_lab)
            paragraophs, feedback= st.columns(2)
            with paragraophs:
                st.info(para)
            with feedback:
                st.warning(neg_fb,)
                if len(pos_fb)>0:
                    st.success(pos_fb, icon="👍")
        

def analyse_paragraph(para):
    tokens=tokenizer(para, return_tensors="pt")
    label_gen=general(tokens)

    if "Graphisch" not in label_gen:
        if text_contains_pattern(GRAPHIC,para):
            label_gen.append("Graphisch")
    if "Sensationalistisch" not in label_gen:
        if text_contains_pattern(SENSATIONALIST,para):
            label_gen.append("Sensationalistisch")   
    label_nat=nationality(tokens)
    neg_fb=get_neg_feedback(label_gen+[label_nat])
    label_stat=statistics(para)
    label_supp=support(para)
    pos_fb=get_pos_feedback([label_stat]+[label_supp])
    all_lab=label_gen+[label_nat,label_stat,label_supp]
    return neg_fb, pos_fb, all_lab

def general(tokens):   
    outputs = trainer_gen(**tokens)
    logits = outputs.logits
    probs = sigmoid(logits.squeeze().cpu())
    predictions = np.zeros(probs.shape)
    predictions[np.where(probs >= 0.5)] = 1
    return list(compress(labels_gen, predictions))   

def nationality(tokens):
    outputs = trainer_nat(**tokens)
    logits = outputs.logits
    probs = sigmoid(logits.squeeze().cpu())
    predictions = np.zeros(probs.shape)
    predictions[np.where(probs >= 0.5)] = 1
    label=trainer_nat.config.id2label[predictions.argmax().item()]
    return label

def get_neg_feedback(label_list):
    label_list = [x for x in label_list if x != '']
    fb=[]
    if label_list==["Domestic Violence"] or len(label_list)==0 :
        return FEEDBACK["Domestic Violence"]
    if "Graphisch" in label_list:
        fb.append(FEEDBACK["Graphisch"])
    if "Sensationalistisch" in label_list:
        fb.append(FEEDBACK["Sensationalistisch"])
    if "Nationality" in label_list:
        fb.append(FEEDBACK["Nationality"])
    return "  \n".join(fb)

def get_pos_feedback(label_list):
    label_list = [x for x in label_list if x != '']
    fb=[]
    if "Support Service" in label_list:
        fb.append(FEEDBACK["Support Service"])
    if "Statistic" in label_list:
        fb.append(FEEDBACK["Statistic"])
    return "  \n".join(fb)


def statistics(text):
    for pattern in STATS:
        if len(re.findall(pattern=pattern,string=text,flags=re.IGNORECASE))>0:
            return "Statistic"
    return ""


def support(text):
  for pattern in SUPPORT:
    if len(re.findall(pattern=pattern,string=text,flags=re.IGNORECASE))>0:
      return "Support Service"
  return ""

def text_contains_pattern(PATTERNS, text):
  for pattern in PATTERNS:
    if len(re.findall(pattern=pattern,string=text,flags=re.IGNORECASE))>0:
      return True
  return False

def get_written_feedback(label, nat_label):
    if len(nat_label)==0:
        return ", ".join(label)
    else:
        return ", ".join(label+nat_label)


# PAGE CONTENTS
article  = st.text_area('**Füge hier Deinen Artikel ein:**', key="art")
if st.button("Artikel überprüfen"):
    paragraphs, feedback= st.columns(2)
    with paragraphs:
        st.subheader("Dein Input")
    with feedback:
        st.subheader("Feedback")
    start_analysis(article)
st.markdown(f"Mehr Informationen zur Frage, warum die Berichterstattung zu Partnerschaftsgewalt wichtig ist und worauf man achten soll, erfährst Du [hier](Kontext_&_Guidelines)")
   