import requests
import pandas as pd 

def fetch_post_data():
    url = "https://jsonplaceholder.typicode.com/posts"

    response = requests.get(url)
    print(f"Status Code : {response.status_code}")

    data = response.json()
    return data


def main():
    try:
        posts = fetch_post_data()

        for post in posts:
            userid = post['userId']
            post_id = post['id']
            title = post['title']
            body = post['body']

            print("-------------------------")
            print(f"userid : {userid}")
            print(f"id : {post_id}")
            print(f"title : {title}")
            print(f"body : {body}")

    except Exception as e:
        print(f"Error : {e}")


if __name__ == "__main__":
    main()