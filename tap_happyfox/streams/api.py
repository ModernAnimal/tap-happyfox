from requests.auth import HTTPBasicAuth
import requests


def happyfox_api(api_key, api_code, page_num):
    # Define page size. Max size = 50
    page_size = 50

    auth = HTTPBasicAuth(api_key, api_code)

    paginated_url = (
        f"https://support.modernanimal.com/api/1.1/json/tickets/?size={page_size}&page={page_num}"
    )
    page_response = requests.get(paginated_url, auth=auth).json()
    data = page_response["data"]
    has_next = page_num < int(page_response["page_info"]["page_count"])

    return data, has_next
