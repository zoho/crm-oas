# GET /org
**Operation:** `getOrganization` — Get organization details
> To retrieve the organization details associated with your Zoho CRM account.

**Responses:**

- **200**: Returns the organization details for the CRM account. [application/json]
    > Contains the organization details returned by the Get Organization operation.
    - `org` (array of object) [maxItems=1] **REQ** — Represents the list of organization details.
      schema: `OrgDetails`
      - `country` (object) — Represents the country of the organization.
        oneOf:
            type: string [maxLen=50] — Represents the country of the organization when a value is available.
            type: null — Represents a null value when no country is set for the organization.
      - `photo_id` (object) — Represents the photo ID of the organization's logo. Refer to [upload files API](https://www.zoho.com/crm/developer/docs/api/v8/upload-files-to-zfs.html) for more details.
        oneOf:
            type: string [maxLen=50] — Represents the photo ID of the organization's logo when one is available. Refer to the [POST - Upload Files to Zoho File System (ZFS) API](files.yaml#$.path./files.post) for more details.
            type: null — Represents a null value when no logo is set for the organization.
      - `city` (object) — Represents the city where the organization is located.
        oneOf:
            type: string [maxLen=50] — Represents the city where the organization is located when a value is available.
            type: null — Represents a null value when no city is set for the organization.
      - `description` (object) — Represents the description of the organization.
        oneOf:
            type: string [maxLen=250] — Represents the description of the organization when one is provided.
            type: null — Represents a null value when no description is set for the organization.
      - `type` (string) [enum=['bigin', 'production', 'sandbox', 'developer'], readOnly] — Represents the type of the Zoho CRM organization.
Possible values:
**bigin** - Bigin organization.
**production** - Standard production CRM organization.
**sandbox** - Sandbox organization for testing.
**developer** - Developer organization.
      - `created_time` (string/date-time) [readOnly] — Represents the creation date and time of the organization.
      - `mc_status` (boolean) [readOnly, nullable] — Indicates the multi-currency status of the organization.
Possible values:
**true** - Multi-currency is enabled.
**false** - Multi-currency is not enabled.
      - `gapps_enabled` (boolean) [readOnly] — Indicates whether Google Apps integration is enabled for the organization.
Possible values:
**true** - Google Apps integration is enabled.
**false** - Google Apps integration is not enabled.
      - `translation_enabled` (boolean) [readOnly] — Indicates whether translation is enabled for the organization.
Possible values:
**true** - Translation is enabled.
**false** - Translation is not enabled.
      - `street` (object) — Represents the street address of the organization.
        oneOf:
            type: string [maxLen=50] — Represents the street address of the organization when one is provided.
            type: null — Represents a null value when no street address is set for the organization.
      - `domain_name` (string) [maxLen=30, pattern=[a-z][a-z0-9]{4,30}] — Represents the domain name of the organization. For instance, org694902300.
      - `alias` (object) — Represents the alias name of the organization.
        oneOf:
            type: string [maxLen=50] — Represents the alias of the organization when one is set.
            type: null — Represents a null value when no alias is set for the organization.
      - `currency` (string) [maxLen=30] — Represents the home currency of the organization.
      - `id` (string) [maxLen=19, readOnly] — Represents the unique ID of the organization.
      - `employee_count` (object) — Represents the number of employees in the organization.
        oneOf:
            type: string [maxLen=18, pattern=[0-9]+] — Represents the number of employees in the organization when a value is available.
            type: null — Represents a null value when no employee count is set for the organization.
      - `state` (object) — Represents the state or province where the organization is located.
        oneOf:
            type: string [maxLen=50] — Represents the state or province of the organization when a value is available.
            type: null — Represents a null value when no state is set for the organization.
      - `fax` (object) — Represents the fax number of the organization.
        oneOf:
            type: string [maxLen=30] — Represents the fax number of the organization when one is provided.
            type: null — Represents a null value when no fax number is set for the organization.
      - `zip` (object) — Represents the postal code of the organization.
        oneOf:
            type: string [maxLen=20] — Represents the postal code of the organization when one is provided.
            type: null — Represents a null value when no postal code is set for the organization.
      - `website` (object) — Represents the website URL of the organization.
        oneOf:
            type: string [maxLen=50, pattern=^(http:\/\/www.|https:\/\/www.|ftp:\/\/www.|www.|http:\/\/|https:\/\/|ftp:\/\/|){1}[^\x00-\x19\x22-\x27\x2A-\x2C\x2E-\x2F\x3A-\x3F\x5B-\x5E\x60\x7B\x7D-\x7F]+(\.[^\x00-\x19\x22\x24-\x2C\x2E-\x2F\x3C\x3E\x40\x5B-\x5E\x60\x7B\x7D-\x7F]+)+([\/\?].*)*$] — Represents the website URL of the organization when one is provided.
            type: null — Represents a null value when no website is set for the organization.
      - `currency_symbol` (string) [maxLen=5, minLen=1] — Represents the currency symbol for the organization's home currency.
      - `mobile` (object) — Represents the mobile phone number of the organization.
        oneOf:
            type: string [maxLen=30, pattern=^[+]?([0-9A-Za-z()\.\-\s]){1,30}$] — Represents the mobile phone number of the organization when one is provided.
            type: null — Represents a null value when no mobile number is set for the organization.
      - `currency_locale` (string) [maxLen=10] — Represents the locale code for the organization's home currency. For instance, 'en_IN'.
      - `primary_zuid` (object) — Represents ZUID of the organization. This is the ID visible in the profile details in Zoho CRM UI.
        oneOf:
            type: string [maxLen=19] — Represents the Zoho user ID (ZUID) of the super admin when one is assigned.
            type: null [readOnly] — Represents a null value when no super admin is assigned to the organization.
      - `zia_portal_id` (object) — Represents Zia portal ID of the organization, if configured.
        oneOf:
            type: integer/int32 — Represents the Zia portal ID associated with the organization when one exists.
            type: null — Represents a null value when no Zia portal is associated with the organization.
      - `time_zone` (string) [maxLen=30] — Represents the time zone configured for the organization.
      - `zgid` (string) [maxLen=19, readOnly] — Represents the unique Zoho Group ID (ZGID) of the organization.
      - `country_code` (object) — Represents the country code of the organization.
        oneOf:
            type: string [maxLen=10] — Represents the country code of the organization when a value is available.
            type: null — Represents a null value when no country code is set for the organization.
      - `deletable_org_account` (boolean) [readOnly] — Indicates whether the organization account can be deleted.
