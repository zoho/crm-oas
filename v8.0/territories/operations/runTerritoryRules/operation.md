# POST /settings/territories/actions/run_rules
**Operation:** `runTerritoryRules` — Run territory assignment rules
> To schedule territory assignment rules to run against records in a specified module in your Zoho CRM organization. The rules can be applied based on filter criteria, a Custom View, or specific territories, and the execution is queued as a background job.

**Tags:** Territories

**Schemas:**
`BetweenFilterCriterionRequest`:
  > Represents a filter criterion for the between and not_between comparators. The value must be an array of exactly two elements — [lower_bound, upper_bound]. The value type is determined by the field's data_type: use SimpleFilterCriterionValueString for date or datetime fields, and SimpleFilterCriterionValueNumber for integer, currency, or double fields. Resolve the data_type from the field's FieldSchema. For formula fields, use formula.return_type as the effective data_type; for rollup_summary fields, use rollup_summary.return_type.
  - `field` (object) **REQ** — Represents the target field definition to which the range filter criterion is applied, conforming to the base field structure.
  - `comparator` (string) **REQ** [enum=['between', 'not_between']] — Represents the range comparison operator applied to the criterion, indicating whether the field value falls within or outside the specified bounds.
Possible values:
between - Matches records where the field value falls within the specified range.
not_between - Matches records where the field value falls outside the specified range.
  - `value` (array of object) [minItems=2, maxItems=2] **REQ** — Contains the two boundary values — [lower_bound, upper_bound] — against which the field is evaluated for the between or not_between comparator.
    oneOf:
      - `SimpleFilterCriterionValueString` (string) [maxLen=255] — Represents a string filter criterion value applicable to fields with a data_type of text, textarea, email, phone, website, autonumber, picklist, multiselectpicklist, date, or datetime, as well as any data_type not explicitly covered by SimpleFilterCriterionValueNumber, SimpleFilterCriterionValueBoolean, SimpleFilterCriterionValueObjectRequest, SimpleFilterCriterionValueObjectResponse, or the multiselect lookup value schemas.
      - `SimpleFilterCriterionValueNumber` (number) — Represents a numeric filter criterion value applicable to fields with a data_type of integer, currency, or double.
  - `type` (string) [enum=['merge_field', 'pre_defined', 'value', 'field'], default=value] — Indicates the value resolution mode of the criterion, distinguishing whether the filter value is a literal value, a merge field reference, a predefined system variable, or another field reference.
Possible values:
value - The value is a direct literal.
merge_field - The value is a merge field reference.
pre_defined - The value is a predefined system variable placeholder.
field - The value references another field.
`EqualFilterCriterionRequest`:
  > Represents a filter criterion for the equal comparator. The value type is determined by the field's data_type: use SimpleFilterCriterionValueString for text, textarea, email, phone, website, autonumber, picklist, multiselectpicklist, date, or datetime fields; SimpleFilterCriterionValueNumber for integer, currency, or double fields; SimpleFilterCriterionValueBoolean for Boolean fields; SimpleFilterCriterionValueObjectRequest for lookup, ownerlookup, or userlookup fields; and SimpleFilterCriterionValueObjectPredefined for predefined user or role object placeholders. Accepts scalar or array values. Resolve the data_type from the field's FieldSchema.
  - `field` (object) **REQ** — Represents the target field definition to which the equal filter criterion is applied, conforming to the base field structure.
  - `comparator` (string) **REQ** [enum=['equal']] — Represents the equal comparison operator applied to the criterion.
Possible values:
equal - Matches records where the field value equals the specified filter value.
  - `value` (object) **REQ** — Represents the filter value used in the equal comparator. Accepts a scalar or an array of values, depending on the field's data_type.
    anyOf:
        type: array of object [minItems=1, maxItems=500]
          oneOf:
            - `SimpleFilterCriterionValueString` (string) [maxLen=255] — Represents a string filter criterion value applicable to fields with a data_type of text, textarea, email, phone, website, autonumber, picklist, multiselectpicklist, date, or datetime, as well as any data_type not explicitly covered by SimpleFilterCriterionValueNumber, SimpleFilterCriterionValueBoolean, SimpleFilterCriterionValueObjectRequest, SimpleFilterCriterionValueObjectResponse, or the multiselect lookup value schemas.
            - `SimpleFilterCriterionValueNumber` (number) — Represents a numeric filter criterion value applicable to fields with a data_type of integer, currency, or double.
              anyOf:
                - `SimpleFilterCriterionValueObjectRequest` — Represents a lookup object filter criterion value for request bodies, applicable when the field's data_type is lookup, ownerlookup, or userlookup. The ID property is required.
                - `SimpleFilterCriterionValueObjectPredefined` — Represents a predefined placeholder object filter criterion value for lookup fields, applicable with equal or not_equal comparators when the field's data_type is ownerlookup or userlookup. Two forms are supported: (1) the currently logged-in user, represented by passing only the name property with the predefined value ${CURRENTUSER} and no ID property; and (2) the logged-in user's role, represented by passing the ID property with the predefined value ${CURRENTUSERROLE} and an optional display label in the name property. For specific real users or roles that are not predefined, use SimpleFilterCriterionValueObjectRequest, which requires the ID property.
      - `SimpleFilterCriterionValueString` (string) [maxLen=255] — Represents a string filter criterion value applicable to fields with a data_type of text, textarea, email, phone, website, autonumber, picklist, multiselectpicklist, date, or datetime, as well as any data_type not explicitly covered by SimpleFilterCriterionValueNumber, SimpleFilterCriterionValueBoolean, SimpleFilterCriterionValueObjectRequest, SimpleFilterCriterionValueObjectResponse, or the multiselect lookup value schemas.
      - `SimpleFilterCriterionValueNumber` (number) — Represents a numeric filter criterion value applicable to fields with a data_type of integer, currency, or double.
      - `SimpleFilterCriterionValueBoolean` (boolean) — Represents a Boolean filter criterion value. Applicable only when the field has a Boolean data type (checkbox field).
      - `SimpleFilterCriterionValueObjectRequest` — Represents a lookup object filter criterion value for request bodies, applicable when the field's data_type is lookup, ownerlookup, or userlookup. The ID property is required.
      - `SimpleFilterCriterionValueObjectPredefined` — Represents a predefined placeholder object filter criterion value for lookup fields, applicable with equal or not_equal comparators when the field's data_type is ownerlookup or userlookup. Two forms are supported: (1) the currently logged-in user, represented by passing only the name property with the predefined value ${CURRENTUSER} and no ID property; and (2) the logged-in user's role, represented by passing the ID property with the predefined value ${CURRENTUSERROLE} and an optional display label in the name property. For specific real users or roles that are not predefined, use SimpleFilterCriterionValueObjectRequest, which requires the ID property.
      - `SimpleFilterCriterionValueGeneralPredefined` (string) [enum=['${EMPTY}', '${NOTEMPTY}']] — Represents a predefined placeholder value applicable to any field data_type with the equal comparator.
