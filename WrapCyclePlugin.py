import sublime
import sublime_plugin
import itertools
import re
import datetime

class WrapCycleCommand(sublime_plugin.WindowCommand):

    PREFERENCES_BASE_NAME   = 'Preferences.sublime-settings'
    WRAP_WIDTH_DEFAULT      = 80
    WRAP_WIDTH_PROPERTY     = 'wrap_width'
    RULERS_PROPERTY         = 'rulers'
    RULERS_DEFAULT          = [80, 100, 120]
    STATUS_KEY              = "Wrap Width"
    STATUS_TEMPLATE         = "Wrap Width: %d"

    def run(self, forward):
        # get the current wrap_width from the user's preferences
        settings = sublime.load_settings(self.PREFERENCES_BASE_NAME)
        
        # Only change settings if 'wrap_width' is supported
        if settings.has(self.WRAP_WIDTH_PROPERTY):

            rulers = settings.get(self.RULERS_PROPERTY, self.RULERS_DEFAULT)
            if rulers == None or len(rulers) == 0:
                rulers = RULERS_DEFAULT

            wrap_width_setting = settings.get(self.WRAP_WIDTH_PROPERTY, self.WRAP_WIDTH_DEFAULT)
            # for some reason you might get 0 instead of `WRAP_WIDTH_DEFAULT` 
            if wrap_width_setting == 0:
                idx = 0
            else:
                idx = rulers.index(wrap_width_setting)
            
            # cycle left or right (forward or backward)
            if forward:
                idx = (idx + 1) % len(rulers)
            else:
                idx = (idx - 1) % len(rulers)

            wrap_width_new = rulers[idx]

            # set the new wrap_width and save the settings
            settings.set(self.WRAP_WIDTH_PROPERTY, wrap_width_new)
            sublime.save_settings(self.PREFERENCES_BASE_NAME)
            # say something in the status bar
            sublime.active_window().active_view().set_status(self.STATUS_KEY, self.STATUS_TEMPLATE % (wrap_width_new))