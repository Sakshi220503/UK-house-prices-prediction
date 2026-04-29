import requests

URL = "https://prod.publicdata.landregistry.gov.uk.s3-website-eu-west-1.amazonaws.com/pp-monthly-update-new-version.csv"
OUTPUT = "../data/raw/uk_house_prices.csv"

def download_data():
    r = requests.get(URL)
    with open(OUTPUT, "wb") as f:
        f.write(r.content)

if __name__ == "__main__":
    download_data()
