INVALID_DATA error: Invalid data (field: color)

```json
{
  "AB_testing": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "color",
        "maximum_length": 10,
        "json_path": "$.AB_testing[*].variant_form[*].button_attributes[*].color"
      },
      "status": "error"
    }
  ]
}
```
