# Examples: getOrganization

**GET /org**

## Response examples

### Status `200` — `application/json` — OrgGetResponse

Successful retrieval of organization details

```json
{
  "org": [
    {
      "country": "US",
      "photo_id": null,
      "city": "Austin",
      "description": "Main office",
      "type": "production",
      "created_time": "2023-01-01T12:00:00Z",
      "mc_status": true,
      "gapps_enabled": false,
      "translation_enabled": false,
      "street": "123 Main St",
      "domain_name": "acmeinc",
      "alias": "acme",
      "currency": "US Dollar - USD",
      "id": "1234567890",
      "employee_count": "100",
      "state": "TX",
      "fax": null,
      "zip": "78701",
      "website": "www.acmeinc.com",
      "currency_symbol": "$",
      "mobile": null,
      "currency_locale": "USD",
      "primary_zuid": "zuid123",
      "zia_portal_id": null,
      "time_zone": "America/Chicago",
      "zgid": "zgid123",
      "country_code": "US",
      "deletable_org_account": false,
      "license_details": {
        "paid_expiry": null,
        "users_license_purchased": 3,
        "trial_type": "enterprise",
        "trial_expiry": "2025-12-04T17:26:17+05:30",
        "paid": false,
        "paid_type": "free",
        "portal_users_license_purchased": 0,
        "trial_action": "Update Evaluation"
      },
      "hierarchy_preferences": {
        "type": "Role_Hierarchy",
        "strictly_reporting": false
      },
      "phone": "+915551234",
      "company_name": "Acme Inc.",
      "privacy_settings": true,
      "primary_email": "acmeadmin@acmei.com",
      "iso_code": "US",
      "hipaa_compliance_enabled": false,
      "lite_users_enabled": false,
      "max_per_page": 200,
      "ezgid": "ezgid123",
      "call_icon": "show",
      "oauth_presence": true,
      "zia_zgid": 12345,
      "checkin_preferences": {
        "restricted_event_types": null
      }
    }
  ]
}
```
