# dashcast

Un service de streaming open source en pair to pair utilisant l'encodage AV1. 

Lorsque vous lancez le programme vous devez indiquer si vous voulez regarder un stream ou en commancer un.

Un viewer peux envoyer des messages et voir les messages des autres, le tout en utilisant une interface web.

Install chocolatey if you are on windows to use auto install of FFMPEG :

```
Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))
```
