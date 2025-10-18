# Executive Summary - Design and Build of a Secure, Scalable, and Compliant Clinical Trial Database

## Aim
To write an executive summary on the design and build of the database system proposed for managing global clinical trial data in the team report of Unit 6. Unlike the team project which was a collaorative technical exercise, this summary presents an individual analysis which proposed the database solution in a concise, user-friendly format.

## Overview
The proposed system supports a global clinical trials organisation which manages sensitive data, including patien demographics, medical images, and trial outcomes. It must comply with GDPR (European Union, 2016) and other global standards to ensure traceability, transparency, and protection of patient rights.

The key requirements were:
- **Security** - encryption, pseudonymisation, and auditability
- **Scalability** - capable of handling large data volumes with mixed formats from global sources, which will probably grow in future
- **Compliance** - meeting strict GDPR and regulatory standards
- **Usability** - allowing authorised stakeholders secure and validated access to data

## Data Management Pipeline
The project followed a structured pipeline to safeguard data integrity, minimise error, and ensure regulatory compliance (Figure 1).

![Figure1](/images/Fig1.png)
*Figure 1: Data Management Pipeline (Developed by the team based on Williams, 2025; European Union, 2016; EMA, 2023).*

The pipeline included:
- **Data Capture:** Via electronic data capture systems, maintaining input accuracy through validation rules (Martin, 2023).
- **Validation & Cleaning:** Use of mandatory fields, range checks, and full audit trails (Data validation, 2024).
- **Storage & Retrieval:** Structure data is stored in PostgreSQL, unstructured data stored securely in managed cloud storage (Ali, 2024).

Patient identifiers were pseudonymised using separate identifiers to maintain privacy while preserving traceability (European Commission, 2021).

## Database Modelling Concepts
A relational model was designed to show how clinical trial entities connect such as participants, visits, and procedures. The Entity Relationship Diagram can be seen below (Figure 2).

![Figure2](/images/Fig2.png)
*Figure 2 – Entity–Relationship Diagram (ERD) – Clinical Trial Database (Developed by the team; compliance considerations refereced from EMA, 2023; Sarkar & Roychowdhury, 2019).*

Key entities included:
- Trial Participant; subject information (ID, name, etc.).
- Clinical Trial, Trial Centers; trial-level details and trial site details.
- Principal Investigator; records the lead investigator for each site.
- Visits; participant trial visit details.
- Medical Procedures; details of medical tests or procedures done at each visit, capturing lab result.
- Medication; stores information about drugs used in the trial.
- Dose; records dosage of medication administered to participant.
- Adverse Event; stores side effects which may occur during the trial.
- Medical History ; stores participants pre-existing medical conditions.
- Medical Images; stores metadata of available medical images and links to external cloud storage site where image is held.

## Database Management System (DBMS) Selection
PostgreSQL, Microsoft SQL Server, and NoSQL were compare, from which PostgreSQL was chosen for its reliability, security, and compliance. It was also more cost-effective thn Microsoft SQL Server, which would have been more expensive and led to vendor-depenency. NoSQL would have been more suitable for unstructured data but it  had reduced compliance and auditability.

## Hosting Solution
Amazon Web Services (AWS) was chosen as it provided automated backups, global data-storing centers, and GDPR compliance (AWS, 2025). It also offered storage options (S3) for unstructured data and is widely used for clinical research.

## Legal, Ethical, and Compliance Considerations

 - Key GDPR principles such as data minimisation, consent, right to erasure, data portability, and secure transfer between systems had to be taken into account (European Comission, 2021).
 - Role based access and clear audit trails were implemented (EMA, 2023).
 - Archiving and decommissioning of database were considered (which were not taken into account in the team project), certifying long-term storage for at least 25 years (Adams, 2025; EMA, 2023).

## Findings and Analysis
The proposed system successfully:
- Met client needs,
- Ensured data quality and compliance,
- Balanced flexibility and control,
- Ensured scalability and validated access.

