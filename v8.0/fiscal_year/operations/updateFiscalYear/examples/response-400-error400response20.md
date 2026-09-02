Missing quarter in surplus_week error

```json
{
  "fiscal_year": {
    "code": "DEPENDENT_FIELD_MISSING",
    "details": {
      "dependee": {
        "api_name": "surplus_week",
        "json_path": "$.fiscal_year.surplus_week"
      },
      "api_name": "quarter",
      "json_path": "$.fiscal_year.surplus_week.quarter"
    },
    "message": "Provide valid quarter for surplus week",
    "status": "error"
  }
}
```