Possible values:
${EMPTY} - Matches records where the field has no value.
${NOTEMPTY} - Matches records where the field has any non-empty value.
      - `SimpleFilterCriterionValueDateTimePredefined` (string) [enum=[22 values]] — Represents a predefined placeholder value applicable only when the field's data_type is date or datetime, with the equal comparator.
      - `SimpleFilterCriterionValueNDaysPredefined` (string) [maxLen=255, pattern=^\$\{(LAST_N_|NEXT_N_)(DAYS|WEEKS|MONTHS|YEARS):([0-9]+)\}$] — Represents a predefined N-period range placeholder value applicable only when the field's data_type is date or datetime, with the equal comparator. Follows the pattern ${NEXT_N_<PERIOD>:<n>} or ${LAST_N_<PERIOD>:<n>}, where PERIOD is DAYS, WEEKS, MONTHS, or YEARS and n is a positive integer. The current period is always excluded from the range.
      - `SimpleFilterCriterionValueAgeDuePredefined` (string) [maxLen=255, pattern=^\$\{(AGEINDAYS|DUEINDAYS)\}\+[0-9]+$] — Represents a predefined age or due-in-days placeholder value applicable only when the field's data_type is date or datetime. Follows the pattern ${AGEINDAYS}+<n> for records where the date field was exactly n days in the past, or ${DUEINDAYS}+<n> for records where the date field is exactly n days in the future. Supported comparators are equal, not_equal, less_than, greater_than, less_equal, and greater_equal.
  - `type` (string) [enum=['merge_field', 'pre_defined', 'value', 'field'], default=value] — Indicates the value resolution mode of the criterion, distinguishing whether the filter value is a literal value, a merge field reference, a predefined system variable, or another field reference.
Possible values:
value - The value is a direct literal.
merge_field - The value is a merge field reference.
pre_defined - The value is a predefined system variable placeholder.
field - The value references another field.
`EqualityFilterCriterionRequest`:
  oneOf:
    - `EqualFilterCriterionRequest` — Represents a filter criterion for the equal comparator. The value type is determined by the field's data_type: use SimpleFilterCriterionValueString for text, textarea, email, phone, website, autonumber, picklist, multiselectpicklist, date, or datetime fields; SimpleFilterCriterionValueNumber for integer, currency, or double fields; SimpleFilterCriterionValueBoolean for Boolean fields; SimpleFilterCriterionValueObjectRequest for lookup, ownerlookup, or userlookup fields; and SimpleFilterCriterionValueObjectPredefined for predefined user or role object placeholders. Accepts scalar or array values. Resolve the data_type from the field's FieldSchema.
    - `NotEqualFilterCriterionRequest` — Represents a filter criterion for the not_equal comparator. The value type is determined by the field's data_type: use SimpleFilterCriterionValueString for text, textarea, email, phone, website, autonumber, picklist, multiselectpicklist, date, or datetime fields; SimpleFilterCriterionValueNumber for integer, currency, or double fields; SimpleFilterCriterionValueBoolean for Boolean fields; SimpleFilterCriterionValueObjectRequest for lookup, ownerlookup, or userlookup fields; and SimpleFilterCriterionValueObjectPredefined for predefined user or role object placeholders.
`FilterFieldBase`:
  > Represents the base field reference used in filter operations, containing minimal required properties. The field's data_type is not part of this object; resolve it from the corresponding FieldSchema. For formula fields, use formula.return_type as the effective data_type; for rollup_summary fields, use rollup_summary.return_type.
  - `id` (string/int64) — Represents the unique ID of the field used for filter operations.
  - `api_name` (string) **REQ** — Represents the API name of the field used for filter application. Supports relationship notation, for example, Deals__r.Stage.
  additionalProperties: any
`GroupedFilterCriterionRequest`:
  > Represents a grouped filter criterion containing multiple filter conditions evaluated with a logical operator. Supports recursive nesting for complex filtering logic.
  - `group` (array of object) [minItems=2, maxItems=25] **REQ** — Contains an array of filter conditions grouped together and evaluated with the specified logical operator.
    oneOf:
      - `SimpleFilterCriterionRequest` — Represents a simple field-based filter criterion that dispatches to the appropriate comparator-specific schema. The equal and not_equal comparators support scalar or array values; text comparators support scalar or array strings; ordering comparators require a scalar; between and not_between comparators require a two-element array; in and not_in comparators require an array of primitives; and include_all, include_any, exclude_all, and exclude_any comparators require an array of lookup objects and apply only when the field's data_type is multiuserlookup or multiselectlookup.
      - `GroupedFilterCriterionRequest` — Represents a grouped filter criterion containing multiple filter conditions evaluated with a logical operator. Supports recursive nesting for complex filtering logic.
  - `group_operator` (string) **REQ** [enum=['AND', 'OR', 'and', 'or']] — Represents the logical operator applied between the filter conditions in the group.
Possible values:
AND - All conditions in the group must be satisfied.
OR - At least one condition in the group must be satisfied.
and - Equivalent to AND; all conditions in the group must be satisfied.
or - Equivalent to OR; at least one condition in the group must be satisfied.
`MultiSelectLookupFilterCriterionRequest`:
  > Represents a filter criterion for the include_all, include_any, exclude_all, and exclude_any comparators. Applicable only when the field's data_type is multiuserlookup or multiselectlookup. The value must be an array of SimpleFilterCriterionValueObjectRequest lookup objects.
  - `field` (object) **REQ** — Represents the target field definition to which the multi-select lookup filter criterion is applied. The field must have a data_type of multiuserlookup or multiselectlookup.
  - `comparator` (string) **REQ** [enum=['include_all', 'include_any', 'exclude_all', 'exclude_any']] — Represents the multi-select lookup comparison operator applied to the criterion. Applicable only when the field's data_type is multiuserlookup or multiselectlookup.
Possible values:
include_all - Matches records that include all specified lookup values.
include_any - Matches records that include at least one of the specified lookup values.
exclude_all - Matches records that exclude all specified lookup values.
exclude_any - Matches records that exclude at least one of the specified lookup values.
  - `value` (array of object `SimpleFilterCriterionValueObjectRequest`) [minItems=1, maxItems=5] **REQ** — Contains an array of lookup object references used in the multi-select comparison.
  - `type` (string) [enum=['merge_field', 'pre_defined', 'value', 'field'], default=value] — Indicates the value resolution mode of the criterion, distinguishing whether the filter value is a literal value, a merge field reference, a predefined system variable, or another field reference.
Possible values:
value - The value is a direct literal.
merge_field - The value is a merge field reference.
pre_defined - The value is a predefined system variable placeholder.
field - The value references another field.
`NotEqualFilterCriterionRequest`:
  > Represents a filter criterion for the not_equal comparator. The value type is determined by the field's data_type: use SimpleFilterCriterionValueString for text, textarea, email, phone, website, autonumber, picklist, multiselectpicklist, date, or datetime fields; SimpleFilterCriterionValueNumber for integer, currency, or double fields; SimpleFilterCriterionValueBoolean for Boolean fields; SimpleFilterCriterionValueObjectRequest for lookup, ownerlookup, or userlookup fields; and SimpleFilterCriterionValueObjectPredefined for predefined user or role object placeholders.
  - `field` (object) **REQ** — Represents the target field definition to which the not-equal filter criterion is applied, conforming to the base field structure.
  - `comparator` (string) **REQ** [enum=['not_equal']] — Represents the not-equal comparison operator applied to the criterion.
