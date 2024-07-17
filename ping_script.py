import requests

# List of Streamlit app URLs
urls = [
    "https://seo-analyzer.streamlit.app/",
    "https://hooks-generator.streamlit.app/",
    "https://blog-writer-tool.streamlit.app/",
    "https://youtube-scipt-generator.streamlit.app/"
]

def ping_urls(url_list):
    for url in url_list:
        try:
            response = requests.get(url)
            if response.status_code == 200:
                print(f"Successfully pinged {url}")
            else:
                print(f"Failed to ping {url} with status code: {response.status_code}")
        except requests.exceptions.RequestException as e:
            print(f"Error pinging {url}: {e}")

if __name__ == "__main__":
    ping_urls(urls)
