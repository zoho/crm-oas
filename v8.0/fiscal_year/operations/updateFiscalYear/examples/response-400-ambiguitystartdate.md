Ambiguity error — calendar_type gregorian sent with start_date

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
          "api_name": "start_date",
          "json_path": "$.fiscal_year.start_date"
        }
      ]
    },
    "message": "Ambiguity while processing",
    "status": "error"
  }
}
```
