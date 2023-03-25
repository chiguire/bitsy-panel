# Bitsy-Ledpanel

Ciro Durán (ciro.duran@gmail.com / [@chiguire@mastodon.social](https://mastodon.social/@chiguire) )

Re-implementation of the [Bitsy](https://www.bitsy.org) engine in Python, with its visual output going to a LED panel.

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
* Run bitsy-panel.py --game-dir=[...path to where exported games are...]

## Games accepted

Bitsy-panel accepts exported Bitsy games, compatible with up to Bitsy 8.4.

This project has no editor. You should use the [original Bitsy editor](https://ledoux.itch.io/bitsy) to make your games.
