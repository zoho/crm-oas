INVALID_DATA: Invalid data (Field: api_name)

```json
{
  "AB_testing": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "api_name",
        "maximum_length": 100,
        "json_path": "$.AB_testing[*].variant_form[*].fields[*].api_name"
      },
      "status": "error"
    }
  ]
}
```
