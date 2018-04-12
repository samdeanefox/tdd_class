"""Goal: Demo of the logging module in Python

Severity: DEBUG INFO WARNING ERROR CRITICAL
By default, INFO and below is filtered out.

Logging supports different "loggers" for different systems.
It is often helpful to divide messages into sub-systems.

"""

import logging

log_format = '%(name)s | %(levelname)s | %(module)s:%(lineno)s | %(message)s'

logging.basicConfig(level=logging.DEBUG,
                    format=log_format,
                    filename='sample.log')

logging.critical('The CPU is on fire')
logging.error('13 records read but only 11 written')
logging.warning('10 credits remaining')
logging.info('ran %d tests in %.6f seconds', 4, 13e-6)
logging.debug('garbage collector collected %d objects', 7)

management = logging.getLogger('mgmt')
management.info('Arrived to work at 9am today')

dev = logging.getLogger('developers')
dev.critical('The automation is broken!')

module_logger = logging.getLogger(__name__)
module_logger.info('Currently executing %s module', __name__)

values = [0,1,2,3]
try:
    print(values[100])
except IndexError:
    logging.exception('oops! something went wrong!')