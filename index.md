## E-Portfolio of   

![My image](https://raw.githubusercontent.com/mmiz02/eportfolio/master/images/2.jpg)

# Monique Mizzi - Numerical Analysis       

## MSc. Data Science

---

### About Me

### [Professional](https://github.com/crypto61/eportfolio/blob/master/Professional.md)

### [Personal](https://github.com/crypto61/eportfolio/blob/master/Personal.md) 


### University of Essex Learning Experience

### University of Essex Learning Experience

* [Induction Module](https://github.com/crypto61/eportfolio/blob/master/Induction.md)

<details>
<summary><strong>Module 1: The Data Professional</strong></summary>
<ul>
  <li>
    <details>
      <summary>Lecture Notes</summary>
      <p>Insert your lecture notes here or link to them:  
      <a href="module-1/lecture-notes.md">View Notes</a></p>
    </details>
  </li>
  <li>
   <details>
  <summary>Week 2</summary>
  <p><strong>Crime Victimisation in the Last 12 Months – Summary of Findings</strong></p>

  <p>Using the Crime Survey for England and Wales, 2013–2014, I examined the variable <code>bcsvictim</code>, which indicates whether respondents experienced any crime in the 12 months prior to the survey.</p>

  <p><strong>Summary:</strong></p>
  <ul>
    <li>1,383 respondents (15.6%) reported experiencing a crime.</li>
    <li>7,460 respondents (84.4%) reported no crime experience.</li>
  </ul>

  <p><strong>R Code:</strong></p>

```r
install.packages("haven")
install.packages("dplyr")
install.packages("forcats")

library(haven)
library(dplyr)
library(forcats)

data <- read_sav("~/Downloads/R/UKDA-8011-spss/spss/spss24/csew1314teachingopen.sav")

table(data$bcsvictim)
prop.table(table(data$bcsvictim))

data$bcsvictim <- as_factor(data$bcsvictim)
table(data$bcsvictim)

    <details>
      <summary>Reflections</summary>
      <p>Add your reflections or link to a Markdown file.</p>
    </details>
  </li>
  <li>
    <details>
      <summary>Project</summary>
      <p>Describe your final project or link it:  
      <a href="module-1/project.md">View Project</a></p>
    </details>
  </li>
</ul>
</details>

<details>
<summary><strong>Module 2: Numerical Analysis</strong></summary>
<ul>
  <li>
    <details>
      <summary>Data Activity 1.1 and 1.2</summary>
      <p><a href="https://github.com/mmiz02/eportfolio/blob/master/module-1/data-activity-1.2.md">View Data Activity</a></p>
    </details>
  </li>
  <li>
    <details>
      <summary>Assignments</summary>
      <p><a href="module-2/assignments.md">View Assignments</a></p>
    </details>
  </li>
  <li>
    <details>
      <summary>Reflections</summary>
      <p>Write about what you learned or experienced during this module.</p>
    </details>
  </li>
  <li>
    <details>
      <summary>Project</summary>
      <p>Include your final analysis or link to your notebook/project repo.</p>
    </details>
  </li>
</ul>
</details>


---

---

Page template forked from [evanca](https://github.com/evanca/quick-portfolio)
