INVALID_DATA error when name value exceeds the maximum length

```json
{
  "AB_testing": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "name",
        "maximum_length": 50,
        "json_path": "$.AB_testing[*].name"
      },
      "status": "error"
    }
  ]
}
```
