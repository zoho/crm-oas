INVALID_DATA error when the description field is not a text type

```json
{
  "kiosks": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "description",
        "expected_data_type": "text",
        "json_path": "$.kiosks[*].description"
      },
      "status": "error"
    }
  ]
}
```
