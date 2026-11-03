INVALID_DATA error when the group_api_name field is not a text type

```json
{
  "kiosks": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "group_api_name",
        "expected_data_type": "text",
        "json_path": "$.kiosks[*].group_api_name"
      },
      "status": "error"
    }
  ]
}
```
