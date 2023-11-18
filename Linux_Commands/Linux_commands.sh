what is operating system?
-> Operating system is an interface b/w user and the computer hardware.

types of operating systems:

-> single user -> single task OS -> MS-DOS
-> single user -> multitasking OS --> windows 98 vista, seven etc..
-> Multi User - Multitasking OS -> UNIX, LINUX etx.


what is UNIX principles: 

1. everthing is file
2. Configuration data stored in text
3. Small, single-purpose programs
4 avoid user interface
5. Ability to chain programs together to perform complex tasks.

How we talk with Hardware?
------------------------------

File Systems
-----------------------------

/ it is parent director or ROOT directory

/root  it is home dir for root user(super user)

/home it is home dir for other users

/boot  it contains bootable file for Linux, GRUB 

/etc it contains all configuration files 
     /etc/passwd userinfo
     /etc/dhcpd.conf   DHCP server

/usr by default softwares are installed in /usr dir

/opt it is optional dir for /usr
     it contains third party software 


/bin it contains commands used by all users ( Binary files)

/sbin it contains cmds used by only super user(ROOT) (super users binary files)


/dev its contains device files -> like /dev/hda 

/proc it contains process file and its not permanent, they keep changing
       acts as Virtual Dir.

/var its contains variable data like mails and log files.

/mnt it is default mount point for any partition 


/media all of removable media like pen drive, CD-ROM.

/lib it contains library files which are used by OS.

-----------------------------------------------

how to create file ?

$ touch <filename> 

To read a file 

$ cat <filename>

creating a dir 
-------------------
$ mkdir shane

making multiple dir inside a dir

$ mkdir -p Kernel/{Linux/{advlinux,linuxstore},Aix/{hacmp,lpar},Storage/{san,netapp}}

Copying files into dir
-------------------------

$ cp <filename> <dest>
     <scr>  <dest>
$ cp * or . <dest>

------------------------
Moving files from one location to other
-----------------------------------------

$ mv <filename> <dest>

Renaming the file
-------------------

$ mv <oldname> <newname>

$ mv <old dir name> <new dir name>

Removing the file
--------------------
$ rm 
$ rm -f
$ rm -rf ( r stands for recursive and f stands for forcefully.

VIM Editor or NANO 
-----------------------

VI -> Visual display Editor 
VIM -> Visual display edior improved

gedit, emacs

-> i = to begin insert mode at the cursor postion
-> I = to insert at the begining of line
-> a = to append to next words letter
-> A = to append at the end of the line
-> o = to insert a new line below the cursor postion
-> O = new line above the coursor postion
-> gg = to go to the beginning of the page
-> G = end of the page
-> w = to move the cursor forward, word by word (nw or 5W words) 
-> b = backward of the cursor (nb or 5B words)
-> u = to undo last changes(word)
-> U = to undo the pervious changes
-> ctrl+r = to redo the changes
-> yy = to copy a line ( nyy or 5yy or 4yy lines)
-> p = to paste line below the cursor postion
-> P = paste line above the cursor postion.
-> dw = to delete the word letter by letter( like backspace)
-> x = to delete the letter by letter (DEL key)
-> dd = to delete the entire line ( ndd or 3dd)
-> / = to search a word in the file

Extended mode: 
----------------------

-> ESC + :W -> to save the changes
-> ESC + :q -> to quit( without saving)
-> ESC + :wq -> save and quit
-> ESC + :w! -> save forcefully
-> ESC + wq! -> save and quit forcefully
-> ESC + :x -> to save and quit
-> ESC + :X -> to give password to the file and remove password
-> ESC + :20(n) -> it will go to 20th line

listing files and dir's
------------------------
$ ls -> list the files names
$ ls -l long listing of the file
$ ls -al -> it will show the all long list files
$ ls -l <filename> -> to see the permissions of the particular file

-----------------------------------------------

Filter Commands:
---------------------
 
$ less - ex: less /etc/passwd 
$ more - ex: more /etc/passwd 
$ head - it used to show the top 10 lines for file. ex: head /etc/passwd
$ tail - it used to show the last 10 lines of the file. ex: tail /etc/passwd
$ sort - output will be in numberic or alphabatic order 
$ cut - the cut command is used to pic the given expression (in columns) and display the output 
          # cut -d -f file ( where d stands for delimiter ex: :, " "  and f stands for field)
$ sed - sed 's/yum/setting/g' <filename>

----------------------------------------------------

Redirection is a process where we can copy the output of any commands, files into a new file.

# ls -a > /root/list.txt or to append the output ls -a >> /root/list.txt

----------------------------------------------

find: is used to find the files or dir path, it is exactly like the find option in our windows.

-name: for searching a file with its name
-inum: ffor searching a file with particular inode number.
-type: searching a particular type of file
-user: files whose owner is particular user
-group: files belonging to particular group 

----------------------------------------------------------------
File Permission: 

three levels: 
1. owner or user level 
2. Group level
3. others level

----------------------------

read = 4
write = 2
execute = 1 


chmod u+x <file> adding execute permission to user only

chmod go-wx <file> (removing the write and execute permission of the file)

chmod +x <file>

-----------------------------------------------------------------------------
Mounting 
-------

# mount <device name> <dir name (mount point)> 


$ mount /dev/sda7 /kernel 

$ vi /etc/fstab  ( path to mount)
----------------------------------------------------------------------
user
-------

adduser <name>

passwd <username>
-------------------
1. super user or root user: root user is powerful user. he is the administrator user.

2. System user: System users are the users created by the software or application 

3. Normal user: like shane, rahul, 

---------------------------------------------------------

service
-------

# service or systemctl 

# service start <service name>
          stop
          restart


# systemctl <service name> start
                           stop
                           restart

------------------------------------------------------------

# ps 

# ps -a -> all

# ps -u username 

# ps -x 

# ps -G <groupname> (for group)

# ps -aux

-----------------------------------
kill
---------
signal 
-------
1 for reloading the process
9 for killing hr process
15 for teminating the process
20 for stopping the process

# kill -1 <pid>

nice
-----------

i want to run a jenkins -20 -1 , maven -19-2 in top postion

from -20 to 19 

renice <nice value (-20 to 19)> <PID>

-------------------------------------------
crontab
---------
for edit crontab # crontab -e 
for display ur crontab files # crontab -l
for removing  # crontab -r

# crontab -l (listing)
#crontab -l u <username>

ex: 

#tty

#crontab -e

*/1 * * * * date > /dev/pts/0
--------------------------------------


     




































 


























   




















 







































































































































































 



