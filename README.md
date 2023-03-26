# Bitsy-Ledpanel

Ciro Durán (ciro.duran@gmail.com / [@chiguire@mastodon.social](https://mastodon.social/@chiguire) )

Implements a large LED panel display software for [Bitsy](https://www.bitsy.org) games. This script runs a webserver that accepts a localhost websocket connection. The connection receives graphical data from a modified Bitsy exported game and display such data in the panel.

Part of an installation to allow people play Bitsy games in a large screen.

Work in progress, no releases yet.

## Requirements

* Raspberry Pi 3
* 4 64x64 LED panels chained together
* Raspberry Pi LED panel bonnet optional
* Power supply for panels and Raspberry Pi
* Input (tbd)

## Installation

* Create virtual environment and install requirements.txt
* Run bitsy-panel.py --port=[webserver port]

## Games accepted

Bitsy-panel accepts exported Bitsy games, compatible with up to Bitsy 8.4. Bitsy games must be modified to send graphical data to a websocket (method to do this tbd).

This project has no editor. You should use the [original Bitsy editor](https://ledoux.itch.io/bitsy) to make your games, export them, and then modify them.
