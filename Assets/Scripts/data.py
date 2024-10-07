import requests
from bs4 import BeautifulSoup
import re

# List of star names to search
star_names = [
    "Betelgeuse","Rigel","Bellatrix","Alnilam","Mintaka","Alnitak","Saiph","Meissa","Hatsya","Tabit","Dubhe","Merak","Phecda","Megrez","Alioth","Mizar","Alkaid","Talitha","Tania Borealis","Polaris","Kochab","Pherkad","Yildun","Epsilon Ursae Minoris","Caph","Schedar","Ruchbah","Gamma Cassiopeiae","Epsilon_Cassiopeiae","Achird","Mu_Cassiopeiae","Gamma_Cassiopeiae","Antares","Shaula","Sargas","Dschubba","Beta_Scorpii","Pi Scorpii","Kappa Scorpii","Epsilon Scorpii","Girtab","Regulus","Denebola","Algieba","Zosma","Theta_Leonis","Subra","Rasalas","Al Jabhah","Aldebaran","Elnath","Alcyone","Atlas","Maia","Electra","Taygeta","Celaeno","Merope","Deneb","Albireo","Sadr","Epsilon_Cygni","Delta Cygni","Sirius","Adhara","Wezen","Eta Canis Majoris","Mirzam","Muliphein","Furud","Procyon","Beta Canis Minoris","Castor","Pollux","Alhena","Delta Geminorum","Mebsuta","Tejat Posterior","Mekbuda","Epsilon_Sagittarii","Nunki","Zeta Sagittarii","Kaus Media","Gamma2_Sagittarii","Arkab Posterior","Terebellum","Vega","Sheliak","Sulafat","Delta2 Lyrae","Epsilon Lyrae","Beta Persei","Alpha Persei","Omicron Persei","Gorgonea Tertia","Xi Persei","Zeta Persei","Psi Persei","Acrux","Mimosa","Gacrux","Delta Crucis","Epsilon Crucis","Alphard","Ashlesha","Sigma Hydrae","Xi Hydrae","Gamma Hydrae","Alpheratz","Mirach","Almach","Delta Andromedae","Pi_Andromedae","Mu Andromedae","Alpha Centauri (Rigil Kentaurus)","Beta Centauri (Hadar)","Theta Centauri","Epsilon Centauri"
]

# Base URL for Wikipedia
base_url = "https://en.wikipedia.org/wiki/"

def search_hr_number(star_name):
    try:
        # Helper function to extract HR number from a given URL
        def get_hr_number(url):
            response = requests.get(url, allow_redirects=True)
            if response.status_code != 200:
                return None, response.url  # Return None if the page doesn't exist

            # Parse the HTML content
            soup = BeautifulSoup(response.content, 'html.parser')
            html_content = str(soup)

            # Search for "Harvard Revised catalogue" or "Bright Star Catalogue"
            pattern_harvard = r'title="Harvard Revised catalogue">HR</a>'
            pattern_bright_star = r'title="Bright Star Catalogue">HR</a>'

            # Try finding the Harvard Revised catalogue first
            start_index = html_content.find(pattern_harvard)
            if start_index == -1:
                # If not found, try finding the Bright Star Catalogue pattern
                start_index = html_content.find(pattern_bright_star)

            if start_index != -1:
                # Extract the HR number after the "HR" anchor tag
                after_hr_content = html_content[start_index + len(pattern_harvard):]
                match = re.search(r'[^&#;]([0-9]+)', after_hr_content)
                if match:
                    return f"HR {match.group(1)}", response.url

            return None, response.url  # Return None if no HR number is found

        # First try: base URL (e.g., /Atlas)
        formatted_name = star_name.replace(" ", "_")
        url = base_url + formatted_name
        hr_number, final_url = get_hr_number(url)

        if hr_number:
            return f"{hr_number}"

        # Second try: URL with _(star) suffix (e.g., /Atlas_(star))
        star_url = base_url + formatted_name + "_(star)"
        hr_number, final_star_url = get_hr_number(star_url)

        if hr_number:
            return f"{hr_number}"

        # If neither URL contains an HR number
        return ""

    except Exception as e:
        print(f"Error searching for {star_name}: {str(e)}")
        return ""

# Create an empty list to store the HR numbers
hr_results = []

# Loop over each star name and search for the HR number
for star in star_names:
    hr_number = search_hr_number(star)
    if hr_number:
        print(f"Found HR number for {star}: {hr_number}")
    else:
        print(f"No HR number found for {star}")
    hr_results.append(hr_number)

# Convert the results array into a single string, joined by a space
final_result = ','.join(hr_results)

# Print the final string result
print("\nFinal HR results as a single string:")
print(final_result)