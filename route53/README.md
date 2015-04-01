# Route 53

Route 53 is a basic DNS service.

- [Official Documentation](http://aws.amazon.com/documentation/route53/)

## CLI

```bash
aws route53 list-hosted-zones
aws route53 get-hosted-zone --id /hostedzone/Z27NDWU34VPO2H
aws route53 list-resource-record-sets --hosted-zone-id /hosted-zone/Z27NDWU34VPO2H
aws route53 change-resource-record-sets --hosted-zone-id /hosted-zone/Z27NDWU34VPO2H --change-batch JSON_STRING
```