Possible values:
not_equal - Matches records where the field value does not equal the specified filter value.
  - `value` (object) **REQ** — Represents the filter value used in the not_equal comparator. Accepts a scalar or an array of values, depending on the field's data_type.
    anyOf:
        type: array of object [minItems=1, maxItems=500]
          oneOf:
            - `SimpleFilterCriterionValueString` (string) [maxLen=255] — Represents a string filter criterion value applicable to fields with a data_type of text, textarea, email, phone, website, autonumber, picklist, multiselectpicklist, date, or datetime, as well as any data_type not explicitly covered by SimpleFilterCriterionValueNumber, SimpleFilterCriterionValueBoolean, SimpleFilterCriterionValueObjectRequest, SimpleFilterCriterionValueObjectResponse, or the multiselect lookup value schemas.
            - `SimpleFilterCriterionValueNumber` (number) — Represents a numeric filter criterion value applicable to fields with a data_type of integer, currency, or double.
              anyOf:
                - `SimpleFilterCriterionValueObjectRequest` — Represents a lookup object filter criterion value for request bodies, applicable when the field's data_type is lookup, ownerlookup, or userlookup. The ID property is required.
                - `SimpleFilterCriterionValueObjectPredefined` — Represents a predefined placeholder object filter criterion value for lookup fields, applicable with equal or not_equal comparators when the field's data_type is ownerlookup or userlookup. Two forms are supported: (1) the currently logged-in user, represented by passing only the name property with the predefined value ${CURRENTUSER} and no ID property; and (2) the logged-in user's role, represented by passing the ID property with the predefined value ${CURRENTUSERROLE} and an optional display label in the name property. For specific real users or roles that are not predefined, use SimpleFilterCriterionValueObjectRequest, which requires the ID property.
      - `SimpleFilterCriterionValueString` (string) [maxLen=255] — Represents a string filter criterion value applicable to fields with a data_type of text, textarea, email, phone, website, autonumber, picklist, multiselectpicklist, date, or datetime, as well as any data_type not explicitly covered by SimpleFilterCriterionValueNumber, SimpleFilterCriterionValueBoolean, SimpleFilterCriterionValueObjectRequest, SimpleFilterCriterionValueObjectResponse, or the multiselect lookup value schemas.
      - `SimpleFilterCriterionValueNumber` (number) — Represents a numeric filter criterion value applicable to fields with a data_type of integer, currency, or double.
      - `SimpleFilterCriterionValueBoolean` (boolean) — Represents a Boolean filter criterion value. Applicable only when the field has a Boolean data type (checkbox field).
      - `SimpleFilterCriterionValueObjectRequest` — Represents a lookup object filter criterion value for request bodies, applicable when the field's data_type is lookup, ownerlookup, or userlookup. The ID property is required.
      - `SimpleFilterCriterionValueObjectPredefined` — Represents a predefined placeholder object filter criterion value for lookup fields, applicable with equal or not_equal comparators when the field's data_type is ownerlookup or userlookup. Two forms are supported: (1) the currently logged-in user, represented by passing only the name property with the predefined value ${CURRENTUSER} and no ID property; and (2) the logged-in user's role, represented by passing the ID property with the predefined value ${CURRENTUSERROLE} and an optional display label in the name property. For specific real users or roles that are not predefined, use SimpleFilterCriterionValueObjectRequest, which requires the ID property.
      - `SimpleFilterCriterionValueAgeDuePredefined` (string) [maxLen=255, pattern=^\$\{(AGEINDAYS|DUEINDAYS)\}\+[0-9]+$] — Represents a predefined age or due-in-days placeholder value applicable only when the field's data_type is date or datetime. Follows the pattern ${AGEINDAYS}+<n> for records where the date field was exactly n days in the past, or ${DUEINDAYS}+<n> for records where the date field is exactly n days in the future. Supported comparators are equal, not_equal, less_than, greater_than, less_equal, and greater_equal.
  - `type` (string) [enum=['merge_field', 'pre_defined', 'value', 'field'], default=value] — Indicates the value resolution mode of the criterion, distinguishing whether the filter value is a literal value, a merge field reference, a predefined system variable, or another field reference.
Possible values:
value - The value is a direct literal.
merge_field - The value is a merge field reference.
pre_defined - The value is a predefined system variable placeholder.
field - The value references another field.
`OrderingFilterCriterionRequest`:
  > Represents a filter criterion for the less_than, less_equal, greater_than, and greater_equal comparators. The value must be a scalar; arrays and objects are not supported. The value type is determined by the field's data_type: use SimpleFilterCriterionValueString for date or datetime fields, and SimpleFilterCriterionValueNumber for integer, currency, or double fields.
  - `field` (object) **REQ** — Represents the target field definition to which the ordering filter criterion is applied, conforming to the base field structure.
  - `comparator` (string) **REQ** [enum=['less_than', 'less_equal', 'greater_than', 'greater_equal']] — Represents the ordering comparison operator applied to the criterion.
Possible values:
less_than - Matches records where the field value is less than the specified filter value.
less_equal - Matches records where the field value is less than or equal to the specified filter value.
greater_than - Matches records where the field value is greater than the specified filter value.
greater_equal - Matches records where the field value is greater than or equal to the specified filter value.
  - `value` (object) **REQ** — Represents the scalar filter value used in the ordering comparator. Arrays and objects are not supported for ordering comparators.
    anyOf:
      - `SimpleFilterCriterionValueString` (string) [maxLen=255] — Represents a string filter criterion value applicable to fields with a data_type of text, textarea, email, phone, website, autonumber, picklist, multiselectpicklist, date, or datetime, as well as any data_type not explicitly covered by SimpleFilterCriterionValueNumber, SimpleFilterCriterionValueBoolean, SimpleFilterCriterionValueObjectRequest, SimpleFilterCriterionValueObjectResponse, or the multiselect lookup value schemas.
      - `SimpleFilterCriterionValueNumber` (number) — Represents a numeric filter criterion value applicable to fields with a data_type of integer, currency, or double.
      - `SimpleFilterCriterionValueAgeDuePredefined` (string) [maxLen=255, pattern=^\$\{(AGEINDAYS|DUEINDAYS)\}\+[0-9]+$] — Represents a predefined age or due-in-days placeholder value applicable only when the field's data_type is date or datetime. Follows the pattern ${AGEINDAYS}+<n> for records where the date field was exactly n days in the past, or ${DUEINDAYS}+<n> for records where the date field is exactly n days in the future. Supported comparators are equal, not_equal, less_than, greater_than, less_equal, and greater_equal.
  - `type` (string) [enum=['merge_field', 'pre_defined', 'value', 'field'], default=value] — Indicates the value resolution mode of the criterion, distinguishing whether the filter value is a literal value, a merge field reference, a predefined system variable, or another field reference.
Possible values:
value - The value is a direct literal.
merge_field - The value is a merge field reference.
pre_defined - The value is a predefined system variable placeholder.
field - The value references another field.
`SetFilterCriterionRequest`:
  > Represents a filter criterion for the in and not_in comparators. The value must be an array of primitive values. The value type is determined by the field's data_type: use SimpleFilterCriterionValueString for text-based types, and SimpleFilterCriterionValueNumber for integer, currency, or double fields.
  - `field` (object) **REQ** — Represents the target field definition to which the set filter criterion is applied, conforming to the base field structure.
  - `comparator` (string) **REQ** [enum=['in', 'not_in']] — Represents the set membership comparison operator applied to the criterion.
