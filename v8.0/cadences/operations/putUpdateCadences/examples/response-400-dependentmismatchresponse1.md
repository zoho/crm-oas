Dependent field value mismatch error

```json
{
  "cadences": [
    {
      "code": "DEPENDENT_MISMATCH",
      "details": {
        "dependee": {
          "api_name": "type",
          "json_path": "$.cadences[0].execution_details.unenroll_properties[3].type"
        },
        "api_name": "type",
        "json_path": "$.cadences[0].execution_details.unenroll_properties[3].details.type",
        "supported_values": [
          "Tasks",
          "Calls",
          "Email",
          "WhatsApp"
        ]
      },
      "message": "Dependent Field is not matching",
      "status": "error"
    }
  ]
}
```
