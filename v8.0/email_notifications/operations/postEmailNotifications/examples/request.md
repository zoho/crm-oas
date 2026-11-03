### `application/json` — SamplePostRequest

Create an email notification for the Deals module with multiple recipient types

```json
{
  "email_notifications": [
    {
      "bulk_email": false,
      "module": {
        "api_name": "Deals",
        "id": "6660682000000002181"
      },
      "name": "BigDealNotify",
      "recipients": {
        "to": [
          {
            "details": {
              "api_name": "${!Deals.Created_By}"
            },
            "type": "merge_field"
          },
          {
            "details": {
              "api_name": "${!Deals.Owner}"
            },
            "type": "merge_field"
          },
          {
            "details": {
              "api_name": "${!Deals.Owner.Reporting_To}"
            },
            "type": "merge_field"
          },
          {
            "details": {
              "api_name": "${!Deals.Campaign_Source.Owner}"
            },
            "type": "merge_field"
          },
          {
            "details": {
              "api_name": "${!Deals.Campaign_Source.Created_By}"
            },
            "type": "merge_field"
          },
          {
            "details": {
              "api_name": "${!Deals.Account_Name.Owner}"
            },
            "type": "merge_field"
          },
          {
            "details": {
              "api_name": "${!Deals.Account_Name.Created_By}"
            },
            "type": "merge_field"
          },
          {
            "resource": {
              "name": "Patricia Boyle",
              "id": "6660682000000501001"
            },
            "type": "user"
          },
          {
            "details": {
              "api_name": "${!Deals.Contact_Name.Email}"
            },
            "type": "merge_field"
          },
          {
            "resource": {
              "name": "UserGroup",
              "id": "6660682000001441002"
            },
            "type": "group"
          },
          {
            "resource": {
              "name": "CEO",
              "id": "6660682000000026005"
            },
            "type": "role"
          },
          {
            "resource": {
              "name": "Manager",
              "id": "6660682000000026008"
            },
            "type": "role_and_subordinate"
          },
          {
            "resource": {
              "name": "Territory_EU",
              "id": "6660682000001453003"
            },
            "type": "territory"
          },
          {
            "resource": {
              "name": "CEO",
              "id": "6660682000001454004"
            },
            "type": "territory_and_subterritory"
          }
        ]
      },
      "from_address": {
        "resource": {
          "id": "6660682000000501001"
        },
        "type": "user"
      },
      "reply_to_address": {
        "resource": {
          "id": "6660682000000501001"
        },
        "type": "user"
      },
      "template": {
        "name": "Big Deal Alert",
        "id": "6660682000000000079"
      }
    }
  ]
}
```
