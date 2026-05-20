# 📘 Guide d'Installation et d'Utilisation - SAE 24 (Scapy)

Ce guide détaille pas-à-pas comment configurer et utiliser le projet de la SAE 204. Ce projet utilise **Scapy**, une bibliothèque Python puissante pour la manipulation de paquets réseau, ce qui impose certaines contraintes techniques.

---

## ⚙️ 1. Comprendre les contraintes techniques

### Pourquoi Linux ?
La manipulation de paquets "bruts" (Raw Sockets) nécessite un accès direct à la carte réseau. Windows et macOS limitent fortement cet accès pour des raisons de sécurité. Linux est donc l'environnement recommandé et utilisé pour ce projet.

### Pourquoi `sudo` ?
L'envoi et la capture de paquets réseau sont des opérations privilégiées. Si vous lancez un script Scapy sans les droits d'administrateur, vous obtiendrez une erreur de type `PermissionError` ou `Socket Error`. **L'utilisation de `sudo` est donc obligatoire pour les scripts de forge et de capture.**

---

## 🛠️ 2. Installation pas-à-pas

### A. Création de l'environnement virtuel
Il est fortement recommandé d'utiliser un environnement virtuel (`venv`) pour éviter de polluer votre installation Python système et garantir que toutes les versions de bibliothèques sont identiques.

```bash
# 1. Créer l'environnement virtuel
python3 -m venv sae24_env

# 2. L'activer
source sae24_env/bin/activate
```

### B. Installation des dépendances
Une fois l'environnement activé, installez Scapy et les autres outils nécessaires :

```bash
pip install -r requirements.txt
```

---

## 🚀 3. Guide d'utilisation détaillé

### Étape 1 : Forge de paquets (`step1_scapy_basics`)
L'objectif est de créer des paquets ICMP (Ping) personnalisés.

**Lancement :**
```bash
cd step1_scapy_basics
sudo ../sae24_env/bin/python basic_forge.py
```
*Note : On utilise le chemin vers le python du venv même avec sudo pour être sûr d'utiliser les bibliothèques installées.*

**Ce qu'il faut observer :**
- Le script doit envoyer un paquet et attendre une réponse.
- Utilisez la méthode `.show()` dans Scapy pour inspecter la structure du paquet envoyé.

### Étape 2 : Analyse Ping6 (`step2_ping6_analysis`)
Cette étape consiste à analyser le comportement du protocole IPv6.

- Les résultats sont consignés dans `analysis_results.txt`.
- L'analyse porte sur la structure des en-têtes IPv6 et la gestion des adresses de lien local.

### Étape 3 : Manipulation Python (`step3_python_manipulation`)
Ici, on travaille sur le parsing de données réseau (extraction d'infos depuis des logs).

**Lancement :**
```bash
cd step3_python_manipulation
sudo ../sae24_env/bin/python exercises.py
```

---

## 🆘 4. Guide de survie (Dépannage)

| Problème | Cause possible | Solution |
| :--- | :--- | :--- |
| `Permission denied` | Absence de droits root | Ajoutez `sudo` devant votre commande. |
| `Command not found` | Mauvais chemin vers Python | Vérifiez que vous pointez bien vers `bin/python` à l'intérieur de votre dossier `sae24_env`. |
| `No route to host` | Cible réseau injoignable | Vérifiez votre connexion ou l'adresse IP de destination. |
| `ModuleNotFoundError` | Venv non activé ou dép. manquantes | Lancez `pip install -r requirements.txt` dans l'environnement activé. |

---

## 📝 Résumé des commandes rapides
```bash
# Activer
source sae24_env/bin/activate

# Lancer un script (exemple)
sudo ./sae24_env/bin/python path/to/script.py
```
