LIMIT_EXCEEDED error when the 500-active-service limit for the organization is reached

```json
{
  "data": [
    {
      "code": "LIMIT_EXCEEDED",
      "details": {
        "api_name": "Status",
        "limit": 3,
        "json_path": "$.data[0].Status"
      },
      "message": "You cannot create more than 500 active services",
      "status": "error"
    }
  ]
}
```
