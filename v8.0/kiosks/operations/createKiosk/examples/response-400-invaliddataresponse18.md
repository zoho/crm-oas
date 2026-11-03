INVALID_DATA error when a kiosk array item status exceeds the maximum allowed length

```json
{
  "kiosks": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "status",
        "maximum_length": 5,
        "json_path": "$.kiosks[*].status"
      },
      "status": "error"
    }
  ]
}
```
