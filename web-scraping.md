# Web Scraping Project - Data Scientists Job Listings

Using Python's 'requests' and 'BeautifulSoup' modules, I performed web scraping to extract job listings for the keyword **Data Scientist**. The scraped data was saved in JSON format.

## Steps Taken
1. Used robots.txt to ascertain whether I could even scrape the website legally. After checking various websites, I decided to use the Real Python fake jobs page.
2. Sent an HTTP request

## Steps Taken
1. Sent an HTTP request to the target website using `requests`.
2. Parsed HTML content using `BeautifulSoup`.
3. Extracted relevant data fields (job titles, companies, locations).
4. Saved the results into a JSON file for later analysis.

## Learning Outcomes Demonstrated
- **IT and Digital Skills:** Using Python libraries and understanding web protocols.
- **Problem Solving & Critical Thinking:** Extracted structured data from semi-structured HTML.
- **Numeracy & Data Handling:** Processed and stored extracted data in JSON format.

## Reflections
- This exercise taught me how to parse and extract relevant data from web pages.
- I gained practical experience with `requests`, `BeautifulSoup`, and JSON.
- A challenge was handling different HTML structures; I overcame it by inspecting elements carefully using browser developer tools.

## Artefacts
- [Python Script](web-scraping-code.py)  


## Code Used

from bs4 import BeautifulSoup
import requests
import json
# Base URL for Real Python jobs board
url = "https://realpython.github.io/fake-jobs/"
# Send request with a user agent header
headers = {"User-Agent": "Mozilla/5.0"}
response = requests.get(url, headers=headers)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")
    
    jobs = []
    
    # Each job post container
    job_cards = soup.find_all("div", class_="card-content")
    
    for card in job_cards:
        title_tag = card.find("h2", class_="title")
        company_tag = card.find("h3", class_="company")
        location_tag = card.find("p", class_="location")
        link_tag = card.find("a", string="Apply")
        
        title = title_tag.get_text(strip=True) if title_tag else "N/A"
        company = company_tag.get_text(strip=True) if company_tag else "N/A"
        location = location_tag.get_text(strip=True) if location_tag else "Remote / Unspecified"
        link = link_tag['href'] if link_tag else ""
        
        # Only keep jobs with "Data Scientist" in the title
        if "data scientist" in title.lower():
            jobs.append({
                "title": title,
                "company": company,
                "location": location,
                "link": link
            })
    
    # Save results to JSON
    with open("data_scientist_jobs.json", "w", encoding="utf-8") as f:
        json.dump(jobs, f, indent=4, ensure_ascii=False)
    
    print(f"Scraped {len(jobs)} 'Data Scientist' jobs and saved to data_scientist_jobs.json.")
else:
    print(f"Failed to retrieve jobs page. Status code: {response.status_code}")

This gave me the output: Scraped 1 'Data Scientist' jobs and saved to data_scientist_jobs.json.

with open("data_scientist_jobs.json", "r", encoding="utf-8") as f:
    data = json.load(f)

print(json.dumps(data, indent=4, ensure_ascii=False))

Giving me the final output, showing the only available Data Scientist job:
        "title": "Data scientist",
        "company": "Thomas Group",
        "location": "Port Robertfurt, AA",
        "link": "https://realpython.github.io/fake-jobs/jobs/data-scientist-26.html"
    }





