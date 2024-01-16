# 0x17. Web stack debugging #3

## Description
This project aims to automate the resolution of an Apache 500 error on a Wordpress website running on a LAMP stack using Puppet.

## Requirements
- All files will be interpreted on <link>Ubuntu 14.04 LTS</link>
- All files should end with a new line
- Your Puppet manifests must pass <link>puppet-lint version 2.1.1</link> without any errors
- Your Puppet manifests must run without error
- Your Puppet manifests first line must be a comment explaining what the Puppet manifest is about
- Your Puppet manifests files must end with the extension .pp
- Files will be checked with <link>Puppet v3.4</link>
- More info: Install <link>puppet-lint</link>
  $ apt-get install -y ruby
  $ gem install puppet-lint -v 2.1.1

## Tasks
### 0. Strace is your friend
- Using <link>strace</link>, find out why Apache is returning a 500 error. Once you find the issue, fix it and then automate it using Puppet (instead of using Bash as you were previously doing).
- Your 0-strace_is_your_friend.pp file must contain Puppet code
- You can use whatever Puppet resource type you want for your fix

## How to Run
1. Clone the repository to your local machine.
2. Navigate to the project directory.
3. Run the Puppet manifest using the following command:
