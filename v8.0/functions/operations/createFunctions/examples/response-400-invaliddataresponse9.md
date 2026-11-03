INVALID_DATA Error When the Name Field Contains an Invalid Data Type

```json
{
  "functions": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "name",
        "maximum_length": 100,
        "expected_data_type": "text",
        "json_path": "$.functions[*].name"
      },
      "status": "error"
    }
  ]
}
```
