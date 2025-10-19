# Reflective Essay

This reflection uses Gibbs’ Reflective Cycle (1988) and Rolfe et al.’s (2001) structure to analyse my learning experience throughout this module. The aim is to explore how I developed both technically and professionally, reflecting on challenges, successes, and areas for further development.

I engaged in a variety of tasks and projects, from collaborative discussions and data cleaning to database design and API security. Key activities include:
-	Collaborative discussions on the Internet of Things (IoT) and GDPR compliance where I critically evaluated large-scale data collection, privacy risks, and regulatory requirement.
-	Web scraping task to extract job listings and manipulate JSON data using Python, enhancing my ability to work with semi-structured datasets.
```
{
        "title": "Data scientist", <br />
        "company": "Thomas Group", <br />
        "location": "Port Robertfurt, AA", <br />
        "link": "[](https://realpython.github.io/fake-jobs/jobs/data-scientist-26.html)"}
```
*Figure 1: 1 Job listing found after web scraping task was successful.*
-	Cleaning and automating UNICEF survey datasets with *pandas*, applying data wrangling techniques such as mapping headers, handling missing values, and creating reusable functions.
-	Collaboration to propose a clinical trial database solution involving relational modelling, database normalisation, and cloud hosting evaluation.
![](/Images/Fig2.png)
*Figure 2: Entity–Relationship Diagram of the Clinical Trial Database our team proposed showing links between tables using primary and foreign keys.*
-	Normalisation (3NF) of a flat table, turning it into a relational database.
-	Specification of security risks and mitigations for IPstack data.
-	Executive summary writing for the database solution proposed in a team, translating technical details into a client proposal.
-	Evaluation of the Grandfather-Father-Son backup approach, with comparisons to other strategies.

Through these tasks, I gained well-rounded technical understanding of coding, data and project management, and compliance.

At the beginning of the module, I felt both excitement and apprehension. I had good knowledge of Python but had only used SQL a few times, and applying these to large datasets, databases, and real-world API security challenges felt daunting. Collaborative discussions also intimidated me, as I was unsure if I was contributing meaningfully or not. Additionally balancing module tasks with full-time employment required careful planning.

One success I was proud of was that whilst previously I had not managed to develop my e-portfolio due to time constraints, this module, I placed a strong emphasis on time management and managed to document my learning journey. 

![](/Images/epor.png)
*Figure 3: Snippet of my e-portfolio showing progress in my time-management, documentation, and GitHub skills.*

As the module progressed, I started gaining more confidence in handling technical tasks. Successfully implementing a relational database using MySQL gave me a sense of accomplishment. This task reinforced my understanding of normalisation principles. Completing the API security exercise independently strengthened my problem-solving skills, while the executive summary task challenged me to appeal to a new audience while translating complex technical concepts into easily understandable jargon.
```
{'ip': '134.201.250.155', 'type': 'ipv4', 'continent_code': 'NA', 'continent_name': 'North America', 'country_code': 'US', 'country_name': 'United States', 'region_code': 'CA', 'region_name': 'California', 'city': 'Huntington Beach', 'zip': '92647', 'latitude': 33.70962142944336, 'longitude': -117.99259185791016, 'msa': '31100', 'dma': '803', 'radius': '0', 'ip_routing_type': 'fixed', 'connection_type': 'tx', 'location': {'geoname_id': 5358705, 'capital': 'Washington D.C.', 'languages': [{'code': 'en', 'name': 'English', 'native': 'English'}], 'country_flag': 'https://assets.ipstack.com/flags/us.svg', 'country_flag_emoji': '🇺🇸', 'country_flag_emoji_unicode': 'U+1F1FA U+1F1F8', 'calling_code': '1', 'is_eu': False}}
```
*Figure 4: Output from API security task, demonstrating ability to extract and interpret geolocation data securely.*

Overall, the module provided a highly practical learning experience, with a myriad of hands-on-tasks that reinforced theoretical concepts. Practical exercises, such as dataset cleaning and database building, allowed me to apply knowledge directly. Collaborative tasks such as the clinical trial database project improved my teamwork and communication. The reflection sections in my e-portfolio encouraged me to evaluate my learning, helping me identify areas for improvement. Moreover, exposure to diverse tools including Python, SQL, and GitHub, amongst others, broadened my technical competence.

Even though I am happier with my progress this module and I managed to develop my e-portfolio, time management was a recurring challenge. At times, I struggled to balance coding, documentation, and reflection tasks, which may have led to inconsistencies in my e-portfolio entries. Such time limitations occasionally prevented me from exploring tasks to their full potential,limiting their refinement and my opportunity for deeper analysis.

Additionally, I joined later than ideal in the second collaborative discussion which meant that only one peer responded to me, which limited the perspective and understanding I could gain. Similarly, if I had the time to engage with peers for the API security exercises, I could have consolidated my knowledge better. Improving my time management would likely have enhanced my knowledge and the presentation of my work.

Another area I believed I lacked in was my communication in the executive summary, as I think my language could have been more concise and business focused. Also, the documentation of tasks could have been more systemic to track my learning progression better and facilitate reflection.

Reflecting on my experiences, I realise that the combination of technical and reflective activities strengthened multiple competencies. For instance, the IoT discussion highlighted the intersection of technology, ethics, and governance. Engaging with peers deepened my understanding of data privacy, GDPR compliance, and emerging practices like edge computing. In one instance, a peer corrected a statement of mine which I had made based on outdated sources, which emphasised the importance of verifying information and using the most recent sources.

The UNICEF dataset cleaning project reinforced the value of reproducibility. By creating functions for header mapping, missing value handling, and data normalisation, I learned how to design scalable workflows, minimising manual effort. This skill directly translates to my professional life, where handling environmental and regulatory datasets efficiently is essential.
```
    # Example normalization for yes/no columns
    df = normalize_yes_no(df, yes_no_cols=['Ever Smoked'])  # update as needed

    # Remove duplicates
    df = remove_duplicates(df)
```
*Figure 5: Calling functions I had already defined, automating workflows.*

Testing referential integrity in MySQL highlighted how relational design prevents data inconsistencies and errors. Through the database team project, I enhanced my decision-making and analytical skills in order to propose a good DBMS solution. Finally, the executive summary writing was a good introduction in audience-focused communication. Attempting to translate technical language into understandable, business jargon taught me about the gap between technical execution and stakeholder understanding. This skill is highly relevant to professional practice, and I am hopeful to be able to bridge this gap in future.

This module had a profound impact on my development in a variety of ways. Technically, I gained practical experience in Python, SQL, GitHub, cloud hosting, and database design. Professionally, I developed skills in teamwork, communication, and documentation, Personally, I improved my reflective practice, time management skills, and confidence in independent problem-solving.

Looking forward I plan to:
1.	Enhance documentation, reflection, and e-portfolio practices,
2.	Engage more actively in collaborative discussions,
3.	Improve communication skills, taking the audience into consideration,
4.	Strengthen technical fluency in Python, SQL, and GitHub use,
5.	Apply learning to professional context.

In conclusion, this module was a highly valuable practical learning experience, combining technical skill development with reflection. While there are areas for improvement, I am motivated to build on the knowledge gained and continue developing my technical and professional capabilities.

## References

Gibbs, G. (1988), *Learning by doing: A guide to teaching and learning methods*, Further
Education Unit, London

Rolfe, G., Freshwater, D. and Jasper, M. (2001) *Critical reflection for nursing and the helping
professions: A user’s guide*. Houndmills, Basingstoke, Hampshire: Palgrave.

[← Back to Home](https://mmiz02.github.io/eportfolio/)
