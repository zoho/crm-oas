# Examples: getValidateBeforeTransferStatus

**GET /users/{userId}/actions/validate_before_transfer**

## Response examples

### Status `200` — `application/json` — TransferStatusResponse

An example successful response for pre-transfer validation.

```json
{
  "validate_before_transfer": [
    {
      "id": "5725767000000411001",
      "name": "John Doe",
      "assignment": true,
      "criteria": false,
      "subordinates": true,
      "alert": false
    }
  ]
}
```

### Status `400` — `application/json` — InvalidData

An example error response for an invalid user ID.

```json
{
  "code": "INVALID_DATA",
  "details": {
    "resource_path_index": 1
  },
  "message": "the id given seems to be invalid",
  "status": "error"
}
```

### Status `403` — `application/json` — SelfValidationNotAllowed

An example error response when validating your own account.

```json
{
  "status": "error",
  "code": "NOT_ALLOWED",
  "message": "Super Admin cannot be validated.",
  "details": {
    "resource_path_index": 1
  }
}
```
