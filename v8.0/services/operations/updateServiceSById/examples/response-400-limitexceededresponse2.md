LIMIT_EXCEEDED error for Status breaching the 500 active services limit.

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
