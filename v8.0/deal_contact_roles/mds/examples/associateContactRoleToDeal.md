# Examples: associateContactRoleToDeal

**PUT /{module}/{dealId}/Contact_Roles/{contactId}**

## Request examples

### `application/json` — AssociateContactRoleRequest

```json
{
  "data": [
    {
      "Contact_Role": {
        "name": "Engineering Lead",
        "id": "4408068000000007178"
      }
    }
  ]
}
```

## Response examples

### Status `200` — `application/json` — AssociateContactRoleResponse

```json
{
  "data": [
    {
      "code": "SUCCESS",
      "details": {
        "id": "4408068000000963455"
      },
      "message": "relation updated",
      "status": "success"
    }
  ]
}
```

### Status `500` — `application/json` — ErrorExample

```json
{
  "code": "INTERNAL_ERROR",
  "message": "Internal Server Error",
  "details": {},
  "status": "error"
}
```
