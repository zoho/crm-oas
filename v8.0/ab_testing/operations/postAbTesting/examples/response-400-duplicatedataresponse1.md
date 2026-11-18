DUPLICATE_DATA error for duplicate AB testing name in the module

```json
{
  "AB_testing": [
    {
      "code": "DUPLICATE_DATA",
      "details": {
        "api_name": "name",
        "json_path": "$.AB_testing[0].name"
      },
      "message": "ABTesting with the same name already exists in this module",
      "status": "error"
    }
  ]
}
```
