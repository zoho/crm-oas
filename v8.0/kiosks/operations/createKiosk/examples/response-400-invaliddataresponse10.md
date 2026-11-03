INVALID_DATA error when group_api_name exceeds the maximum allowed length

```json
{
  "kiosks": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "group_api_name",
        "maximum_length": 25,
        "json_path": "$.kiosks[*].group_api_name"
      },
      "status": "error"
    }
  ]
}
```
