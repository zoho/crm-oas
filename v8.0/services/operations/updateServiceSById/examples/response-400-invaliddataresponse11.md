INVALID_DATA on Unavailable_Till field containing a malformed value.

```json
{
  "data": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "Unavailable_Till",
        "supported_values": [
          "Temporarily Unavailable",
          "Available",
          "Not In Use",
          "Scheduled"
        ],
        "json_path": "$.data[*].Unavailable_Till"
      },
      "status": "error"
    }
  ]
}
```
