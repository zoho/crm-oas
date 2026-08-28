# Examples: updateContactRoles

**PUT /Contacts/roles**

## Request examples

### `application/json` — Success

Update a single contact role

```json
{
  "contact_roles": [
    {
      "name": "Manager",
      "id": "123456789",
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

### Status `207` — `application/json` — MultiStatus

Mixed success and error results

```json
{
  "contact_roles": [
    {
      "code": "SUCCESS",
      "details": {
        "id": "123456789"
      },
      "message": "Contact role created successfully.",
      "status": "success"
    },
    {
      "code": "MANDATORY_NOT_FOUND",
      "details": {
        "api_name": "id",
        "json_path": "$.contact_roles[0].id"
      },
      "message": "required field not found",
      "status": "error"
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
      "details": {
        "api_name": "id",
        "json_path": "$.contact_roles[0].id"
      },
      "message": "required field not found",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidData

Invalid data in contact role field

```json
{
  "contact_roles": [
    {
      "code": "INVALID_DATA",
      "details": {
        "api_name": "name",
        "json_path": "$.contact_roles[0].name",
        "id": "1718237000010991001"
      },
      "message": "invalid data",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — DuplicateData

Duplicate contact role name

```json
{
  "contact_roles": [
    {
      "code": "DUPLICATE_DATA",
      "details": {
        "api_name": "name",
        "json_path": "$.contact_roles[0].name",
        "id": "1718237000010991001"
      },
      "message": "duplicate data",
      "status": "error"
    }
  ]
}
```
