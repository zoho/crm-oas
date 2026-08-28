# Examples: updateRoles

**PUT /settings/roles**

## Request examples

### `application/json` — UpdateRoles

Update a role

```json
{
  "roles": [
    {
      "id": "4413524000000991001",
      "name": "Senior Sales Manager",
      "description": "Updated description for senior sales manager role",
      "share_with_peers": false,
      "reporting_to": {
        "id": "4413524000000991010"
      },
      "forecast_manager": {
        "id": "4413524000000991011",
        "name": "John Doe"
      }
    }
  ]
}
```

## Response examples

### Status `200` — `application/json` — Success

Successful role update response

```json
{
  "roles": [
    {
      "code": "SUCCESS",
      "details": {
        "id": "4413524000000991001"
      },
      "message": "Role updated",
      "status": "success"
    }
  ]
}
```

### Status `400` — `application/json` — Error

Validation error during role update

```json
{
  "roles": [
    {
      "status": "error",
      "code": "INVALID_DATA",
      "message": "Invalid role name",
      "details": {
        "maximum_length": 200,
        "api_name": "name",
        "json_path": "$.roles[0].name"
      }
    }
  ]
}
```
