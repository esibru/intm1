from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Liste de métiers (chaque élément = un "mot" complet dans la bulle)
metiers = [
    "développeur full stack",
    "technicien réseau",
    "ingénieur système",
    "développeur graphique",
    "exploitation informatique",
    "accompagnateur du changement",
    "rédacteur de documentation",
    "développeur logiciel",
    "concepteur développeur informatique",
    "administrateur de base de données",
    "administrateur système",
    "développeur web",
    "testeur",
    "technical account manager",
    "administrateur réseau",
    "architecte",
    "administrateur sécurité",
    "webmaster",
    "ingénieur logiciel",
    "analyste",
    "intégrateur",
    "ingénieur logiciel bio informaticien",
    "développeur",
    "chief data officier"
]

# Convertir en dictionnaire avec une fréquence par défaut (ici 1)
frequences = {metier: 1 for metier in metiers}

# Générer le nuage
wordcloud = WordCloud(
    width=800,
    height=400,
    background_color="white",
    max_words=50,
    prefer_horizontal=0.5,  # proportion de mots horizontaux
    random_state=42,         # pour la reproductibilité
    min_font_size=10,
    max_font_size=80,
    margin=2
).generate_from_frequencies(frequences)

# Affichage / sauvegarde
plt.figure(figsize=(10,5))
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.savefig("nuage_metiers.png", bbox_inches='tight', dpi=300)
