# aws-sandbox

This is my personal repository of notes and scripts for how to use varioius parts of AWS.


## Recipes

Examples of how to combine commands from various services to perform example tasks.


### Set up a static S3 web server

```bash
aws s3 mb s3://bitkickers-test/
aws s3 website bitkickers-test --index-document index.html --error-document error.html
aws iam create-user --user-name www-data
aws iam put-user-policy --user-name www-data --policy-name s3-bitkickers-test-access --policy-document file://s3-bitkickers-test-access.json
```
