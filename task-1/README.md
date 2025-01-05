---
# Task-1 --- The command line cup
---

# Steps did for Step-1
---

Firstly cloned the repository in the local machine using git clone command,git clone `https://github.com/KshitijThareja/TheCommandLineCup.git`. Created a new directory in the same repository named "codes" using the command `mkdir codes`.Went insde the directory using the command `cd codes`.Create files inside the codes folder called Part_1.txt,Part_2.txt,Part_3.txt,Part_4.txt using the command `touch filename.txt`.

---

# Steps did for Step-2 (First Challange)
---

By the problems given, found out the values for x and y as the values of x and y are 6 and 5. So the spell is located in 06th directory and Spell_05. Went inside the directory using `cd 06` and listed the files using the command `ls` and saw the contents inside the text file using the command `cat Spell_05.txt`.Found out the code, copied it and went to the spellbook and saw every visible items in human readable form using the command `ls`.Found the exact name of the file and ran it using python.Found out the code and saved the code in the Part_1.txt file in the directory "codes".

---

# Steps did for Step-3 (Second Challange)
---

Determined the values of x and y and they are 3 and 2. So the spell is located at the 02th directory and Spell_03.txt.Found out the code using the 'cat Spell_03.txt` command. Now i went to the spellbook and ran the file which had the same name and found the secret code. I saved this secret code in the Part_2.txt file in the directory "codes". After this i used the command `git branch -a` to the all the available branchs.

---

#Steps did for Step-4 (Third Challange)
---

The subject taught by Professor Lupin at Hogwarts was `defenseAgainstTheDarkArts` and i have seen this name in the branchs when i did the command `git branch -a`. I moved into that branch using the command `git checkout defenseAgainstTheDarkArts`. Found out the solution for the riddle and it was `Riddikulux`. Found the same name in the spellbook. Since its present in another branch i moved the file into the main branch.Firstly we need to type the command from the main branch spellbook. After going to the main branch spellbook directory i used the command `git checkout <remote branch> <Relative path of the file to be copied from the other branch>`.Ran the file now and found out the secret code. Saved this secret code in the Part_3.txt file in the directory "codes".

---

#Steps did for Step-5 (Fourth Challange)
---

Firstly i used to the command `git log` to checkout the commit logs of that repository.On the 27th july commit i found another puzzle to solve. Found out the values for x and y and they are 7 and 4. So the spell was located in the 07th directory and Spell_04.txt but in thegraveyard. So i `git checkout thegraveyard` and went into the file location, ran the file and found out the spell and went unsde the spellbook and i did the same steps in step-4 as git checking out it to the main file and running it. Saved the code in the Part_4.txt file in the directory "codes".

---

#Steps did for Step-6 (End)
---

Firstly i created a new file called "finalcode.txt" where i pasted all the codes together in the directory "codes". Then i decoded the file which was encoded in base64 using the command `echo <contents in the finalcode.txt> | base64 --decode`. Found another GitHub repository link so i git cloned it to the local machine. Ran the text file and python and i got the congratulation screen.

---

# Steps for pushing the files from local machine to repository

1. Assuming we have set up an SSH in our local machine and added it to our repository.Since its a private repository for making any changes we need to set up and SSH key or any another keys.
  
2. Aftering seting all up clone the repository in our local machine
  
3. aftering doing the changes in the files we need to first add the changes into our repository, for example if we have created a directory named "task-0" we cant leave the directory empty as git wont recogonize it as a file we need to either add contents or a README.md file or .gitignore file.

4. After adding the file go the main directory i.e the "task-0" and then write the command `git add .` where . means everything inside that directory or we can add seperatly also using the command `git add <filename>`.

5. After adding we need to commit it to the github repository for this we can use the command `git commit -m "<any message for commiting>"` where -m used for message.

6. after this we need to push the contents into the repository using the command `git push origin main`.

--- 
