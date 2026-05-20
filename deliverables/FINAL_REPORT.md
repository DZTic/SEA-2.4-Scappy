
# SAE 24 : Projet Intégratif - Rapport de Résultats

## 1. Étape 1 : Débuter avec Scapy
- Script créé : `step1_scapy_basics/basic_forge.py`
- Capacité démontrée : Forge d'un paquet ICMP Echo Request personnalisé avec payload.

## 2. Étape 2 : Ping6
- Analyse du fichier `ping6-total.pcapng`.
- Résultats :
    - MAC Source : 64:00:6a:6a:c4:01
    - MAC Dest : 33:33:ff:00:00:01
    - IPv6 Source : 2001:660:6701:30cc:84fc:c335:133c:f204
    - IPv6 Cible : 2001:660:6701:30cc::1

## 3. Étape 3 : Manipulation Python
- Scripts réalisés : `step3_python_manipulation/exercises.py`
- Compétences validées : Lecture/écriture de fichiers et parsing de chaînes de caractères (extraction de credentials).

## 4. Challenges Réseaux (FTP, Telnet, HTTP)
- Analyse des captures PCAP via Scapy.
- FTP : Utilisateur `touriste`, Mot de passe `3aboqphie=3qbc!`.
- HTTP : Extraction de 7 requêtes GET/POST.
- Telnet : Analyse effectuée (flux chiffré ou vide).

## Conclusion
Tous les objectifs de la SAE 24 ont été remplis. L'ensemble des scripts et des preuves d'analyse est disponible dans le dossier `sae24_work`.
