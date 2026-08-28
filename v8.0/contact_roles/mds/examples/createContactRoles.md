# Examples: createContactRoles

**POST /Contacts/roles**

## Request examples

### `application/json` — Success

Create a single contact role

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

Successful contact role creation

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
      "code": "INVALID_DATA",
      "details": {
        "api_name": "name",
        "json_path": "$.contact_roles[1].name",
        "expected_data_type": "text"
      },
      "message": "invalid data provided",
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
      "message": "Required field is missing",
      "details": {
        "api_name": "name",
        "json_path": "$.contact_roles[0].name"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataSimple

Invalid data in contact role field

```json
{
  "contact_roles": [
    {
      "code": "INVALID_DATA",
      "details": {
        "expected_data_type": "text",
        "api_name": "name",
        "json_path": "$.contact_roles[0].name"
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
        "json_path": "$.contact_roles[0].name"
      },
      "message": "duplicate data",
      "status": "error"
    }
  ]
}
```
