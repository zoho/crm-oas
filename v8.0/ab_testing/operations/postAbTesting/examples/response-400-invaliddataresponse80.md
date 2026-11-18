INVALID_DATA error: Invalid data (field: ID)

```json
{
  "AB_testing": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "id",
        "maximum_length": 19,
        "json_path": "$.AB_testing[*].variant_form[*].fields[*].id"
      },
      "status": "error"
    }
  ]
}
```
