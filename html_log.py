# Вывод в виде html

emanon@emanon-MiniBook-X:~$ ls
Arduino     minicom.log             Public       Videos
c_project   Music                   setup_ap.sh  Webvenv
Desktop     muto-bak.gz             snap         yahboom_backup_software
Documents   old_board.bin           Templates    yahboomcar_backup_yahboomcar_ws
Downloads   package-lock.json       venvMavlink
esp32_uart  packages.microsoft.gpg  VenvSystem
esptool     Pictures                VescVenv
emanon@emanon-MiniBook-X:~$ cd ..
emanon@emanon-MiniBook-X:/home$ ls
emanon
emanon@emanon-MiniBook-X:/home$ mkdir training
mkdir: cannot create directory ‘training’: Permission denied
emanon@emanon-MiniBook-X:/home$ sudo kdir training
[sudo] password for emanon: 
sudo: a password is required
emanon@emanon-MiniBook-X:/home$ sudo mkdir training
[sudo] password for emanon: 
emanon@emanon-MiniBook-X:/home$ ls
emanon  training
emanon@emanon-MiniBook-X:/home$ cd training
emanon@emanon-MiniBook-X:/home/training$ mkdir day1
mkdir: cannot create directory ‘day1’: Permission denied
emanon@emanon-MiniBook-X:/home/training$ sudo mkdir day1
emanon@emanon-MiniBook-X:/home/training$ sudo mkdir day2
emanon@emanon-MiniBook-X:/home/training$ sudo mkdir day3
emanon@emanon-MiniBook-X:/home/training$ ls
day1  day2  day3
emanon@emanon-MiniBook-X:/home/training$ cd day_1
bash: cd: day_1: No such file or directory
emanon@emanon-MiniBook-X:/home/training$ cd day1
emanon@emanon-MiniBook-X:/home/training/day1$ echo "План на день: отработать день,сделать дз,написать курсовую,помыть полы и лечь спать" >plan.txt
bash: plan.txt: Permission denied
emanon@emanon-MiniBook-X:/home/training/day1$ sudo echo "План на день: отработать день,сделать дз,написать курсовую,помыть полы и лечь спать" >plan.txt
bash: plan.txt: Permission denied
emanon@emanon-MiniBook-X:/home/training/day1$ sudo echo "План на день: отработать день,сделать дз,написать курсовую,помыть полы и лечь спать" > plan.txt
bash: plan.txt: Permission denied
emanon@emanon-MiniBook-X:/home/training/day1$ sudo echo "План на день: отработать день,сделать дз,написать курсовую,помыть полы и лечь спать" > plan.txt^C
emanon@emanon-MiniBook-X:/home/training/day1$ sudo touch plan.txt
emanon@emanon-MiniBook-X:/home/training/day1$ sudo nano plan.txt
emanon@emanon-MiniBook-X:/home/training/day1$ sudo touch notes.txt
emanon@emanon-MiniBook-X:/home/training/day1$ cat -n plan.txt
     1	В Linux можно использовать команды универсальные, такие как echo и touch, но я предпочитаю использовать утилиту nano.
emanon@emanon-MiniBook-X:/home/training/day1$ sudo nano plan.txt
emanon@emanon-MiniBook-X:/home/training/day1$ cat -n plan.txt
     1	В Linux можно использовать универсальные команды, такие как echo и touch, но я предпочитаю использовать утилиту nano.
     2	
     3	Она позволят одной командой создать файл и сразу же вписать в нем необходимый текст.
     4	Удобная и читаемая платформа позволяет вносить разные изменения с текстом в файле.
