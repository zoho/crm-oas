INVALID_DATA error: Invalid data (field: width)

```json
{
  "AB_testing": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "width",
        "supported_values": [
          600,
          700,
          800,
          900
        ],
        "json_path": "$.AB_testing[*].variant_form[*].form_attributes.width"
      },
      "status": "error"
    }
  ]
}
```
