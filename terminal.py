import sublime
import sublime_plugin
import os
import subprocess


class OpenOsxTerminalCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        view = self.view
        window = view.window()
        file = view.file_name()
        if file:
            thefolder = os.path.dirname(file)
        pd = window.project_data()
        if pd and "folders" in pd and len(pd["folders"]) > 0:
            project_path = pd["folders"][0].get("path")
            if project_path:
                thefolder = project_path

        script = sublime.load_resource(
                    "Packages/OSXTerminal/Terminal.applescript")
        p = subprocess.Popen(['osascript', '-e', script, thefolder], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = p.communicate()
        print(stderr)