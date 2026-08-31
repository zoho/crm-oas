Current and next shift IDs cannot be the same

```json
{
  "users": [
    {
      "code": "NOT_ALLOWED",
      "details": {
        "api_name": "$next_shift.id",
        "json_path": "$.users[0].$next_shift.id"
      },
      "message": "current shift and next shift should not be same",
      "status": "error"
    }
  ]
}
```
