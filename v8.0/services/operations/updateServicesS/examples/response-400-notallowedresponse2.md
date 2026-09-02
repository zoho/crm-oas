NOT_ALLOWED error when past availability dates prevent an Active or Temporarily Unavailable status change

```json
{
  "data": [
    {
      "code": "NOT_ALLOWED",
      "details": {
        "api_name": "Status",
        "json_path": "$.data[0].Status"
      },
      "message": "As service availability is not valid, status cannot be changed",
      "status": "error"
    }
  ]
}
```
