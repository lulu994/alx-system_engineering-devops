# 0x1B. Web stack debugging #4

## Description

This project aims to address and resolve issues related to web server performance and user login errors in a Ubuntu 14.04 LTS environment. Two specific tasks have been tackled:

### Task 0: Sky is the limit, let's bring that limit higher
In this task, the goal is to improve the performance of a web server setup featuring Nginx. ApacheBench is used for benchmarking, and the initial results show a significant number of failed requests. The Puppet manifest file (0-the_sky_is_the_limit_not.pp) is provided to fix the issues and improve the server's performance.

### Task 1: User limit
In this task, the challenge is to resolve issues related to the holberton user's login. Attempting to log in as holberton resulted in error messages related to too many open files. The Puppet manifest file (1-user_limit.pp) is provided to change the OS configuration, allowing the holberton user to log in without encountering errors.

## Requirements

- All files are interpreted on Ubuntu 14.04 LTS.
- All files end with a new line.
- A mandatory README.md file is included at the root of the project folder.
- Puppet manifests must pass puppet-lint version 2.1.1 without any errors.
- Puppet manifests must run without errors.
- Puppet manifests must have a comment on the first line explaining their purpose.
- Puppet manifests files must end with the extension .pp.
- Files are checked with Puppet v3.4.

### Installation of puppet-lint

$ apt-get install -y ruby
$ gem install puppet-lint -v 2.1.1

## Usage

### Task 0: Sky is the limit, let's bring that limit higher
- Run ApacheBench to benchmark the current web server performance:
* $ ab -c 100 -n 2000 localhost/
- Review the results for failed requests and other performance metrics.
- Apply the Puppet manifest to fix the issues:
* $ puppet apply 0-the_sky_is_the_limit_not.pp
- Run ApacheBench again to verify the performance improvements.

### Task 1: User limit
- Attempt to log in as the holberton user, observe error messages related to too many open files.

- Apply the Puppet manifest to change the OS configuration:
* $ puppet apply 1-user_limit.pp
- Attempt to log in as the holberton user again and verify that the login is successful without any error messages.

## Repository
- GitHub Repository: alx-system_engineering-devops
- Directory: 0x1B-web_stack_debugging_4
- Files:
* 0-the_sky_is_the_limit_not.pp
* 1-user_limit.pp
