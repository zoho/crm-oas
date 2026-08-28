# Examples: deleteTerritories

**DELETE /settings/territories**

## Response examples

### Status `200` — `application/json` — TerritoryDeleteByIds

Delete territories using the ids parameter

```json
{
  "territories": [
    {
      "code": "SUCCESS",
      "details": {
        "id": "431581000000798016"
      },
      "message": "Given Territory Removed Successfully",
      "status": "success"
    }
  ]
}
```

### Status `400` — `application/json` — TerritoryNotYetEnabled

Territory management not yet enabled

```json
{
  "code": "FEATURE_NOT_ENABLED",
  "details": {},
  "message": "Territory Management is not enabled",
  "status": "error"
}
```

### Status `400` — `application/json` — TerritoryDisabled

Territory disabled error

```json
{
  "code": "FEATURE_NOT_ENABLED",
  "details": {},
  "message": "Territory Management is disabled",
  "status": "error"
}
```

### Status `400` — `application/json` — InvalidRequestIdsLimitExceeded

Invalid request — ids parameter exceeds maximum limit

```json
{
  "code": "INVALID_REQUEST",
  "details": {},
  "message": "unable to process your request. please verify whether you have entered proper method name, parameter and parameter values.",
  "status": "error"
}
```

### Status `401` — `application/json` — AuthenticationFailure

Authentication failure

```json
{
  "code": "AUTHENTICATION_FAILURE",
  "details": {},
  "message": "Authentication failed",
  "status": "error"
}
```
