INVALID_DATA Error — api_name Field Fails Format Validation

```json
{
  "functions": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "api_name",
        "maximum_length": 100,
        "minimum_length": 3,
        "regex": "^[A-Za-z][A-Za-z0-9_-]*$",
        "json_path": "$.functions[*].api_name"
      },
      "status": "error"
    }
  ]
}
```
