INVALID_DATA error: Invalid data (field: field_label)

```json
{
  "AB_testing": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "field_label",
        "maximum_length": 50,
        "json_path": "$.AB_testing[*].variant_form[*].fields[*].field_label"
      },
      "status": "error"
    }
  ]
}
```
