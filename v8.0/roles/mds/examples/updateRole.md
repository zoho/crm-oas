# Examples: updateRole

**PUT /settings/roles/{role}**

## Request examples

### `application/json` — UpdateRole

Update a role with new name and description

```json
{
  "roles": [
    {
      "name": "Senior Sales Manager",
      "description": "Updated description for senior sales manager role"
    }
  ]
}
```

## Response examples

### Status `200` — `application/json` — Success

Successful single role update response

```json
{
  "roles": [
    {
      "code": "SUCCESS",
      "details": {
        "id": "4413524000000991004"
      },
      "message": "Role updated",
      "status": "success"
    }
  ]
}
```

### Status `400` — `application/json` — Error

Validation error during single role update

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
