Duplicate api_name value in module creation request

```json
{
  "modules": [
    {
      "code": "DUPLICATE_DATA",
      "details": {
        "api_name": "api_name",
        "json_path": "$.modules[0].api_name"
      },
      "message": "A module with the provided api_name already exists. Please use a unique api_name.",
      "status": "error"
    }
  ]
}
```