Possible values:
**true** - The organization can be deleted.
**false** - The organization cannot be deleted.
      - `license_details` (object) — Represents the license and subscription details for the organization.
        - `paid_expiry` (object) — Represents the expiry date of the paid license for the organization.
          oneOf:
              type: string/date-time — Represents the license details variant.
              type: null — Represents the license details variant.
        - `users_license_purchased` (integer/int32) **REQ** [readOnly] — Represents the number of user licenses purchased for the organization.
        - `trial_type` (object) — Represents the type of trial subscription for the organization.
          oneOf:
              type: string [maxLen=50] — Represents the license details variant.
              type: null — Represents the license details variant.
        - `trial_expiry` (object) — Represents the expiry date of the trial subscription for the organization.
          oneOf:
              type: string/date-time — Represents the license details variant.
              type: null — Represents the license details variant.
        - `paid` (boolean) **REQ** [readOnly] — Indicates whether the organization has a paid subscription.
Possible values:
**true** - The organization has a paid subscription.
**false** - The organization does not have a paid subscription.
        - `paid_type` (string) **REQ** [enum=[7 values], readOnly] — Represents the license type for the organization.
Possible values:
**free** - Free edition.
**standard** - Standard edition.
**professional** - Professional edition.
**enterprise** - Enterprise edition.
**ultimate** - Ultimate edition.
**crmplus** - CRM Plus edition.
**zohoone** - Zoho One edition.
        - `portal_users_license_purchased` (integer/int32) **REQ** [readOnly] — Represents the number of portal user licenses purchased for the organization.
      - `hierarchy_preferences` (object) — Represents the hierarchy preferences configured for the organization.
        - `type` (string) **REQ** [enum=['Role_Hierarchy', 'Reporting_To_Hierarchy']] — Represents the hierarchy type configured for the organization. 
Possible values:
**Role_Hierarchy** - Access is based on the user's role in the hierarchy.
**Reporting_To_Hierarchy** - Access is based on the user's reporting structure.
        - `strictly_reporting` (boolean) [nullable] — Indicates whether data visibility is restricted to the direct reporting chain.
Possible values:
**true** - Data is visible only to the CEO and administrators.
**false** - Data is visible to any user higher in the hierarchy.
      - `phone` (object) — Represents the primary phone number of the organization.
        oneOf:
            type: string [maxLen=30, pattern=^[+]?([0-9A-Za-z()\.\-\s]){1,30}$] — Represents the phone number of the organization when one is provided.
            type: null — Represents a null value when no phone number is set for the organization.
      - `company_name` (object) — Represents the name of the organization.
        oneOf:
            type: string [maxLen=100] — Represents the name of the organization when one is set.
            type: null [readOnly] — Represents a null value when the company name has not been set.
      - `privacy_settings` (boolean) [readOnly] — Indicates whether privacy settings are enabled for the organization.
Possible values:
**true** - Privacy settings are enabled.
**false** - Privacy settings are not enabled.
      - `primary_email` (object) — Represents the email address of the super admin of the organization.
        oneOf:
            type: string [maxLen=100, pattern=^[\+\-\p{L}\p{M}\p{N}_]([\p{L}\p{M}\p{N}!#$%&'*+\-\/=?^_`{|}~.]*)@(?=.{4,256}$)(([\p{L}\p{N}\p{M}]+)(([\-_]*[\p{L}\p{M}\p{N}])*)[.])+[\p{L}\p{M}]{2,22}$] — Represents the email address of the super admin when one is assigned to the organization.
            type: null — Represents a null value when no super admin is assigned to the organization.
      - `iso_code` (string) [maxLen=10] — Represents the ISO code of the organization's home currency.
      - `hipaa_compliance_enabled` (boolean) [readOnly] — Indicates whether [HIPAA compliance](https://www.zoho.com/crm/developer/docs/api/v8/hipaa-compliance.html) is enabled for the organization.
Possible values:
**true** - HIPAA compliance is enabled.
**false** - HIPAA compliance is not enabled.
      - `lite_users_enabled` (boolean) — Indicates whether lite users are enabled for the organization.
Possible values:
**true** - Lite users are enabled.
**false** - Lite users are not enabled.

**Scopes:** ZohoCRM.org.READ
