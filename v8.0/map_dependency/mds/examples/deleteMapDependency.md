# Examples: deleteMapDependency

**DELETE /settings/layouts/{layoutId}/map_dependency/{dependencyId}**

## Response examples

### Status `200` — `application/json` — SuccessResponse

Example of field dependency deleted successfully.

```json
{
  "map_dependency": [
    {
      "code": "SUCCESS",
      "details": {
        "id": "111111000000058515"
      },
      "message": "map dependency deleted",
      "status": "success"
    }
  ]
}
```

### Status `400` — `application/json` — InternalDependencyNotModifiable

Example of internal dependency cannot be deleted.

```json
{
  "code": "NOT_ALLOWED",
  "details": {
    "resource_path_index": 4
  },
  "message": "Internal Map Dependency cannot be deleted",
  "status": "error"
}
```

### Status `500` — `application/json` — ErrorExample

Example of an internal server error.

```json
{
  "code": "INTERNAL_ERROR",
  "message": "Internal Server Error",
  "details": {},
  "status": "error"
}
```
