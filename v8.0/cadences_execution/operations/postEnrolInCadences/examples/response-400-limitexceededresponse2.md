LIMIT_EXCEEDED error for ids exceeding 100

```json
{
  "code": "LIMIT_EXCEEDED",
  "details": {
    "limit": 100,
    "limit_due_to": [
      {
        "api_name": "ids",
        "json_path": "$.ids"
      }
    ]
  },
  "message": "Limit Exceeded, You cannot give more than 100 record ids",
  "status": "error"
}
```
