import requests


url = "https://graph.facebook.com/v18.0/me?fields=id%2Cname%2Cposts&access_token=EAAOd32tBztkBOZChHEW417nGJNQX0BVFIcfOQd0EFQLkRP3lyLQvT0gqWbNOUNPamZARoCOYzYTqUgk7VXp9xdWyIqUCubMaVXQr0ENDXc8USK5c1cSlZCQx6JJrmWnVDc9eTUg7j9UmQHtx4GpNXzuFHSBeOQSqEbBnCDBc3ZA1GbuynAlFiZBEmGvIZBYdKneO69JSZB7go8nvZCj6fqnaIWdJrQJ0K80SPPq2grz9MvURzNXrkVH7oEhMY51XR6kZD"

responce = requests.get(url)

print(responce.content)