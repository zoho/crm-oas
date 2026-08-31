Invalid holiday type value in bulk update

```json
{
  "holidays": [
    {
      "code": "INVALID_DATA",
      "details": {
        "api_name": "type",
        "json_path": "$.holidays[0].type",
        "supported_values": [
          "business_holiday",
          "shift_holiday"
        ]
      },
      "message": "Invalid type",
      "status": "error"
    }
  ]
}
```
