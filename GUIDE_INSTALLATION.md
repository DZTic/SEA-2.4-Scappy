# 📘 Guide d'Installation et d'Utilisation - SAE 24

Ce guide détaille la mise en place de l'environnement nécessaire pour exécuter les scripts de la SAE 24.

## ⚙️ Prérequis Système

### 1. Système d'Exploitation
**Linux est impératif.** Scapy utilise des "raw sockets" pour manipuler les paquets réseau, une fonctionnalité qui est soit restreinte, soit absente sur Windows et macOS.

### 2. Privilèges Administrateur
L'envoi et la capture de paquets réseau nécessitent des droits root. Tous les scripts doivent être lancés avec `sudo`.

---

## 🚀 Installation Pas-à-Pas

### Étape 1 : Clonage du projet
```bash
git clone https://github.com/DZTic/SEA-2.4-Scappy.git
cd SEA-2.4-Scappy
```

### Étape 2 : Création de l'environnement virtuel
Il est fortement recommandé d'utiliser un environnement virtuel pour éviter les conflits de versions.
```bash
python3 -m venv venv
```

### Étape 3 : Installation des dépendances
Activez l'environnement et installez Scapy via le fichier `requirements.txt` :
```bash
source venv/bin/activate
pip install -r requirements.txt
deactivate
```

---

## 🛠️ Utilisation et Lancement

### La règle d'or du lancement
Pour que le script ait les droits root (**sudo**) tout en utilisant les bibliothèques installées dans l'environnement virtuel (**venv**), vous devez appeler l'interpréteur Python situé à l'intérieur du venv.

**Syntaxe générale :**
```bash
sudo venv/bin/python nom_du_script.py
```

### Exemples concrets par étape :

#### Étape 1 : Forge de paquets
```bash
cd step1_scapy_basics
sudo ../venv/bin/python basic_forge.py
```

#### Étape 3 : Manipulation de données
```bash
cd step3_python_manipulation
sudo ../venv/bin/python exercises.py
```

> **Note :** Si vous êtes à la racine du projet, la commande est simplement `sudo venv/bin/python step1_scapy_basics/basic_forge.py`.

---

## ❓ Résolution des problèmes (FAQ)

**Q : "Permission denied" ou "socket error"**
$\rightarrow$ Vous avez oublié d'utiliser `sudo`. Scapy ne peut pas accéder à la carte réseau sans droits administrateurs.

**Q : "ModuleNotFoundError: No module named 'scapy'"**
$\rightarrow$ Vous avez lancé le script avec le Python du système (`sudo python ...`) au lieu du Python du venv (`sudo venv/bin/python ...`).

**Q : "Commande introuvable"**
$\rightarrow$ Vérifiez que vous êtes dans le bon dossier et que le dossier `venv` a bien été créé à la racine du projet.
