emanon@emanon-MiniBook-X:~/1/task3$ cd ..
emanon@emanon-MiniBook-X:~/1$ mkdir manuals
emanon@emanon-MiniBook-X:~/1$ sudo nano Linux.txt
[sudo] password for emanon: 
emanon@emanon-MiniBook-X:~/1$ sudo nano Linux_command.txt
emanon@emanon-MiniBook-X:~/1$ sudo nano Linux_command.txt
emanon@emanon-MiniBook-X:~/1$ sudo nano Linux_command.txt
emanon@emanon-MiniBook-X:~/1$ cat -n Linux.txt
     1	# Файл с кратким описанием Linux
     2	
     3	Linux - это операционная сичтема, которая на данной момент набирает свою популярность.Лично я столкнулась с ней когда,стала работать с сайтами - большинство сервером на Linux-ядре, поэтому знание базовых команд необходимо знать каждому программисту.
     4	Когда я сменила место работы и стала инженером-программистом,то только стала развивать свои  навыки, так как большинство одноплатных компьютеров работают только на ядре Linux.Это связано с тем,что Windows требует большие требования к железу,в отличии от Linux.
     5	
     6	Основне плюсы Linux:
     7	
     8	-Open Source -система с открытым исходным кодом.
     9	-Гибкие настройки 
    10	-Большой выбор Linux программ, каждый выбирает под себя,многие программисты выбирают arch-linux так как имеет больше возможности в настройках,но они для более продвинутых пользователей.Лично я выбираю Ubuntu и Raspberry PI OS (на Linux Debian)
    11	-Производительность
    12	-Безопсность
    13	-Много документаций и форумов для обсуждения 
    14	
emanon@emanon-MiniBook-X:~/1$ cat Linux.txt Linux_command.txt >> Linux_general.txt
emanon@emanon-MiniBook-X:~/1$ ls
Linux_command.txt  Linux_general.txt  Linux.txt  manuals  task1  task2  task3
emanon@emanon-MiniBook-X:~/1$ cat Linux_general.txt
# Файл с кратким описанием Linux

Linux - это операционная сичтема, которая на данной момент набирает свою популярность.Лично я столкнулась с ней когда,стала работать с сайтами - большинство сервером на Linux-ядре, поэтому знание базовых команд необходимо знать каждому программисту.
Когда я сменила место работы и стала инженером-программистом,то только стала развивать свои  навыки, так как большинство одноплатных компьютеров работают только на ядре Linux.Это связано с тем,что Windows требует большие требования к железу,в отличии от Linux.

Основне плюсы Linux:

-Open Source -система с открытым исходным кодом.
-Гибкие настройки 
-Большой выбор Linux программ, каждый выбирает под себя,многие программисты выбирают arch-linux так как имеет больше возможности в настройках,но они для более продвинутых пользователей.Лично я выбираю Ubuntu и Raspberry PI OS (на Linux Debian)
-Производительность
-Безопсность
-Много документаций и форумов для обсуждения 

Пять команд Linux без которых я не могу обойтись и день:

1.sudo apt update
2.sudo apt upgrade
3.cd (cd ..)
4.echo "" >> main.py
5.ls 
6. mkdir dir 

emanon@emanon-MiniBook-X:~/1$ cp Linux_general.txt ~/1/manuals
emanon@emanon-MiniBook-X:~/1$ cp Linux.txt ~/1/manuals
emanon@emanon-MiniBook-X:~/1$ cp Linux_command.txt ~/1/manuals
emanon@emanon-MiniBook-X:~/1$ cd manuals
emanon@emanon-MiniBook-X:~/1/manuals$ ls
Linux_command.txt  Linux_general.txt  Linux.txt
emanon@emanon-MiniBook-X:~/1/manuals$ cd ..
emanon@emanon-MiniBook-X:~/1$ ls
Linux_command.txt  Linux_general.txt  Linux.txt  manuals  task1  task2  task3
emanon@emanon-MiniBook-X:~/1$ rm Linux_command.txt 
rm: remove write-protected regular file 'Linux_command.txt'? y
emanon@emanon-MiniBook-X:~/1$ ls
Linux_general.txt  Linux.txt  manuals  task1  task2  task3
emanon@emanon-MiniBook-X:~/1$ rm Linux.txt 
rm: remove write-protected regular file 'Linux.txt'? y
emanon@emanon-MiniBook-X:~/1$ ls
Linux_general.txt  manuals  task1  task2  task3
emanon@emanon-MiniBook-X:~/1$ rm Linux_general.txt 
emanon@emanon-MiniBook-X:~/1$ ls
manuals  task1  task2  task3
emanon@emanon-MiniBook-X:~/1$ cd manuals
emanon@emanon-MiniBook-X:~/1/manuals$ ls
Linux_command.txt  Linux_general.txt  Linux.txt
emanon@emanon-MiniBook-X:~/1/manuals$ ls -S
Linux_general.txt  Linux.txt  Linux_command.txt
emanon@emanon-MiniBook-X:~/1/manuals$ ls -t
Linux_command.txt  Linux.txt  Linux_general.txt
emanon@emanon-MiniBook-X:~/1/manuals$ ls -la
total 20
drwxrwxr-x 2 emanon emanon 4096 Oct 25 13:30 .
drwxrwxr-x 7 emanon emanon 4096 Oct 25 13:32 ..
-rw-r--r-- 1 emanon emanon  190 Oct 25 13:30 Linux_command.txt
-rw-rw-r-- 1 emanon emanon 1853 Oct 25 13:30 Linux_general.txt
-rw-r--r-- 1 emanon emanon 1663 Oct 25 13:30 Linux.txt
emanon@emanon-MiniBook-X:~/1/manuals$ ls -lA
total 12
-rw-r--r-- 1 emanon emanon  190 Oct 25 13:30 Linux_command.txt
-rw-rw-r-- 1 emanon emanon 1853 Oct 25 13:30 Linux_general.txt
-rw-r--r-- 1 emanon emanon 1663 Oct 25 13:30 Linux.txt
emanon@emanon-MiniBook-X:~/1/manuals$ touch .hidden_file.txt
emanon@emanon-MiniBook-X:~/1/manuals$ ls 
Linux_command.txt  Linux_general.txt  Linux.txt
emanon@emanon-MiniBook-X:~/1/manuals$ ls -la
total 20
drwxrwxr-x 2 emanon emanon 4096 Oct 25 13:36 .
drwxrwxr-x 7 emanon emanon 4096 Oct 25 13:32 ..
-rw-rw-r-- 1 emanon emanon    0 Oct 25 13:36 .hidden_file.txt
-rw-r--r-- 1 emanon emanon  190 Oct 25 13:30 Linux_command.txt
-rw-rw-r-- 1 emanon emanon 1853 Oct 25 13:30 Linux_general.txt
-rw-r--r-- 1 emanon emanon 1663 Oct 25 13:30 Linux.txt
emanon@emanon-MiniBook-X:~/1/manuals$ ls -lA
total 12
-rw-rw-r-- 1 emanon emanon    0 Oct 25 13:36 .hidden_file.txt
-rw-r--r-- 1 emanon emanon  190 Oct 25 13:30 Linux_command.txt
-rw-rw-r-- 1 emanon emanon 1853 Oct 25 13:30 Linux_general.txt
-rw-r--r-- 1 emanon emanon 1663 Oct 25 13:30 Linux.txt
emanon@emanon-MiniBook-X:~/1/manuals$ sudo nano .hidden_file.txt
emanon@emanon-MiniBook-X:~/1/manuals$ sudo nano .hidden_file.txt
emanon@emanon-MiniBook-X:~/1/manuals$ 

