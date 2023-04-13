### while dreaming
import googlesearch
import re

# Define the keywords to search
keywords = ['ruyada']

# Search Google for the keywords and retrieve the search results
search_results = list(googlesearch.search('ruyada rüyada ' + ' '.join(keywords), num_results=100))

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

