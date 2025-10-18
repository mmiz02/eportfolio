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

# This gave me the output: Scraped 1 'Data Scientist' jobs and saved to data_scientist_jobs.json.

with open("data_scientist_jobs.json", "r", encoding="utf-8") as f:
    data = json.load(f)

print(json.dumps(data, indent=4, ensure_ascii=False))