Possible values:
in - Matches records where the field value is in the specified set of values.
not_in - Matches records where the field value is not in the specified set of values.
  - `value` (array of object) [minItems=1, maxItems=500] **REQ** — Contains an array of primitive filter values used in the set comparison.
    oneOf:
      - `SimpleFilterCriterionValueString` (string) [maxLen=255] — Represents a string filter criterion value applicable to fields with a data_type of text, textarea, email, phone, website, autonumber, picklist, multiselectpicklist, date, or datetime, as well as any data_type not explicitly covered by SimpleFilterCriterionValueNumber, SimpleFilterCriterionValueBoolean, SimpleFilterCriterionValueObjectRequest, SimpleFilterCriterionValueObjectResponse, or the multiselect lookup value schemas.
      - `SimpleFilterCriterionValueNumber` (number) — Represents a numeric filter criterion value applicable to fields with a data_type of integer, currency, or double.
  - `type` (string) [enum=['merge_field', 'pre_defined', 'value', 'field'], default=value] — Indicates the value resolution mode of the criterion, distinguishing whether the filter value is a literal value, a merge field reference, a predefined system variable, or another field reference.
Possible values:
value - The value is a direct literal.
merge_field - The value is a merge field reference.
pre_defined - The value is a predefined system variable placeholder.
field - The value references another field.
`SimpleFilterCriterionRequest`:
  oneOf:
    - `EqualityFilterCriterionRequest` — Represents an equality filter criterion that dispatches to either the EqualFilterCriterionRequest or NotEqualFilterCriterionRequest schema based on the comparator value.
    - `TextFilterCriterionRequest` — Represents a filter criterion for the like, not_like, starts_with, ends_with, contains, and not_contains comparators. The value must be a string scalar or array; use SimpleFilterCriterionValueString for text-based field types. Object and Boolean values are not supported. Resolve the data_type from the field's FieldSchema.
    - `OrderingFilterCriterionRequest` — Represents a filter criterion for the less_than, less_equal, greater_than, and greater_equal comparators. The value must be a scalar; arrays and objects are not supported. The value type is determined by the field's data_type: use SimpleFilterCriterionValueString for date or datetime fields, and SimpleFilterCriterionValueNumber for integer, currency, or double fields.
    - `BetweenFilterCriterionRequest` — Represents a filter criterion for the between and not_between comparators. The value must be an array of exactly two elements — [lower_bound, upper_bound]. The value type is determined by the field's data_type: use SimpleFilterCriterionValueString for date or datetime fields, and SimpleFilterCriterionValueNumber for integer, currency, or double fields. Resolve the data_type from the field's FieldSchema. For formula fields, use formula.return_type as the effective data_type; for rollup_summary fields, use rollup_summary.return_type.
    - `SetFilterCriterionRequest` — Represents a filter criterion for the in and not_in comparators. The value must be an array of primitive values. The value type is determined by the field's data_type: use SimpleFilterCriterionValueString for text-based types, and SimpleFilterCriterionValueNumber for integer, currency, or double fields.
    - `MultiSelectLookupFilterCriterionRequest` — Represents a filter criterion for the include_all, include_any, exclude_all, and exclude_any comparators. Applicable only when the field's data_type is multiuserlookup or multiselectlookup. The value must be an array of SimpleFilterCriterionValueObjectRequest lookup objects.
`SimpleFilterCriterionValueObjectBase`:
  > Represents the base minified record structure of a lookup module, containing the record's unique identifier and display name.
  - `id` (string/int64) — Represents the unique ID of the lookup module record.
  - `name` (string) [maxLen=255] — Represents the display name of the lookup module record.
  additionalProperties: any
`SimpleFilterCriterionValueObjectPredefined`:
  oneOf:
      - `name` (string) **REQ** [enum=['${CURRENTUSER}']] — Represents the predefined placeholder for the currently logged-in user.
Possible values:
${CURRENTUSER} - Represents the currently logged-in user.
      - `id` (string) **REQ** [enum=['${CURRENTUSERROLE}']] — Represents the predefined placeholder for the logged-in user's role record ID.
Possible values:
${CURRENTUSERROLE} - Represents the role of the currently logged-in user.
      - `name` (string) [maxLen=255] — Represents an optional display label for the predefined role, such as Logged in User Role.
      additionalProperties: any
`SimpleFilterCriterionValueObjectRequest`:
  > Represents the base minified record structure of a lookup module, containing the record's unique identifier and display name.
  - `id` (object) **REQ**
  - `name` (string) [maxLen=255] — Represents the display name of the lookup module record.
  additionalProperties: any
`TerritoryRuleModuleReference`:
  - `id` (string/int64) — Represents the unique identifier of the module associated with the territory rule.
  - `api_name` (string) [maxLen=50] — Represents the API name of the module associated with the territory rule.
  anyOf:
`TextFilterCriterionRequest`:
  > Represents a filter criterion for the like, not_like, starts_with, ends_with, contains, and not_contains comparators. The value must be a string scalar or array; use SimpleFilterCriterionValueString for text-based field types. Object and Boolean values are not supported. Resolve the data_type from the field's FieldSchema.
  - `field` (object) **REQ** — Represents the target field definition to which the text filter criterion is applied, conforming to the base field structure.
  - `comparator` (string) **REQ** [enum=['like', 'not_like', 'starts_with', 'ends_with', 'contains', 'not_contains']] — Represents the text comparison operator applied to the criterion.
Possible values:
like - Matches records where the field value contains the specified pattern.
not_like - Matches records where the field value does not contain the specified pattern.
starts_with - Matches records where the field value begins with the specified string.
ends_with - Matches records where the field value ends with the specified string.
contains - Matches records where the field value contains the specified string.
not_contains - Matches records where the field value does not contain the specified string.
  - `value` (object) **REQ** — Represents the string filter value used in the text comparator. Accepts a scalar string or an array of string values.
    oneOf:
        type: array of object [minItems=1, maxItems=500]
          oneOf:
            - `SimpleFilterCriterionValueString` (string) [maxLen=255] — Represents a string filter criterion value applicable to fields with a data_type of text, textarea, email, phone, website, autonumber, picklist, multiselectpicklist, date, or datetime, as well as any data_type not explicitly covered by SimpleFilterCriterionValueNumber, SimpleFilterCriterionValueBoolean, SimpleFilterCriterionValueObjectRequest, SimpleFilterCriterionValueObjectResponse, or the multiselect lookup value schemas.
      - `SimpleFilterCriterionValueString` (string) [maxLen=255] — Represents a string filter criterion value applicable to fields with a data_type of text, textarea, email, phone, website, autonumber, picklist, multiselectpicklist, date, or datetime, as well as any data_type not explicitly covered by SimpleFilterCriterionValueNumber, SimpleFilterCriterionValueBoolean, SimpleFilterCriterionValueObjectRequest, SimpleFilterCriterionValueObjectResponse, or the multiselect lookup value schemas.
  - `type` (string) [enum=['merge_field', 'pre_defined', 'value', 'field'], default=value] — Indicates the value resolution mode of the criterion, distinguishing whether the filter value is a literal value, a merge field reference, a predefined system variable, or another field reference.
Possible values:
value - The value is a direct literal.
merge_field - The value is a merge field reference.
pre_defined - The value is a predefined system variable placeholder.
field - The value references another field.

