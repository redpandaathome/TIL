# Freetier time up.
Log of considering new mms-api server setup for 2022 🤔

----
## Alternative - Oracle Cloud Free tier
### step1.
Q. How to replace Elastic beanstalk and AWS Code pipeline for CI/CD ??<br>
A. Let's try Jenkins<br><br>

Q2. Jenkins install issue on linux...<br> 
A. Firewall problem and fixed after changing to Ubuntu<br><br>

Q3. Jenkins Plugin install timeout errors... on port 8080<br>
A. Firewall setting trouble shooting... -> partially installed.<br><br>

## step2.
Q.How to set git repository?<br>
A.added new server's newly generated ssh key to github setting. Fixed.<br><br>
Q2.RDS... options are too limited - Just oracle.<br> Worth of refactoring all the codes from mysql-sequelize to oracle-something?<br>
A.There's alternative of using sequelize-oracle. But is it really good idea to go for? 💭<br>

A.Making another oci instance and install mysql to use as a RDS instance.<br><br>

## step3.
- adding .env for prod server and run node<br>

Q. Connection from mysql workbench via ssh was successful. But what about as a RDS using a connection string?


