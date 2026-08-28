# Examples: postClone

**POST /settings/automation/scoring_rules/{ruleId}/actions/clone**

## Request examples

### `application/json` — SamplePostRequest

Sample clone Scoring Rule request body

```json
{}
```

## Response examples

### Status `200` — `application/json` — Success200

Successful clone Scoring Rule response

```json
{
  "scoring_rules": [
    {
      "code": "SUCCESS",
      "details": {
        "id": "111114000000317265"
      },
      "message": "scoring rule cloned successfully",
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

### Status `400` — `application/json` — LimitExceededResponse1

Error response with code LIMIT_EXCEEDED: More than 10 scoring rules cannot be created for a layout (Field: id)

```json
{
  "scoring_rules": [
    {
      "code": "LIMIT_EXCEEDED",
      "details": {
        "api_name": "id",
        "limit": 10,
        "json_path": "$.scoring_rules[0].layout.id"
      },
      "message": "More than 10 scoring rules cannot be created for a layout",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — ActiveStateLimitExceededResponse1

Error response with code ACTIVE_STATE_LIMIT_EXCEEDED: More than 5 active scoring rules cannot be created for a layout (Field: id)

```json
{
  "scoring_rules": [
    {
      "code": "ACTIVE_STATE_LIMIT_EXCEEDED",
      "details": {
        "api_name": "id",
        "limit": 5,
        "json_path": "$.scoring_rules[0].layout.id"
      },
      "message": "More than 5 active scoring rules cannot be created for a layout",
      "status": "error"
    }
  ]
}
```
