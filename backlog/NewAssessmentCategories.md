# New Assessment Categories Backlog

## SWE Agent Instructions

As a Software Engineer (SWE) agent working on this backlog:

1. For each assessment task:
   - Review the provided link/documentation
   - Create a new assessment file in the `assessments` directory
   - Use naming convention: `assessment_name_YYYYMMDD.json`
   - Follow the standard assessment format:
     ```json
     {
       "name": "assessment_name",
       "version": "1.0",
       "categories": [
         {
           "name": "category_name",
           "subcategories": [
             {
               "name": "subcategory_name",
               "criteria": [
                 {
                   "id": "unique_id",
                   "description": "criterion_description",
                   "level": "required/recommended/optional"
                 }
               ]
             }
           ]
         }
       ]
     }
     ```
   - Update this file with completion status and date
   - Create a pull request with the new assessment

## Assessment Tasks

| Name | Description | Category | Reference Link | Status | Last Updated |
|------|-------------|----------|----------------|---------|--------------|
| Mobile Accessibility | W3C WCAG 2.2 Mobile Accessibility Guidelines | Accessibility | [WCAG 2.2 Mobile](https://www.w3.org/TR/wcag2mobile-22/) | Completed | 2024-06-24 |
| Google Workspace | Google Workspace Marketplace App Review Guidelines | Marketplace | [Google Workspace Guidelines](https://developers.google.com/workspace/marketplace/about-app-review) | Not Started | 2024-06-24 |
| Apple App Store | Apple App Store Review Guidelines | App Store | [App Store Guidelines](https://developer.apple.com/app-store/review/guidelines/) | Not Started | 2024-06-24 |
| Android Marketplace | Android App Publication Guidelines | App Store | [Android Publishing](https://developer.android.com/studio/publish) | Not Started | 2024-06-24 |

## Notes
- Each assessment should include relevant examples and best practices
- Consider adding automated validation where possible
- Include links to official documentation and resources
- Add implementation guidance where appropriate
- Consider versioning for guidelines that change frequently (especially app store guidelines)

## Categories Overview
- **Accessibility**: Standards for making applications accessible to all users
- **Marketplace**: Requirements for publishing to various software marketplaces
- **App Store**: Platform-specific guidelines for mobile applications

## Priority Order
1. Mobile Accessibility (Foundation for all mobile applications)
2. Android Marketplace (Large developer base)
3. Apple App Store (High impact for iOS developers)
4. Google Workspace (Growing enterprise market)