# tesi-carmela
LLMs for Dark Web OSINT: An Ethical and Methodological Framework to Support Threat Intelligence

##  Thesis Structure

### 1. Introduction
- Motivation  
- Research Problem  
- Thesis Statement  
- Contributions
- Structure of the Thesis   

### 2. Background
- OSINT methodologies 
- Dark Web and TOR Ecosystem
- Large Language Models   
- Dark Web Marketplaces  
- Ethical Hacking & Legal Considerations 
  

### 3. Related Work
- Dark Web Intelligence Research  
- TOR Crawling and CRATOR  
- Threat Actor Communication Studies  
- LLMs in Cybersecurity  
- Research gaps  

### 4. Ethical Dark Web Monitoring Methodology
- Ethical and legal constraints   
- Technical environment (Kali Linux, Tor Browser, VM isolation,OpSec)  
- Passive Data Collection Strategy  
- Room Identification and Documentation  
- Experimental Methodology Oterview  

### 5. Dataset Selection and Processing
- Selection criteria (from HiddenLayer)  
- Chosen dataset: Qualifire Prompt Injection Benchmark  
- Dataset structure and labeling  
- Preprocessing pipeline  
- Limitations  

### 6. Dark Web Marketplace Analysis
- Marketplace selected: Cocorico Market (CRATOR)  
- Marketplace structure  
- Identified rooms (categories, vendor pages, product pages)  
- HTML structural analysis (non‑sensitive)  
- Threat actor behavior patterns  
- Comparison with OSINT reports  

### 7. Dark Web Room Database
- Database schema  
- Fields and metadata  
- Room entries (20–30 documented rooms)  
- Category classification  
- Insights  

### 8. Experimental Analysis
- Quantitative analysis of the dataset  
- Qualitative analysis of attack patterns  
- Correlation: dark web linguistic patterns vs LLM risk‑related patterns  
- Threat intelligence interpretation  
- Discussion  

### 9. Discussion
- Ethical implications  
- Strengths and limitations  
- Real‑world relevance  
- Implications for enterprise LLM security  

### 10. Conclusion and Future Work
- Summary  
- Contributions  
- Future research  
- Professional applications  

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



