# Exercice CRON

Installer cron si la commande ne fonctionne pas

`crontab -l`

Se rendre dans le répertoire courant.

Rendre le script executable

`chmod +x my_cron_script.sh`

Editer le crontab

`crontab -e`

Configuration

`* * * * * CHEMIN_VERS_VOTRE_SCRIPT/my_cron_script.sh`

Afficher le fichier de log

`cat ~/cron_test.log`

Commentez la ligne pour desactiver le CRON :

`crontab -e`

`# * * * * * CHEMIN_VERS_VOTRE_SCRIPT/my_cron_script.sh`
