# alfred-password-generator
Yet another [Alfred 4][1] workflow for generating passwords.

## Installation

1) Install the [pwgen][2] to your MacOS.

   - You could do it for example by using [Homebrew][3] and installing [pwgen package.][4]
   - ````brew install pwgen````
2) Install [alfred-password-generator workflow.][5]
3) All further updates are handled automatically.

## Usage

Workflow could be executed by typing ```passwd``` followed by the expected password length.

![Alfred password generator](doc/images/alfred-password-generator-execution.png?raw=true "")

Three different passwords will be generated.

- Alphanumeric password with special characters
- Alphanumeric password
- Numeric password

Select the one you would like to use and press <kbd>Enter</kbd>. Password will be copied to the cipboard in a transient mode, which means,
that password will not be saved in the clipboard history.

Before selection, you can also press <kbd>⌘</kbd> to additionally show the selected password using the Alfred Large Type.

![Alfred actions submenu screenshot](doc/images/alfred-password-generator-large-type.png?raw=true "")

-------------------

The default shortcut ```passwd``` could be easily changed in workflow settings. Just overwrite the ```passwd``` value of ```keyword```.

![Alfred actions submenu screenshot](doc/images/alfred-password-generator-settings.png?raw=true "")


[1]: https://www.alfredapp.com/
[2]: https://sourceforge.net/projects/pwgen/
[3]: https://brew.sh/
[4]: https://formulae.brew.sh/formula/pwgen
[5]: https://github.com/vookimedlo/alfred-password-generator/releases/latest