**Request Body** (required) — application/json
> The request body must contain a **run_rules** object with one of the following execution configurations: criteria-based, Custom View-based, or territory-based.
  > Specify the configuration for scheduling territory rule execution. The schema supports three execution methods: criteria-based, Custom View-based, and territory-based.
  - `run_rules` (object) **REQ** — Specify the configuration for territory rule execution. The **run_rules** object must match one of three execution methods: criteria-based, Custom View-based, or territory-based.
    oneOf:
        - `module` (object `TerritoryRuleModuleReference`) **REQ** — Specify the API name of the module for which to run territory assignment rules.
        - `based_on` (string) **REQ** [enum=['criteria']] — Specify the execution method for territory assignment rules.
Possible values:
**criteria** - Runs territory rules against records matching a specified filter criterion.
        - `criteria` (object `FilterCriterionRequest`) **REQ** — Filter criteria for territory rule execution.
          oneOf:
            - `SimpleFilterCriterionRequest` — Represents a simple field-based filter criterion that dispatches to the appropriate comparator-specific schema. The equal and not_equal comparators support scalar or array values; text comparators support scalar or array strings; ordering comparators require a scalar; between and not_between comparators require a two-element array; in and not_in comparators require an array of primitives; and include_all, include_any, exclude_all, and exclude_any comparators require an array of lookup objects and apply only when the field's data_type is multiuserlookup or multiselectlookup.
            - `GroupedFilterCriterionRequest` — Represents a grouped filter criterion containing multiple filter conditions evaluated with a logical operator. Supports recursive nesting for complex filtering logic.
        - `module` (object `TerritoryRuleModuleReference`) **REQ** — Specify the API name of the module for which to run territory assignment rules.
        - `based_on` (string) **REQ** [enum=['custom_view']] — Specify the execution method for territory assignment rules.
Possible values:
**custom_view** - Runs territory rules against records included in a specified Custom View.
        - `custom_view` (object) **REQ** — Specify the Custom View for which the territory assignment rules apply. Provide either the **ID** or the **api_name** of the Custom View.
          - `id` (string/int64) [maxLen=25] — Specify the unique identifier of the Custom View for which the territory assignment rules apply.
          - `api_name` (string) [maxLen=100] — Specify the API name of the Custom View for which the territory assignment rules apply.
          anyOf:
        - `module` (object `TerritoryRuleModuleReference`) **REQ** — Specify the API name of the module for which to run territory assignment rules.
        - `based_on` (string) **REQ** [enum=['territory']] — Specify the execution method for territory assignment rules.
Possible values:
**territory** - Runs territory rules against records associated with specified territories.
        - `territories` (array of object) [minItems=1, maxItems=100] **REQ** — Specify the list of territories for which the territory assignment rules apply.
          - `id` (string/int64) **REQ** — Specify the unique identifier of the territory for which the assignment rules apply.
        - `include_child` (boolean) — Specify whether to include child territories when running the territory assignment rules.
Possible values:
**true** - Includes child territories of the specified territories in the rule execution.
**false** - Runs rules only for the specified territories, without their child territories.

**Responses:**

- **202**: Returns a scheduled status response indicating that the territory assignment rules execution has been queued as a background job. The response includes a **job_id** for tracking the scheduled execution. — Schema: `TerritoryRunRulesScheduledResponse` [application/json]
    > Represents the response returned when territory rules execution has been scheduled.
    schema: `TerritoryRunRulesScheduledResponse`
    - `run_rules` (object) **REQ** — Represents the result of the scheduled territory rules execution.
      - `code` (string) **REQ** [enum=['SCHEDULED']] — Represents the result code for the scheduled territory rules execution. Possible values: **SCHEDULED**.
      - `details` (object) **REQ** — Represents additional details about the scheduled execution, including the job identifier.
        - `job_id` (string/int64) **REQ** — Represents the unique identifier of the scheduled territory rules execution job.
      - `message` (string) **REQ** [maxLen=100, enum=[2 values]] — Represents the success message returned when territory rules execution is scheduled. Possible values: **Territory rules scheduled successfully.Once done, completion email is sent.**, **Territory rules Scheduled successfully.Once done Completion email will sent**.
      - `status` (string) **REQ** [enum=['success']] — Represents the status of the scheduled territory rules execution. Possible values: **success**.

- **400**: Returns an error response when the request contains invalid or missing data. The response identifies the specific validation failure, such as invalid field values, missing required fields, or unsupported module names. [application/json]
    oneOf:
      - `RunRulesInvalidData` — Represents the error response when invalid data is provided in a territory run rules request.
        - `run_rules` (object) **REQ** — Represents the error details for the run-rules operation when invalid data is provided.
          - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code for the request. Possible values: **INVALID_DATA**.
          - `details` (object) **REQ** — Represents additional details about the error, including the field name, JSON path, and regex pattern for valid values.
            - `api_name` (string) **REQ** [maxLen=100, minLen=1] — Represents the API name of the field that contains an invalid value.
            - `json_path` (string) **REQ** [maxLen=250, minLen=1] — Represents the JSON path of the field in the request body that contains an invalid value.
            - `regex` (string) [maxLen=100, minLen=1] — Represents the regular expression pattern that describes the valid values for the field.
          - `message` (string) **REQ** [maxLen=100, enum=[3 values]] — Represents the error message returned when invalid data is provided. Possible values: **the given value is invalid**, **the given filter value is invalid**, **invalid data**.
          - `status` (string) **REQ** [enum=['error']] — Represents the status of the operation. Possible values: **error**.
      - `RunRulesInvalidIncludeChild` — Represents the error response when the include_child parameter has an invalid value.
        - `run_rules` (object) **REQ** — Represents the error details for the run-rules operation when an invalid value is provided for the include_child parameter.
          oneOf:
            - `InvalidDataType` — Represents the error response returned when a criterion field value is provided with an incorrect data type. Contains the error code, a descriptive message, the response status, and details identifying the offending field and its expected data type.
              - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code that identifies the category of validation failure.
Possible values:
INVALID_DATA - Indicates that the value provided for a criterion field does not match the expected data type.
              - `details` (object) **REQ** — Contains the details of the invalid data type error, including the API name of the offending criterion field, its JSON path within the request body, and the data type that was expected.
                - `api_name` (string) **REQ** [maxLen=256] — Represents the API name of the criterion field whose value was supplied with an invalid data type.
                - `json_path` (string) **REQ** [maxLen=512] — Represents the JSON path that locates the specific field within the request body where the invalid data type was detected.
                - `expected_data_type` (string) **REQ** [maxLen=256] — Represents the data type that the API expected for the criterion field identified by the API name, against which the supplied value was validated.
              - `message` (string) **REQ** [maxLen=512] — Represents the error message describing the invalid data type failure in a form suitable for display or logging.
              - `status` (string) **REQ** [enum=['error']] — Represents the response status for this error response.
Possible values:
error - Indicates that the request failed due to an invalid data type on a criterion field.
            - `FieldComparatorValueMissing` — Represents the error response returned when a criterion comparator cannot be applied because the comparator value supplied by the dependee field is absent. Carries error code DEPENDENT_FIELD_MISSING along with details identifying both the field in error and the dependee field whose value is missing.
              - `code` (string) **REQ** [enum=['DEPENDENT_FIELD_MISSING']] — Represents the error code that identifies the category of failure for this error response.
