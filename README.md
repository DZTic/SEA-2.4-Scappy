# 🛡️ SAE 24 : Projet Intégratif - Analyse Réseau avec Scapy

Ce projet, réalisé dans le cadre de la **SAE 204**, explore les mécanismes fondamentaux des réseaux informatiques à travers la manipulation et l'analyse de trafic. L'objectif est de passer de la théorie à la pratique en utilisant la bibliothèque **Scapy** pour interagir directement avec les couches du modèle OSI.

## 🛠️ Stack Technique
- **Langage :** Python 3.11+
- **Bibliothèque principale :** [Scapy](https://scapy.net/) (Manipulation de paquets, forge et sniffing)
- **Environnement :** Linux (indispensable pour l'accès aux raw sockets)

## 🎯 Objectifs Pédagogiques & Techniques
Le projet est conçu pour valider les compétences suivantes :
1. **Forge de Paquets (Packet Crafting) :** Maîtrise de l'empilement des couches (Layering) pour créer des paquets ICMP personnalisés.
2. **Analyse Forensics IPv6 :** Capacité à disséquer des captures réseau (`.pcapng`) pour identifier les adresses MAC et IPv6 source/destination.
3. **Parsing de Protocoles :** Développement de scripts d'automatisation pour extraire des données structurées à partir de flux bruts.
4. **Audit de Protocoles Non Sécurisés :** Analyse de la vulnérabilité des protocoles en clair (FTP, HTTP, Telnet) pour l'extraction d'identifiants.

## 📁 Architecture du Projet

| Dossier | Description Technique | Livrable Clé |
| :--- | :--- | :--- |
| `step1_scapy_basics/` | **Introduction à la forge.** Création de paquets ICMP Echo Request avec payload personnalisé. | `basic_forge.py` |
| `step2_ping6_analysis/` | **Analyse IPv6.** Extraction d'adresses MAC et IPv6 depuis des captures de trafic Ping6. | `analysis_results.txt` |
| `step3_python_manipulation/` | **Traitement de données.** Scripts de parsing pour l'extraction automatique de credentials. | `exercises.py` |
| `challenges_ftp_telnet_http/` | **Analyse de trafic.** Extraction de secrets (utilisateurs/mots de passe) via l'inspection de paquets FTP/HTTP. | `final_secrets.txt` |
| `deliverables/` | **Synthèse.** Rapport final détaillant la méthodologie et les résultats obtenus. | `FINAL_REPORT.md` |

--- 
👉 **Installation et Lancement :** Pour configurer l'environnement virtuel et exécuter les scripts, consultez le [GUIDE_INSTALLATION.md](./GUIDE_INSTALLATION.md).
