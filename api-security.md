Chose IPStack
# API Security Requirements - IPStack

## Aim
To define and mitigate security risks associated with integrating the IPStack API with Python programs that retrieve geolocation data (JSON) and store it in SQL databases for data analysis.

## Scope
- **API:** IPStack (https://ipstack.com/) 
- **Endpoints:** `/check`, `{ip}` - for IP-based geolocation (API endpoint, n.d.)
- **Format:** JSON
- **Storage:** SQL
- **Client:**  Python script performing lookups and storing results
(Getting started, n.d.)

## Identified threats
- Exposed API keys could allow unauthorised access
- Machine-in-the-Middle (MITM) attack - communication between client and API can be intercepted to steal sensitive information
- Invalid IP inputs could trigger unexpected responses
- Automated scripts might exceed query limits
- Data integirty - JSON responses might be tampered
- SQL injection - where malicious SQL queries are inserted into API requests to manipulate the database.
(What are API security threats?, n.d.; Bruce, 2025).

## Security Requirements & Mitigations

**Authentication and Authorisation**
- API keys should be properly secured (such as in an external config file) to protect against unauthorised access. OAuth and multi-factor authentication should be used for authorisation (What are API security threats?, n.d.)
- Care should be taken not to expose keys in URLs when sharing scripts.
- Keys should be rotated regularly and restricted by domain or IP (as supported by IPstack).

*The Python code reads the key from 'os.environ' or '.env' file.*

**Transport security**
- Transport Layer Security (TLS) is used to encrypt data in transit - use HTTPS instead of HTTP for all requests (What are API security threats?, n.d.; Getting started, n.d.)

*Unencrypted HTTP requests fail or are redirected to HTTPS.*

**Input validation**
- Validate that all IP inputs are in correct IPv4/IPv6 format before sending.

**Use web application firewalls to protect from web-based attacks.** (What are API security threats?, n.d.)

**Data Protection and Storage**
- Store minimal required data only.
- Restrict file permissions.

**Rate Limiting**
- Implement rate limiting and throttling to prevent DoS and DDoS attacks. This sets a limit on the number of requests an API can handle in a certain amount of time (What are API security threats?, n.d.).

**Logging & Monitoring**
-Log only anonymised IPs where possible and monitor API behaviour (What are API security threats?, n.d.).

*Most importantly, follow the Open Worldwide Application Security Project (OWASP) guidelines for securing APIs (What are API security threats?, n.d.).*

# Code
The secure implementation example in Python can be donwloaded [here](api.py).

# Output
The following output was received, showing that the code worked:
```
{'ip': '134.201.250.155', 'type': 'ipv4', 'continent_code': 'NA', 'continent_name': 'North America', 'country_code': 'US', 'country_name': 'United States', 'region_code': 'CA', 'region_name': 'California', 'city': 'Huntington Beach', 'zip': '92647', 'latitude': 33.70962142944336, 'longitude': -117.99259185791016, 'msa': '31100', 'dma': '803', 'radius': '0', 'ip_routing_type': 'fixed', 'connection_type': 'tx', 'location': {'geoname_id': 5358705, 'capital': 'Washington D.C.', 'languages': [{'code': 'en', 'name': 'English', 'native': 'English'}], 'country_flag': 'https://assets.ipstack.com/flags/us.svg', 'country_flag_emoji': '🇺🇸', 'country_flag_emoji_unicode': 'U+1F1FA U+1F1F8', 'calling_code': '1', 'is_eu': False}}
```

**Main Takeaways:**
- IPstack requires an access key to authenticate requests, meaning only authorised users can query the service. This prevents abuse. In this example, the key was assigned directly in the code fo demonstration purposes. In reality, it shouldbe stored securely in environmental variables or external configuration files.
- HTTPS is enforced and 'verify=True' ensures all requests are encrypted in transit, protecting the API key and the data from interception (ex:MITM attacks).
- Using 'try/except' with 'resp.raise_forstatus() to handle errors so that errors are noticed instead of the system silently failing.
- The API returns a JSON object containing the IP address, country, city, latitude, and longitude, which can be stored or analysed, as needed.

## Reflection
- Hard-coding the access key is convenient for testing but insecure in real applications.
- HTTPS should always be used instead of HTTP.
- Error handling improves reliability.

Moreover, this task was supposed to be completed as a team, however, I was abroad during this period and therefore had to complete this task independently. I missed the opportunity to discuss ideas and gain different perspectives from teammates, which could have helped clarify this complex topic. On the other hand, working independently strengthened my technical and problem-solving skills since I had to research the documentation and implement the Python code on my own.

## Conclusion
This exercise taught me how to evaluate API security requirements and to mitigate threats such as key exposure or MITM attacks, alikgning with the learning objectives of this task.

[← Back to Home](https://mmiz02.github.io/eportfolio/)
