
from Launch_Z import Launch_Z
from _Framework.Capabilities import controller_id, inport, outport, CONTROLLER_ID_KEY, PORTS_KEY, NOTES_CC, SCRIPT

def get_capabilities():
    return {CONTROLLER_ID_KEY: controller_id(vendor_id=4661, product_ids=[53], model_name='Launch_Z'),
     PORTS_KEY: [inport(props=[NOTES_CC]),
                 inport(props=[SCRIPT]),
                 outport(props=[NOTES_CC]),
                 outport(props=[SCRIPT])]}


def create_instance(c_instance):
    return Launch_Z(c_instance)