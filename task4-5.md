# UNICEF Dataset Cleaning & Automation

## Aim
To clean and prepare the UNICEF Multiple Cluster Survey (MICS) dataset (mn.csv) for analysis. The dataset contains survey responses with acronyms as headers, which need to be replaced with readable headers from mn_headers.csv. This process involved identifying missing headers, handling missing data, normalising values, and ensuring consistency.

The goal was also to create a reusable and partially automated workflow using Python for future similar datasets. This task was done in weeks 4 and 5 and the datasets were extracted directly from the textbook's Github repository instead of creating the data files myself from the UNICEF's website due to time constraints. The *pandas* method was used as this was easiest.

The code used can be found in the **Code** section below.

## Code
- [Python Script](task4-5.py)

## Automation
The Python scripts developed automated most of the data cleaning process:

- Header mapping: Acronyms in the headers in mn.csv were replaced with readable headers from mn_headers.csv.
- Data cleaning steps: String columns were trimmed, yes/no answers were normalised, numeric columns were converted, missing values were handle, and duplicate rows were removed.
- Unmatched column detection: Columns without mapping were automatically detected and their first 5 values were outputted to allow for manual inspection.
- Reusable functions: The cleaning steps were divided into functions that can be applied to other datasets in future with minimal modification.

## Output
The following was outputted:

```
Data loaded. Total columns: 159
Matched columns: 150
Unmatched columns: 9
Unmatched columns detected:
  Unnamed: 0: ['1', '2', '3', '4', '5']
  MDV1F: ['No', 'Yes', 'DK', 'Missing']
  MTA8E: ['Rolled tobacco']
  mwelevel: ['Higher', 'Primary', 'Secondary', 'None']
  mnweight: ['0.403797141860459', '1.03192602919895', '0', '1.34530895870472', '0.937422731863394']
  wscoreu: ['1.27255184167736', '1.08902631982422', '-0.930720561098312', '0', '-1.79318301717754']
  windex5u: ['5', '1', '0', '4', '2']
  wscorer: ['0', '-0.228568613043929', '0.52313044941239', '0.212630095316783', '-0.336835758707082']
  windex5r: ['0', '3', '5', '4', '2']

Intermediate cleaned CSV saved as mn_clean_intermediate.csv
```

From the above, I could deduce what some of the unmatched columns were. 'Unnamed' was probably an index, 'mwelevel' was educational level. However, further inspecton is required to be certain.

The clean version of mn.csv may be viewed [here](mn_clean_intermediate.csv).

## Conclusion
The workflow is partially automated. Most of the manual effort required for data cleaning has been reduced but human oversight is required where mappings are missing. With minor enhancements, such as automatic detection of numeric/categorical columns and placeholder headers for unmatched columns, this workflow could be applied to future UNICEF datasets.

## Skills gained
- Python data wrangling with pandas,
- Data cleaning practices,
- Automation - writing reusable functions and designing a pipeline applicable to future datasets,
- Fuzzy string matching,
- Critical thinking in data quality - deciding how to handle missing data while maintaining integrity of the dataset.

## Reflection
Working on this task allowed me to work with real-world survey data. While these datasets were structured, the use of acronyms and missing headers highlighted the need for careful inspection and flexible cleaning workflows. I learned how to automate workflows, handle inconsistent or missing data, and map raw data to readable form.

Overall, this task strengthened my skills in Python and my critical thinking abilities.
  
[← Back to Home](https://mmiz02.github.io/eportfolio/)


