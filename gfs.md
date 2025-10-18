# Back Up Procedure

## Aim
To critically evaluate the Grandfather-Father-Son (GFS) backup strategy and assess its effectiveness formanaging large datasets, focusing on efficiency, scalability, and recovrability compared to other backup methods.

## Critical Evaluation
The Grandfather-Father-Son (GFS) backup strategy is a hierarchical data backup method which saves data efficiently while minimising resource use. Data is backed up at three levels: daily ("son"), weekly ("father"), and monthly ("grandfather"). This offers frequent, short-term recovery points, making the data environment safer (Blocki, 2024). 

This easily understandable scheme allows the user to choose the number of backups needed at each level, meaning organisations can allocate resources as needed. It is highly scalable, accommodates large datasets, and can be extended with a yearly "great-grandfather" backup. Since multiple copies of data are created, it is very reliable and old data may be restored from any point in time across the three sets available (Blocki, 2024). 

However, compared to incremental or diffeential backup methods, GFS may have less storage efficiency since daily full backups can still accumulate, causing high operation costs and increased network bandwidth consumption. Overall, GFS balances efficiency and recoverability, making it effective for organisations managing large, evolving datasets (Blocki, 2024). 

## Reflection
Exploring GFS has strengthened my underestanding of hierarchichal backup systems and their role in disaster recovery. I learned how backup frequency and scalability impact both resource management and data security, and that different need to make trade-offs between cost, network bandwidth, srtorage efficiency, and data safety. This evaluation also reinforced the importance of planning backup systems thoughtfully for large, dynamic datasets.

## Skills Gained
- Better understanding of disaster recovery strategies and hierarchical backup structures,
- Ability to compare different backup methods

## References
Blocki, L. (2024) *Grandfather-father-son (GFS) backup: Storware blog*, Storware. Available at: https://storware.eu/blog/grandfather-father-son-gfs-backup/ (Accessed: 18 October 2025). 

[← Back to Home](https://mmiz02.github.io/eportfolio/)
