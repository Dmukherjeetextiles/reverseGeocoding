import streamlit as st
import pandas as pd
import requests

# Replace with your actual Bing Maps API key (stored as environment variable)
api_key = st.secrets["API_KEY"]

def reverse_geocode(latitude, longitude):
    """Reverse geocodes coordinates using Bing Maps API"""
    url = f"http://dev.virtualearth.net/REST/v1/Locations/{latitude},{longitude}?key={api_key}"
    response = requests.get(url).json()
    if response["resourceSets"] and response["resourceSets"][0]["resources"]:
        address = response["resourceSets"][0]["resources"][0]["address"]["formattedAddress"]
        return address
    else:
        return "Address not found"

def process_csv(file):
    """Processes a CSV file, adding an 'Address' column with geocoded results"""
    df = pd.read_csv(file)
    if "Latitude" in df.columns and "Longitude" in df.columns:
        df["Address"] = df.apply(lambda row: reverse_geocode(row["Latitude"], row["Longitude"]), axis=1)
        return df
    else:
        st.error("CSV must have 'Latitude' and 'Longitude' columns")
        return None

def single_coordinate_mode():
    """Handles single coordinate input and geocoding"""
    lat = st.number_input("Latitude")
    lon = st.number_input("Longitude")
    if st.button("Get Address"):
        address = reverse_geocode(lat, lon)
        st.write(f"**Address:** {address}")

def csv_mode():
    """Handles CSV file upload, processing, and download"""
    uploaded_file = st.file_uploader("Upload CSV file", type="csv")
    if uploaded_file:
        df = process_csv(uploaded_file)
        if df is not None:
            st.dataframe(df)
            csv_output = df.to_csv(index=False)
            st.download_button("Download Updated CSV", csv_output, "updated.csv", "text/csv")

def main():
    """Main function of the Streamlit app"""
    st.title("Reverse Geocoding with Bing Maps")

    option = st.radio("Input Method:", ("Single Coordinates", "CSV File"))

    if option == "Single Coordinates":
        single_coordinate_mode()
    elif option == "CSV File":
        csv_mode()

if __name__ == "__main__":
    main()
