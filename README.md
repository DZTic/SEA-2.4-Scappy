# 🛡️ SAE 24 - Analyse Réseau avec Scapy

Ce projet s'inscrit dans le cadre de la **SAE 204** et se concentre sur la manipulation de paquets réseau, l'analyse de trafic IPv6 et le parsing de protocoles classiques (FTP, Telnet, HTTP) en utilisant la bibliothèque Python **Scapy**.

## 🎯 Objectifs du Projet
L'objectif est de comprendre le fonctionnement des couches réseau en pratiquant :
- La **forge de paquets** personnalisés.
- L'**analyse de captures** réseau (PCAP).
- L'**automatisation** du traitement de données réseau via Python.

## 📁 Structure du Projet

Le projet est organisé en trois étapes progressives :

- **`step1_scapy_basics/`** : Introduction à Scapy. Création et forge de paquets ICMP (Ping) personnalisés pour tester la connectivité et la structure des couches.
- **`step2_ping6_analysis/`** : Analyse spécifique du protocole IPv6. Étude des mécanismes de résolution et de communication IPv6.
- **`step3_python_manipulation/`** : Exercices de manipulation de fichiers et de chaînes de caractères, appliqués au parsing de logs de protocoles (extraction d'utilisateurs et de mots de passe).
- **`challenges_ftp_telnet_http/`** : Résultats des challenges de capture et d'analyse de protocoles non chiffrés.

## 🚀 Guide de Lancement

### 1. Prérequis
- **Système :** Linux (recommandé pour l'accès aux sockets brutes).
- **Privilèges :** Accès `sudo` (indispensable pour envoyer/capturer des paquets avec Scapy).
- **Python :** Version 3.11+.

### 2. Installation et Environnement
Le projet utilise un environnement virtuel pour isoler les dépendances.

```bash
# Activer l'environnement virtuel
source /home/vboxuser/sae24_env/bin/activate
```

### 3. Exécution des scripts
Tous les scripts manipulant le réseau doivent être lancés avec `sudo` en utilisant le chemin vers l'interpréteur de l'environnement virtuel.

**Forge de paquets (Étape 1) :**
```bash
cd step1_scapy_basics
sudo /home/vboxuser/sae24_env/bin/python basic_forge.py
```

**Exercices de manipulation (Étape 3) :**
```bash
cd step3_python_manipulation
sudo /home/vboxuser/sae24_env/bin/python exercises.py
```

## 🛠️ Fonctionnement Technique
Le projet repose sur **Scapy**, qui permet de :
1. **Empiler les couches :** `packet = IP(dst="...") / ICMP() / "Payload"`
2. **Inspecter les paquets :** Utilisation de `.show()` pour visualiser la structure détaillée.
3. **Analyser le trafic :** Lecture de fichiers `.pcap` pour extraire des informations sensibles (comme les identifiants FTP/Telnet).

---
*Livrables : Le rapport final se trouve dans le dossier `deliverables/FINAL_REPORT.md`.*
