# WrapCycle README

## Overview

The purpose of this plugin is to quickly cycle through a list of wrap `wrap_width` settings in the user preferences.

Although it's fairly easy to change `wrap_width` I like to have a keyboard shortcut to cycle round ruler markers, especially when I change screen size, or split the window in two, or just go from text to code.

## Get started

1. Open the user preferences `Sublime Text > Preferences > Settings`
2. In the *User* preferences, set the `rulers` option to your desired cycle points e.g. `[80, 100, 120]`
3. Use key mappings (see below) to cycle round

## Defaults

If no rulers are set, the plugin will cycle through `[80, 100, 120]`. It won't set the rulers

## Key mappings

The user can switch to a different `wrap_width` using the following default key maps:

- CTRL + Left Arrow: cycle right to left in the list (usually decreasing the width)
- CTRL + Right Arrow: cycle left to right in the list (usually increasing the width)

## TODO

- [ ] add unit tests