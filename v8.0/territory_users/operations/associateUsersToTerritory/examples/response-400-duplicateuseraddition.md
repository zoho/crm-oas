Example error response for adding existing user to Territory

```json
{
  "users": [
    {
      "code": "DUPLICATE_DATA",
      "message": "Given user id already exists for that record",
      "status": "error",
      "details": {
        "api_name": "id",
        "json_path": "$.users[0].id"
      }
    }
  ]
}
```
