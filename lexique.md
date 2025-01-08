
# LEXIQUE DATA

### **Qu'est-ce que l'encodage "One-Hot"?**

L'**encodage one-hot** est une méthode utilisée pour convertir des données **catégorielles** (par exemple, des noms de mois, des types de produits) en un format que les algorithmes de machine learning peuvent comprendre. 

Plutôt que de représenter chaque catégorie par un seul entier (ce qui pourrait induire un **ordre ou une relation incorrecte entre les catégories**), on crée une nouvelle colonne binaire pour chaque catégorie. Chaque colonne contient **1** si l'observation appartient à cette catégorie, et **0** sinon.

#### Exemple : Encodage one-hot pour `month_of_year`
Si vous avez la colonne suivante :

| month_of_year |
|---------------|
| 1             |
| 2             |
| 3             |

Après un **one-hot encoding**, cela devient :

| month_1 | month_2 | month_3 |
|---------|---------|---------|
| 1       | 0       | 0       |
| 0       | 1       | 0       |
| 0       | 0       | 1       |

---

### **Lexique des termes importants**

#### 1. **Corrélation**
   - **Définition** : Mesure la relation linéaire entre deux variables.
   - **Échelle** :
     - +1 : Relation positive parfaite (quand une variable augmente, l’autre aussi).
     - 0 : Aucune relation linéaire.
     - -1 : Relation négative parfaite (quand une variable augmente, l’autre diminue).
   - **Exemple** : Si la température augmente, la consommation d’électricité (par exemple pour la climatisation) peut aussi augmenter.

#### 2. **Normalisation**
   - **Définition** : Ajuster les valeurs de variables continues pour qu'elles soient sur une échelle commune.
   - **Pourquoi** : Certains algorithmes (comme les régressions ou les réseaux de neurones) sont sensibles à la **différence d'échelle** entre les variables.
   - **Types** :
     - **Standardisation** : Ajuster pour une moyenne de 0 et un écart-type de 1.
     - **MinMax Scaling** : Ajuster les valeurs pour qu'elles se situent entre 0 et 1.

#### 3. **Encodage catégoriel**
   - **Définition** : Transformation des colonnes **catégoriques** (texte ou classes) en **valeurs numériques** pour qu’elles soient utilisables par les modèles.
   - **Types** :
     - **Label Encoding** : Chaque catégorie est remplacée par un entier unique (peut induire des biais si les catégories n’ont pas d’ordre naturel).
     - **One-Hot Encoding** : Chaque catégorie est transformée en une colonne binaire (1 ou 0).

#### 4. **Valeurs manquantes**
   - **Définition** : Données absentes ou non enregistrées dans votre dataset.
   - **Solutions courantes** :
     - **Suppression** des lignes/colonnes contenant des valeurs manquantes.
     - **Imputation** : Remplacement des valeurs manquantes par une valeur calculée (moyenne, médiane, mode).

#### 5. **Matrice de corrélation**
   - **Définition** : Tableau carré où chaque élément représente la corrélation entre deux variables du dataset.
   - **Pourquoi utile** : Permet d’identifier les relations fortes entre les variables.

#### 6. **Régression linéaire**
   - **Définition** : Modèle simple de machine learning qui prédit une variable cible (y) en fonction d'une ou plusieurs variables explicatives (x).
   - **Formule** : \( y = ax + b \)
     - \( a \) : Coefficient qui indique l’impact de \( x \) sur \( y \).
     - \( b \) : Constante.
   - **Exemple** : Prédire la consommation électrique en fonction de la température.

#### 7. **StandardScaler**
   - **Définition** : Méthode pour normaliser les données en ajustant les valeurs à une moyenne de 0 et un écart-type de 1.
   - **Utilisation** : Réduction de l’impact des échelles différentes entre variables.

#### 8. **Imputation**
   - **Définition** : Remplir les valeurs manquantes dans un dataset.
   - **Méthodes courantes** :
     - Moyenne/médiane/mode.
     - Valeurs spécifiques (exemple : 0 pour des colonnes monétaires).

#### 9. **DataFrame**
   - **Définition** : Structure de données tabulaire dans Python (librairie **pandas**).
   - **Pourquoi utile** : Permet de manipuler les données de manière intuitive (comme une feuille Excel).

#### 10. **Feature engineering**
   - **Définition** : Processus de création de nouvelles variables (ou caractéristiques) à partir des données brutes pour améliorer les performances d’un modèle.
   - **Exemples** :
     - Extraire la saison d’une colonne **date**.
     - Combiner des variables pour en créer de nouvelles (exemple : température ressentie).

#### 11. **One-Hot Encoding vs. Label Encoding**
   - **One-Hot Encoding** : Crée plusieurs colonnes binaires pour chaque catégorie.
   - **Label Encoding** : Remplace chaque catégorie par un entier unique.
   - **Quand utiliser quoi** : One-hot est préférable pour des catégories sans ordre, tandis que le label encoding est adapté pour des catégories ordonnées (exemple : petit, moyen, grand).

#### 12. **Évaluation des performances (MAE, RMSE, etc.)**
   - **MAE (Mean Absolute Error)** : Moyenne des erreurs absolues entre les prédictions et les valeurs réelles.
   - **RMSE (Root Mean Square Error)** : Racine carrée de la moyenne des carrés des erreurs. Donne plus de poids aux grandes erreurs.


## DEEP LEARNING

#### (a) Les couches (layers) :
**Input Layer** : Les données que tu donnes au modèle (ex. température, humidité...).
**Hidden Layers** : Les couches qui apprennent à détecter les motifs cachés dans les données.
**Output Layer** : La prédiction (ex. consommation d’électricité).
 
#### (b) Les poids et biais (weights and biases) :
**Les poids** indiquent l’importance d’une connexion entre deux neurones.
**Les biais** aident le modèle à s’ajuster pour être plus précis.

#### (c) Fonction d’activation :
**Une fonction mathématique** qui introduit de la non-linéarité pour que le modèle puisse apprendre des relations complexes. Exemple : ReLU (Rectified Linear Unit), sigmoïde, tanh.

#### (d) Entraînement (training) :
**Propagations avant (forward pass)** : Les données traversent le réseau pour donner une prédiction.
**Rétropropagation (backpropagation)** : Le modèle ajuste les poids pour réduire l’erreur entre la prédiction et la réalité.

#### (e) Fonction de coût (loss function) :
**Une mesure** qui indique à quel point le modèle se trompe. Le but est de minimiser cette erreur. Exemple : Mean Squared Error (MSE) pour la régression.

---

