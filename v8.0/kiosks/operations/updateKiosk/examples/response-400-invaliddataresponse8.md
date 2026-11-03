INVALID_DATA error — invalid data in the description field

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
