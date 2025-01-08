from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
import numpy as np

# Les données d'entraînement
X = np.array([[1, 2], [0, 1], [1, 1], [0, 2], [1, 3]])  # Caractéristiques : Couleur, Taille
y = np.array([1, 0, 1, 0, 1])  # Cible : 1=Pomme, 0=Orange

# 1. Créer un réseau de neurones simple
model = Sequential([
    Dense(4, activation='relu', input_shape=(2,)),  # 4 neurones dans la couche cachée
    Dense(1, activation='sigmoid')  # 1 neurone pour la sortie (Pomme ou Orange)
])

# 2. Compiler le modèle
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# 3. Entraîner le modèle
model.fit(X, y, epochs=50, batch_size=1)

# 4. Tester sur de nouveaux fruits
nouveaux_fruits = np.array([[0, 3], [1, 1]])  # Ex : Orange grande, Pomme petite
predictions = model.predict(nouveaux_fruits)

# 5. Afficher les prédictions
print("Prédictions :", predictions)
