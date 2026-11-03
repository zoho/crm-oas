Error for Exceeding Maximum Length on Module API Name

```json
{
  "functions": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "api_name",
        "maximum_length": 5,
        "json_path": "$.functions[*].module.api_name"
      },
      "status": "error"
    }
  ]
}
```
