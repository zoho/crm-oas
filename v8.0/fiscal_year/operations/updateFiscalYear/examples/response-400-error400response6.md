Invalid start_month error

```json
{
  "fiscal_year": {
    "status": "error",
    "code": "INVALID_DATA",
    "message": "Please give a valid month",
    "details": {
      "supported_values": [
        "JANUARY",
        "FEBRUARY",
        "MARCH",
        "APRIL",
        "MAY",
        "JUNE",
        "JULY",
        "AUGUST",
        "SEPTEMBER",
        "OCTOBER",
        "NOVEMBER",
        "DECEMBER"
      ],
      "api_name": "start_month",
      "json_path": "$.fiscal_year.start_month"
    }
  }
}
```
