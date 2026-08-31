Error response for invalid request data

```json
{
  "variable_groups": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "name",
        "maximum_length": 50,
        "json_path": "$.variable_groups[*].name"
      },
      "status": "error"
    }
  ]
}
```
