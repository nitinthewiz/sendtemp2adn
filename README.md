# sendtemp2adn
A (now defunct) piece of code to send your raspi's temperature to (now defunct) app.net


This program was used to send my raspberry pi's temperature to the ADN social network. It uses Fernando Nava's excellent [python-adn library](https://github.com/fnava621/python-adn)

A crontab was used to run the script every 7 minutes -

*/7 * * * * /home/pi/appnet/sendtemp2adn.py
