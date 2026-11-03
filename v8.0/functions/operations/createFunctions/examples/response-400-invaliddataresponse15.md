INVALID_DATA Error for Incorrect Data Type on api_name Field

```json
{
  "functions": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "api_name",
        "maximum_length": 100,
        "expected_data_type": "text",
        "json_path": "$.functions[*].api_name"
      },
      "status": "error"
    }
  ]
}
```
