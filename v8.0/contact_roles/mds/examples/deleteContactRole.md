# Examples: deleteContactRole

**DELETE /Contacts/roles/{role}**

## Response examples

### Status `200` — `application/json` — Success

Successful contact role deletion

```json
{
  "contact_roles": [
    {
      "code": "SUCCESS",
      "details": {
        "id": "123456789"
      },
      "message": "Contact role deleted successfully.",
      "status": "success"
    }
  ]
}
```

### Status `400` — `application/json` — LowerLimitReached

Lower limit reached on contact roles

```json
{
  "contact_roles": [
    {
      "status": "error",
      "code": "LOWER_LIMIT_REACHED",
      "message": "Lower limit reached",
      "details": {
        "limit": 1,
        "id": "123456789"
      }
    }
  ]
}
```

### Status `400` — `application/json` — InvalidData

Invalid contact role ID

```json
{
  "contact_roles": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data provided",
      "details": {
        "id": "123456789"
      },
      "status": "error"
    }
  ]
}
```
