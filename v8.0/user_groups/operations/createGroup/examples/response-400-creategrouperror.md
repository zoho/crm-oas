Invalid request body for group creation

```json
{
  "user_groups": [
    {
      "status": "error",
      "code": "DUPLICATE_DATA",
      "message": "A user group with the same name already exists.",
      "details": {
        "api_name": "name",
        "json_path": "$.user_groups[0].name"
      }
    }
  ]
}
```
