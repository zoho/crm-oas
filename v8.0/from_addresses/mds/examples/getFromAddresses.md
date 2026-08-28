# Examples: getFromAddresses

**GET /settings/emails/actions/from_addresses**

## Response examples

### Status `200` — `application/json` — GetFromAddressesResponseExample

Successful response with a single from-address entry

```json
{
  "from_addresses": [
    {
      "email": "example@zoho.com",
      "type": "user",
      "user_name": "Example User",
      "default": true
    }
  ]
}
```
