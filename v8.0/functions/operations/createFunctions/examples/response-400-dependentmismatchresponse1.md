DEPENDENT_MISMATCH Error for Mismatched Category and Runtime Fields

```json
{
  "functions": [
    {
      "code": "DEPENDENT_MISMATCH",
      "message": "Dependent Field is not matching",
      "details": {
        "dependee": {
          "api_name": "runtime",
          "json_path": "$.functions[0].runtime"
        },
        "api_name": "category",
        "json_path": "$.functions[0].category",
        "supported_values": [
          "Button",
          "Automation",
          "Schedule",
          "Related List",
          "Standalone",
          "Signals",
          "Validation Rule"
        ]
      },
      "status": "error"
    }
  ]
}
```
