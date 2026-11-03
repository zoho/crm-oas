INVALID_DATA error when the name field is not a text type

```json
{
  "kiosks": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "name",
        "expected_data_type": "text",
        "json_path": "$.kiosks[*].name"
      },
      "status": "error"
    }
  ]
}
```
