@echo off
cd server2\
## Mettre l'emplacement du server avec le Jar dedans
java -Xms1000M -Xmx1000M -jar spigot-1.16.5.jar --nogui
pause
