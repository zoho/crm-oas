INVALID_DATA Error for Name Field Value Failing Format Constraints

```json
{
  "functions": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "name",
        "maximum_length": 100,
        "minimum_length": 3,
        "regex": "^[A-Za-z][A-Za-z0-9 _-]*$",
        "json_path": "$.functions[*].name"
      },
      "status": "error"
    }
  ]
}
```