Possible values:
DEPENDENT_FIELD_MISSING - Indicates that the comparator value required from the dependee criterion field is absent, preventing the comparator from being evaluated.
              - `details` (object) **REQ** — Contains detailed information about the criterion field that caused the error and the dependee field whose comparator value is missing, including the API name and JSON path for each.
                - `dependee` (object) **REQ** — Represents the dependee criterion field — that is, the field whose value determines what the current comparator accepts — and whose missing comparator value triggered this error. Contains the API name and JSON path of that dependee field.
                  - `api_name` (string) **REQ** [maxLen=256] — Represents the API name of the dependee criterion field whose comparator value is absent and caused the evaluation failure.
                  - `json_path` (string) **REQ** [maxLen=512] — Represents the JSON path that locates the dependee criterion field within the request body, identifying where the missing comparator value was expected.
                - `api_name` (string) **REQ** [maxLen=256] — API name of the criterion field that triggered the DEPENDENT_FIELD_MISSING error.
                - `json_path` (string) **REQ** [maxLen=512] — JSON path locating the criterion field in error within the request body.
              - `message` (string) **REQ** [maxLen=512] — Error message describing the DEPENDENT_FIELD_MISSING condition returned in the response envelope.
              - `status` (string) **REQ** [enum=['error']] — Status of the response. Possible values: error.
            - `FieldComparatorMismatch` — Error schema returned when the comparator value supplied for a criterion field does not match the valid comparator values determined by its dependee field. Contains the error code DEPENDENT_MISMATCH and a details object identifying the criterion field, its dependee field, and the list of supported comparator values.
              - `code` (string) **REQ** [enum=['DEPENDENT_MISMATCH']] — Error code identifying the type of field comparator mismatch condition. Possible values: DEPENDENT_MISMATCH.
              - `details` (object) **REQ** — Detailed information about the field comparator mismatch, including the API name and JSON path of the criterion field in error, the dependee field that governs valid comparator values, and the array of supported comparator values.
                - `dependee` (object) **REQ** — The dependee field whose value determines which comparator values are valid for the criterion field that raised the DEPENDENT_MISMATCH error. Contains the API name and JSON path of the dependee field.
                  - `api_name` (string) **REQ** [maxLen=256] — API name of the dependee field that determines the valid comparator values for the criterion field in error.
                  - `json_path` (string) **REQ** [maxLen=512] — JSON path locating the dependee field within the request body.
                - `api_name` (string) **REQ** [maxLen=256] — Represents the API name of the criterion field whose comparator value does not match any of the supported values determined by the dependee field.
                - `json_path` (string) **REQ** [maxLen=512] — Represents the JSON path locating the criterion field whose comparator value does not match any of the supported values determined by the dependee field.
                - `supported_values` (array of string) [minItems=1, maxItems=100] **REQ** — Contains the comparator values that are valid for the criterion field, as determined by the dependee field.
                  items: [maxLen=256]
              - `message` (string) **REQ** [maxLen=512] — Represents the error message describing the comparator mismatch condition for the criterion field.
              - `status` (string) **REQ** [enum=['error']] — Represents the status of the error response. Possible values: error.
            - `FieldValueMismatch` — Represents the error response returned when the data type of the value supplied for a criterion field does not match the expected data type determined by the dependee field. Returned with error code DEPENDENT_MISMATCH. Contains details identifying the mismatched criterion field, its dependee field, and the expected data type.
              - `code` (string) **REQ** [enum=['DEPENDENT_MISMATCH']] — Represents the error code identifying the type of error condition encountered. Possible values: DEPENDENT_MISMATCH.
              - `details` (object) **REQ** — Contains detailed information about the data type mismatch, including the criterion field that raised the error, the dependee field whose value determines the expected data type, and the expected data type itself.
                - `dependee` (object) **REQ** — Represents the dependee field whose value determines the expected data type for the criterion field that raised the mismatch error. Contains the API name and JSON path of the dependee field.
                  - `api_name` (string) **REQ** [maxLen=256] — API name of the dependee field that determines the expected data type for the criterion field in error.
                  - `json_path` (string) **REQ** [maxLen=512] — JSON path locating the dependee field within the request body.
                - `api_name` (string) **REQ** [maxLen=256] — API name of the criterion field whose value does not match the expected data type.
                - `json_path` (string) **REQ** [maxLen=512] — JSON path locating the criterion field whose value contains the data type mismatch.
                - `expected_data_type` (string) **REQ** [maxLen=256] — Data type expected for the criterion field value, as determined by the dependee field.
              - `message` (string) **REQ** [maxLen=512] — Descriptive message providing details about the field value mismatch error.
              - `status` (string) **REQ** [enum=['error']] — Status of the response. Possible values: error.
            - `ComparatorValueMismatch` — Error schema returned when the comparator value itself does not satisfy the dependency validation rules imposed by the dependee field. Carries error code DEPENDENT_MISMATCH and includes details identifying the criterion field with the invalid comparator value, its dependee field (api_name, json_path), and the criterion field own api_name and json_path.
              - `code` (string) **REQ** [enum=['DEPENDENT_MISMATCH']] — Error code identifying the comparator dependency mismatch condition. Possible values: DEPENDENT_MISMATCH.
              - `details` (object) **REQ** — Object containing diagnostic detail about the dependency mismatch, including the criterion field with the invalid comparator value (api_name, json_path) and the dependee field that imposed the violated validation rule (dependee.api_name, dependee.json_path).
                - `dependee` (object) **REQ** — Identifies the dependee field whose value determines the validation rules applied to the comparator of the criterion field in error. Contains the API name and JSON path of the dependee field.
                  - `api_name` (string) **REQ** [maxLen=256] — API name of the dependee field whose value imposed the violated validation rule on the criterion field comparator.
                  - `json_path` (string) **REQ** [maxLen=512] — JSON path locating the dependee field within the request body.
                - `api_name` (string) **REQ** [maxLen=256] — API name of the criterion field whose comparator value does not satisfy the dependency rule imposed by the dependee field.
                - `json_path` (string) **REQ** [maxLen=512] — JSON path locating the criterion field with the invalid comparator value within the request body.
              - `message` (string) **REQ** [maxLen=512] — Descriptive message providing details about the comparator value mismatch error.
              - `status` (string) **REQ** [enum=['error']] — Status of the response indicating the outcome of the request. Possible values: error.
            - `InvalidComparator` — Error schema returned when the comparator specified in a criterion field is not one of the allowed comparator values for the given field type. Returned with error code INVALID_DATA. The details object identifies the offending field by API name and JSON path, and enumerates the supported comparator values.
              - `code` (string) **REQ** [enum=['INVALID_DATA']] — Error code identifying the category of error. Possible values: INVALID_DATA.
              - `details` (object) **REQ** — Contains structured information about the invalid comparator error. Identifies the offending criterion field by API name and JSON path, and provides the list of supported comparator values valid for the given field type.
                - `api_name` (string) **REQ** [maxLen=256] — API name of the criterion field for which an invalid comparator was specified.
                - `json_path` (string) **REQ** [maxLen=512] — JSON path locating the criterion field with the invalid comparator within the request body.
                - `supported_values` (array of string) [minItems=1, maxItems=100] **REQ** — Contains the comparator values that are valid for the criterion field type.
                  items: [maxLen=256]
              - `message` (string) **REQ** [maxLen=512] — Descriptive error message conveying the nature of the invalid comparator condition to the caller.
              - `status` (string) **REQ** [enum=['error']] — Status of the response indicating the outcome of the request. Possible values: error.
            - `LookupLimitExceeded` — Represents the error response returned when the count of lookup fields used in criterion expressions exceeds the allowed limit. The error code is LOOKUP_LIMIT_EXCEEDED. The details object contains a used_in array (minItems: 1, maxItems: 10) in which each entry identifies an affected location by name and provides the relevant lookup fields and the applicable lookup limit.
              - `code` (string) **REQ** [enum=['LOOKUP_LIMIT_EXCEEDED']] — Identifies the error code that signals the lookup field limit has been exceeded. Possible values: LOOKUP_LIMIT_EXCEEDED.
              - `details` (object) **REQ** — Provides structured information about the locations where the lookup field count exceeded the allowed limit. The required used_in array contains objects that each specify a location name (such as "criteria" or "cross_filters"), the lookup fields in use, and the applicable lookup limit.
                - `used_in` (array of object) [minItems=1, maxItems=10] **REQ** — Lists the locations (for example, "criteria" or "cross_filters") where lookup field usage exceeded the allowed limit. Each entry in the array contains a location name, the lookup fields involved, and the applicable lookup limit. The array contains between 1 and 10 items.
                  - `name` (string) **REQ** [maxLen=256] — Identifies the location — such as criteria or cross_filters — where the lookup field count exceeded the allowed limit.
                  - `lookup_fields` (array of object) [minItems=1, maxItems=100] **REQ** — Lists the lookup fields present in the specified location that contributed to exceeding the allowed lookup field limit. Contains between 1 and 100 entries, each identifying a single lookup field by its API name.
                    - `api_name` (string) **REQ** [maxLen=256] — Specifies the API name of a lookup field that was counted against the lookup field limit for the specified location.
                  - `lookup_limit` (integer/int32) **REQ** — Specifies the maximum number of lookup fields permitted in the associated location, such as criteria or cross_filters.
              - `message` (string) **REQ** [maxLen=512] — Contains a descriptive error message explaining why the lookup field limit was exceeded.
              - `status` (string) **REQ** [enum=['error']] — Indicates the outcome of the request. Possible values: error.
            - `NotSupportedApiName` — Represents the error response returned when the API name specified in a criterion field is not supported by the target module. Contains the error code, a descriptive message, the response status, and details identifying the unsupported field and its location in the request body.
              - `code` (string) **REQ** [enum=['NOT_SUPPORTED']] — Represents the error code that identifies the category of validation failure.
