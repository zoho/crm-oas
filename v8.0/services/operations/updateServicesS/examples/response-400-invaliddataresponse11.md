Invalid data error when Available_Till has an invalid date format.

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
