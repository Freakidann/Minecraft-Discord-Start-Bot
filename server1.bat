@echo off
## Mettre l'emplacement du server avec le Jar dedans
cd server1\
java -Xms3000M -Xmx3000M -jar spigot-1.16.5.jar --nogui
pause
