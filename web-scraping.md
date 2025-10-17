# Web Scraping Project - Data Scientists Job Listings

Using Python's 'requests' and 'BeautifulSoup' modules, I performed web scraping to extract job listings for the keyword **Data Scientist**. The scraped data was saved in JSON format and the code I used can be found in the **Artefacts** section..

## Steps Taken
1. Used robots.txt to ascertain whether I could even scrape the website legally. After checking various websites, I decided to use the Real Python fake jobs page.
2. Used Python's 'requests' library to send a GET request to the website.
3. Used 'BeautifulSoup' to parse the HTML response.
4. Located each job post ontainer ('div.card-content') and extracted relevant tags.
5. Converted job titles to lowercase and selected only those containing "data scientist".
6. Stored the extracted jobs in a JSON file ('data_scientist_jobs.json') for easy retrieval and sharing.
7. Loaded the JSON file and printed it to check correctness.
8. Ensured all fields were correctly populated.

## Output
{
        "title": "Data scientist",
        "company": "Thomas Group",
        "location": "Port Robertfurt, AA",
        "link": "[https://realpython.github.io/fake-jobs/jobs/data-scientist-26.html]"(https://realpython.github.io/fake-jobs/jobs/data-scientist-26.html)

The script successfully found 1 Data Scientists job and saved it in JSON format.

## Learning Outcomes
- Used different Python libraries, gaining practical experience with 'requests', 'BeautifulSoup', and JSON. 
- Enhanced my understanding on parsing, extracting data from web pages, and web protocols.
- Extracted structured data from semi-structured HTML.
- Processed and stored extracted data in JSON format.

## Artefacts
- [Python Script](web-scraping-code.py)

  
[← Back to Home](../index.md)


## Reflections
- This exercise taught me how to parse and extract relevant data from web pages.
- I gained practical experience with `requests`, `BeautifulSoup`, and JSON.
- A challenge was handling different HTML structures; I overcame it by inspecting elements carefully using browser developer tools.






