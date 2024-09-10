import requests

class BaseAPI:
    def __init__(self, base_url):
        self.base_url = base_url

    def get(self, endpoint):
        response = requests.get(f"{self.base_url}/{endpoint}")
        response.raise_for_status()  # Raises an error for bad status codes
        return response.json()

    def post(self, endpoint, data):
        response = requests.post(f"{self.base_url}/{endpoint}", json=data)
        response.raise_for_status()  # Raises an error for bad status codes
        return response.json()

class UserAPI(BaseAPI):
    def __init__(self, base_url):
        super().__init__(base_url)

    def get_user(self, user_id):
        endpoint = f"users/{user_id}"
        return self.get(endpoint)

    def create_user(self, user_data):
        endpoint = "users"
        return self.post(endpoint, data=user_data)

if __name__ == "__main__":
    base_url = "https://jsonplaceholder.typicode.com"
    user_api = UserAPI(base_url)

    # Get user with ID 1
    user = user_api.get_user(1)
    print("User details:", user)

    # Create a new user (note: JSONPlaceholder will not actually create a user, but will return the data you sent)
    new_user = {"name": "Keer", "email": "hello@gmail.com"}
    response = user_api.create_user(new_user)
    print("Create response:", response)
