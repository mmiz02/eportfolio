Crime Victimisation in the Last 12 Months – Summary of Findings
Using the Crime Survey for England and Wales, 2013–2014: Unrestricted Access Teaching Dataset, I examined the variable bcsvictim, which indicates whether respondents experienced any crime in the 12 months prior to the survey.

After converting the variable from its original labelled format to a factor using haven::as_factor(), I produced a frequency table to explore responses:

1,383 respondents (15.6%) reported experiencing a crime.

7,460 respondents (84.4%) reported no crime experience.

These results suggest that the majority of survey respondents did not experience any crime in the previous year. The bcsvictim variable was successfully transformed into a factor variable to allow for clearer interpretation of the results.

install.packages("haven")      # For reading .sav files
install.packages("dplyr")      # For data manipulation
install.packages("forcats")    # For factor handling

library(haven)
library(dplyr)
library(forcats)

data <- read_sav("~/Downloads/R/UKDA-8011-spss/spss/spss24/csew1314teachingopen.sav")

> table(data$bcsvictim)

   0    1 
7460 1383 
> 
> prop.table(table(data$bcsvictim))

        0         1 
0.8436051 0.1563949 
> data$bcsvictim <- as_factor(data$bcsvictim)
> table(data$bcsvictim)

Not a victim of crime       Victim of crime 
                 7460                  1383 
