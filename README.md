# tesi-carmela
### Title 
LLMs for Dark Web OSINT: An Ethical and Methodological Framework to Support Threat Intelligence

##  Thesis Structure
 
### .Introdution
- Motivation  
- Research Problem  
- Thesis Statement  
- Contributions  
- Structure of the Thesis  

### 1. Background
- OSINT Methodologies  
- Dark Web and TOR Ecosystem  
- Large Language Models  
- Dark Web Marketplaces  
- Ethical Hacking and Legal Considerations  

### 2. Related Work
- Dark Web Intelligence Research  
- TOR Crawling and CRATOR  
- Threat Actor Communication Studies  
- LLMs in Cybersecurity  
- Research Gaps  

### 3. Ethical Dark Web Monitoring Methodology
- Ethical and Legal Constraints  
- Technical Environment (Kali Linux, Tor Browser, VM Isolation, OpSec)  
- Passive Data Collection Strategy  
- Room Identification and Documentation  
- Experimental Methodology Overview  

### 4.Dataset Selection and Processing
4.1 Source Dataset: CRATOR Structural Extraction  
4.2 Dataset Scope and Rationale  
4.3 Dataset Organization  
4.4 Selection of the 100-Room Experimental Subset  
4.5 Preprocessing for Rule-Based Analysis  
4.6 Preprocessing for LLM-Based Evaluation  
4.7 Dataset Integrity and Reproducibility

### 5. Dark Web Marketplace Analysis
-5.1 Overview of the Eight-Target Dataset  
5.2 Initial Raw Dataset (16,000 Files)  
5.3 Normalization and Filtering (7,241 Files)  
5.4 Construction of the 1,500-File Subset  
5.5 Marketplace and Forum Structures  
5.6 Non‑Sensitive Structural Patterns  
5.7 Behavioral Patterns (Structural Only)  
5.8 Alignment with OSINT Reports
  
### 6. Dark Web Room Database
- Database Schema  
- Fields and Metadata  
- Documented Room Entries (20–30 rooms)  
- Category Classification  
- Insights and Observations  

### 7. Experimental Analysis
- Quantitative Analysis of the Dataset  
- Qualitative Analysis of Attack Patterns  
- Correlation: Dark Web Linguistic Patterns vs. LLM Risk‑Related Patterns  
- Threat Intelligence Interpretation  
- Integrated Discussion of Findings  

### 8. Ethical and Practical Implications
- Ethical Implications  
- Strengths and Limitations  
- Real‑World Relevance  
- Implications for Enterprise LLM Security  

### 9. Conclusion and Future Work
- Summary of Findings  
- Contributions  
- Future Research Directions  
- Professional Applications

### Analysis Workflow
L’analisi del dataset seguirà una pipeline strutturata in più fasi:

1. **Caricamento del dataset preprocessato**  
   Utilizzando gli script presenti in `src/`.

2. **Esplorazione statistica**  
   - distribuzione delle label  
   - lunghezza media dei prompt  
   - rilevamento di pattern ricorrenti  
   - analisi dei duplicati  

3. **Analisi linguistica**  
   - identificazione di marker linguistici tipici dei jailbreak  
   - classificazione delle tecniche di manipolazione  
   - confronto con i pattern osservati nel dark web  

4. **Correlazione con i contenuti del dark web**  
   - confronto tra pattern linguistici  
   - individuazione di similarità strutturali  
   - analisi qualitativa delle room del marketplace  

5. **Risultati e visualizzazioni**  
   - grafici, statistiche e osservazioni finali  
   - implicazioni per la sicurezza degli LLM  


### Abstract

Questa tesi esplora l’impiego etico dei Large Language Models (LLM) come strumenti di supporto nell’analisi strutturale e linguistica dei marketplace del dark web. Il lavoro si basa su una metodologia di raccolta dati passiva, condotta in ambiente isolato e nel rispetto di rigorose misure di sicurezza operativa. La fase di acquisizione utilizza CRATOR, un crawler accademico progettato per l’analisi etica dei marketplace del dark web, che consente di estrarre esclusivamente la struttura HTML e i metadati non sensibili delle room.

I dati raccolti vengono organizzati in un dataset strutturale e linguistico costruito appositamente per questa ricerca e memorizzato in un database MySQL. L’analisi si fonda sull’impiego degli LLM come valutatori semantici, seguendo i principi delineati nella letteratura recente sul paradigma “LLM-as-a-Judge”. I modelli vengono utilizzati per classificare le room, identificare ricorrenze linguistiche, sintetizzare pattern descrittivi e supportare l’interpretazione qualitativa delle dinamiche interne dei marketplace.

I risultati mostrano che gli LLM possono contribuire in modo efficace e controllato all’analisi OSINT del dark web, pur richiedendo attenzione ai limiti metodologici, alla variabilità dei modelli e alla necessità di supervisione umana. Il lavoro propone infine un quadro metodologico replicabile per l’impiego responsabile degli LLM nell’analisi strutturale e linguistica dei marketplace del dark web.

