# Examples: updateContactRole

**PUT /Contacts/roles/{role}**

## Request examples

### `application/json` — Success

Update a specific contact role

```json
{
  "contact_roles": [
    {
      "name": "Manager",
      "sequence_number": 2
    }
  ]
}
```

## Response examples

### Status `200` — `application/json` — Success

Successful contact role update

```json
{
  "contact_roles": [
    {
      "code": "SUCCESS",
      "details": {
        "id": "123456789"
      },
      "message": "Contact role updated successfully.",
      "status": "success"
    }
  ]
}
```

### Status `400` — `application/json` — MandatoryNotFound

Required field missing in request

```json
{
  "contact_roles": [
    {
      "code": "MANDATORY_NOT_FOUND",
      "message": "required field not found",
      "details": {
        "api_name": "name",
        "json_path": "$.contact_roles[0]"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataWithId

Invalid contact role ID in request

```json
{
  "contact_roles": [
    {
      "code": "INVALID_DATA",
      "message": "invalid data",
      "details": {
        "id": "738964000000242001"
      },
      "status": "error"
    }
  ]
}
```
