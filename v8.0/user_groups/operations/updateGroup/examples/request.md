### `application/json` — UpdateGroupExample

Update a user group name, description, and sources

```json
{
  "user_groups": [
    {
      "name": "Updated Sales Team",
      "description": "Updated sales department user group",
      "sources": [
        {
          "type": "users",
          "source": {
            "id": "3652397000000186017"
          }
        },
        {
          "type": "roles",
          "source": {
            "id": "3652397000000026008"
          },
          "subordinates": true
        }
      ]
    }
  ]
}
```
