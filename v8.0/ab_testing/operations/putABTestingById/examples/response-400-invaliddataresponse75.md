INVALID_DATA: Invalid data (Field: name)

```json
{
  "AB_testing": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "name",
        "minimum_length": 1,
        "json_path": "$.AB_testing[*].variant_form[*].button_attributes[*].name"
      },
      "status": "error"
    }
  ]
}
```
