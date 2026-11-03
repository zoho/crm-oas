INVALID_DATA error when a kiosk array item status is not a text type

```json
{
  "kiosks": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "status",
        "expected_data_type": "text",
        "json_path": "$.kiosks[*].status"
      },
      "status": "error"
    }
  ]
}
```
