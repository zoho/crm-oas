INVALID_DATA error: Invalid data (field: help)

```json
{
  "AB_testing": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "help",
        "minimum_length": 1,
        "json_path": "$.AB_testing[*].variant_form[*].fields[*].help"
      },
      "status": "error"
    }
  ]
}
```
