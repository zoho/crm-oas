Ambiguity error — calendar_type gregorian sent with structure

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
          "api_name": "structure",
          "json_path": "$.fiscal_year.structure"
        }
      ]
    },
    "message": "Ambiguity while processing",
    "status": "error"
  }
}
```
