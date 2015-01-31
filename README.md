# PackageGrupper
Sublime Text package group manager

## Summary
The PackageGrupper allows easily toggle(disable/unable) groups of packages which are created by user.
See example below. This is useful when you work with Laravel for example and want to disable other framework packages like Codeigniter, which contains multiple packages (ex. "CodeIgniter 2 ModelController", "CodeIgniter Snippets", "CodeIgniter Utilities", ...). You can disable all them at once.

## Usage
Define groups in `Preferences -> Package Settings -> Package Grupper ` settings (you can find examples of grouping your packages in `Settings-Default`).
Cut the example from this file and Paste it in  Settings-User, after you can modify it as you wish. You can find the list of installed packages in here `Preferences -> Package Settings -> Package Control -> Settings-User `.

* Select `"Package Grupper"` from the Command Palette (Ctrl+Shift+p)
* Choose `Enable Package Group` or `Disable Package Group` then choose the group.
* That's it.

## Installation

### Using Sublime Package Control

Using Will Bond's [Sublime Package Control](http://wbond.net/sublime_packages/package_control),

- Open the Command Palette `Tools -> Command Palette...`.
- Type `Package Control: Install Package`.
- Search for `PackageGrupper` in the packages list.

### Download Manually

* Download the files using the GitHub .zip download option
* Unzip the files and rename the folder to `PackageGrupper`
* Find your `Packages` directory using the menu item  `Preferences -> Browse Packages...`
* Copy the folder into your Sublime Text `Packages` directory

**Example User Settings **

* Modify this as you wish

```json
 "groups": {
		"Css / Less": [
			"CSS Media Query Snippets",
			"CSS Snippets",
			"Emmet Css Snippets",
			"Hayaku - tools for writing CSS faster",
			"SublimeLinter-csslint",
			"LESS",
			"LESS-build",
			"Less2Css",
			"lessc"
		],
		"Codeigniter": [
			"CodeIgniter 2 ModelController",
			"CodeIgniter Snippets",
			"CodeIgniter Utilities"
		],
		"Laravel": [
			"Laravel 4 Artisan",
			"Laravel Blade Highlighter"
		],
		"Bootstrap": [
			"Bootstrap 3 Snippets",
			"Goto Bootstrap",
			"Twitter Bootstrap ClassNames Completions"
		],
		"Git": [
			"Gist",
			"Git",
			"SideBarGit"
		],
		"Tools": [
			"Alignment",
			"auto-save",
			"CodeFormatter",
			"ColorPicker",
			"ColorSchemeSelector",
			"Composer",
			"Console Wrap for js",
			"FileBrowser",
			"GoToLastEdit",
			"Grunt",
			"Grunt Snippets",
			"JsFormat",
			"LiveReload",
			"MaxPane",
			"More Layouts",
			"npm",
			"SFTP",
			"Terminal"
		]

	} 
```
---
