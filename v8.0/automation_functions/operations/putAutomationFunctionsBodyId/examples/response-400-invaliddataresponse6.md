Error for Incorrect Data Type on the Name Field in Arguments

```json
{
  "functions": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "name",
        "expected_data_type": "text",
        "json_path": "$.functions[*].arguments[*].name"
      },
      "status": "error"
    }
  ]
}
```
