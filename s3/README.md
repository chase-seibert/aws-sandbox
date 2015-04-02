# S3

S3 is a file hosting service.

- [Official Documentation](http://aws.amazon.com/documentation/s3/)

*Note:* When making buckets, those names are _global to the entire S3 system_.

## CLI

```bash
aws s3 mb s3://new-bucket/
aws s3 website new-bucket --index-document index.html --error-document error.html
aws s3 sync /tmp/foo s3://new-bucket/ --acl public-read --delete
```
