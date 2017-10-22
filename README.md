<h1 align="center">ArgosMoonPhase</h1>

<h3 align="center">Display the current moon phase in the menu bar</h3>

<div align="center"><img src ="https://user-images.githubusercontent.com/25762130/31857400-d6b9b5b4-b6ab-11e7-90a1-a66bcf07ac57.png" /></div>

This Python 3 script is designed to work with <a href="https://github.com/p-e-w/argos">Argos</a>, a wonderful GNOME 3 shell extention that allows for the easy creation of new extentions.  This program finds the users location with <a href= "https://freegeoip.net/">freegeoip.net</a> and uses that to find the current moon phase with <a href="http://aa.usno.navy.mil/data/docs/api.php">Astronomical Applications API</a>.  The resulting moon phase is displayed as an emoji in the user's GNOME menu bar.  Clicking on the emoji creates a dropdown that displays the name of the current phase, as well as the percent of the moon illuminated.  
</html>

### Installation
**Make sure Argos is installed and working properly in your GNOME 3 installation.**  The install link can be found here <a href="https://extensions.gnome.org/extension/1176/argos/">here</a>.  All that is needed to add this plugin is to download MoonPhase.4h.py and place it in the ~/.config/argos folder.  For example, if the Python file is located in the Downloads folder, the user could run `cp MoonPhase.4h.py ~/.config/argos`.
