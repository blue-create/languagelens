import numpy as np
import pandas as pd

#  Funktion zum Extrahieren der Annotationen der Jsons von ELinor
def extract_annotations(test):
  """
  Funktion zum Extrahieren der Annotationen der Jsons von ELinor
  Arguments:
    - Liste der Annotationen, wie sie von Elinor bereitgestellt werden.
  Returns:
    - ann_dict (dict): Key sind Initialien des Annotatoren und Value die Annotation
    - leeres dict, wenn keine Annotation vorhanden
  """
  ann_dict=dict()
  for ann in test:
    name=ann["annotator"]["name"][0]
    label=ann["concept"]["preferred_label"]["name"]
    if name in ann_dict.keys():
      ann_dict[name].append(label)
    else:
      ann_dict[name]=[label]
  #remove duplicates
  for key in ann_dict.keys():
    ann_dict[key]=set(ann_dict[key])
    ann_dict[key]=clean_annotation(ann_dict[key])
  return ann_dict

# Funktion zum Berechnen der Jaccard-Ähnlichkeit von Sets  
def jaccard_similarity(sets):
    """
  Funktion zum Berechnen der Jaccard-Ähnlichkeit von Sets  
  Arguments:
    - sets (list of sets): Sets mit denen die Jaccard-Ähnlichkeit berechnet werden soll
  Returns:
    - similarity (float): Jaccard-Ähnlichkeit
  """
    intersection = set.intersection(*sets)
    union = set.union(*sets)
    similarity = len(intersection) / len(union)
    return similarity

def calculate_similarity(annotations: dict, sim="jaccard"):
  """
  Funktion zum Berechnen der Ähnlichkeit von Sets  
  Arguments:
    - annotations (dict of sets): Sets mit denen die Ähnlichkeit berechnet werden soll
    - sim (str): "jaccard" oder "dice" je nach dem welche Ähnlichkeit berechnet werden soll
  Returns:
    - similarity (float): Ähnlichkeit, np.nan, wenn keine Annotationen vorhanden
  """
  if len(annotations)==1:
    return np.nan
  else:
    if sim=="jaccard":
      return jaccard_similarity(list(annotations.values()))
    elif sim=="dice":
      return dice_similarity_multiple(list(annotations.values()))
    
def dice_similarity_multiple(sets):
  """
  Funktion zum Berechnen der Dice-Ähnlichkeit von Sets  
  Arguments:
    - sets (list of sets): Sets mit denen die Jaccard-Ähnlichkeit berechnet werden soll
  Returns:
    - similarity (float): Dice-Ähnlichkeit
  """
  num_sets = len(sets)
  similarity_sum = 0
  for i in range(num_sets - 1):
      for j in range(i + 1, num_sets):
          set1 = sets[i]
          set2 = sets[j]
          intersection = set1.intersection(set2)
          set_sum = len(set1) + len(set2)
          similarity = 2 * len(intersection) / set_sum
          similarity_sum += similarity
  average_similarity = similarity_sum / (num_sets * (num_sets - 1) / 2)
  return average_similarity


def ground_truth_filter(entry, min_coannotation=1, min_similarity=0.5, similarity="jaccard"):
    """
  Funktion zum Extrahieren der Annotation, mit 2 Konditionen:
      - eine Mindestanzahl von Personen, die einen Text kommentiert haben
      - ein Minimum an Ähnlichkeit zwischen allen Annotationen eines Textes
  Arguments:
      - annotations (dict): dict mit den Annotationen aller Annotatoren eines Textes
      - min_coannotation (int): minimum der gewünschten Ko-Annotationen eines Textes
      - min_similarity (int): minimale Ähnlichkeit der Annotationen
  Returns:
      - entweder:
        - most_common (set): mit denen am häufigsten vorkommenden Labels, wenn Konditionen erfüllt sind
        - NaN: wenn die Annotationen nicht die Konditionen erfüllen
  """
  if len(entry)==0:
    return np.nan
  if len(entry["annotations"])<min_coannotation or entry[similarity]<min_similarity:
    return np.nan
  else:
    all_values = [value for s in entry["annotations"].values() for value in s]
    most_common=pd.DataFrame(all_values).mode().values
    most_common=[i[0]for i in most_common]
    if len(most_common)>1 and "Domestic Violence" in most_common:
      most_common.remove("Domestic Violence")
    return set(most_common)
  

def clean_annotation(ann):
  """
  Funktion zum Entfernen vom Label "Domestic Violence" von einer Annotation, wenn sie in Kombination mit anderem Label auftaucht  
  Arguments:
    - ann (set): Set mit Annotationen
  Returns:
    - ann (set): Annotation ohne "Domestic Violence", wenn es nicht alleine vorkommt
  """
  if len(ann)>1:
    ann.discard("Domestic Violence")
  return ann
