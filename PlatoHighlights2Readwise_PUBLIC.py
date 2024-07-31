import os
import json
import requests
from datetime import datetime

# Constants
LOCATION_X = 'LINK TO HIGHLIGHTS PATH'  # Replace with the actual path to your highlights, for me it was : /Volumes/KOBOeReader/.reading-states/
METADATA_FILE = 'LINK TO METADATA JSON'  # Replace with the actual path to your .metadata.json, for me it was : /Volumes/KOBOeReader/.metadata.json
READWISE_API_TOKEN = 'YOUR READWISE API TOKEN'  # Replace with your Readwise API token, get it here : https://readwise.io/access_token

def get_metadata(metadata_file):
    try:
        with open(metadata_file, 'r', encoding='utf-8') as f:
            return json.load(f)
    except UnicodeDecodeError:
        print(f"Error reading metadata file due to encoding issues: {metadata_file}")
    except json.JSONDecodeError:
        print(f"Error reading metadata file due to JSON decoding issues: {metadata_file}")
    return {}

def get_highlights(location_x):
    highlights = []
    for file_name in os.listdir(location_x):
        if file_name.startswith('.'):
            # Skip hidden/system files
            continue
        if file_name.endswith('.json'):
            try:
                with open(os.path.join(location_x, file_name), 'r', encoding='utf-8') as f:
                    highlights.append((file_name, json.load(f)))
            except UnicodeDecodeError:
                print(f"Skipping file due to encoding error: {file_name}")
            except json.JSONDecodeError:
                print(f"Skipping file due to JSON decoding error: {file_name}")
    return highlights

def format_highlights(highlights, metadata):
    formatted_highlights = []
    for file_name, highlight in highlights:
        ebook_id = os.path.splitext(file_name)[0]
        
        if ebook_id in metadata:
            book_metadata = metadata[ebook_id]
            for annotation in highlight.get('annotations', []):
                formatted_highlight = {
                    "text": annotation.get("text", ""),
                    "title": book_metadata.get("title", "Unknown Title"),
                    "author": book_metadata.get("author", "Unknown Author"),
                    "source_type": "Annas-Plato-Imports",
                    "category": "books",
                    "highlighted_at": annotation.get("modified", datetime.now().isoformat()),
                    "api_source": 'null'
                }
                
                note = annotation.get("note", "")
                if note:  # Only include if note has any value
                    formatted_highlight["note"] = note
                
                formatted_highlights.append(formatted_highlight)
        else:
            print(f"Metadata not found for ebook_id: {ebook_id}")
    return formatted_highlights

def upload_highlights(formatted_highlights):
    url = "https://readwise.io/api/v2/highlights/"
    headers = {"Authorization": f"Token {READWISE_API_TOKEN}"}
    for highlight in formatted_highlights:
        response = requests.post(url, headers=headers, json={"highlights": [highlight]})
        if response.status_code != 200:
            print(f"Failed to upload highlight: {highlight['text']}")
            print(f"Response Status Code: {response.status_code}")
            print(f"Response Content: {response.content.decode('utf-8')}")
        else:
            print(f"Successfully uploaded highlight: {highlight['text']}")

if __name__ == "__main__":
    metadata = get_metadata(METADATA_FILE)
    highlights = get_highlights(LOCATION_X)
    formatted_highlights = format_highlights(highlights, metadata)
    upload_highlights(formatted_highlights)