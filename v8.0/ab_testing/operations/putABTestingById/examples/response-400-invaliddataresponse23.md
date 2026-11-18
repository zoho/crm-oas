INVALID_DATA error for exceeding maximum length on the module ID field

```json
{
  "AB_testing": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "id",
        "maximum_length": 19,
        "json_path": "$.AB_testing[*].module.id"
      },
      "status": "error"
    }
  ]
}
```
