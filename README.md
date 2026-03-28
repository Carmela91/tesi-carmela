# tesi-carmela
### Title 
LLMs for Dark Web OSINT: An Ethical and Methodological Framework to Support Threat Intelligence

##  Thesis Structure
 
### 1.Introdution
- Motivation  
- Research Problem  
- Thesis Statement  
- Contributions  
- Structure of the Thesis  

### 2. Background
- OSINT Methodologies  
- Dark Web and TOR Ecosystem  
- Large Language Models  
- Dark Web Marketplaces  
- Ethical Hacking and Legal Considerations  

### 3. Related Work
- Dark Web Intelligence Research  
- TOR Crawling and CRATOR  
- Threat Actor Communication Studies  
- LLMs in Cybersecurity  
- Research Gaps  

### 4. Ethical Dark Web Monitoring Methodology
- Ethical and Legal Constraints  
- Technical Environment (Kali Linux, Tor Browser, VM Isolation, OpSec)  
- Passive Data Collection Strategy  
- Room Identification and Documentation  
- Experimental Methodology Overview  

### 5. Dataset Selection and Processing
- Selection Criteria (HiddenLayer guidelines)  
- Chosen Dataset: Qualifire Prompt Injection Benchmark  
- Dataset Structure and Labeling  
- Preprocessing Pipeline  
- Limitations  

### 6. Dark Web Marketplace Analysis
- Selected Marketplace: Cocorico Market (via CRATOR)  
- Marketplace Structure  
- Identified Rooms (categories, vendor pages, product pages)  
- Non‑sensitive HTML Structural Analysis  
- Threat Actor Behavioral Patterns  
- Comparison with OSINT Reports  

### 7. Dark Web Room Database
- Database Schema  
- Fields and Metadata  
- Documented Room Entries (20–30 rooms)  
- Category Classification  
- Insights and Observations  

### 8. Experimental Analysis
- Quantitative Analysis of the Dataset  
- Qualitative Analysis of Attack Patterns  
- Correlation: Dark Web Linguistic Patterns vs. LLM Risk‑Related Patterns  
- Threat Intelligence Interpretation  
- Integrated Discussion of Findings  

### 9. Ethical and Practical Implications
- Ethical Implications  
- Strengths and Limitations  
- Real‑World Relevance  
- Implications for Enterprise LLM Security  

### 10. Conclusion and Future Work
- Summary of Findings  
- Contributions  
- Future Research Directions  
- Professional Applications

## Repository Structure (to be filled as work progresses)

## Dataset Selection & Processing

### Dataset Selection
Il dataset utilizzato per questa analisi è stato selezionato seguendo i criteri proposti da HiddenLayer per la valutazione dei dataset di prompt injection. I criteri principali considerati sono stati:

- presenza di esempi realistici di attacchi linguistici (jailbreak, prompt injection, manipolazioni semantiche)
- distinzione chiara tra prompt benigni e malevoli
- struttura semplice e facilmente preprocessabile
- dimensione sufficiente per analisi statistiche e qualitative
- riproducibilità del processo di analisi

Il dataset originale, così come ottenuto dalla fonte, è disponibile nella cartella:
data/raw/test.csv


### Preprocessing Pipeline
Il dataset grezzo presentava alcune criticità comuni nei dataset non standardizzati:

- encoding non uniforme
- separatori non dichiarati
- colonne non etichettate
- presenza di dati sensibili (nomi, email, numeri)
- duplicati e valori mancanti

Per affrontare questi problemi è stato sviluppato uno script di preprocessing dedicato (`src/preprocessing.py`) che esegue automaticamente:

1. rilevamento del separatore (`;`, `,`, `\t`) e dell’encoding (`utf-8`, `utf-8-sig`, `cp1252`, `latin-1`)
2. normalizzazione dei nomi delle colonne
3. rimozione di duplicati e valori mancanti
4. anonimizzazione di nomi propri, email e numeri sensibili
5. salvataggio del dataset pulito e strutturato

La versione preprocessata e anonimizzata del dataset è disponibile in:
data/processed/test_anonymized.csv


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

Gli script utilizzati per il caricamento, il preprocessing e l’analisi sono disponibili nella cartella:
src/



