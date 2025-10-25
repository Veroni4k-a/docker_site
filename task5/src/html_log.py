emanon@emanon-MiniBook-X:~$ cd 1
emanon@emanon-MiniBook-X:~/1$ mkdir task5
emanon@emanon-MiniBook-X:~/1$ cd task5
emanon@emanon-MiniBook-X:~/1/task5$ mkdir project
emanon@emanon-MiniBook-X:~/1/task5$ cd project
emanon@emanon-MiniBook-X:~/1/task5/project$ mkdir bin src docs
emanon@emanon-MiniBook-X:~/1/task5/project$ ls
bin  docs  src
emanon@emanon-MiniBook-X:~/1/task5/project$ cd docs
emanon@emanon-MiniBook-X:~/1/task5/project/docs$ sudo nano text1.txt
emanon@emanon-MiniBook-X:~/1/task5/project/docs$ cat -s text1.txt
Описание проекта

Тема: Познание Linux
Кафедра: ИС
Группа: 43/9
Студентка: Купцова Вероника Евгеньевна
emanon@emanon-MiniBook-X:~/1/task5/project/docs$ cp text1.txt ~/1/task5/project/src/README.txt
emanon@emanon-MiniBook-X:~/1/task5/project/docs$ cd ..
emanon@emanon-MiniBook-X:~/1/task5/project$ cd src
emanon@emanon-MiniBook-X:~/1/task5/project/src$ ls
README.txt
emanon@emanon-MiniBook-X:~/1/task5/project/src$ cp README.txt ~/1/task5/project/bin/text_read.txt
emanon@emanon-MiniBook-X:~/1/task5/project/src$ cd ..
emanon@emanon-MiniBook-X:~/1/task5/project$ ls
bin  docs  src
emanon@emanon-MiniBook-X:~/1/task5/project$ cd bin
emanon@emanon-MiniBook-X:~/1/task5/project/bin$ ls
text_read.txt
emanon@emanon-MiniBook-X:~/1/task5/project/bin$ cd ..
emanon@emanon-MiniBook-X:~/1/task5/project$ touch .hidden_text.txt
emanon@emanon-MiniBook-X:~/1/task5/project$ ls
bin  docs  src
emanon@emanon-MiniBook-X:~/1/task5/project$ ls -la
total 20
drwxrwxr-x 5 emanon emanon 4096 Oct 25 13:57 .
drwxrwxr-x 3 emanon emanon 4096 Oct 25 13:49 ..
drwxrwxr-x 2 emanon emanon 4096 Oct 25 13:57 bin
drwxrwxr-x 2 emanon emanon 4096 Oct 25 13:53 docs
-rw-rw-r-- 1 emanon emanon    0 Oct 25 13:57 .hidden_text.txt
drwxrwxr-x 2 emanon emanon 4096 Oct 25 13:55 src
emanon@emanon-MiniBook-X:~/1/task5/project$ touch .congig.txt
emanon@emanon-MiniBook-X:~/1/task5/project$ ls -la
total 20
drwxrwxr-x 5 emanon emanon 4096 Oct 25 13:58 .
drwxrwxr-x 3 emanon emanon 4096 Oct 25 13:49 ..
drwxrwxr-x 2 emanon emanon 4096 Oct 25 13:57 bin
-rw-rw-r-- 1 emanon emanon    0 Oct 25 13:58 .congig.txt
drwxrwxr-x 2 emanon emanon 4096 Oct 25 13:53 docs
-rw-rw-r-- 1 emanon emanon    0 Oct 25 13:57 .hidden_text.txt
drwxrwxr-x 2 emanon emanon 4096 Oct 25 13:55 src
emanon@emanon-MiniBook-X:~/1/task5/project$ touch log.txt 
emanon@emanon-MiniBook-X:~/1/task5/project$ echo "Текущая дата: $(date '+%d-%m-%Y %H:%M:%S') $(whoami) $(uptime)" >> log.txt
emanon@emanon-MiniBook-X:~/1/task5/project$ cat log.txt
Текущая дата: 25-10-2025 14:01:05 emanon  14:01:05 up  5:45,  1 user,  load average: 0.16, 0.32, 0.39
emanon@emanon-MiniBook-X:~/1/task5/project$ tree -l
.
├── bin
│   └── text_read.txt
├── docs
│   └── text1.txt
├── log.txt
└── src
    └── README.txt

4 directories, 4 files
emanon@emanon-MiniBook-X:~/1/task5/project$ tree -la
.
├── bin
│   └── text_read.txt
├── .congig.txt
├── docs
│   └── text1.txt
├── .hidden_text.txt
├── log.txt
└── src
    └── README.txt

4 directories, 6 files
emanon@emanon-MiniBook-X:~/1/task5/project$ 

