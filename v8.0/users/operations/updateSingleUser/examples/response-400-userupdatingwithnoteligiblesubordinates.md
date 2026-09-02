Role Change Creates Invalid Subordinate Relationships

```json
{
  "users": [
    {
      "code": "CONFLICTING_DATA_FOUND",
      "details": {
        "api_name": "Reporting_To",
        "json_path": "$.users[0].Reporting_To"
      },
      "message": "the user must be updated with new eligible reporting manager and the subordinates  who are going to report to a user in a role below them, because of new role change are need to transfer to new eligible reporting manager",
      "status": "error"
    }
  ]
}
```
