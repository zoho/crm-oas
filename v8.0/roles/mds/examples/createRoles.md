# Examples: createRoles

**POST /settings/roles**

## Request examples

### `application/json` — CreateRole

Create a new role with required and optional fields

```json
{
  "roles": [
    {
      "name": "Marketing Manager",
      "description": "Manages marketing campaigns and strategies",
      "share_with_peers": true,
      "reporting_to": {
        "id": "4413524000000991006"
      }
    }
  ]
}
```

## Response examples

### Status `201` — `application/json` — Success

Successful role creation response

```json
{
  "roles": [
    {
      "code": "SUCCESS",
      "details": {
        "id": "4413524000000991004"
      },
      "message": "Role added",
      "status": "success"
    }
  ]
}
```

### Status `400` — `application/json` — Error

Validation error during role creation

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
