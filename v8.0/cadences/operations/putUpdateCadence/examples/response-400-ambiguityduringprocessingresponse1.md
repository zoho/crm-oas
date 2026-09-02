Ambiguity during processing error

```json
{
  "cadences": [
    {
      "code": "AMBIGUITY_DURING_PROCESSING",
      "details": {
        "ambiguity_due_to": [
          {
            "api_name": "specific",
            "json_path": "$.cadences[0].execution_details.unenroll_properties[3].details.specific"
          },
          {
            "api_name": "state",
            "json_path": "$.cadences[0].execution_details.unenroll_properties[3].details.state"
          }
        ]
      },
      "message": "invalid data",
      "status": "error"
    }
  ]
}
```
