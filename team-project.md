# Team Project: Clinical Trial Database Report

## Aim
To collaboratively design and document a secure, scalable, and compliant database solution for a global clinical research organisation conducting clinical trials.




# Team Project: Clinical Research Database Design Report

## Aim
To collaboratively design and document a secure, scalable, and compliant **database solution** for a global clinical research organisation conducting clinical trials. The objective was to demonstrate the ability to design logical and physical database components while meeting **GDPR** and international compliance standards.

---

## Project Overview
Our team, acting as **Software Consultants and Developers**, was contracted to design a database capable of storing, managing, and analysing sensitive clinical and personal data. The solution needed to ensure data integrity, auditability, and compliance with international regulations, while enabling role-based access for multiple stakeholders (trial staff, sponsors, regulators, and data analysts).

We adopted **PostgreSQL** as our database management system, supported by **AWS RDS** for hosting and **AWS S3** for unstructured data such as medical images. The system was designed around a structured data management pipeline (Figure 1) and an entity–relationship model (Figure 2), which ensured relational integrity, normalisation (3NF), and secure data flows.

---

## Logical Design and Data Management Pipeline
Our proposed pipeline included:

1. **Data Capture:** Structured data entry through electronic data capture systems, validated with standardised forms and dropdown menus.  
2. **Validation:** Mandatory field enforcement, range checks, and standardised medical terminologies to minimise entry errors.  
3. **Cleaning:** Automated logic queries to flag anomalies, machine learning for pattern detection, and traceable audit logs.  
4. **Storage:** PostgreSQL database ensuring integrity and referential consistency with encryption at rest and in transit.  
5. **Retrieval:** Controlled role-based access enabling clean, validated data retrieval for analysis, monitoring, and auditing.

> Figures and diagrams (ERD, data flow pipeline) can be embedded here as screenshots or `.png` files stored in your repository:
> ```markdown
> ![Figure 1 – Data Management Pipeline](../assets/data-pipeline.png)
> ![Figure 2 – Entity–Relationship Diagram](../assets/erd.png)
> ```

---

## Database Management System (DBMS) Selection
PostgreSQL was selected due to its:
- Open-source flexibility and cost-effectiveness.
- Support for **JSONB** and mixed data (structured and semi-structured).
- Strong auditing, encryption, and regulatory compliance features.
- Compatibility with cloud-based hosting such as **AWS RDS**, which offers automatic backups and GDPR-aligned compliance.

Alternatives such as Microsoft SQL Server and NoSQL databases were evaluated but found less suitable due to vendor dependency and limited relational integrity.

---

## Hosting Solution
After comparing **AWS**, **Azure**, and **Google Cloud**, our team selected **AWS RDS for PostgreSQL** due to its:
- Strong adoption within the clinical research sector.
- Scalability, encryption, and automated backup capabilities.
- Integration with AWS S3 for secure unstructured data storage.

---

## My Individual Contributions
Within the team, I focused on:
- Leading the **data validation and cleaning** framework design.
- Drafting the **data pipeline** documentation and ensuring alignment with GDPR compliance requirements.
- Implementing **audit trail** logic and data access control specifications.
- Contributing to the ERD structure and entity definitions (Participants, Clinical Trials, Visits, and Medical History).

I also consolidated and proofread the final technical sections to ensure academic tone and formatting consistency before submission.

---

## Meeting Minutes and Collaboration
To ensure effective collaboration, we held regular meetings on Microsoft Teams and documented key actions and progress.

**Excerpt from Meeting Minutes (Week 4):**
| Date | Discussion Points | Actions Agreed | Responsible |
|------|-------------------|----------------|-------------|
| 02 Oct 2025 | Decided on project topic (Clinical Trials Database) | Create ERD draft | Me & Sam |
| 05 Oct 2025 | Data cleaning strategy | Research audit trail standards | Me |
| 08 Oct 2025 | DBMS selection | Compare PostgreSQL vs. SQL Server | Alex |
| 12 Oct 2025 | Hosting options | Review AWS RDS documentation | Whole team |

We collaborated using shared Google Docs and GitHub for version control. This improved transparency, traceability, and accountability.

---

## Feedback and Reflection
Feedback from the **Unit 5 lecturecast discussion** suggested strengthening our database justification with industry-based hosting rationale. Incorporating this led to the **AWS hosting section** and a better understanding of feasibility considerations.

Through this project, I learned how **theoretical database design** translates into **real-world constraints**, such as compliance, security, and team communication challenges in distributed settings.

---

## Skills Developed
- Database design and relational modelling (ERD, 3NF)
- Data pipeline design and validation techniques
- Technical writing and documentation
- Team communication and collaboration using remote tools
- Critical analysis and compliance-based reasoning

---

## References
Amazon Web Services (2025). *Amazon RDS for PostgreSQL – Features.* Available at: [https://aws.amazon.com/rds/postgresql/](https://aws.amazon.com/rds/postgresql/)  
European Medicines Agency (2023). *Guideline on computerised systems and electronic data in clinical trials (EMA/INS/GCP/112288/2023).* EMA, Amsterdam.  
European Union (2016). *Regulation (EU) 2016/679 of the European Parliament and of the Council of 27 April 2016 (GDPR).* Available at: [https://eur-lex.europa.eu/eli/reg/2016/679/oj](https://eur-lex.europa.eu/eli/reg/2016/679/oj)  
Google Cloud (2025). *Cloud SQL for PostgreSQL.* Available at: [https://cloud.google.com/sql/postgresql](https://cloud.google.com/sql/postgresql)  
Microsoft (2025). *Azure Database for PostgreSQL – Documentation.* Available at: [https://learn.microsoft.com/en-us/azure/postgresql/](https://learn.microsoft.com/en-us/azure/postgresql/)  
Sarkar, T. & Roychowdhury, S. (2019). *Data Wrangling with Python: Creating Actionable Data from Raw Sources.* Packt Publishing.  
Sethi, S. & Panda, S. (2024). SQL or NoSQL—Practical Aspect and Rational behind Choosing Data Stores. *Journal of Computer and Communications*, 12, 1–20.  
Weissler, E. H. et al. (2021). *The role of machine learning in clinical research.* *Trials*, 22(1), 537.  
Williams, G. (2025). *Deciphering Big Data* [module materials]. University of Essex Online.
