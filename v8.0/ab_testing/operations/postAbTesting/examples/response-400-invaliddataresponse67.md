INVALID_DATA error: Invalid data (field: align)

```json
{
  "AB_testing": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "align",
        "supported_values": [
          "right",
          "left",
          "top"
        ],
        "json_path": "$.AB_testing[*].variant_form[*].form_attributes.align"
      },
      "status": "error"
    }
  ]
}
```
