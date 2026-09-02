### `application/json` — Example1

Request body for bulk status change

```json
{
  "change_status": [
    {
      "users": [
        {
          "active": false,
          "personality_id": "12346789899"
        },
        {
          "active": false,
          "personality_id": "12346789898"
        }
      ]
    }
  ]
}
```
