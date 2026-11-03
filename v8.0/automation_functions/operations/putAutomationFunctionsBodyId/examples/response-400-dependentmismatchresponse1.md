Error When Argument Type and Value Are Mismatched

```json
{
  "functions": [
    {
      "code": "DEPENDENT_MISMATCH",
      "details": {
        "dependee": {
          "api_name": "type",
          "json_path": "$.functions[0].arguments[0].type"
        },
        "api_name": "value",
        "json_path": "$.functions[0].arguments[0].value"
      },
      "message": "Type and value is mismatched",
      "status": "error"
    }
  ]
}
```
