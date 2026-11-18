CANNOT_PROCESS error when a deleted transition leaves an orphan state

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
