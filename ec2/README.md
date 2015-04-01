# ec2

EC2 is a virtual machine service.

- [Official Documentation](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/concepts.html)

## CLI

There are *two different* interfaces, the [Java based CLI tools](http://docs.aws.amazon.com/AWSEC2/latest/CommandLineReference/set-up-ec2-cli-linux.html) and the [AWS Command Line Interface](http://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-set-up.html).

- [Official Documentation](http://docs.aws.amazon.com/cli/latest/userguide/cli-chap-welcome.html)


### Install

```bash
sudo pip install awscli
aws configure
complete -C aws_completer aws
# enter credentials from a IAM role (make sure to add to AdministratorAccess policy)
# us-west-2 & json
# these are stored in ~/.aws
```

### Common Commands

```bash
# most commands take a "help" suffix
aws ec2 describe-instances --output text
aws ec2 start-instances --instance-ids i-7f64c972
aws ec2 stop-instances --instance-ids i-7f64c972
aws ec2 describe-key-pairs
aws ec2 describe-images
aws ec2 run-instances --image-id ami-29ebb519 --key-name cseibert --instance-type t2.micro
ssh ubuntu@ec2-54-191-79-106.us-west-2.compute.amazonaws.com
```

Make sure your security group settings allow ssh access.

## Elastic Load Balancer (ELB)

Load balance between two or more EC2 instances. Make sure that BOTH your ELB security group and the security group of the instances allow the inbound port.

```bash
aws elb describe-load-balancers
aws elb create-load-balancer
aws elb register-instances-with-load-balancer --instances FOO,BAR
aws elb describe-instance-health --load-balancer-name www
```

*Note*: make sure that your daemon can handle the traffic well, otherwise the ELB health check may fail and remove the instance; consisder using something like nginx
