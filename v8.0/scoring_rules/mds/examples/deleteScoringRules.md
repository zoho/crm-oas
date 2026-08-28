# Examples: deleteScoringRules

**DELETE /settings/automation/scoring_rules**

## Response examples

### Status `200` — `application/json` — Success200

Successful delete Scoring Rules response

```json
{
  "scoring_rules": [
    {
      "code": "SUCCESS",
      "details": {
        "id": "111114000000317218"
      },
      "message": "scoring rule deleted successfully",
      "status": "success"
    },
    {
      "code": "SUCCESS",
      "details": {
        "id": "111114000000317220"
      },
      "message": "scoring rule deleted successfully",
      "status": "success"
    }
  ]
}
```

### Status `207` — `application/json` — Success207

Partial success delete Scoring Rules response

```json
{
  "scoring_rules": [
    {
      "code": "INVALID_DATA",
      "details": {
        "id": "111114000000317200"
      },
      "message": "The id given seems to be invalid",
      "status": "error"
    },
    {
      "code": "SUCCESS",
      "details": {
        "id": "111114000000317218"
      },
      "message": "scoring rule deleted successfully",
      "status": "success"
    }
  ]
}
```
