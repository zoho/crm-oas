INVALID_DATA error when the description field exceeds the maximum allowed length

```json
{
  "kiosks": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "description",
        "maximum_length": 500,
        "json_path": "$.kiosks[*].description"
      },
      "status": "error"
    }
  ]
}
```
