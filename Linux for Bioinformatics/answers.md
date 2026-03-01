# Linux CLI (Bash / Shell) for Bioinformatics Answers
**Note:** When setting up the linux instance, neither `Ubuntu Server 20.04 LTS` nor `t2.micro` were available. `Ubuntu Server 24.04 LTS` and `t3.micro` were used instead to create the instance. 

### Q1. What is your home directory?
The home directory is the folder specific to a particular user within an operating system such as Windows, Linux or MacOS. It can be used to store a variety of files and documents.

### Q2. What is the output of this command?
The output of the `ls` command is the list of the names of all the folders and files within the current directory. When in the `my_folder/` directory, it will only output `hello_world.txt` as it is the  only file in that directory.

### Q3. What is the output of each `ls` command?
The output of the `ls` command on `my_folder/` will be nothing as the `hello_world.txt` file has been deleted making that directory empty. The output of the `ls` command on `my_folder2/` will be `hello_world.txt`.

### Q4. What is the output of each?
The output of the `ls` command on `my_folder/` will be nothing, the output on `my_folder2/` will also be nothing as the `hello_world.txt` file has been moved into a new directory. The output of the `ls` command on my `my_folder3/` will be `hello_world.txt`.

### Q5. What editor did you use and what was the command to save your file changes?
I used the nano command-line text editor to change `hello_world.txt`. To save changes on the file I used ctrl-O and enter to confirm the changes, and then ctrl-X to exit the text editor.

### Q6. What is the error?
The error message I got was `Permission denied (publickey).`

### Q7. What was the solution?
The solution was to first generate a SSH key pair locally with the following command `ssh-keygen`. After that I logged in as `ubuntu` on the remoter server and switched to `sudouser`. Then I manually copied the public key onto a newly created `.ssh/authorized_keys` file in the home directory of `sudouser`.

### Q8. What does the `sudo docker run` part of the command do? and what does the `salmon swim` part of the command do?
`sudo docker run` uses a docker image to run and create a new container as a sudo user with admin privileges. `salmon swim` prints out a salmon logo as well version information.

### Q9. What is the output of this command?
When running the command `sudo ls /root` as `serveruser`, the output you would get is `serveruser is not in the sudoers file.`

### Q10. What is the output of `flask --version`?
The output shows the current version of `flask`, `python` as well as `werkzeug` a Web Server Gateway Interface (WSGI) library for `python`.

### Q11. What is the output of `mamba -V`?
The output was:<br>`The following argument was not expected: -V` <br> `Run with --help for more information.`

In order to get version information of mamba, the command would be `mamba --version`.

### Q12. What is the output of `which python`?
The output of the command in the `py27` environment is `/home/serveruser/miniforge3/envs/py27/bin/python`.

### Q13. What is the output of `which python` now?
The output of the command in the `base` environment is `/home/serveruser/miniforge3/bin/python`.

### Q14. What is the output of `salmon -h`?
The command prints out some useful command-line flags for `salmon`.

### Q15. What does the `-o athal.fa.gz` part of the command do?
That part of the command saves the output of the link to a file called `athal.fa.gz`

### Q16. What is a `.gz` file?
It is a compressed archive file commonly used in Unix/Linux environments.

### Q17. What does the `zcat` command do?
The command outputs the content of a `.gz` file.

### Q18. What does the `head` command do?
The command outputs the first part of an input file as specified by the user.

### Q19. What does the number `100` signify in the command?
It is part of the `head` command and specifies that the output should be the first 100 lines of the input file.

### Q20. What is `|` doing? -- Hint using `|` in Linux is called "piping"
Piping takes the output of the first command and uses it as the input of the second command.

### Q21. What is a `.fa file`? What is this file format used for?
It is a FASTA file used to store nucleotide and protein sequences.

### Q22. What format are the downloaded sequencing reads in?
They are in the `.sra` file format.

### Q23. What is the total size of the disk?
It is 6.8 GB.

### Q24. How much space is remaining on the disk?
There is 1.7 GB remaining. Much of the memory was used to install the necessary dependencies for the main packages.

### Q25. What went wrong?
There wasn’t enough storage for the command to be executed.

### Q26: What was your solution?
I added the `--gzip` flag to the command to save the output file as a `.gz` file to save on storage space.