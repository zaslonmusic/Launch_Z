# zaSLON
from Launch_Parent import Launchkey, LaunchkeyControlFactory, make_button, make_configurable_button

class Launch_ZControlFactory(LaunchkeyControlFactory):

    def create_next_track_button(self):
        return make_button(107, 'Next_Track_Button')

    def create_prev_track_button(self):
        return make_button(106, 'Prev_Track_Button')

class Launch_Z(Launchkey):

    def __init__(self, c_instance):
        super(Launch_Z, self).__init__(c_instance, control_factory=Launch_ZControlFactory(), identity_response=(240, 126, 127, 6, 2, 0, 32, 41, 53, 0, 0))
        self._suggested_input_port = 'LK Mini InControl'
        self._suggested_output_port = 'LK Mini InControl'

    def _setup_navigation(self):
        super(Launch_Z, self)._setup_navigation()
        self._next_scene_button = make_button(105, 'Next_Scene_Button')
        self._prev_scene_button = make_button(104, 'Prev_Scene_Button')
        self._session_navigation.set_next_scene_button(self._next_scene_button)
        self._session_navigation.set_prev_scene_button(self._prev_scene_button)

    def _setup_transport(self):
        pass