emanon@emanon-MiniBook-X:/home/training/day1$ cp -r dir1 der2
cp: cannot stat 'dir1': No such file or directory
emanon@emanon-MiniBook-X:/home/training/day1$ cp -r day1 day2
cp: cannot stat 'day1': No such file or directory
emanon@emanon-MiniBook-X:/home/training/day1$ cd ..
emanon@emanon-MiniBook-X:/home/training$ cp -r day1 day2
cp: cannot create directory 'day2/day1': Permission denied
emanon@emanon-MiniBook-X:/home/training$ sudo cp -r day1 day2
emanon@emanon-MiniBook-X:/home/training$ ls
day1  day2  day3
emanon@emanon-MiniBook-X:/home/training$ cd day2
emanon@emanon-MiniBook-X:/home/training/day2$ ls
day1
emanon@emanon-MiniBook-X:/home/training/day2$ cd day1
emanon@emanon-MiniBook-X:/home/training/day2/day1$ ls
notes.txt  plan.txt
emanon@emanon-MiniBook-X:/home/training/day2/day1$ cd ..
emanon@emanon-MiniBook-X:/home/training/day2$ ls
day1
emanon@emanon-MiniBook-X:/home/training/day2$ cd day1
emanon@emanon-MiniBook-X:/home/training/day2/day1$ cd ..
emanon@emanon-MiniBook-X:/home/training/day2$ rm -r day1
rm: descend into write-protected directory 'day1'? y
rm: remove write-protected regular file 'day1/plan.txt'? y
rm: cannot remove 'day1/plan.txt': Permission denied
rm: remove write-protected regular empty file 'day1/notes.txt'? y
rm: cannot remove 'day1/notes.txt': Permission denied
emanon@emanon-MiniBook-X:/home/training/day2$ ls
day1
emanon@emanon-MiniBook-X:/home/training/day2$ sudo rm -r day1
emanon@emanon-MiniBook-X:/home/training/day2$ ls
emanon@emanon-MiniBook-X:/home/training/day2$ cd ..
emanon@emanon-MiniBook-X:/home/training$ ls
day1  day2  day3
emanon@emanon-MiniBook-X:/home/training$ cd day1
emanon@emanon-MiniBook-X:/home/training/day1$ sudo cp plan.txt
cp: missing destination file operand after 'plan.txt'
Try 'cp --help' for more information.
emanon@emanon-MiniBook-X:/home/training/day1$ sudo cp  plan.txt /home/training/day1
cp: 'plan.txt' and '/home/training/day1/plan.txt' are the same file
emanon@emanon-MiniBook-X:/home/training/day1$ sudo cp  plan.txt /home/training/day1/.
cp: 'plan.txt' and '/home/training/day1/./plan.txt' are the same file
emanon@emanon-MiniBook-X:/home/training/day1$ ls
notes.txt  plan.txt
emanon@emanon-MiniBook-X:/home/training/day1$ sudo cp  plan.txt /home/training/day1/.^C
emanon@emanon-MiniBook-X:/home/training/day1$ 
emanon@emanon-MiniBook-X:/home/training/day1$ 
emanon@emanon-MiniBook-X:/home/training/day1$ sudo cp plan.txt ../day2/daily_plan.txt
emanon@emanon-MiniBook-X:/home/training/day1$ cd ..
emanon@emanon-MiniBook-X:/home/training$ ls
day1  day2  day3
emanon@emanon-MiniBook-X:/home/training$ cd day2
emanon@emanon-MiniBook-X:/home/training/day2$ ls
daily_plan.txt
emanon@emanon-MiniBook-X:/home/training/day2$ cat dailay_plan.txt
cat: dailay_plan.txt: No such file or directory
emanon@emanon-MiniBook-X:/home/training/day2$ cat daily_plan.txt
В Linux можно использовать универсальные команды, такие как echo и touch, но я предпочитаю использовать утилиту nano.

Она позволят одной командой создать файл и сразу же вписать в нем необходимый текст.
Удобная и читаемая платформа позволяет вносить разные изменения с текстом в файле.
emanon@emanon-MiniBook-X:/home/training/day2$ cd ..
emanon@emanon-MiniBook-X:/home/training$ cd day1
emanon@emanon-MiniBook-X:/home/training/day1$ sudo mv notes.txt ../day3/dayli_notes.txt
emanon@emanon-MiniBook-X:/home/training/day1$ ls
plan.txt
emanon@emanon-MiniBook-X:/home/training/day1$ cd ..
emanon@emanon-MiniBook-X:/home/training$ ls -la
total 20
drwxr-xr-x 5 root root 4096 Oct 24 13:28 .
drwxr-xr-x 4 root root 4096 Oct 24 13:27 ..
drwxr-xr-x 2 root root 4096 Oct 24 13:51 day1
drwxr-xr-x 2 root root 4096 Oct 24 13:49 day2
drwxr-xr-x 2 root root 4096 Oct 24 13:51 day3
emanon@emanon-MiniBook-X:/home/training$ tree -a
.
├── day1
│   └── plan.txt
├── day2
│   └── daily_plan.txt
└── day3
    └── dayli_notes.txt

4 directories, 3 files
emanon@emanon-MiniBook-X:/home/training$ 

