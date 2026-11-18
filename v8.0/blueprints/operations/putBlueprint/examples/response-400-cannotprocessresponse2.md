Error — deleted transition leaving orphan state (CANNOT_PROCESS)

```json
{
  "blueprints": [
    {
      "code": "CANNOT_PROCESS",
      "details": {
        "api_name": "id",
        "json_path": "$.blueprints[0].connections[0].id"
      },
      "message": "the transition is deleted but the state only connected by it is not deleted",
      "status": "error"
    }
  ]
}
```
