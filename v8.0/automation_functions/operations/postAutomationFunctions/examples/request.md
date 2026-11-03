### `application/json` — SamplePostRequest

Create a Custom Function Linked to the Leads Module With Workflow Trigger

```json
{
  "functions": [
    {
      "name": "FnAPIPost2",
      "description": "",
      "module": {
        "id": "678446000000000125",
        "api_name": "Leads"
      },
      "feature_type": "workflow",
      "language": "deluge",
      "function": {
        "id": "120851000000875006"
      },
      "arguments": [
        {
          "name": "arg1",
          "value": "${!Leads.Last_Name}",
          "type": "merge_field"
        },
        {
          "name": "arg2",
          "value": "city",
          "type": "static"
        }
      ]
    }
  ]
}
```
