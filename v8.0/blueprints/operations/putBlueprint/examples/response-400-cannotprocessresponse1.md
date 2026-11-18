Error — deleted state with active transitions (CANNOT_PROCESS)

```json
{
  "blueprints": [
    {
      "code": "CANNOT_PROCESS",
      "details": {
        "api_name": "id",
        "json_path": "$.blueprints[0].states.id"
      },
      "message": "the state is deleted but transitions connecting the state are not deleted",
      "status": "error"
    }
  ]
}
```
