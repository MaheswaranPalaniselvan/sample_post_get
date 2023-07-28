import requests

data =  {
  "topic": "string",
  "pages": [
    {
      "id": 1,
      "subtopic": [
        {
          "id": 1,
          "title": "string",
          "description": "html"
        },
        {
          "id": 2,
          "title": "string",
          "description": "html"
        },
        {
          "id": 3,
          "title": "string",
          "description": "html"
        },
        {
          "id": 4,
          "title": "string",
          "description": "html"
        }
      ]
    },
    {
      "id": 2,
      "subtopic": [
        {
          "id": 1,
          "title": "string",
          "description": "html"
        },
        {
          "id": 2,
          "title": "string",
          "description": "html"
        },
        {
          "id": 3,
          "title": "string",
          "description": "html"
        },
        {
          "id": 4,
          "title": "string",
          "description": "html"
        }
      ]
    },
    {
      "id": 3,
      "subtopic": [
        {
          "id": 1,
          "title": "string",
          "description": "html"
        },
        {
          "id": 2,
          "title": "string",
          "description": "html"
        },
        {
          "id": 3,
          "title": "string",
          "description": "html"
        },
        {
          "id": 4,
          "title": "string",
          "description": "html"
        }
      ]
    }
  ]
}



url = "http://localhost:8000/save_data/"
response = requests.post(url, json=data)

if response.status_code == 200:
    print("Data successfully saved!")
else:
    print(f"Failed to save data. Status code: {response.status_code}")
