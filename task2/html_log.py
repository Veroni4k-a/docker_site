<pre><font color="#26A269"><b>emanon@emanon-MiniBook-X</b></font>:<font color="#12488B"><b>~/1</b></font>$ mkdir task2
<font color="#26A269"><b>emanon@emanon-MiniBook-X</b></font>:<font color="#12488B"><b>~/1</b></font>$ cd task2
<font color="#26A269"><b>emanon@emanon-MiniBook-X</b></font>:<font color="#12488B"><b>~/1/task2</b></font>$ mkdir sandbox
<font color="#26A269"><b>emanon@emanon-MiniBook-X</b></font>:<font color="#12488B"><b>~/1/task2</b></font>$ cd sandbox
<font color="#26A269"><b>emanon@emanon-MiniBook-X</b></font>:<font color="#12488B"><b>~/1/task2/sandbox</b></font>$ mkdir test
<font color="#26A269"><b>emanon@emanon-MiniBook-X</b></font>:<font color="#12488B"><b>~/1/task2/sandbox</b></font>$ touch text1.txt
<font color="#26A269"><b>emanon@emanon-MiniBook-X</b></font>:<font color="#12488B"><b>~/1/task2/sandbox</b></font>$ ^C
<font color="#26A269"><b>emanon@emanon-MiniBook-X</b></font>:<font color="#12488B"><b>~/1/task2/sandbox</b></font>$ ^C
<font color="#26A269"><b>emanon@emanon-MiniBook-X</b></font>:<font color="#12488B"><b>~/1/task2/sandbox</b></font>$ cd test
<font color="#26A269"><b>emanon@emanon-MiniBook-X</b></font>:<font color="#12488B"><b>~/1/task2/sandbox/test</b></font>$ touch text1.txt
<font color="#26A269"><b>emanon@emanon-MiniBook-X</b></font>:<font color="#12488B"><b>~/1/task2/sandbox/test</b></font>$ echo &quot;Строчка текста&quot; &gt;&gt; text1.txt
<font color="#26A269"><b>emanon@emanon-MiniBook-X</b></font>:<font color="#12488B"><b>~/1/task2/sandbox/test</b></font>$ touch text2.txt
<font color="#26A269"><b>emanon@emanon-MiniBook-X</b></font>:<font color="#12488B"><b>~/1/task2/sandbox/test</b></font>$ touch text3.txt
<font color="#26A269"><b>emanon@emanon-MiniBook-X</b></font>:<font color="#12488B"><b>~/1/task2/sandbox/test</b></font>$ echo &quot;Еще одна строчка во втором файле&quot; &gt;&gt; text2.txt
<font color="#26A269"><b>emanon@emanon-MiniBook-X</b></font>:<font color="#12488B"><b>~/1/task2/sandbox/test</b></font>$ echo &quot;Студентка ИС-43/9&quot; &gt;&gt; text3.txt
<font color="#26A269"><b>emanon@emanon-MiniBook-X</b></font>:<font color="#12488B"><b>~/1/task2/sandbox/test</b></font>$ cat text1.txt text2.txt text3.txt
Строчка текста
Еще одна строчка во втором файле
Студентка ИС-43/9
<font color="#26A269"><b>emanon@emanon-MiniBook-X</b></font>:<font color="#12488B"><b>~/1/task2/sandbox/test</b></font>$ cat text1.txt text2.txt text3.txt &gt;&gt;general_text.txt
<font color="#26A269"><b>emanon@emanon-MiniBook-X</b></font>:<font color="#12488B"><b>~/1/task2/sandbox/test</b></font>$ cat general_text.txt
Строчка текста
Еще одна строчка во втором файле
Студентка ИС-43/9
<font color="#26A269"><b>emanon@emanon-MiniBook-X</b></font>:<font color="#12488B"><b>~/1/task2/sandbox/test</b></font>$ mkdir backup
<font color="#26A269"><b>emanon@emanon-MiniBook-X</b></font>:<font color="#12488B"><b>~/1/task2/sandbox/test</b></font>$ cp general_text.txt /backup
cp: cannot create regular file &apos;/backup&apos;: Permission denied
<font color="#26A269"><b>emanon@emanon-MiniBook-X</b></font>:<font color="#12488B"><b>~/1/task2/sandbox/test</b></font>$ sudo cp general_text.txt /backup
[sudo] password for emanon: 
<font color="#26A269"><b>emanon@emanon-MiniBook-X</b></font>:<font color="#12488B"><b>~/1/task2/sandbox/test</b></font>$ ls
<font color="#12488B"><b>backup</b></font>  general_text.txt  text1.txt  text2.txt  text3.txt
<font color="#26A269"><b>emanon@emanon-MiniBook-X</b></font>:<font color="#12488B"><b>~/1/task2/sandbox/test</b></font>$ cd backup
<font color="#26A269"><b>emanon@emanon-MiniBook-X</b></font>:<font color="#12488B"><b>~/1/task2/sandbox/test/backup</b></font>$ ls
<font color="#26A269"><b>emanon@emanon-MiniBook-X</b></font>:<font color="#12488B"><b>~/1/task2/sandbox/test/backup</b></font>$ sudo cp general_text.txt ~/1/task2/sandbox/test/backup
cp: cannot stat &apos;general_text.txt&apos;: No such file or directory
<font color="#26A269"><b>emanon@emanon-MiniBook-X</b></font>:<font color="#12488B"><b>~/1/task2/sandbox/test/backup</b></font>$ cd ..
<font color="#26A269"><b>emanon@emanon-MiniBook-X</b></font>:<font color="#12488B"><b>~/1/task2/sandbox/test</b></font>$ sudo cp general_text.txt ~/1/task2/sandbox/test/backup
<font color="#26A269"><b>emanon@emanon-MiniBook-X</b></font>:<font color="#12488B"><b>~/1/task2/sandbox/test</b></font>$ ls
<font color="#12488B"><b>backup</b></font>  general_text.txt  text1.txt  text2.txt  text3.txt
<font color="#26A269"><b>emanon@emanon-MiniBook-X</b></font>:<font color="#12488B"><b>~/1/task2/sandbox/test</b></font>$ cd backup
<font color="#26A269"><b>emanon@emanon-MiniBook-X</b></font>:<font color="#12488B"><b>~/1/task2/sandbox/test/backup</b></font>$ ls
general_text.txt
<font color="#26A269"><b>emanon@emanon-MiniBook-X</b></font>:<font color="#12488B"><b>~/1/task2/sandbox/test/backup</b></font>$ ls
general_text.txt
<font color="#26A269"><b>emanon@emanon-MiniBook-X</b></font>:<font color="#12488B"><b>~/1/task2/sandbox/test/backup</b></font>$ cd ..
<font color="#26A269"><b>emanon@emanon-MiniBook-X</b></font>:<font color="#12488B"><b>~/1/task2/sandbox/test</b></font>$ ls
<font color="#12488B"><b>backup</b></font>  general_text.txt  text1.txt  text2.txt  text3.txt
<font color="#26A269"><b>emanon@emanon-MiniBook-X</b></font>:<font color="#12488B"><b>~/1/task2/sandbox/test</b></font>$ rm -i text3.txt
rm: remove regular file &apos;text3.txt&apos;? y
<font color="#26A269"><b>emanon@emanon-MiniBook-X</b></font>:<font color="#12488B"><b>~/1/task2/sandbox/test</b></font>$ rm  text2.txt
<font color="#26A269"><b>emanon@emanon-MiniBook-X</b></font>:<font color="#12488B"><b>~/1/task2/sandbox/test</b></font>$ cd ..
<font color="#26A269"><b>emanon@emanon-MiniBook-X</b></font>:<font color="#12488B"><b>~/1/task2/sandbox</b></font>$ cd ..
<font color="#26A269"><b>emanon@emanon-MiniBook-X</b></font>:<font color="#12488B"><b>~/1/task2</b></font>$ rm -r sandbox
rm: remove write-protected regular file &apos;sandbox/test/backup/general_text.txt&apos;? y
<font color="#26A269"><b>emanon@emanon-MiniBook-X</b></font>:<font color="#12488B"><b>~/1/task2</b></font>$ ls
<font color="#26A269"><b>emanon@emanon-MiniBook-X</b></font>:<font color="#12488B"><b>~/1/task2</b></font>$ ls
<font color="#26A269"><b>emanon@emanon-MiniBook-X</b></font>:<font color="#12488B"><b>~/1/task2</b></font>$ 

</pre>
