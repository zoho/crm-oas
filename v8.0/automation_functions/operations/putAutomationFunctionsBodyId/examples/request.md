### `application/json` — SamplePutRequest

Update a Custom Function With Merge Field and Static Arguments

```json
{
  "functions": [
    {
      "arguments": [
        {
          "name": "arg1",
          "type": "merge_field",
          "value": "${!Leads.Last_Name}"
        },
        {
          "name": "arg2",
          "type": "static",
          "value": "cityupdated"
        }
      ],
      "id": "678446000051490013",
      "module": {
        "id": "678446000000000125",
        "api_name": "Leads"
      },
      "feature_type": "workflow"
    }
  ]
}
```
