INVALID_DATA Error for api_name Field Failing Format Constraints

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
