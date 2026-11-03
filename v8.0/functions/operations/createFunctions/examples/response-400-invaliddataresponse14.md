INVALID_DATA Error — Category Field Contains an Unsupported Value

```json
{
  "functions": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "category",
        "supported_values": [
          "Button",
          "Automation",
          "Schedule",
          "Related List",
          "Standalone",
          "Signals",
          "Validation Rule",
          "Dynamic"
        ],
        "json_path": "$.functions[*].category"
      },
      "status": "error"
    }
  ]
}
```
