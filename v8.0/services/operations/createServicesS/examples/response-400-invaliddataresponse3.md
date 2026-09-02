Invalid data when duration value is outside allowed range.

```json
{
  "data": [
    {
      "code": "INVALID_DATA",
      "details": {
        "api_name": "Duration",
        "json_path": "$.data[0].Duration"
      },
      "message": "Duration value should not be greater than 24hrs or less than 5mins",
      "status": "error"
    }
  ]
}
```
