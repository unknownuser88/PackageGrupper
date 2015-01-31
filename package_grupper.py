import sublime
import sublime_plugin
import os

class GrupperMenuShowCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        self.settings = sublime.load_settings("PackageGrupper.sublime-settings")
        self.menu = ['Enable Package Group', 'Disable Package Group', 'Group Settings']
        show_quick_panel(self, self.menu, self.menuCallback)

    def menuCallback(self, index):
        if index == -1:
            return
        self.setiingsGroups = self.settings.get("groups", [])
        self.keys = list(self.setiingsGroups.keys())
        if len(self.setiingsGroups) == 0:
            open_plugin_system_settings(self)
            return
        if index == 0:
            show_quick_panel(self,self.keys, self.enableMenu)
        if index == 1:
            show_quick_panel(self,self.keys, self.disableMenu)
        if index == 2:
            open_plugin_system_settings(self)

    def enableMenu(self, index):
        if index == -1:
            return
        pList = self.generateNewPackageList(index, False)
        self.saveList(pList)

    def disableMenu(self, index):
        if index == -1:
            return
        pList = self.generateNewPackageList(index, True)
        self.saveList(pList)

    def generateNewPackageList(self, index, enable=True):
        groups = list(self.setiingsGroups.values()) # all groups
        packages = groups[index] # group packages
        sublimeSettings = sublime.load_settings("Preferences.sublime-settings")
        sublime_ignored_packages = sublimeSettings.get("ignored_packages")
        # print(packages)
        sublime.status_message("  |  ".join(packages))
        if enable:
            for p in packages:
                if p not in sublime_ignored_packages:
                    sublime_ignored_packages.append(p)
        else:
            for p in packages:
                if p in sublime_ignored_packages:
                    sublime_ignored_packages.remove(p)
        return sublime_ignored_packages

    def saveList(self, pList):
        settings = sublime.load_settings("Preferences.sublime-settings")
        settings.set('ignored_packages', pList)
        sublime.save_settings("Preferences.sublime-settings")
        # sublime.status_message(('Success'))

def open_plugin_system_settings(self):
    self.view.window().open_file("PackageGrupper.sublime-settings")

def show_quick_panel(self, options, done_callback, index=None):
    if index is None or not IS_ST3 or not self.settings.get("return_to_previous", False):
        sublime.set_timeout(lambda: self.view.window().show_quick_panel(options, done_callback), 10)
    else:
        sublime.set_timeout(lambda: self.view.window().show_quick_panel(options, done_callback, selected_index=index), 10)

