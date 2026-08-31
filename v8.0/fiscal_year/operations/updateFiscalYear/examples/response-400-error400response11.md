Surplus week year out-of-range error

```json
{
  "fiscal_year": {
    "status": "error",
    "code": "NOT_ALLOWED",
    "message": "Surplus week can be updated only for current year and next year",
    "details": {
      "api_name": "year",
      "json_path": "$.fiscal_year.surplus_week.year",
      "supported_values": [
        2025,
        2026
      ]
    }
  }
}
```
