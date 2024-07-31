# Readwise Highlights Uploader

This script allows you to upload highlights from your e-reader if made using the Plato environment on your Kobo to Readwise (Readwise.io). October (https://github.com/marcus-crane/october) works really well for highlights made in the default UI of the Kobo, but does not recognize the highlights and notes made if you are running Plato (https://github.com/baskerville/plato). This script does that. It extracts highlights from JSON files, formats them, and uploads them to your Readwise account using the Readwise API.

## Requirements

- Python 3.x
- `requests` library

You can install the `requests` library using pip:

```sh
pip install requests
```

## Configuration

Before running the script, you need to configure the following constants in the script:

1. `LOCATION_X`: Path to the directory containing your highlights JSON files. 
2. `METADATA_FILE`: Path to your `.metadata.json` file. 
3. `READWISE_API_TOKEN`: Your Readwise API token. Get it here : https://readwise.io/access_token

Example:

```python
LOCATION_X = '/Volumes/KOBOeReader/.reading-states/'  # Replace with the actual path to your highlights
METADATA_FILE = '/Volumes/KOBOeReader/.metadata.json'  # Replace with the actual path to your metadata file
READWISE_API_TOKEN = 'your_readwise_api_token'  # Replace with your Readwise API token
```

## Usage

1. Clone or download this repository.
2. Configure the constants as described above.
3. Run the script:

```sh
python script_name.py
```

4. If it works, make sure to run the script every time you attach your Kobo.
5. Enjoy!
6. Important : it only adds highlights, doesn't actually check and remove deleted highlights. 

## Functions

### `get_metadata(metadata_file)`

Reads and parses the metadata JSON file.

- **Parameters**: `metadata_file` (str) - Path to the metadata file.
- **Returns**: A dictionary containing the metadata.

### `get_highlights(location_x)`

Reads and parses the highlights JSON files from the specified directory.

- **Parameters**: `location_x` (str) - Path to the directory containing the highlights.
- **Returns**: A list of tuples, each containing the file name and the parsed JSON content.

### `format_highlights(highlights, metadata)`

Formats the highlights for uploading to Readwise.

- **Parameters**:
  - `highlights` (list) - List of tuples containing file names and parsed JSON content.
  - `metadata` (dict) - Dictionary containing the metadata.
- **Returns**: A list of formatted highlights.

### `upload_highlights(formatted_highlights)`

Uploads the formatted highlights to Readwise.

- **Parameters**: `formatted_highlights` (list) - List of formatted highlights.

## Error Handling

The script includes basic error handling for file reading and JSON parsing errors. It will print error messages and skip problematic files.

## License

This project is not licensed. Just have fun with it. 

## Acknowledgements

This script was created to help users easily upload their e-reader highlights from Plato to Readwise.
Thanks to [@heyarne](https://github.com/heyarne) for the idea. 


