import streamlit as st
import pandas as pd
import requests

# Function for reverse geocoding using Bing Maps Geocoding API
def reverse_geocode(latitude, longitude, api_key):
    base_url = "http://dev.virtualearth.net/REST/v1/Locations"
    params = {
        "point": f"{latitude},{longitude}",
        "key": api_key
    }
    response = requests.get(base_url, params=params)
    data = response.json()
    if response.status_code == 200:
        try:
            resource_sets = data["resourceSets"]
            if len(resource_sets) > 0:
                resources = resource_sets[0]["resources"]
                if len(resources) > 0:
                    address = resources[0]["address"]
                    formatted_address = ", ".join(address.values())
                    return formatted_address
        except KeyError:
            pass
    return None

# Streamlit UI
def main():
    st.title("Reverse Geocode Coordinates with Bing Maps API")
    
    # Get Bing Maps API key
    api_key = st.secrets["API_KEY"]
    
    # Single coordinates input
    latitude_input = st.number_input("Enter latitude:")
    longitude_input = st.number_input("Enter longitude:")
    
    if latitude_input is not None and longitude_input is not None and api_key:
        st.write("Reverse Geocoding...")
        address = reverse_geocode(latitude_input, longitude_input, api_key)
        
        if address:
            st.write("Address:", address)
        else:
            st.write("Error: Unable to reverse geocode the coordinates.")
    
    # File upload
    uploaded_file = st.file_uploader("Upload CSV file", type=["csv"])
    
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        
        # Check if 'Latitude' and 'Longitude' columns exist
        if 'Latitude' in df.columns and 'Longitude' in df.columns:
            st.write("Original data:")
            st.write(df)
            
            # Reverse geocode coordinates
            st.write("Reverse Geocoding...")
            df['Address'] = df.apply(lambda row: reverse_geocode(row['Latitude'], row['Longitude'], api_key), axis=1)
            
            # Display reverse geocoded data
            st.write("Reverse Geocoded data:")
            st.write(df)
            
            # Button to download reverse geocoded data
            st.download_button(
                label="Download Reverse Geocoded Data",
                data=df.to_csv().encode(),
                file_name="reverse_geocoded_data.csv",
                mime="text/csv"
            )
        else:
            st.write("Error: No 'Latitude' and 'Longitude' columns found in the uploaded CSV file.")

    else:
        st.write("Please upload a CSV file.")

if __name__ == "__main__":
    main()
