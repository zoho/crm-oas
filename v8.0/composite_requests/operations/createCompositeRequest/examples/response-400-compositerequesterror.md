Error response for composite request with invalid data.

```json
{
  "__composite_requests": [
    {
      "code": "INVALID_DATA",
      "details": {
        "expected_data_type": "text",
        "regex": "/crm(/.*)?/v[0-9]+([.][0-9]+)?/.*",
        "api_name": "uri",
        "json_path": "$.__composite_requests[0].uri"
      },
      "message": "invalid data",
      "status": "error"
    }
  ]
}
```
