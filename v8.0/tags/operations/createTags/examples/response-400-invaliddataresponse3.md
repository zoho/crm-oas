Error response for invalid tag name

```json
{
  "tags": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "name",
        "maximum_length": 26,
        "json_path": "$.tags[*].name"
      },
      "status": "error"
    }
  ]
}
```
