# Examples: getFiscalYear

**GET /settings/fiscal_year**

## Response examples

### Status `200` — `application/json` — Success200

Get fiscal year settings - custom calendar with surplus week

```json
{
  "fiscal_year": {
    "id": "111111000000008761",
    "calendar_type": "custom",
    "start_month": "MARCH",
    "display_based_on": "start_month",
    "start_date": "2026-03-24",
    "structure": "4-4-5",
    "interval_display_option": "quarter",
    "surplus_week": {
      "quarter": 3,
      "period": 1,
      "year": 2027
    },
    "past_surplus_weeks": null
  }
}
```

### Status `401` — `application/json` — ScopeMismatch

OAuth scope mismatch error

```json
{
  "code": "OAUTH_SCOPE_MISMATCH",
  "details": {},
  "message": "invalid oauth scope to access this URL",
  "status": "error"
}
```

### Status `401` — `application/json` — AuthenticationFailed

Authentication failure error

```json
{
  "code": "AUTHENTICATION_FAILURE",
  "details": {},
  "message": "Authentication failed",
  "status": "error"
}
```