## Remaining Challenges
My summary shows that relational databases are ideal for structured data, however they are less suited for unstructured data like medical images. This limitation highlights the need for potential NoSQL integration in future (Ali, 2022). Moreover, AWS may show scaling limitations in future and the strict compliance adherence may increase system workload.

## Conclusion and Recommendations
The relational design delivered a compliant and secure solution tailored to global clinical trials. 

Recommendations include providing training to users on data validation processes, to establish a compliance monitoring team to track evolving regulations, and to explore NoSQL integration for unstructured data.

## Comparison to Team Project
The database solution was elaborated further in the executive summary which is contradictory since a summary is supposed to be shorter and more concise, however the word limit was double that of the team project. This was because the assignment required reflection on design choices and deeper explanation for the potential client. 

In contrast to the team project, less technical jargon was used such as coding structure, and I concentrated on translating technical elements into a business and compliance-oriented narrative which would be more understandable for the client with a better appeal. The goal was to explain why design decisions were made and how they aligned with the client's requirements.

## Reflection
The process of converting a technical report into an executive summary allowed me to learn a new communication and writing style, taking into consideration a new audience, and translating technical jargon into easily understandable concepts.

While I tried my best to tailor the summary to this particular audience, my language and structure could be improved as they might have been too technical and complex for an executive summary. I also found it difficult to balance technical accuracy with accessibility and to explain business impact, an area fairly new to me.

In future reports, I plan to use simpler language and focus more on appealing to business-minded clients.

## References

Adams, B. (2025) *Regulatory compliance in the Global Clinical Research Evolution*, Florence. Available at: https://www.florencehc.com/blog-post/regulatory-compliance-in-the-global-clinical-research-evolution/ (Accessed: 10 September 2025). 

Ali, M. (2022) *Relational database vs. Non-Relational Database*, LogicMonitor. Available at: https://www.logicmonitor.com/blog/relational-database-vs-non-relational-database (Accessed: 10 September 2025). 

Ali, M. (2024) *What is Postgresql? How it works, use cases, and resources*, Datacamp. Available at: https://www.datacamp.com/blog/what-is-postgresql-introduction (Accessed: 10 September 2025). 

Amazon Web Services (2025). *Amazon RDS for PostgreSQL – Features*. Available at: https://aws.amazon.com/rds/postgresql/ (Accessed: 1 September 2025)

*Data validation in clinical data management* (2024) Quanticate. Available at: https://www.quanticate.com/blog/data-validation-in-clinical-data-management (Accessed: 10 September 2025). 

European Commission. (2021) *Data Protection Aspects of Clinical Trials*. Available at: https://health.ec.europa.eu/document/download/f7be57c2-f40b-45cd-b0e9-b9d00f1234f9_en.

European Medicines Agency (2023). *Guideline on computerised systems and electronic data in clinical trials (EMA/INS/GCP/112288/2023)*. EMA, Amsterdam. Available at: chrome-extension://efaidnbmnnnibpcajpcglclefindmkaj/https://www.ema.europa.eu/en/documents/regulatory-procedural-guideline/guideline-computerised-systems-and-electronic-data-clinical-trials_en.pdf

European Union (2016) *Regulation (EU) 2016/679 of the European Parliament and of the Council of 27 April 2016 on the protection of natural persons with regard to the processing of personal data and on the free movement of such data (General Data Protection Regulation).* Official Journal of the European Union, L119, 1-88. Available at: https://eur-lex.europa.eu/eli/reg/2016/679/oj (Accessed: 1 September 2025)

Martin, M. (2023) *What is an EDC system and how does IT support clinical trials?*, NAMSA. Available at: https://namsa.com/resources/blog/what-is-electronic-data-capture-in-clinical-trials/ (Accessed: 10 September 2025). 

Sarkar, T. & Roychowdhury, S. (2019) *Data Wrangling with Python: creating actionable data from raw sources.* 1st edition. Birmingham; Packt Publishing Ltd.
    
Williams, G. (2025) *Deciphering Big Data [module materials].* University of Essex Online, July- October.


[← Back to Home](https://mmiz02.github.io/eportfolio/)
