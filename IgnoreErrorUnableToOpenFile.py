import sublime_plugin

REGEX_TO_IGNORE = '^.*:$\n\s+ERROR: Unable to open file\n\n'


def is_search_view(view):
    return view.scope_name(0).startswith('text.find-in-files')


class IgnoreErrorUnableToOpenFileCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        if (is_search_view(self.view)):
            regions = self.view.find_all(REGEX_TO_IGNORE)

            for region in regions:
                self.view.erase(edit, region)


class IgnoreErrorUnableToOpenFileListener(sublime_plugin.ViewEventListener):
    def on_modified(self):
        if (is_search_view(self.view)):
            self.view.run_command('ignore_error_unable_to_open_file')
