# CLI Helpers

This folder contains some wrappers that I have writter around the aws command line tool. In order to keep them distinct from the built-in commands, I have prefixed them all with `aws-`.

## CLI Tips

See the [reInvent YouTube video](https://www.youtube.com/watch?v=qiPt1NoyZm0)

- All commands can take a `file:///home/user/foo` value for their parameters, which reads the contents of that file into the attribute. This is very useful for parameters that take long JSON values, or for uploading SSH keys.
- Instead of `file:///` you can also use `http://` or `https://`.


## Commands

- `source aws-completion`
- `aws-upload-ssh-key cseibert ~/.ssh/id_rsa.pub`
- `aws-instances`
