Successful Retrieval of an Automation Function

```json
{
  "functions": [
    {
      "created_time": "2026-03-04T18:42:24+05:30",
      "lock_status": {
        "locked": false
      },
      "editable": true,
      "module": {
        "singular_label": "Lead",
        "plural_label": "Leads",
        "api_name": "Leads",
        "moduleName": "Leads",
        "id": "678446000000000125"
      },
      "related_module": null,
      "deletable": true,
      "description": null,
      "language": "deluge",
      "source": "crm",
      "created_by": {
        "name": "Patricia Adams",
        "id": "678446000000280009"
      },
      "feature_type": "workflow",
      "modified_time": "2026-03-04T18:42:24+05:30",
      "associated": false,
      "function": {
        "api_name": "apidocfn",
        "id": "120851000000875001"
      },
      "name": "APIDocFn",
      "modified_by": {
        "name": "Patricia Adams",
        "id": "678446000000280009"
      },
      "arguments": [
        {
          "name": "mergeArg",
          "type": "merge_field",
          "value": "${!Leads.id}"
        },
        {
          "name": "argument",
          "type": "static",
          "value": "testingarg"
        }
      ],
      "id": "678446000051450070"
    }
  ]
}
```
