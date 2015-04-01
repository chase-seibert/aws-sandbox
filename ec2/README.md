# ec2

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
