Ambiguity error — calendar_type gregorian sent with interval_display_option

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
          "api_name": "interval_display_option",
          "json_path": "$.fiscal_year.interval_display_option"
        }
      ]
    },
    "message": "Ambiguity while processing",
    "status": "error"
  }
}
```