Possible values:
NOT_SUPPORTED - Indicates that the API name specified for the criterion field is not supported by the target module.
              - `details` (object) **REQ** — Contains detailed information identifying the criterion field whose API name is not supported by the target module, including the field API name and its location within the request body.
                - `api_name` (string) **REQ** [maxLen=256] — Represents the API name of the criterion field that is not supported by the target module.
                - `json_path` (string) **REQ** [maxLen=512] — Represents the JSON path that locates the unsupported criterion field within the request body.
              - `message` (string) **REQ** [maxLen=512] — Represents the error message describing why the criterion field API name is not supported by the target module.
              - `status` (string) **REQ** [enum=['error']] — Represents the outcome status of the response for this error condition.
Possible values:
error - Indicates the request failed because the specified criterion field API name is not supported by the target module.
      - `RunRulesMandatoryNotFound` — Represents the error response when a mandatory field is missing from a territory run rules request.
        - `run_rules` (object `MandatoryNotFound`) **REQ** — Details of each territory error.
          schema: `MandatoryNotFound`
          - `code` (string) **REQ** [enum=['MANDATORY_NOT_FOUND']] — Error code identifying the category of error.

Possible values:
MANDATORY_NOT_FOUND - Indicates that a required criterion field was absent from the request.
          - `details` (object) **REQ** — Object identifying the mandatory criterion field that is absent from the request. Contains the api_name of the missing field and the json_path indicating its expected location in the request body.
            - `api_name` (string) **REQ** [maxLen=256] — API name of the criterion field that is required but was not found in the request.
            - `json_path` (string) **REQ** [maxLen=512] — JSON path to the location in the request body where the mandatory criterion field was expected but not found.
          - `message` (string) **REQ** [maxLen=512] — Error message describing the mandatory field not found condition returned in the response envelope.
          - `status` (string) **REQ** [enum=['error']] — Status of the error response.

