# reverseGeocoding
Latitude and longitude data to address.

https://reversegeocoding.streamlit.app/

# Reverse Geocode Coordinates with Bing Maps API

This Streamlit application allows users to perform reverse geocoding, converting latitude and longitude coordinates into human-readable addresses using the Bing Maps Geocoding API. Users can either enter individual coordinates or upload a CSV file containing multiple sets of coordinates.

## Usage

1. **Bing Maps API Key**: Obtain a Bing Maps API key from the [Bing Maps Dev Center](https://www.bingmapsportal.com/).
2. **Clone Repository**: Clone this repository to your local machine using `git clone https://github.com/Dmukherjeetextiles/reverseGeocoding.git`.
3. **Install Dependencies**: Install the required Python dependencies listed in `requirements.txt` using `pip install -r requirements.txt`.
4. **Run Application**: Run the Streamlit application by executing `streamlit run app.py` in your terminal.
5. **Enter Coordinates or Upload CSV**: Enter latitude and longitude coordinates manually or upload a CSV file with "Latitude" and "Longitude" columns.
6. **View Results**: The application will display the reverse geocoded addresses.
7. **Download Data**: Click the "Download Reverse Geocoded Data" button to download the reverse geocoded data as a CSV file.

## Requirements

- Python 3.6+
- Streamlit
- Pandas
- Requests

## License

This project is licensed under the [MIT License](https://github.com/Dmukherjeetextiles/reverseGeocoding/blob/main/LICENSE).
