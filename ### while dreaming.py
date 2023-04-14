### while dreaming
import googlesearch
import re
import time

# Define the keywords to search
keywords = ['ruyada']

# Search Google for the keywords and retrieve the search results
search_results = []
for keyword in keywords:
    query = 'ruyada rüyada ' + keyword
    results = list(googlesearch.search(query, num_results=10))
    search_results.extend(results)
    time.sleep(1) # Add a 0.5-second delay between each query

# Extract the search terms that start with "ruyada"
ruyada_terms = []
for result in search_results:
    # Extract the search terms from the search result URL
    url_terms = re.findall(r'\b[\w.]+\b', result)
    # Check if any of the search terms start with "ruyada"
    for term in url_terms:
        if term.startswith('ruyada'):
            ruyada_terms.append(term)

# Print the extracted search terms
print(ruyada_terms)