Possible values:
error - Indicates that the request failed because a mandatory criterion field was not found.
      - `RunRulesAlreadyScheduled` — Represents the error response when territory rules execution is already scheduled.
        - `code` (string) **REQ** [enum=['ALREADY_SCHEDULED']] — Represents the error code for the request. Possible values: **ALREADY_SCHEDULED**.
        - `details` (object) **REQ** — Represents additional details about the error, including the job ID of the already scheduled run-rules task.
          - `job_id` (string/int64) **REQ** — Represents the unique identifier of the already scheduled run-rules job.
        - `message` (string) **REQ** [maxLen=100, enum=[1 values]] — Represents the error message returned when a run-rules task is already scheduled. Possible values: **Previously scheduled Run Rules Action was not yet Completed. Please try again once it is completed**.
        - `status` (string) **REQ** [enum=['error']] — Represents the status of the operation. Possible values: **error**.
      - `AmbiguityDuringProcessing` — Represents the error response when an ambiguity is encountered during territory processing.
        - `run_rules` (object) **REQ** — Represents the ambiguity error details returned when the run-rules operation encounters conflicting assignment criteria.
          - `code` (string) **REQ** [enum=['AMBIGUITY_DURING_PROCESSING']] — Represents the error code returned when ambiguity is detected during run-rules processing.
          - `message` (string) **REQ** [enum=['Ambiguity while processing the request']] — Represents the error message returned when ambiguity is encountered during processing.
          - `status` (string) **REQ** [enum=['error']] — Represents the status of the response. Possible values: **error**.
          - `details` (object) **REQ** — Represents the details about the fields causing ambiguity during processing.
            - `ambiguity_due_to` (array of object) [minItems=2, maxItems=2] **REQ** — Represents the list of fields causing ambiguity.
              - `api_name` (string) **REQ** [maxLen=100] — Represents the API name of the conflicting or ambiguous field.
              - `json_path` (string) **REQ** [maxLen=100] — Represents the JSON path pointing to the ambiguous field in the request.
      - `RunRulesLeadModuleNotEnabled` — Represents the error response when the territory lead rule is not enabled.
        - `run_rules` (object) **REQ** — Represents the error details for the run-rules operation when the territory lead rule is not enabled.
          - `code` (string) **REQ** [enum=['FEATURE_NOT_ENABLED']] — Represents the error code for the request. Possible values: **FEATURE_NOT_ENABLED**.
          - `details` (object) **REQ** — Represents additional details about the error.
          - `message` (string) **REQ** [maxLen=100, enum=['Territory Lead Rule Disabled']] — Represents the error message returned when the territory lead rule is not enabled. Possible values: **Territory Lead Rule Disabled**.
          - `status` (string) **REQ** [enum=['error']] — Represents the status of the operation. Possible values: **error**.
      - `RunRulesDealModuleNotEnabled` — Represents the error response when the territory deal rule is not enabled.
        - `run_rules` (object) **REQ** — Represents the error details for the run-rules operation when the territory deal rule is not enabled.
          - `code` (string) **REQ** [enum=['FEATURE_NOT_ENABLED']] — Represents the error code for the request. Possible values: **FEATURE_NOT_ENABLED**.
          - `details` (object) **REQ** — Represents additional details about the error.
          - `message` (string) **REQ** [maxLen=100, enum=['Territory Deal Rule Disabled']] — Represents the error message returned when the territory deal rule is not enabled. Possible values: **Territory Deal Rule Disabled**.
          - `status` (string) **REQ** [enum=['error']] — Represents the status of the operation. Possible values: **error**.
      - `RunRulesExpectedFieldMissing` — Represents the error response when an expected field is missing from a territory run rules request.
        - `run_rules` (object) **REQ** — Represents the error details for the run-rules operation when an expected field is missing.
          - `code` (string) **REQ** [enum=['EXPECTED_FIELD_MISSING']] — Represents the error code for the request. Possible values: **EXPECTED_FIELD_MISSING**.
          - `details` (object) **REQ** — Represents additional details about the error, including the list of expected fields that are missing.
            - `expected_fields` (array of object) [minItems=2, maxItems=2] **REQ** — Represents the list of expected fields that are missing from the request.
              - `api_name` (string) **REQ** [maxLen=100] — Represents the API name of the expected field that is missing.
              - `json_path` (string) **REQ** [maxLen=100] — Represents the JSON path of the expected field that is missing from the request body.
          - `message` (string) **REQ** [maxLen=100, enum=['one of the expected field is missing']] — Represents the error message returned when an expected field is missing. Possible values: **one of the expected field is missing**.
          - `status` (string) **REQ** [enum=['error']] — Represents the status of the operation. Possible values: **error**.
      - `TerritoryFeatureNotEnabledError` — Represents the error response when the territory feature is not enabled for the organization.
        - `code` (string) **REQ** [enum=['FEATURE_NOT_ENABLED']] — Represents the error code for the request. Possible values: **FEATURE_NOT_ENABLED**.
        - `details` (object) **REQ** — Represents additional details about the error.
        - `message` (string) **REQ** [maxLen=100, enum=[5 values]] — Represents the error message returned when the territory feature is not enabled for the organization. Possible values: **Territory Management is disabled**, **Territory Management is not enabled**, **Territory Management Disabled**, **the territory feature is not enabled for Leads Module**, **Territory Management is not enabled for Leads Module**.
        - `status` (string) **REQ** [enum=['error']] — Represents the status of the operation. Possible values: **error**.
      - `DependentFieldMissingError` — Represents the error response when a required dependent field is missing from the territory request.
        - `territories` (array of object) [minItems=1, maxItems=1] **REQ** — Represents the list of territory objects with their error details.
          - `code` (string) **REQ** [enum=['DEPENDENT_FIELD_MISSING']] — Represents the error code indicating the type of error for the territory operation.
          - `details` (object) **REQ** — Represents additional details about the error, including the API name and JSON path of the problematic field.
            - `api_name` (string) **REQ** [maxLen=100, minLen=1] — Represents the API name of the field that caused the error.
            - `json_path` (string) **REQ** [maxLen=250, minLen=1] — Represents the JSON path of the field that caused the error.
            - `dependee` (object) — Represents the dependent field that is required but missing from the request.
              - `api_name` (string) **REQ** [maxLen=100] — Represents the API name of the dependent field.
              - `json_path` (string) **REQ** [maxLen=250, minLen=1] — Represents the JSON path of the dependent field.
          - `message` (string) **REQ** [enum=['This territory has its child. Please Give the transfer_to_id field value']] — Represents the error message describing the reason for this failure.
          - `status` (string) **REQ** [enum=['error']] — Represents the status of the operation. Possible values: **error**.
      - `RunRulesDependentFieldMissing` — Represents the error response when the territory run rules request contains invalid data. The schema supports multiple error variants, each corresponding to a specific validation failure.
        - `run_rules` (object) **REQ** — Details of the run rules dependent field missing error.
          - `code` (string) **REQ** [enum=['DEPENDENT_FIELD_MISSING']] — Error or status code representing the outcome of the request.
          - `details` (object) **REQ** — Additional contextual information about the error or status.
            - `api_name` (string) **REQ** [enum=['criteria', 'custom_view']] — The API field name associated with the validation error.
            - `json_path` (string) **REQ** [enum=['$.run_rules.criteria', '$.run_rules.custom_view']] — JSON path pointing to the field that caused the issue.
            - `dependee` (object) **REQ** — Dependency information related to the error.
              - `api_name` (string) **REQ** [enum=['based_on']] — The API field name of the dependee.
              - `json_path` (string) **REQ** [enum=['$.run_rules.based_on']] — JSON path pointing to the field that caused the issue.
          - `message` (string) **REQ** [enum=['Dependent Field missing']] — Detailed error message to help fix the validation issue.
          - `status` (string) **REQ** [enum=['error']] — Indicates whether the operation failed or succeeded.

- **401**: Authentication failed.
**Resolution:** A new access token must be generated with the required scope for this API. — Schema: `UnauthorizedError` [application/json]
    > Represents the error response when authentication fails for the request.
    schema: `UnauthorizedError`
    - `code` (string) **REQ** [enum=['AUTHENTICATION_FAILURE']] — Represents the error code for the request. Possible values: **AUTHENTICATION_FAILURE**.
    - `details` (object) **REQ** — Represents additional details about the authentication error.
    - `message` (string) **REQ** [maxLen=100, enum=['Authentication failed']] — Represents the error message returned when authentication fails. Possible values: **Authentication failed**.
    - `status` (string) **REQ** [enum=['error']] — Represents the status of the operation. Possible values: **error**.

- **403**: Permission denied to run territory assignment rules.
**Resolution:** The CRM administrator must grant the required permission to the user's profile. [application/json]
    > Represents the error response when the requesting user does not have permission to run territory assignment rules.
    oneOf:
      - `RunRulesNoPermission` — Represents the error response when the user does not have permission to run territory rules.
        - `run_rules` (object) **REQ** — Represents the error details for the run-rules operation when the user lacks permission.
          - `code` (string) **REQ** [enum=['NO_PERMISSION']] — Represents the error code for the request. Possible values: **NO_PERMISSION**.
          - `details` (object) **REQ** — Represents additional details about the error.
          - `message` (string) **REQ** [maxLen=100, enum=["You don't have permission to run rules based on criteria filter."]] — Represents the error message returned when the user lacks permission to run rules. Possible values: **You do not have permission to run rules based on criteria filter.**
          - `status` (string) **REQ** [enum=['error']] — Represents the status of the operation. Possible values: **error**.
      - `RunRulesModuleNoPermission` — Represents the error response when the user does not have permission for the specified module in a territory run rules request.
        - `run_rules` (object) **REQ** — Represents the error details for the run-rules operation when the user lacks permission for the specified module.
          - `code` (string) **REQ** [enum=['NO_PERMISSION']] — Represents the error code for the request. Possible values: **NO_PERMISSION**.
          - `details` (object) **REQ** — Represents additional details about the error.
          - `message` (string) **REQ** [maxLen=100, enum=["You don't have permission for the module."]] — Represents the error message returned when the user lacks permission for the module. Possible values: **You do not have permission for the module.**
          - `status` (string) **REQ** [enum=['error']] — Represents the status of the operation. Possible values: **error**.

**Scopes:** ZohoCRM.settings.territories.UPDATE, ZohoCRM.settings.territories.ALL
