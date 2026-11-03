INVALID_DATA error when the name field exceeds the maximum allowed length

```json
{
  "kiosks": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "name",
        "maximum_length": 25,
        "json_path": "$.kiosks[*].name"
      },
      "status": "error"
    }
  ]
}
```
