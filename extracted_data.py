def extract_data(html: str) -> dict:
    from bs4 import BeautifulSoup

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(html, 'html.parser')

    # Initialize an empty list to hold project data
    projects = []

    # Find all project grid items
    project_items = soup.find_all('div', class_='grid-item')

    # Iterate over each project item to extract title and description
    for item in project_items:
        # Extract the project title
        title = item.find('h4', class_='card-title').get_text(strip=True)
        
        # Extract the project description
        description = item.find('p', class_='card-text').get_text(strip=True)
        
        # Append the extracted data as a dictionary to the projects list
        projects.append({
            'title': title,
            'description': description
        })

    # Return the structured data as a dictionary matching the desired JSON schema
    return {'projects': projects}