import logging.config


class PluginLog(object):

    def __init__(self):
        return

    def get_logger(self):
        log_config_file = "/usr/lib/heat/qingcloud_heat_plugin/log/log.conf"
        logging.config.fileConfig(log_config_file)
        qingcloud_log = logging.getLogger("root")
        return qingcloud_log
