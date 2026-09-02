Ambiguity error — calendar_type gregorian sent with surplus_week

```json
{
  "fiscal_year": {
    "code": "AMBIGUITY_DURING_PROCESSING",
    "details": {
      "ambiguity_due_to": [
        {
          "api_name": "calendar_type",
          "json_path": "$.fiscal_year.calendar_type"
        },
        {
          "api_name": "surplus_week",
          "json_path": "$.fiscal_year.surplus_week"
        }
      ]
    },
    "message": "Ambiguity while processing",
    "status": "error"
  }
}
```
