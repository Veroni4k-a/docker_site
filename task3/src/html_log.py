<pre> mkdir task3
<font color="#26A269"><b>emanon@emanon-MiniBook-X</b></font>:<font color="#12488B"><b>~/1</b></font>$ cd task3
<font color="#26A269"><b>emanon@emanon-MiniBook-X</b></font>:<font color="#12488B"><b>~/1/task3</b></font>$ mkdir time_experiment
<font color="#26A269"><b>emanon@emanon-MiniBook-X</b></font>:<font color="#12488B"><b>~/1/task3</b></font>$ echo &quot;Файл создан: $(date)&quot; &gt; file1.txt
<font color="#26A269"><b>emanon@emanon-MiniBook-X</b></font>:<font color="#12488B"><b>~/1/task3</b></font>$ cd^C
<font color="#26A269"><b>emanon@emanon-MiniBook-X</b></font>:<font color="#12488B"><b>~/1/task3</b></font>$ ^C
<font color="#26A269"><b>emanon@emanon-MiniBook-X</b></font>:<font color="#12488B"><b>~/1/task3</b></font>$ cd time_experiment
<font color="#26A269"><b>emanon@emanon-MiniBook-X</b></font>:<font color="#12488B"><b>~/1/task3/time_experiment</b></font>$ echo &quot;Файл создан: $(date)&quot; &gt; file1.txt<font color="#26A269"><b>emanon@emanon-MiniBook-X</b></font>:<font color="#12488B"><b>~/1/task3/time_experiment</b></font>$ echo &quot;Пользователь: $(whoami)&quot; &gt;&gt; file1.txt
<font color="#26A269"><b>emanon@emanon-MiniBook-X</b></font>:<font color="#12488B"><b>~/1/task3/time_experiment</b></font>$ touch -d &quot;Jan 1&quot; file1.txt
<font color="#26A269"><b>emanon@emanon-MiniBook-X</b></font>:<font color="#12488B"><b>~/1/task3/time_experiment</b></font>$ echo &quot;Второй файл&quot; &gt; file2.txt
<font color="#26A269"><b>emanon@emanon-MiniBook-X</b></font>:<font color="#12488B"><b>~/1/task3/time_experiment</b></font>$ touch -a -d &quot;2 hours ago&quot; file2.txt
<font color="#26A269"><b>emanon@emanon-MiniBook-X</b></font>:<font color="#12488B"><b>~/1/task3/time_experiment</b></font>$ echo &quot;Третий файл&quot; &gt; file3.txt
<font color="#26A269"><b>emanon@emanon-MiniBook-X</b></font>:<font color="#12488B"><b>~/1/task3/time_experiment</b></font>$ touch -m -d &quot;tomorrow&quot; file3.txt
<font color="#26A269"><b>emanon@emanon-MiniBook-X</b></font>:<font color="#12488B"><b>~/1/task3/time_experiment</b></font>$ ls -la
total 20
drwxrwxr-x 2 emanon emanon 4096 Oct 25 12:53 <font color="#12488B"><b>.</b></font>
drwxrwxr-x 3 emanon emanon 4096 Oct 25 12:52 <font color="#12488B"><b>..</b></font>
-rw-rw-r-- 1 emanon emanon   88 Jan  1  2025 file1.txt
-rw-rw-r-- 1 emanon emanon   22 Oct 25 12:53 file2.txt
-rw-rw-r-- 1 emanon emanon   22 Oct 26  2025 file3.txt
<font color="#26A269"><b>emanon@emanon-MiniBook-X</b></font>:<font color="#12488B"><b>~/1/task3/time_experiment</b></font>$ # Добавляем строку с текущей датой в формате «день-месяц-год часы:минуты:секунды»
echo &quot;Текущая дата: $(date &apos;+%d-%m-%Y %H:%M:%S&apos;)&quot; &gt;&gt; file1.txt
<font color="#26A269"><b>emanon@emanon-MiniBook-X</b></font>:<font color="#12488B"><b>~/1/task3/time_experiment</b></font>$ echo &quot;Текущая дата: $(date &apos;+%d-%m-%Y %H:%M:%S&apos;)&quot; &gt;&gt; file1.txt
<font color="#26A269"><b>emanon@emanon-MiniBook-X</b></font>:<font color="#12488B"><b>~/1/task3/time_experiment</b></font>$ cat file1.txt
Файл создан: Sat Oct 25 12:52:48 PM MSK 2025
Пользователь: emanon
Текущая дата: 25-10-2025 12:54:36
Текущая дата: 25-10-2025 12:55:24
<font color="#26A269"><b>emanon@emanon-MiniBook-X</b></font>:<font color="#12488B"><b>~/1/task3/time_experiment</b></font>$ stat file1.txt file2.txt file3.txt
  File: file1.txt
  Size: 178       	Blocks: 8          IO Block: 4096   regular file
Device: 259,2	Inode: 16270827    Links: 1
Access: (0664/-rw-rw-r--)  Uid: ( 1000/  emanon)   Gid: ( 1000/  emanon)
Access: 2025-10-25 12:55:38.282619597 +0300
Modify: 2025-10-25 12:55:24.432981285 +0300
Change: 2025-10-25 12:55:24.432981285 +0300
 Birth: 2025-10-25 12:52:48.003797123 +0300
  File: file2.txt
  Size: 22        	Blocks: 8          IO Block: 4096   regular file
Device: 259,2	Inode: 16270829    Links: 1
Access: (0664/-rw-rw-r--)  Uid: ( 1000/  emanon)   Gid: ( 1000/  emanon)
Access: 2025-10-25 10:53:43.090919874 +0300
Modify: 2025-10-25 12:53:33.737892263 +0300
Change: 2025-10-25 12:53:43.090321279 +0300
 Birth: 2025-10-25 12:53:33.737892263 +0300
  File: file3.txt
  Size: 22        	Blocks: 8          IO Block: 4096   regular file
Device: 259,2	Inode: 16270830    Links: 1
Access: (0664/-rw-rw-r--)  Uid: ( 1000/  emanon)   Gid: ( 1000/  emanon)
Access: 2025-10-25 12:53:55.439888064 +0300
Modify: 2025-10-26 12:54:03.766882067 +0300
Change: 2025-10-25 12:54:03.766270382 +0300
 Birth: 2025-10-25 12:53:55.439888064 +0300
<font color="#26A269"><b>emanon@emanon-MiniBook-X</b></font>:<font color="#12488B"><b>~/1/task3/time_experiment</b></font>$ 

</pre>
