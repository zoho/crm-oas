# Examples: deleteActivate

**DELETE /settings/automation/scoring_rules/{ruleId}/actions/activate**

## Response examples

### Status `200` — `application/json` — Success200

Successful deactivate Scoring Rule response

```json
{
  "scoring_rules": [
    {
      "code": "SUCCESS",
      "details": {
        "id": "111114000000313122"
      },
      "message": "scoring rule deactivated successfully",
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
