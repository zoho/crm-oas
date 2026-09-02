### `application/json` — CreateGroupExample

Create a user group with role and territory sources

```json
{
  "user_groups": [
    {
      "name": "Sales Team",
      "description": "Sales department user group",
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
