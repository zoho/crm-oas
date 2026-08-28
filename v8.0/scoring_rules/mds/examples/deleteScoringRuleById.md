# Examples: deleteScoringRuleById

**DELETE /settings/automation/scoring_rules/{ruleId}**

## Response examples

### Status `200` — `application/json` — Success200

Successful delete Scoring Rule by ID response

```json
{
  "scoring_rules": [
    {
      "code": "SUCCESS",
      "details": {
        "id": "111114000000317200"
      },
      "message": "scoring rule deleted successfully",
      "status": "success"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse1

Error response with code INVALID_DATA: The id given seems to be invalid

```json
{
  "code": "INVALID_DATA",
  "details": {
    "resource_path_index": 3
  },
  "message": "The id given seems to be invalid",
  "status": "error"
}
```
