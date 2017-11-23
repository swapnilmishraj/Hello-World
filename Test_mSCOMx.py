# -*- coding: iso-8859-15 -*-
"""
\mainpage Software Test Specification
\section intro_sec Introduction
In this document the test scenarios and test cases for the MLib mSCOMx with SYS_MOS83x are specified

\section Groups
- \subpage Scenarios
- \subpage Cases

\page Cases Test-Cases
- Test_mSCOMx.TestCase_mSCOMx

\page Scenarios Test-Scenarios
- Test_mSCOMx.TestScenario_mSCOMx.all
"""
import xmlrunner
from util_syscom import *
import unittest
import time
from collections import namedtuple
import numpy as np
err = getMASErrors()

USINT = namedtuple('USINT', ['MIN', 'MAX', 'MID'])(0, 255, 255/2)
UINT = namedtuple('UINT', ['MIN', 'MAX', 'MID'])(0, 65535, 65535/2)


class SCOM_X_CAN_INIT_IO_T:
    """ Class usable as IO values for SCOM_X_CAN_INIT
    """
    def __init__(self, **kwargs):
        # Input variable
        self.xInit = kwargs.get('xInit')
        self.usiInterfaceId = kwargs.get('usiInterfaceId')
        self.udiSafetyMessageIdentifier = kwargs.get('udiSafetyMessageIdentifier')
        self.usiPDO = kwargs.get('usiPDO')
        
        # Output variable
        self.uiLinkHandler = kwargs.get('uiLinkHandler', -1)
        self.xError = kwargs.get('xError')
        self.iStatus = kwargs.get('iStatus')


class SCOM_X_LAN_CH_INIT_IO_T(object):
    """ Class usable as IO values for function block SCOMx_LAN_CH_INIT
    """
    def __init__(self, **kwargs):
        # input variables
        self.xInit = kwargs.get('xInit', False)
        self.usiInterfaceId = kwargs.get('usiInterfaceId', 1)
        self.udiSafetyMsgId = kwargs.get('udiSafetyMsgId', 1)
        self.uiSafetyComPort = kwargs.get('uiSafetyComPort', 30270)
        self.sSafetyComBroadAddr = kwargs.get('sSafetyComBroadAddr', '255.255.255.255')
        
        # output variables
        self.uiLinkHandler = -1
        self.xError = False
        self.iStatus = -1


class SCOM_X_CPL_CO_INIT_IO_T(object):
    """ Class usable as IO values for function block SCOM_X_CPL_CO_INIT
    """
    def __init__(self, **kwargs):
        # input variables
        self.xInit = kwargs.get('xInit', False)
        self.usiInterfaceId = kwargs.get('usiInterfaceId', 1)
        self.udiSafetyMsgId = kwargs.get('udiSafetyMsgId', 1)
        self.usiNodeAddr = kwargs.get('usiNodeAddr', 0)
        
        # output variables
        self.uiLinkHandler = -1
        self.xError = False
        self.iStatus = -1


class SCOM_X_PRODUCER_IO_T:
    """ Class usable as IO values for Function Block SCOM_X_PRODUCER
    """
    def __init__(self, **kwargs):
        # Input variable
        self.xEnable = kwargs.get('xEnable')
        self.usiProducerInstanceId = kwargs.get('usiProducerInstanceId')
        self.uiLinkHandler = kwargs.get('uiLinkHandler')
        self.uiEventTime = kwargs.get('uiEventTime')
        self.uiInhibitTime = kwargs.get('uiInhibitTime')
        
        # Output variable
        self.pDone = kwargs.get('pDone')
        self.xError = kwargs.get('xError')
        self.iStatus = kwargs.get('iStatus')


class SCOM_X_CONSUMER_IO_T:
    """ Class usable as IO values for Function Block SCOM_X_CONSUMER
    """
    def __init__(self, **kwargs):
        # Input variable
        self.xEnable = kwargs.get('xEnable')
        self.pSync = kwargs.get('pSync')
        self.usiConsumerInstanceId = kwargs.get('usiConsumerInstanceId')
        self.uiLinkHandler = kwargs.get('uiLinkHandler')
        self.usiProducerInterfaceId = kwargs.get('usiProducerInterfaceId')
        self.usiProducerInstanceId = kwargs.get('usiProducerInstanceId')
        self.usiWatchdogTimeoutFactor = kwargs.get('usiWatchdogTimeoutFactor')
        self.uiMaxDelay = kwargs.get('uiMaxDelay')
        self.uiSyncTimeout = kwargs.get('uiSyncTimeout')
        
        # Output variable
        self.xSynchronized = kwargs.get('xSynchronized')
        self.pNdr = kwargs.get('pNdr')
        self.uiNbrOfRxBytes = kwargs.get('uiNbrOfRxBytes')
        self.xError = kwargs.get('xError')
        self.iStatus = kwargs.get('iStatus')


class SCOM_X_CLIENT_IO_T:
    """ Class usable as IO values for SCOM_X_CLIENT
    """
    def __init__(self, **kwargs):
        # Input variable
        self.xEnable = kwargs.get('xEnable')
        self.xConnect = kwargs.get('xConnect')
        self.usiClientInstanceId = kwargs.get('usiClientInstanceId')
        self.uiLinkHandler = kwargs.get('uiLinkHandler')
        self.usiServerInterfaceId = kwargs.get('usiServerInterfaceId')
        self.usiServerInstanceId = kwargs.get('usiServerInstanceId')
        self.uiConnectionTimeout = kwargs.get('uiConnectionTimeout')
        self.uiResponseTimeout = kwargs.get('uiResponseTimeout')
        
        # output variable
        self.xConnected = kwargs.get('xConnected')
        self.xError = kwargs.get('xError')
        self.iStatus = kwargs.get('iStatus')
        self.usiClientHandler = kwargs.get('usiClientHandler')


class SCOM_X_SERVER_REQUEST_IO_T:
    """ Class usable as IO values for SCOM_X_SERVER_REQUEST
    """
    def __init__(self, **kwargs):
        # Input variable
        self.xEnable = kwargs.get('xEnable')
        self.pSend = kwargs.get('pSend')
        self.usiClientHandler = kwargs.get('usiClientHandler')
        
        # output variable
        self.pDone = kwargs.get('pDone')
        self.xBusy = kwargs.get('xBusy')
        self.pError = kwargs.get('pError')
        self.iStatus = kwargs.get('iStatus')
        self.uiNbrOfResponseBytes = kwargs.get('uiNbrOfResponseBytes')


class SCOM_X_SERVER_IO_T:
    """ Class usable as IO values for SCOM_X_SERVER
    """
    def __init__(self, **kwargs):
        # Input variable
        self.xEnable = kwargs.get('xEnable')
        self.usiServerInstanceId = kwargs.get('usiServerInstanceId')
        self.uiLinkHandler = kwargs.get('uiLinkHandler')
        self.usiClientInterfaceMask = kwargs.get('usiClientInterfaceMask')
        self.usiClientInstanceMask = kwargs.get('usiClientInstanceMask')
        self.uiResponseTimeout = kwargs.get('uiResponseTimeout')
        
        # output variable
        self.xConnected = kwargs.get('xConnected')
        self.xError = kwargs.get('xError')
        self.iStatus = kwargs.get('iStatus')
        self.usiServerHandler = kwargs.get('usiServerHandler')


class SCOM_X_GET_REQUEST_IO_T:
    """ Class usable as IO values for SCOM_X_GET_REQUEST
    """
    def __init__(self, **kwargs):
        # Input variable
        self.xEnable = kwargs.get('xEnable')
        self.usiServerHandler = kwargs.get('usiServerHandler')
        
        # output variable
        self.pNdr = kwargs.get('pNdr')
        self.uiNbrOfBytes = kwargs.get('uiNbrOfBytes')
        self.pError = kwargs.get('pError')
        self.iStatus = kwargs.get('iStatus')


class SCOM_X_SEND_RESPONSE_IO_T:
    """ Class usable as IO values for SCOM_X_SEND_RESPONSE
    """
    def __init__(self, **kwargs):
        # Input variable
        self.pSend = kwargs.get('pSend')
        self.usiServerHandler = kwargs.get('usiServerHandler')
        
        # output variable
        self.pDone = kwargs.get('pDone')
        self.pError = kwargs.get('pError')
        self.iStatus = kwargs.get('iStatus')


class Env_mSCOMx(EnvSysComGeneric):
    
    def __init__(self, **kwargs):
        """ Environment class containing all information needed to execute tests
        
        :param: : sysComPath: SysCom access path, e.g. 'LAN,192.168.0.253'
        :param: : sysComConf: SysCom config, e.g. 'MEDIANAME=LAN'
        :param: : iecAppPath: path to the iec application folder containing res.hex and varlist.csv
        :param: : iec_application_variables: dictionary of the IEC Application variables
        :param: : mos_hex_path: path of the mos hex file (including hex-file name)
        :param: :default_system_parameters: path of the system parameter file (including ini-file name)
        """
        self.sysComPath = kwargs.get('sys_com_path')
        self.sysComConf = kwargs.get('sys_com_conf')
        self.iecAppPath = kwargs.get('iec_app_path')
        self.iec_application_variables = kwargs.get('iec_application_variables', None)
        self.mos_hex_file_path = kwargs.get('mos_hex_path')
        self.default_system_parameters = kwargs.get('default_system_parameters', None)
        self.env_name = kwargs.get('env_name', '')
        super(Env_mSCOMx, self).__init__(syscom_path=self.sysComPath,
                                         syscom_config=self.sysComConf,
                                         iec_application_folder_path=self.iecAppPath,
                                         iec_application_variables=self.iec_application_variables,
                                         firmware_hex_file_path=self.mos_hex_file_path,
                                         default_system_parameters=self.default_system_parameters,
                                         test_assertion=kwargs.get('test_assertion', False),
                                         env_name=self.env_name)
    
    def run_cycles_mSCOMx(self, **kwargs):
        """ Executes n cycles on specified environment.
        
        :param: timeout: maximum timeout in seconds for operation
        :param: cycles: number of cycles to execute
        :param: step: the step id for asserts
        :return: None
        """
        cycles = kwargs.get('cycles', 1)
        timeout = kwargs.get('timeout', 10)
        step = kwargs.get('step', 'run_cycles_mSCOMx')
        self.iec_item_write(item_name='do_mSCOMx', data=cycles, test_step_id="{}.1".format(step))
        start_time = time.time()
        while cycles != 0:
            time.sleep(0.01)
            h_result, mas_function_name, cycles = self.iec_item_read(item_name='do_mSCOMx', test_step_id="{}.2".format(step))
            self.assertLess(time.time()-start_time, timeout, '{}.3'.format(step))
    
    def EXECUTE_FB(self, **kwargs):
        """ Common wrapper function for all mSCOM function blocks execution
        
        - Execution Logic for all mSCOM function blocks [FB],
           1. Write all input data
           2. Execute number of cycles
           3. Read all output data
        
        :param: pou_prefix: prefix name of function block POU instance
        :param: io_data: input-output data class object of function block
        :param: fb_enable: pulse input parameter name of function block
        :param: input_list: list of input  parameter names of  function block
        :param: output_list: list of output parameter names of  function block
        :param: update_output_only: read output parameters only
        :param: execution_cycles: execute desired number of cycles (if not None: overrides normal FB execution till xBusy)
        :param: function_activation_flag: Flag name which will activate the function or function block.
        :param: function_activation_value: Flag value to activate function or function block.
        :param: deactivate_after_execution: reset pulse input to FB (Negative edge has no effect)
        :param: step: the step id for asserts
        :return: None
        """
        pou_prefix = kwargs.get('pou_prefix', None)
        io_data = kwargs.get('io_data', None)
        fb_enable = kwargs.get('fb_enable', '')
        input_list = kwargs.get('input_list', [])
        output_list = kwargs.get('output_list', [])
        update_output_only = kwargs.get('update_output_only', False)
        execution_cycles = kwargs.get('execution_cycles', 1)
        function_activation_flag = kwargs.get('function_activation_flag', '')
        function_activation_value = kwargs.get('function_activation_value', True)
        deactivate_after_execution = kwargs.get('deactivate_after_execution',  True)
        step = kwargs.get('step', '')
        
        if function_activation_flag is not '':
            self.iec_item_write(item_name=function_activation_flag, data=function_activation_value, test_step_id='{}.0'.format(step))
        
        if function_activation_value:
            if not update_output_only:
                # Write input data to the function block
                if len(input_list):
                    for list_count in range(0, len(input_list)):
                        io_data_value = getattr(io_data, input_list[list_count])
                        if io_data_value is not None:
                            self.iec_item_write(item_name='{}_{}'.format(pou_prefix, input_list[list_count]), data=io_data_value,
                                                test_step_id=step + '.1: {}: Data write to input, {}'.format(pou_prefix, input_list[list_count]))
                if fb_enable is not '':
                    # Write value from caller function to pulse input
                    io_data_value = getattr(io_data, fb_enable)
                    if io_data_value is not None:
                        self.iec_item_write(item_name='{}_{}'.format(pou_prefix, fb_enable), data=io_data_value,
                                            test_step_id=step + '.2: {}: Pulse input, {}'.format(pou_prefix, fb_enable))
            
            # Execute number of cycles given by caller function
            self.run_cycles_mSCOMx(cycles=execution_cycles, step=step + '.3')
            
            # Read output data
            if len(output_list):
                for list_count in range(0, len(output_list)):
                    h_result, mas_function_name, io_data_value = self.iec_item_read(item_name='{}_{}'.format(pou_prefix, output_list[list_count]),
                                                                                    test_step_id=step + '.4: {}: Data read of output, {}'.format(pou_prefix, output_list[list_count]))
                    setattr(io_data, output_list[list_count], io_data_value)
            
            if deactivate_after_execution:
                if fb_enable is not '':
                    self.iec_item_write(item_name='{}_{}'.format(pou_prefix, fb_enable), data=False,
                                        test_step_id=step + '.5: {}: Pulse reset, {}'.format(pou_prefix, fb_enable))
                    self.run_cycles_mSCOMx(step=step + '.6')  # Execute one cycle
                
                if function_activation_flag is not '':
                    self.iec_item_write(item_name=function_activation_flag, data=False, test_step_id='{}.7'.format(step))
    
    def SCOM_X_CAN_INIT(self, **kwargs):
        """ Wrapper function for time_get_performance_frequency
        
        :param: io_data: input-output data class object of function
        :param: output_type: gives data type of output used for making pou prefix
        :param: cycles: determines how many times function is to be executed.
        :param: step: the step id for asserts
        :return: None
        """
        io_data = kwargs.get('io_data')
        cycles = kwargs.get('cycles')
        step = kwargs.get('step')
        deactivate_after_execution = kwargs.get('deactivate_after_execution', False)
        input_list = ['usiInterfaceId', 'udiSafetyMessageIdentifier', 'usiPDO']
        output_list = ['uiLinkHandler', 'xError', 'iStatus']
        pou_prefix = kwargs.get('pou_prefix', None)
        
        fb_enable = 'xInit'
        self.EXECUTE_FB(pou_prefix=pou_prefix, fb_enable=fb_enable, io_data=io_data, input_list=input_list,
                        deactivate_after_execution=deactivate_after_execution, output_list=output_list, execution_cycles=cycles, step=step)
    
    def SCOM_X_LAN_CH_INIT(self, **kwargs):
        """ Wrapper function for SCOM_X_LAN_CH_INIT
        
        :param: instance: determines which instance is to be used
        :param: function_activation: determines whether to activate function or not.
        :param: io_data: input-output data class object of function
        :param: cycles: determines how many times function is to be executed.
        :param: deactivate_after_execution: Indicates if the function/function block should be disabled after execution
        :param: step: the step id for asserts
        :param: update_output_only: read output parameters only
        :return: None
        """
        instance = kwargs.get('instance', '')
        io_data = kwargs.get('io_data', SCOM_X_LAN_CH_INIT_IO_T())
        step = kwargs.get('step', 'SCOMx_LAN_CH_INIT')
        cycles = kwargs.get('cycles', 1)
        update_output_only = kwargs.get('update_output_only', False)
        deactivate_after_execution = kwargs.get('deactivate_after_execution',  True)
        
        input_list = ['usiInterfaceId', 'udiSafetyMsgId', 'uiSafetyComPort', 'sSafetyComBroadAddr']
        output_list = ['uiLinkHandler', 'xError', 'iStatus']
        fb_enable = 'xInit'
        pou_prefix = 'LAN_INIT_{}'.format(instance)
        self.EXECUTE_FB(pou_prefix=pou_prefix, fb_enable=fb_enable, io_data=io_data, input_list=input_list, update_output_only=update_output_only,
                        deactivate_after_execution=deactivate_after_execution, output_list=output_list, execution_cycles=cycles, step=step)
    
    def SCOM_X_CPL_CO_INIT(self, **kwargs):
        """ Wrapper function for SCOM_X_CPL_CO_INIT
        
        :param: instance: determines which instance is to be used
        :param: function_activation: determines whether to activate function or not.
        :param: io_data: input-output data class object of function
        :param: cycles: determines how many times function is to be executed.
        :param: deactivate_after_execution: Indicates if the function/function block should be disabled after execution
        :param: step: the step id for asserts
        :param: update_output_only: read output parameters only
        :return: None
        """
        instance = kwargs.get('instance', '')
        io_data = kwargs.get('io_data', SCOM_X_CPL_CO_INIT_IO_T())
        step = kwargs.get('step', 'SCOM_X_CPL_CO_INIT')
        cycles = kwargs.get('cycles', 1)
        update_output_only = kwargs.get('update_output_only', False)
        deactivate_after_execution = kwargs.get('deactivate_after_execution',  True)
        
        input_list = ['usiInterfaceId', 'udiSafetyMsgId', 'usiNodeAddr']
        output_list = ['uiLinkHandler', 'xError', 'iStatus']
        pou_prefix = 'CPL_CO_INIT_{}'.format(instance)
        fb_enable = 'xInit'
        
        self.EXECUTE_FB(pou_prefix=pou_prefix, io_data=io_data, input_list=input_list, output_list=output_list, step=step, fb_enable=fb_enable,
                        update_output_only=update_output_only, deactivate_after_execution=deactivate_after_execution, execution_cycles=cycles)
    
    def SCOM_X_PRODUCER(self, **kwargs):
        """ Wrapper function for SCOM_X_PRODUCER
        
        :param: deactivate_after_execution: Indicates if the function/function block should be disabled after execution
        :param: update_output_only: read output parameters only
        :param: function_activation: determines whether to activate function or not.
        :param: io_data: input-output data class object of function
        :param: step: the step id for asserts
        :param: cycles: determines how many times function is to be executed.
        :param: input_list: list of input  parameter names of  function block
        :param: output_list: list of output parameter names of  function block
        :param: pou_prefix: prefix name of function block POU instance
        :return: None
        """
        deactivate_after_execution = kwargs.get('deactivate_after_execution', False)
        update_output_only = kwargs.get('update_output_only', False)
        io_data = kwargs.get('io_data', None)
        step = kwargs.get('step', 'SCOM_X_PRODUCER')
        cycles = kwargs.get('cycles', 1)
        input_list = ['usiProducerInstanceId', 'uiLinkHandler', 'uiEventTime', 'uiInhibitTime']
        output_list = ['pDone', 'xError', 'iStatus']
        instance = kwargs.get('instance', 1)
        test_data = kwargs.get('test_data', [1,3,4,5])
        
        pou_prefix = 'fb_producers_1.PRO_%02d' % instance
        
        fb_enable = 'xEnable'
        
        self.write_data(item_name='fb_producers_1.SCOM_Data_tx_%02d.abData'%instance, data=test_data, test_step_id=step+'.1')
        
        self.EXECUTE_FB(pou_prefix=pou_prefix, fb_enable=fb_enable, io_data=io_data, input_list=input_list,
                        output_list=output_list, update_output_only=update_output_only,
                        deactivate_after_execution=deactivate_after_execution, step=step+'.2', execution_cycles=cycles)
    
    def SCOM_X_CONSUMER(self, **kwargs):
        """ Wrapper function for SCOM_X_CONSUMER
        
        :param: deactivate_after_execution: Indicates if the function/function block should be disabled after execution
        :param: update_output_only: read output parameters only
        :param: function_activation: determines whether to activate function or not.
        :param: io_data: input-output data class object of function
        :param: step: the step id for asserts
        :param: cycles: determines how many times function is to be executed.
        :param: input_list: list of input  parameter names of  function block
        :param: output_list: list of output parameter names of  function block
        :param: instance: instance number of the function block
        :return: None
        """
        deactivate_after_execution = kwargs.get('deactivate_after_execution', False)
        update_output_only = kwargs.get('update_output_only', False)
        io_data = kwargs.get('io_data', None)
        step = kwargs.get('step', 'SCOM_X_CONSUMER')
        cycles = kwargs.get('cycles', 1)
        input_list = ['pSync', 'usiConsumerInstanceId',
                      'uiLinkHandler', 'usiProducerInterfaceId',
                      'usiProducerInstanceId', 'usiWatchdogTimeoutFactor',
                      'uiMaxDelay', 'uiSyncTimeout']
        output_list = ['xSynchronized', 'pNdr', 'uiNbrOfRxBytes', 'xError', 'iStatus']
        instance = kwargs.get('instance', 1)
        
        pou_prefix = 'fb_consumers_1.CON_%02d' % instance
        
        fb_enable = 'xEnable'
        self.EXECUTE_FB(pou_prefix=pou_prefix, fb_enable=fb_enable, io_data=io_data, input_list=input_list,
                        output_list=output_list, update_output_only=update_output_only,
                        deactivate_after_execution=deactivate_after_execution, step=step, execution_cycles=cycles)
        h_result, mas_function_name, received_data = self.iec_item_read(item_name='fb_consumers_1.SCOM_Data_rx_%02d.abData'%instance,
                                                                        test_step_id=step+'.3')
        return received_data
    
    def SCOM_X_CLIENT(self, **kwargs):
        """ Wrapper function for SCOM_X_CLIENT
        
        :param: deactivate_after_execution: Indicates if the function/function block should be disabled after execution
        :param: update_output_only: read output parameters only
        :param: function_activation: determines whether to activate function or not.
        :param: io_data: input-output data class object of function
        :param: step: the step id for asserts
        :param: cycles: determines how many times function is to be executed.
        :param: input_list: list of input  parameter names of  function block
        :param: output_list: list of output parameter names of  function block
        :param: pou_prefix: prefix name of function block POU instance
        :param: function_activation_flag: Flag name which will activate the function or function block.
        :return: None
        """
        deactivate_after_execution = kwargs.get('deactivate_after_execution', True)
        update_output_only = kwargs.get('update_output_only', False)
        io_data = kwargs.get('io_data', None)
        step = kwargs.get('step', 'SCOM_X_CLIENT')
        cycles = kwargs.get('cycles', 1)
        input_list = ['xConnect', 'usiClientInstanceId',
                      'uiLinkHandler', 'usiServerInterfaceId',
                      'usiServerInstanceId', 'uiConnectionTimeout', 'uiResponseTimeout']
        output_list = ['xConnected', 'xError', 'iStatus', 'usiClientHandler']
        instance = kwargs.get('instance', 1)
        pou_prefix = 'fb_clients_1.CLIENT_%02d' % instance
        
        fb_enable = 'xEnable'
        self.EXECUTE_FB(pou_prefix=pou_prefix, fb_enable=fb_enable, io_data=io_data, input_list=input_list,
                        output_list=output_list, update_output_only=update_output_only,
                        deactivate_after_execution=deactivate_after_execution, step=step, execution_cycles=cycles)
    
    def SCOM_X_SERVER_REQUEST(self, **kwargs):
        """ Wrapper function for SCOM_X_SERVER_REQUEST
        
        :param: deactivate_after_execution: Indicates if the function/function block should be disabled after execution
        :param: update_output_only: read output parameters only
        :param: function_activation: determines whether to activate function or not.
        :param: io_data: input-output data class object of function
        :param: step: the step id for asserts
        :param: cycles: determines how many times function is to be executed.
        :param: input_list: list of input  parameter names of  function block
        :param: output_list: list of output parameter names of  function block
        :param: pou_prefix: prefix name of function block POU instance
        :param: function_activation_flag: Flag name which will activate the function or function block.
        :return: None
        """
        deactivate_after_execution = kwargs.get('deactivate_after_execution', True)
        update_output_only = kwargs.get('update_output_only', False)
        io_data = kwargs.get('io_data', None)
        step = kwargs.get('step', 'SCOM_X_SERVER_REQUEST')
        cycles = kwargs.get('cycles', 1)
        input_list = ['pSend', 'usiClientHandler']
        output_list = ['pDone', 'xBusy', 'pError', 'iStatus', 'uiNbrOfResponseBytes']
        instance = kwargs.get('instance', 1)
        
        pou_prefix = 'SRVR_RQT_%02d' % instance
        fb_enable = 'xEnable'
        self.EXECUTE_FB(pou_prefix=pou_prefix, fb_enable=fb_enable, io_data=io_data, input_list=input_list,
                        output_list=output_list, update_output_only=update_output_only,
                        deactivate_after_execution=deactivate_after_execution, step=step, execution_cycles=cycles)
    
    def SCOM_X_SERVER(self, **kwargs):
        """ Wrapper function for time_get_performance_frequency
        
        :param: io_data: input-output data class object of function
        :param: output_type: gives data type of output used for making pou prefix
        :param: cycles: determines how many times function is to be executed.
        :param: step: the step id for asserts
        :return: None
        """
        io_data = kwargs.get('io_data')
        cycles = kwargs.get('cycles')
        step = kwargs.get('step')
        deactivate_after_execution = kwargs.get('deactivate_after_execution', True)
        input_list = ['usiServerInstanceId', 'uiLinkHandler', 'usiClientInterfaceMask',  'usiClientInstanceMask', 'uiResponseTimeout']
        output_list = ['xConnected', 'xError', 'iStatus', 'usiServerHandler']
        instance = kwargs.get('instance', 1)
        pou_prefix = 'fb_servers_1.SERVER_%02d' % instance
        fb_enable = 'xEnable'
        self.EXECUTE_FB(pou_prefix=pou_prefix, fb_enable=fb_enable, deactivate_after_execution=deactivate_after_execution,
                        io_data=io_data, input_list=input_list, output_list=output_list, execution_cycles=cycles, step=step)
    
    def SCOM_X_GET_REQUEST(self, **kwargs):
        """ Wrapper function for SCOM_X_GET_REQUEST
        
        :param: deactivate_after_execution: Indicates if the function/function block should be disabled after execution
        :param: update_output_only: read output parameters only
        :param: function_activation: determines whether to activate function or not.
        :param: io_data: input-output data class object of function
        :param: step: the step id for asserts
        :param: cycles: determines how many times function is to be executed.
        :param: input_list: list of input  parameter names of  function block
        :param: output_list: list of output parameter names of  function block
        :param: pou_prefix: prefix name of function block POU instance
        :param: function_activation_flag: Flag name which will activate the function or function block.
        :return: None
        """
        deactivate_after_execution = kwargs.get('deactivate_after_execution', True)
        update_output_only = kwargs.get('update_output_only', False)
        io_data = kwargs.get('io_data', None)
        step = kwargs.get('step', 'SCOM_X_GET_REQUEST')
        cycles = kwargs.get('cycles', 1)
        input_list = ['usiServerHandler']
        output_list = ['pNdr', 'uiNbrOfBytes', 'pError', 'iStatus']
        instance = kwargs.get('instance', 1)
        
        pou_prefix = 'GET_REQUEST_%02d' % instance
        fb_enable = 'xEnable'
        self.EXECUTE_FB(pou_prefix=pou_prefix, fb_enable=fb_enable, io_data=io_data, input_list=input_list,
                        output_list=output_list, update_output_only=update_output_only,
                        deactivate_after_execution=deactivate_after_execution, step=step, execution_cycles=cycles)
    
    def SCOM_X_SEND_RESPONSE(self, **kwargs):
        """ Wrapper function for SCOM_X_SEND_RESPONSE
        
        :param: deactivate_after_execution: Indicates if the function/function block should be disabled after execution
        :param: update_output_only: read output parameters only
        :param: function_activation: determines whether to activate function or not.
        :param: io_data: input-output data class object of function
        :param: step: the step id for asserts
        :param: cycles: determines how many times function is to be executed.
        :param: input_list: list of input  parameter names of  function block
        :param: output_list: list of output parameter names of  function block
        :param: pou_prefix: prefix name of function block POU instance
        :param: function_activation_flag: Flag name which will activate the function or function block.
        :return: None
        """
        deactivate_after_execution = kwargs.get('deactivate_after_execution', True)
        update_output_only = kwargs.get('update_output_only', False)
        io_data = kwargs.get('io_data', None)
        step = kwargs.get('step', 'SCOM_X_SEND_RESPONSE')
        cycles = kwargs.get('cycles', 1)
        input_list = ['usiServerHandler']
        output_list = ['pDone', 'pError', 'iStatus']
        instance = kwargs.get('instance', 1)
        
        pou_prefix = 'SEND_RESP_%02d' % instance
        fb_enable = 'pSend'
        self.EXECUTE_FB(pou_prefix=pou_prefix, fb_enable=fb_enable, io_data=io_data, input_list=input_list, output_list=output_list,
                        update_output_only=update_output_only,
                        deactivate_after_execution=deactivate_after_execution, step=step, execution_cycles=cycles)


class TestCase_mSCOMx(Env_mSCOMx):
    """
    <table>
        <tr><td><b> Test Case Name        </b></td><td> Test_mSCOMx.TestCase_mSCOMx </td></tr>
        <tr><td><b> Status                </b></td><td> Active </td></tr>
        <tr><td><b> Test concept          </b></td><td> Testkonzept_MOS83x </td></tr>
        <tr><td><b> Description           </b></td><td> Test of MLib mSCOMx </td></tr>
        <tr><td><b> Tested requirements   </b></td><td>
                                                        SYSMOS_83x
                                                        - \what{251,212915} - SafetyCom® CAN
                                                        - \what{251,131251} - SafetyCom® Ethernet
                                                        - \what{251,212916} - SafetyCom® CAN-Powerline
                                                        - \what{251,213681} - Anzahl SafetyCom® Server
                                                        - \what{251,213680} - Anzahl SafetyCom® Client
                                                        PKG_Mlib_SCOM
                                                        - \what{410,83498} - SCOM_X_LAN_INIT
                                                        - \what{410,95095} - SCOM_X_CPL_CO_INIT
                                                        - \what{410,83505} - SCOM_X_PRODUCER
                                                        - \what{410,83770} - SCOM_X_CONSUMER
                                                        - \what{410,83831} - SCOM_X_CLIENT
                                                        - \what{410,83837} - SCOM_X_SERVER_REQUEST
                                                        - \what{410,83839} - SCOM_X_SERVER
                                                        - \what{410,83840} - SCOM_X_GET_REQUEST
                                                        - \what{410,83841} - SCOM_X_SEND_RESPONSE
                                                        - \what{410,95092} - SCOM_X_CAN_INIT
                                                        - \what{410,78951} - Selbstüberwachung
                                             
                                             </td></tr>
        <tr><td><b> Issue                 </b></td><td>
                                             </td></tr>
        <tr><td><b> Test Type             </b></td><td> Functional Test </td></tr>
        <tr><td><b> Test Technique        </b></td><td> Black Box: Equivalence Class Partitioning with Boundary Value Analysis </td></tr>
        <tr><td><b> Test Class            </b></td><td> strategy independent test </td></tr>
        <tr><td><b> Preconditions         </b></td><td>
                                                        #- SysCom instance must be installed and connected to
                                             </td></tr>
        <tr><td><b> Postconditions        </b></td><td> None </td></tr>
        <tr><td><b> Remarks               </b></td><td> None </td></tr>
    </table>
    """
    def __init__(self, test_name, **kwargs):
        unittest.TestCase.__init__(self, test_name)
        # Store default system parameter before changing.
        self.can1_address = None
        self.can2_address = None
        super(TestCase_mSCOMx, self).__init__(test_assertion=True, **kwargs)
    
    def setUp(self):
        super(TestCase_mSCOMx, self).setUp()
        # 'CAN_ADDRESS' should be nonzero.
        # Check and update 'CAN_ADDRESS' of CAN1 if required.
        h_result, mas_function_name, self.can1_address = self.plc_system_parameters_get(
            section='SYSPARAM_CAN1', option='CAN_ADDRESS')
        # Check and update 'CAN_ADDRESS' of CAN2 if required.
        h_result, mas_function_name, self.can2_address = self.plc_system_parameters_get(
            section='SYSPARAM_CAN2', option='CAN_ADDRESS')
        
        if '0' in [self.can1_address, self.can2_address]:
            self.plc_system_parameters_set(
                parameter_sets=(('SYSPARAM_CAN1', 'CAN_ADDRESS', '1'), ('SYSPARAM_CAN2', 'CAN_ADDRESS', '2')), test_step_id='setUp.0')
    
    def tearDown(self):
        
        self.plc_stop()
        time.sleep(0.5)
        self.plc_start()
        
        # Restore back changed system parameters.
        self.plc_system_parameters_set(
            parameter_sets=(('SYSPARAM_CAN1', 'CAN_ADDRESS', self.can1_address),
                            ('SYSPARAM_CAN2', 'CAN_ADDRESS', self.can2_address)),
                            test_step_id='tearDown.0')
        
        if self._testMethodName == 'test_201_SCOM_X_PRODUCER':
            self.close_SafetyCom_for_producer()
            self.deactivate_producer()
        
        if self._testMethodName in ['test_101_ProducerConsumer', 'test_202_SCOM_X_CONSUMER']:
            self.close_SafetyCom_for_producer_and_consumer()
            self.deactivate_producer()
            self.deactivate_consumer()
        
        sys_param_file_modified = False
        if self.default_system_parameters is not None:
            # ToDo: workaround for #24152 --> it must be removed #24179
            #  insert default LAN IP Address if no IP address present in default sysparam file
            with open(self.default_system_parameters, 'r') as config_file:
                config_string = config_file.read()
                if 'LAN_IP_ADDR' not in config_string:
                    config_string = re.sub('\[SYSPARAM_LAN1\]\n', '[SYSPARAM_LAN1]\r\nLAN_IP_ADDR = {}\r\n'.format(self.syscom_path.rsplit(',')[1]), config_string)
                    with open(self.default_system_parameters, 'wb') as sys_param_file:
                        sys_param_file.write(config_string)
                        sys_param_file_modified = True
        
        super(TestCase_mSCOMx, self).tearDown()
        # ToDo: workaround for #24152 --> it must be removed #24179
        if sys_param_file_modified:
            with open(self.default_system_parameters, 'wb') as sys_param_file:
                config_string = re.sub('LAN_IP_ADDR = {}\r\n'.format(self.syscom_path.rsplit(',')[1]), '', config_string)
                sys_param_file.write(config_string)
    
    def init_SafetyCom_for_producer_and_consumer(self, **kwargs):
        """
        This function initialize SafetyCom SafetyCom CAN interface for producer and consumer.
        """
        p_interface_id = kwargs.get('p_interface_id', 2)
        c_interface_id = kwargs.get('c_interface_id', 3)
        # Initializes 'L1_CAN1' and 'L2_CAN2' for the SafetyCom communication --------------------------------------
        io_data_can1 = SCOM_X_CAN_INIT_IO_T(xInit=True, usiInterfaceId=p_interface_id,
                                            udiSafetyMessageIdentifier=28, usiPDO=3)
        io_data_can2 = SCOM_X_CAN_INIT_IO_T(xInit=True,usiInterfaceId=c_interface_id,
                                            udiSafetyMessageIdentifier=28,usiPDO=3)
        self.SCOM_X_CAN_INIT(io_data=io_data_can1, cycles=1, pou_prefix='CAN1',
                             step='init_SafetyCom_for_producer_and_consumer().{}'.format(0))
        self.SCOM_X_CAN_INIT(io_data=io_data_can2, cycles=1, pou_prefix='CAN2',
                             step='init_SafetyCom_for_producer_and_consumer().{}'.format(1))
        
        # Check if SafetyCom Link Handlers are available -----------------------------------------------------------
        self.assertGreater(io_data_can1.uiLinkHandler, -1,
                           msg='SCOM_X_CAN_INIT() Failed to initialize SafetyCom')
        self.assertGreater(io_data_can2.uiLinkHandler, -1,
                           msg='SCOM_X_CAN_INIT() Failed to initialize SafetyCom')
        return io_data_can1.uiLinkHandler, io_data_can2.uiLinkHandler
    
    def close_SafetyCom_for_producer(self):
        """
        This function closes SafetyCom CAN interface for producer and consumer.
        """
        # Disable 'L1_CAN1' and 'L2_CAN2' for the SafetyCom communication --------------------------------------
        io_data_can1 = SCOM_X_CAN_INIT_IO_T(xInit=False)
        self.SCOM_X_CAN_INIT(io_data=io_data_can1, cycles=1, pou_prefix='CAN1', step='S103.1')
        self.assertEqual(io_data_can1.iStatus, 0,
                         msg='SCOM_X_CAN_INIT() Failed to close SafetyCom')
        return io_data_can1.uiLinkHandler
    
    def close_SafetyCom_for_producer_and_consumer(self):
        """
        This function closes SafetyCom CAN interface for producer and consumer.
        """
        # Disable 'L1_CAN1' and 'L2_CAN2' for the SafetyCom communication --------------------------------------
        io_data_can1 = SCOM_X_CAN_INIT_IO_T(xInit=False)
        io_data_can2 = SCOM_X_CAN_INIT_IO_T(xInit=False)
        self.SCOM_X_CAN_INIT(io_data=io_data_can1, cycles=1, pou_prefix='CAN1', step='S103.1')
        self.SCOM_X_CAN_INIT(io_data=io_data_can2, cycles=1, pou_prefix='CAN2', step='S103.2')
        self.assertEqual(io_data_can1.iStatus, 0,
                         msg='SCOM_X_CAN_INIT() Failed to close SafetyCom')
        self.assertEqual(io_data_can2.iStatus, 0,
                         msg='SCOM_X_CAN_INIT() Failed to close SafetyCom')
        return io_data_can1.uiLinkHandler, io_data_can2.uiLinkHandler
    
    def deactivate_producer(self):
        io_data_producer = SCOM_X_PRODUCER_IO_T(xEnable=False)
        self.SCOM_X_PRODUCER(io_data=io_data_producer, cycles=1, step='deactivate_producer()')
        self.assertEqual(io_data_producer.iStatus, 0, msg='SCOM_X_PRODUCER():Failed to deactivate producer')
    
    def deactivate_consumer(self):
        io_data_consumer = SCOM_X_CONSUMER_IO_T(xEnable=False, pSync=False)
        self.SCOM_X_CONSUMER(io_data=io_data_consumer, cycles=1, step='deactivate_consumer()')
        self.assertEqual(io_data_consumer.iStatus, 0, msg='SCOM_X_CONSUMER():Failed to deactivate producer')
    
    def INIT_CAN1_CAN2_SCOM(self, **kwargs):
        
        usi_server_interface_id = kwargs.get('usiServerInstanceId', 2)
        usi_client_instance_id = kwargs.get('usiClientInstanceId', 3)
        udi_safety_message_identifier = kwargs.get('udi_safety_message_identifier', 28)
        usi_pdo = kwargs.get('usi_pdo', 3)
        test_step_id = kwargs.get('test_step_id', 'INIT_CAN1_CAN2_SCOM')
        
        # Initializes 'L1_CAN1' and 'L2_CAN2' for the SafetyCom communication ------------------------------------------
        io_data_can1 = SCOM_X_CAN_INIT_IO_T(xInit=False, usiInterfaceId=usi_server_interface_id, udiSafetyMessageIdentifier=udi_safety_message_identifier, usiPDO=usi_pdo)
        self.SCOM_X_CAN_INIT(io_data=io_data_can1, cycles=1, pou_prefix='CAN1', step='{}.1'.format(test_step_id))
        
        io_data_can2 = SCOM_X_CAN_INIT_IO_T(xInit=False, usiInterfaceId=usi_client_instance_id, udiSafetyMessageIdentifier=28, usiPDO=3)
        self.SCOM_X_CAN_INIT(io_data=io_data_can2, cycles=1, pou_prefix='CAN2', step='{}.2'.format(test_step_id))
        
        io_data_can1.xInit = True
        self.SCOM_X_CAN_INIT(io_data=io_data_can1, cycles=1, pou_prefix='CAN1', step='{}.3'.format(test_step_id))
        
        io_data_can2.xInit = True
        self.SCOM_X_CAN_INIT(io_data=io_data_can2, cycles=1, pou_prefix='CAN2', step='{}.4'.format(test_step_id))
        
        # uiLinkHandler : SafetyCom Link Handler for Server and Client -------------------------------------------------
        server_ui_link_handler = io_data_can1.uiLinkHandler
        client_ui_link_handler = io_data_can2.uiLinkHandler
        
        # Check if SafetyCom Link Handlers are available ---------------------------------------------------------------
        
        self.assertGreater(server_ui_link_handler, -1,
                           msg='{}.5 L1_CAN1 : SafetyCom Link Handler is not available for Server'.format(test_step_id))
        self.assertGreater(client_ui_link_handler, -1,
                           msg='{}.6 L2_CAN2 : SafetyCom Link Handler is not available for Client'.format(test_step_id))
        
        return server_ui_link_handler, client_ui_link_handler
        
    def test_client_server(self, **kwargs):
       
        usi_server_instance_id = kwargs.get('usiServerInstanceId', 2)
        usi_client_interface_mask = kwargs.get('usiClientInterfaceMask', 0)
        usi_client_instance_mask = kwargs.get('usiClientInstanceMask', 0)
        server_ui_response_timeout = kwargs.get('server_uiResponseTimeout', 50000)
        
        usi_client_instance_id = kwargs.get('usiClientInstanceId', 3)
        usi_server_interface_id = kwargs.get('usiServerInterfaceId', 2)
        client_ui_response_timeout = kwargs.get('client_uiResponseTimeout', 50000)
        client_ui_connection_timeout = kwargs.get('client_uiConnectionTimeout', 50000)
        request_to__server_data = kwargs.get('request_to__server_data', [10, 20, 30, 40, 50])
        response_to__client_data = kwargs.get('response_to__client_data', [60, 70, 80, 90, 100])
        
        test_step_id = kwargs.get('test_step_id', 'test_client_server')
        
        self.write_data(item_name='SRVR_RQT_01_Data.abData', data=request_to__server_data, test_step_id='{}.0'.format(test_step_id))
        
        self.write_data(item_name='SEND_RESP_01_Data.abData', data=response_to__client_data, test_step_id='{}.0'.format(test_step_id))
        
        server_ui_link_handler, client_ui_link_handler = self.INIT_CAN1_CAN2_SCOM(usiServerInstanceId=usi_server_instance_id,
                                                                                  usiClientInstanceId=usi_client_instance_id)
        # Act-----------------------------------------------------------------------------------------------------------
        # Define and initialise a client and server communication instance and establish connection between them.
        
        io_data_server = SCOM_X_SERVER_IO_T(xEnable=False, usiServerInstanceId=usi_server_instance_id,
                                            uiLinkHandler=server_ui_link_handler, usiClientInterfaceMask=usi_client_interface_mask,
                                            usiClientInstanceMask=usi_client_instance_mask, uiResponseTimeout=server_ui_response_timeout)
        self.SCOM_X_SERVER(io_data=io_data_server, cycles=1, deactivate_after_execution=False, step='{}.7'.format(test_step_id))
        
        io_data_client = SCOM_X_CLIENT_IO_T(xEnable=False, xConnect=False,
                                            usiClientInstanceId=usi_client_instance_id, uiLinkHandler=client_ui_link_handler,
                                            usiServerInterfaceId=usi_server_interface_id, usiServerInstanceId=usi_server_instance_id,
                                            uiConnectionTimeout=client_ui_connection_timeout, uiResponseTimeout=client_ui_response_timeout)
        self.SCOM_X_CLIENT(io_data=io_data_client, cycles=1, deactivate_after_execution=False, step='{}.8'.format(test_step_id))
        
        io_data_server.xEnable = True
        self.SCOM_X_SERVER(io_data=io_data_server, cycles=1, deactivate_after_execution=False, step='{}.9'.format(test_step_id))
        
        io_data_client.xEnable = True
        self.SCOM_X_CLIENT(io_data=io_data_client, cycles=1, deactivate_after_execution=False, step='{}.10'.format(test_step_id))
        
        io_data_client.xConnect = True
        self.SCOM_X_CLIENT(io_data=io_data_client, cycles=1, deactivate_after_execution=False, step='{}.11'.format(test_step_id))
        
        start_time = time.time()
        while io_data_client.xConnected == 0:
            self.SCOM_X_CLIENT(io_data=io_data_client, cycles=1, deactivate_after_execution=False, step='{}.12'.format(test_step_id))
            self.assertLess(time.time()-start_time, 30, msg='{}.13: SCOM_X_CLIENT() failed to Synchronize'.format(test_step_id))
        
        start_time = time.time()
        while io_data_server.xConnected == 0:
            self.SCOM_X_SERVER(io_data=io_data_server, cycles=1, deactivate_after_execution=False, step='{}.3'.format(test_step_id))
            self.assertLess(time.time()-start_time, 30, msg='{}.14: SCOM_X_SERVER() failed to Synchronize'.format(test_step_id))
        
        # Handlers for Server and Client -------------------------------------------------------------------------------
        
        usi_client_handler = io_data_client.usiClientHandler
        usi_server_handler = io_data_server.usiServerHandler
        
        # Check if Client Handler and Sever Handler are available ------------------------------------------------------
        
        self.assertGreater(usi_client_handler, -1,
                           msg='{}.5 L1_CAN1 : SafetyCom Link Handler is not available for Server'.format(test_step_id))
        self.assertGreater(usi_server_handler, -1,
                           msg='{}.6 L2_CAN2 : SafetyCom Link Handler is not available for Client'.format(test_step_id))
        
        # Send request to server ---------------------------------------------------------------------------------------
        io_data_req_to_server = SCOM_X_SERVER_REQUEST_IO_T(xEnable=False, pSend=False,
                                                           usiClientHandler=usi_client_handler)
        self.SCOM_X_SERVER_REQUEST(io_data=io_data_req_to_server, cycles=1,
                                   deactivate_after_execution=False, step='{}.15'.format(test_step_id))
        
        io_data_get_client_request = SCOM_X_GET_REQUEST_IO_T(xEnable=False, usiServerHandler=usi_server_handler)
        self.SCOM_X_GET_REQUEST(io_data=io_data_get_client_request, cycles=1,
                                deactivate_after_execution=False, step='{}.16'.format(test_step_id))
        
        io_data_req_to_server.xEnable = True
        self.SCOM_X_SERVER_REQUEST(io_data=io_data_req_to_server, cycles=1,
                                   deactivate_after_execution=False, step='{}.17'.format(test_step_id))
        
        io_data_get_client_request.xEnable = True
        self.SCOM_X_GET_REQUEST(io_data=io_data_get_client_request, cycles=1,
                                deactivate_after_execution=False, step='{}.18'.format(test_step_id))
        
        io_data_req_to_server.pSend = True
        self.SCOM_X_SERVER_REQUEST(io_data=io_data_req_to_server, cycles=1,
                                   deactivate_after_execution=False, step='{}.19'.format(test_step_id))
        
        start_time = time.time()
        while io_data_req_to_server.xBusy == 0:
            self.SCOM_X_SERVER_REQUEST(io_data=io_data_req_to_server, cycles=1,
                                       deactivate_after_execution=False, step='{}.20'.format(test_step_id))
            self.assertLess(time.time()-start_time, 30, msg='{}.21: SCOM_X_SERVER_REQUEST() failed to Synchronize'.format(test_step_id))
        
        # Receive Client request ---------------------------------------------------------------------------------------
        start_time = time.time()
        while io_data_get_client_request.uiNbrOfBytes == 0:
            self.SCOM_X_GET_REQUEST(io_data=io_data_get_client_request, cycles=1,
                                    deactivate_after_execution=False, step='{}.22'.format(test_step_id))
            self.assertLess(time.time()-start_time, 30, msg='{}.23: SCOM_X_SERVER_REQUEST() failed to Synchronize'.format(test_step_id))
        
        # Send response to Client --------------------------------------------------------------------------------------
        io_data_send_response_to_client = SCOM_X_SEND_RESPONSE_IO_T(pSend=True, usiServerHandler=usi_server_handler)
        self.SCOM_X_SEND_RESPONSE(io_data=io_data_send_response_to_client, cycles=1,
                                  deactivate_after_execution=False, step='{}.24'.format(test_step_id))
        
        # Receive response from server ---------------------------------------------------------------------------------
        start_time = time.time()
        while io_data_req_to_server.uiNbrOfResponseBytes == 0:
            self.SCOM_X_SEND_RESPONSE(io_data=io_data_send_response_to_client, cycles=1,
                                      deactivate_after_execution=False, step='{}.25'.format(test_step_id))
            self.SCOM_X_SERVER_REQUEST(io_data=io_data_req_to_server, cycles=1,
                                       deactivate_after_execution=False, step='{}.26'.format(test_step_id))
            self.assertLess(time.time()-start_time, 45, msg='{}.27: SCOM_X_SEND_RESPONSE() failed to Synchronize'.format(test_step_id))
        
        # Received request at server -----------------------------------------------------------------------------------
        received_data_at_server = self.read_data(item_name='GET_REQUEST_01_Data.abData', test_step_id='{}.28'.format(test_step_id))
        
        # Received response at client ----------------------------------------------------------------------------------
        received_data_at_client = self.read_data(item_name='SRVR_RQT_01_RESP_Data.abData',  test_step_id='{}.29'.format(test_step_id))
        
        # Assert--------------------------------------------------------------------------------------------------------
        self.assertEqual(request_to__server_data, received_data_at_server[0:len(request_to__server_data)],
                         msg='{}.30 : Sent and Received data mismatched'.format(test_step_id))
        self.assertEqual(response_to__client_data, received_data_at_client[0:len(response_to__client_data)],
                         msg='{}.31 : Sent and Received data mismatched'.format(test_step_id))
    
    def test_002_SCOM_X_CAN_INIT(self):
        """
        \StepDefinition
               S001: Call 'SCOM_X_CAN_INIT' FB and Initialize 1st SCOM CAN1 interface
                     Check iStatus
                     Check xError
                     Check uiLinkHandler
                     Call 'SCOM_X_CAN_INIT' FB and Initialize 2nd SCOM CAN2 interface
                     Check iStatus
                     Check xError
                     Check uiLinkHandler
        \PassCriteria
            - Pass  : iStatus = 0
                      xError = False
                      uiLinkHandler = [1..0xFFFF]
        \Requirement
            - \what{251,212915} - SafetyCom® CAN
            - \what{410,95092} - SCOM_X_CAN_INIT
            - \what{410,8951} - Selbstüberwachung
        \Issue
            - \Redmine{22110} - [FINISHED] Change the interface identifier with SCOM_X_<Interface>_INIT during runtime
            - \Redmine{22107} - [FINISHED] SCOMx_MLib: Change the interface identifier with SCOM_X_<Interface>_INIT during runtime
        \Info
            - None
        """
        # Arrange------------------------------------------------------------------------------------------------------------------------------
        test_set_format = namedtuple('test_set_format',
                                                 ['pou_prefix',     'xInit',  'usiInterfaceId', 'udiSftyMsgId', 'usiPDO',         'iStatus',                        'xError'])
        test_sets = (
                                  test_set_format('CAN1',            True,       1,                 1,             1,               0,                                 False),
                                  test_set_format('CAN2',            True,       1,                 1,             1,               0,                                 False),
                                  test_set_format('CAN1',            True,       0xFD,           0xFEDCBA98,       4,               0,                                 False),
                                  test_set_format('CAN2',            True,       0x7F,           0xFEDCBA98,       4,               0,                                 False),
                                  test_set_format('CAN2',            True,       0xFF,           0xFEDCBA98,       4,               0,                                 False),
                                  test_set_format('CAN2',            True,       0xFF,           0xFEDCBA98,       4,               0,                                 False),
                                  test_set_format('CAN2',            True,       0x00,           0x00,             0,       err['err_MAS_SafetyCom_CAN_InvalidPDO'],    True),
                                  test_set_format('CAN2',            True,       0x00,           0x00,             4,       err['err_MAS_InvalidArgument'],             True),
                    )
        
        for index, test_set in enumerate(test_sets):
            io_data = SCOM_X_CAN_INIT_IO_T(xInit=test_set.xInit, usiInterfaceId=test_set.usiInterfaceId, udiSafetyMessageIdentifier=test_set.udiSftyMsgId, usiPDO=test_set.usiPDO)
            io_data.xInit = False
            self.SCOM_X_CAN_INIT(pou_prefix=test_set.pou_prefix, deactivate_after_execution=False, io_data=io_data, cycles=1, step='s001.1.{}'.format(index))
            io_data.xInit = True
            self.SCOM_X_CAN_INIT(pou_prefix=test_set.pou_prefix, deactivate_after_execution=True, io_data=io_data, cycles=1, step='s001.2.{}'.format(index))
            self.assertEqual(io_data.iStatus, test_set.iStatus, msg="S001.3.{} iStatus wrong".format(index))
            self.assertEqual(io_data.xError, test_set.xError, msg="S001.4.{} xError wrong".format(index))
            if io_data.xError is False:
                self.assertTrue(0 < io_data.uiLinkHandler <= 0xFFFF, msg="S001.5.{} xError wrong".format(index))
    
    def test_001_SCOM_X_LAN_CH_INIT(self):
        """
        \StepDefinition
        S002: Check if SCOM_X_LAN_CH_INIT initializes LAN interface with given values
            - Call SCOM_X_LAN_CH_INIT and write valid values to the specified parameters
        
        \PassCriteria
            - SCOM_X_LAN_CH_INIT writes parameters successfully
        \Requirement
            - \what{410,83498} - SCOM_X_LAN_INIT
            - \what{251,131251} - SafetyCom® Ethernet
            - \what{410,8951} - Selbstüberwachung
        \Issue
            - \Redmine{22110} - [FINISHED] Change the interface identifier with SCOM_X_<Interface>_INIT during runtime
            - \Redmine{22107} - [FINISHED] SCOMx_MLib: Change the interface identifier with SCOM_X_<Interface>_INIT during runtime
        \Info
            - None
        """
        test_data = namedtuple('test_data', 'xInit  usiInterfaceId  udiSafetyMsgId  uiSafetyComPort  sSafetyComBroadAddr xError  iStatus')
        test_sets = (
                                                test_data(True, 1,  50,  30270, '255.255.255.255',  False,  0),
                                                test_data(True, 1,  50,  30270, '224.0.0.0',        False,  0),
        )
        # Arrange ------------------------------------------------------------------------------------------------------
        for index, test_set in enumerate(test_sets):
            io_data = SCOM_X_LAN_CH_INIT_IO_T(xInit=test_set.xInit, usiInterfaceId=test_set.usiInterfaceId, udiSafetyMsgId=test_set.udiSafetyMsgId,
                                              uiSafetyComPort=test_set.uiSafetyComPort, sSafetyComBroadAddr=test_set.sSafetyComBroadAddr)
            # Act -- Read the current setting using function ----------------------------------------------------------
            self.SCOM_X_LAN_CH_INIT(instance='01', pou_prefix='LAN_INIT', function_activation=True, io_data=io_data, step='S002.0.{}'.format(index), cycles=1)
            # Assert -------------------------------------------------------------------------------------------------------
            self.assertEqual(io_data.xError, test_set.xError, msg='S002.1.{} Invalid error returned'.format(index, io_data.xError))
            self.assertEqual(io_data.iStatus, test_set.iStatus, msg='S002.2.{} Node Number is incorrect. expected=0 read={}'.format(index, io_data.iStatus))
            self.assertGreaterEqual(io_data.uiLinkHandler, 0, msg='S002.3.{} Link Handler value is invalid'.format(index))
    
    def test_1001_negative_SCOM_X_LAN_CH_INIT(self):
        """
        \StepDefinition
        S003: Check if invalid values can be written to FB SCOM_X_LAN_CH_INIT
            - Call SCOM_X_LAN_CH_INIT and write invalid values to the specified parameters
        
        \PassCriteria
            - SCOM_X_LAN_CH_INIT returns error
        
        \Requirement
            - \what{410,83498} - SCOM_X_LAN_INIT
            - \what{251,131251} - SafetyCom® Ethernet
            - \what{410,8951} - Selbstüberwachung
        \Issue
            - None
        \Info
            - None
        """
        test_data = namedtuple('test_data', 'xInit  usiInterfaceId  udiSafetyMsgId  uiSafetyComPort  sSafetyComBroadAddr xError  iStatus')
        test_sets = (
                                                test_data(True, 256,  50,  30270, '255.255.255.255',  True,  err['err_MAS_InvalidArgument']),   # invalid argument : usiInterfaceId
                                                test_data(True, 1,    50,  30270, '223.0.0.0',        True,  err['err_MAS_SafetyCom_LAN_SetSocketOptFailure']), # invalid : sSafetyComBroadAddr
        )
        # Arrange ------------------------------------------------------------------------------------------------------
        for index, test_set in enumerate(test_sets):
            io_data = SCOM_X_LAN_CH_INIT_IO_T(xInit=test_set.xInit, usiInterfaceId=test_set.usiInterfaceId, udiSafetyMsgId=test_set.udiSafetyMsgId, uiSafetyComPort=test_set.uiSafetyComPort,
                                              sSafetyComBroadAddr=test_set.sSafetyComBroadAddr)
            # Act -- Read the current setting using function ----------------------------------------------------------
            self.SCOM_X_LAN_CH_INIT(instance='01', function_activation=True, io_data=io_data, step='S003.0.{}'.format(index), cycles=1)
            # Assert -------------------------------------------------------------------------------------------------------
            self.assertEqual(io_data.xError, test_set.xError, msg='S003.1.{} Invalid error returned '.format(index))
            self.assertEqual(io_data.iStatus, test_set.iStatus, msg='S003.2.{} Node Number is incorrect. expected= {}  got={}'.format(index,test_set.iStatus, io_data.iStatus))
            self.assertEqual(io_data.uiLinkHandler, 0, msg='S003.3.{} Link Handler value is invalid'.format(index))
    
    def test_005_local_LAN_instance_SCOM_X_LAN_CH_INIT(self):
        """
        \StepDefinition
        S004: Check FB SCOM_X_LAN_CH_INIT with local CAN instance
            - Call SCOM_X_LAN_CH_INIT and write valid values to the specified parameters and set local LAN instance
        
        \PassCriteria
            - SCOM_X_LAN_CH_INIT returns error 'err_MAS_InvalidArgument'
        \Requirement
            - \what{410,83498} - SCOM_X_LAN_INIT
            - \what{410,8951} - Selbstüberwachung
            - \what{251,131251} - SafetyCom® Ethernet
        \Issue
            - None
        \Info
            - None
        """
        test_data = namedtuple('test_data', 'xInit  usiInterfaceId  udiSafetyMsgId  uiSafetyComPort  sSafetyComBroadAddr xError  iStatus')
        test_sets = (
                                                test_data(True, 1,  50,  30270, '255.255.255.255',  True,  err['err_MAS_InvalidArgument']),
                                                test_data(True, 1,  50,  30270, '224.0.0.0',        True,  err['err_MAS_InvalidArgument']),
        )
        # Arrange ------------------------------------------------------------------------------------------------------
        for index, test_set in enumerate(test_sets):
            io_data = SCOM_X_LAN_CH_INIT_IO_T(xInit=test_set.xInit, usiInterfaceId=test_set.usiInterfaceId, udiSafetyMsgId=test_set.udiSafetyMsgId, uiSafetyComPort=test_set.uiSafetyComPort,
                                              sSafetyComBroadAddr=test_set.sSafetyComBroadAddr)
            # Act -- Read the current setting using function ----------------------------------------------------------
            self.SCOM_X_LAN_CH_INIT(instance='02', pou_prefix='LAN_INIT', function_activation=True, io_data=io_data, step='S004.0.{}'.format(index), cycles=1)
            # Assert -------------------------------------------------------------------------------------------------------
            self.assertTrue(io_data.xError, msg='S004.1.{} Invalid error returned '.format(index))
            self.assertTrue(io_data.iStatus == test_set.iStatus, msg='S004.2.{} Node Number is incorrect. expected=0 read={}'.format(index, io_data.iStatus))
            self.assertGreaterEqual(io_data.uiLinkHandler, 0, msg='S004.3.{} Link Handler value is invalid'.format(index))
    
    def test_003_SCOM_X_CPL_CO_INIT(self):
        """
        \StepDefinition
        S005: Check if SCOM_X_CPL_CO_INIT initializes CAN interface with given values
            - Call SCOM_X_CPL_CO_INIT and write valid values to the specified parameters
        
        \PassCriteria
            - SCOM_X_CPL_CO_INIT writes parameters successfully
        
        \Requirement
            - \what{410,95095} - SCOM_X_CPL_CO_INIT
            - \what{410,8951} - Selbstüberwachung
            - \what{251,212916} - SafetyCom® CAN-Powerline
        \Issue
            - \Redmine{22110} - [FINISHED] Change the interface identifier with SCOM_X_<Interface>_INIT during runtime
            - \Redmine{22107} - [FINISHED] SCOMx_MLib: Change the interface identifier with SCOM_X_<Interface>_INIT during runtime
        \Info
            - None
        """
        test_data = namedtuple('test_data', 'xInit  usiInterfaceId  udiSafetyMsgId  usiNodeAddr xError  iStatus')
        test_sets = (
                                                test_data(True,  1,     50,   1,    False,  err['err_MAS_OK'], ),
                                                test_data(True, 255,    50,  127,  False,   err['err_MAS_OK'],),
        
        )
        # Arrange ------------------------------------------------------------------------------------------------------
        for index, test_set in enumerate(test_sets):
            io_data = SCOM_X_CPL_CO_INIT_IO_T(xInit=test_set.xInit, usiInterfaceId=test_set.usiInterfaceId, udiSafetyMsgId=test_set.udiSafetyMsgId,
                                              usiNodeAddr=test_set.usiNodeAddr)
            # Act -- Read the current setting using function ----------------------------------------------------------
            self.SCOM_X_CPL_CO_INIT(instance='01', function_activation=True, io_data=io_data, step='S005.0.{}'.format(index), cycles=1)
            # Assert -------------------------------------------------------------------------------------------------------
            self.assertEqual(io_data.xError, test_set.xError, msg='S005.1.{} Invalid error returned '.format(index))
            self.assertEqual(io_data.iStatus, test_set.iStatus, msg='S005.2.{} Node Number is incorrect. expected=0 read={}'.format(index, io_data.iStatus))
            self.assertGreater(io_data.uiLinkHandler, 0, msg='S005.3.{} Link Handler value is invalid'.format(index))
    
    def test_1002_negative_SCOM_X_CPL_CO_INIT(self):
        """
        \StepDefinition
        S006: Check if invalid values can be written to FB SCOM_X_CPL_CO_INIT
            - Call SCOM_X_CPL_CO_INIT and write invalid values to the specified parameters
        
        \PassCriteria
            - SCOM_X_CPL_CO_INIT returns error
        
        \Requirement
            - \what{410,95095} - SCOM_X_CPL_CO_INIT
            - \what{410,8951} - Selbstüberwachung
            - \what{251,212916} - SafetyCom® CAN-Powerline
        \Issue
            - None
        \Info
            - None
        """
        test_data = namedtuple('test_data', 'xInit  usiInterfaceId  udiSafetyMsgId  usiNodeAddr xError  iStatus')
        test_sets = (
                                                test_data(True,  256,    50,   1,    True, err['err_MAS_InvalidArgument']),   # invalid argument: usiInterfaceId
                                                test_data(True,  100,    50,  -128,  True, err['err_MAS_SafetyCom_CPL_InvalidNodeAddr']), # invalid node : usiNodeAddr
        )
        # Arrange ------------------------------------------------------------------------------------------------------
        for index, test_set in enumerate(test_sets):
            io_data = SCOM_X_CPL_CO_INIT_IO_T(xInit=test_set.xInit, usiInterfaceId=test_set.usiInterfaceId, udiSafetyMsgId=test_set.udiSafetyMsgId,
                                              usiNodeAddr=test_set.usiNodeAddr)
            # Act -- Read the current setting using function ----------------------------------------------------------
            self.SCOM_X_CPL_CO_INIT(instance='01', function_activation=True, io_data=io_data, step='S006.0.{}'.format(index), cycles=1)
            # Assert -------------------------------------------------------------------------------------------------------
            self.assertEqual(io_data.xError, test_set.xError, msg='S006.1.{} Invalid error returned'.format(index))
            self.assertEqual(io_data.iStatus, test_set.iStatus, msg='S006.2.{} Node Number is incorrect. expected = {} got ={}'.format(index, test_set.iStatus, io_data.iStatus))
            self.assertEqual(io_data.uiLinkHandler, 0, msg='S006.3.{} Link Handler value is invalid'.format(index))
    
    def test_006_local_CAN_instance_SCOM_X_CPL_CO_INIT(self):
        """
        \StepDefinition
        S007: Check FB SCOM_X_CPL_CO_INIT with local CAN instance
            - Call SCOM_X_CPL_CO_INIT and write values to the specified parameters and set local CAN instance
        
        \PassCriteria
            - SCOM_X_CPL_CO_INIT returns error 'err_MAS_InvalidArgument'
        
        \Requirement
            - \what{410,95095} - SCOM_X_CPL_CO_INIT
            - \what{410,8951} - Selbstüberwachung
            - \what{251,212916} - SafetyCom® CAN-Powerline
        \Issue
            - None
        \Info
            - None
        """
        test_data = namedtuple('test_data', 'xInit  usiInterfaceId  udiSafetyMsgId  usiNodeAddr xError  iStatus')
        test_sets = (
                                                test_data(True,  256,    50,   1,    True, err['err_MAS_InvalidArgument']),
                                                test_data(True,  100,    50,  127,  True, err['err_MAS_InvalidArgument']),
        )
        # Arrange ------------------------------------------------------------------------------------------------------
        for index, test_set in enumerate(test_sets):
            io_data = SCOM_X_CPL_CO_INIT_IO_T(xInit=test_set.xInit, usiInterfaceId=test_set.usiInterfaceId, udiSafetyMsgId=test_set.udiSafetyMsgId,
                                              usiNodeAddr=test_set.usiNodeAddr)
            # Act -- Read the current setting using function ----------------------------------------------------------
            self.SCOM_X_CPL_CO_INIT(instance='02', function_activation=True, io_data=io_data, step='S007.0.{}'.format(index), cycles=1)
            # Assert -------------------------------------------------------------------------------------------------------
            self.assertEqual(io_data.xError, test_set.xError, msg='S007.1.{} Incorrect error returned'.format(index))
            self.assertEqual(io_data.iStatus, test_set.iStatus, msg='S007.2.{} Node Number is incorrect. expected = {} got ={}'.format(index, test_set.iStatus, io_data.iStatus))
            self.assertEqual(io_data.uiLinkHandler, 0, msg='S007.3.{} Link Handler value is invalid'.format(index))
    
    def test_101_ProducerConsumer(self):
        """
        \StepDefinition
        S101:   Test if SYS_MOS83x supports the SafetyCom® protocol(Producer, Consumer).
            - Initializes 'L1_CAN1' and 'L2_CAN2' for the SafetyCom communication.
            - Define a producer communication instance.
            - Define a consumer communication instance
            - Wait for consumer to synchronized with producer.
            - Consumer receive data from producer.
        
        \PassCriteria
            - 'L1_CAN1' and 'L2_CAN2' CAN interfaces are initialised.
            - Producer communication instance is initialized.
            - Consumer communication instance is initialized.
            - Producer and Consumer are synchronized.
            - Data sent from Producer end is received successfully at Consumer end.
        
        \Requirement
            - \what{251,212915} - SafetyCom® CAN
        
        \Issue
            - None
        
        \Info
            - None
        """
        # Prepare test data --------------------------------------------------------------------------------------------
        test_data = [10, 20, 30, 40, 50]
        
        # Initialize SafetyCom SafetyCom CAN interface for producer and consumer ---------------------------------------
        producer_link_handler, consumer_link_handler = self.init_SafetyCom_for_producer_and_consumer(
            p_interface_id=2, c_interface_id=3)
        # Act-----------------------------------------------------------------------------------------------------------
        
        # Define a producer communication instance
        io_data_producer = SCOM_X_PRODUCER_IO_T(xEnable=True, usiProducerInstanceId=2,
                                                uiLinkHandler=producer_link_handler,
                                                uiEventTime=2000, uiInhibitTime=200)
        self.SCOM_X_PRODUCER(io_data=io_data_producer, test_data=test_data, cycles=2, step='S101.0')
        
        # Define a consumer communication instance
        io_data_consumer = SCOM_X_CONSUMER_IO_T(xEnable=True, pSync=False,
                                                usiConsumerInstanceId=3, uiLinkHandler=consumer_link_handler,
                                                usiProducerInterfaceId=2, usiProducerInstanceId=2,
                                                usiWatchdogTimeoutFactor=2, uiMaxDelay=1000, uiSyncTimeout=500)
        self.SCOM_X_CONSUMER(io_data=io_data_consumer, cycles=1, step='S101.1')
        
        io_data_consumer.pSync = True
        self.SCOM_X_CONSUMER(io_data=io_data_consumer, cycles=1, step='S101.2')
        # --------------------------------------------------------------------------------------------------------------
        
        # Wait for consumer to synchronized with producer
        start_time = time.time()
        while io_data_consumer.xSynchronized == 0:
            self.SCOM_X_CONSUMER(io_data=io_data_consumer, cycles=1, step='S101.3')
            self.assertLess(time.time()-start_time, 30, msg='S101.4: SCOM_X_CONSUMER() failed to Synchronize')
        
        # Receive data from producer
        start_time = time.time()
        while io_data_consumer.pNdr == 0:
            received_data = self.SCOM_X_CONSUMER(io_data=io_data_consumer, cycles=1, step='S101.10')
            self.assertLess(time.time()-start_time, 30, msg='S101.5: SCOM_X_CONSUMER() failed to Receive data')
        
        # Assert--------------------------------------------------------------------------------------------------------
        self.assertEqual(io_data_producer.xError, False, msg='S101.6: SCOM_X_PRODUCER() Error has occurred')
        self.assertGreaterEqual(io_data_producer.iStatus, 0, msg='S101.7: SCOM_X_PRODUCER() Error has occurred')
        
        self.assertEqual(io_data_consumer.xError, False, msg='S101.8: SCOM_X_CONSUMER() Error has occurred')
        self.assertGreaterEqual(io_data_consumer.iStatus, 0, msg='S101.9: SCOM_X_CONSUMER() Error has occurred')
        self.assertEqual(io_data_consumer.xSynchronized, True,
                         msg='S101.10: SCOM_X_CONSUMER() not synchronized with Producer')
        self.assertEqual(io_data_consumer.pNdr, True, msg='S101.11: SCOM_X_CONSUMER() : Failed to receive new data')
        if io_data_consumer.pNdr:
            self.assertNotEqual(io_data_consumer.uiNbrOfRxBytes, 0,
                                msg='S101.12: SCOM_X_CONSUMER() Number of received bytes did not matched')
        
        self.assertEqual(test_data, received_data[0:5:], msg='S101.13: Sent and Received data mismatched')
        
        # Clean up -----------------------------------------------------------------------------------------------------
        self.close_SafetyCom_for_producer_and_consumer()
        self.deactivate_producer()
        self.deactivate_consumer()
        # --------------------------------------------------------------------------------------------------------------
    
    def test_102_maximum_number_of_producer_instance(self):
        """
        \StepDefinition
        S104: Check if maximum 16 producer instances can be initialized.
            - Initialise the CAN interface for the Safety communication using SCOM_X_CAN_INIT
            - Initialise 17 producer instances using the initialized instance.
            - Check if the first 16 instances can be successfully initialized.
            - Check if the 17th instance gives an err_MAS_SafetyCom_NoFreeInstance (-31647) error.
        
        \PassCriteria
            - CAN interface can be successfully initialized for the safety communication.
            - 16 Producer instances can be successfully initialized.
            - 17th Instance returns -31647 error during initialization.
        
        \Requirement
            - \what{251,213678} - Anzahl SafetyCom® Producer
        
        \Issue
            - \Redmine{24344} - [REJECTED] PKG_MLib_SCOM: Could not create 16 producer instances over CAN interface
        \Info
            - None
        """
        # TODO: 16 producer instaces can be initialized if the data buffer in the DUT is of 5 Bytes. If the data buffer is of 255 bytes then only 5 instances can be initialized.
        
        # Arrange ------------------------------------------------------------------------------------------------------
        init_io_data = SCOM_X_CAN_INIT_IO_T(xInit=True, usiInterfaceId=1, udiSafetyMessageIdentifier=1, usiPDO=1)
        self.SCOM_X_CAN_INIT(pou_prefix='CAN1', fb_enable_value=True, deactivate_after_execution=False, io_data=init_io_data,
                             cycles=1, step='S104.1')
        self.assertFalse(init_io_data.xError, 'S104.2: Error occurred during initialization')
        self.assertEqual(init_io_data.iStatus, 0, 'S104.3: FB returned {} while initializing'.format(init_io_data.iStatus))
        # Act -- Enable producer instance 1 after the other. -----------------------------------------------------------
        prod_io_data = SCOM_X_PRODUCER_IO_T(xEnable=True, usiProducerInstanceId=1, uiInhibitTime=200,
                                            uiLinkHandler=init_io_data.uiLinkHandler, uiEventTime=2000)
        for instance in range(1, 17):
            prod_io_data.usiProducerInstanceId = instance
            self.SCOM_X_PRODUCER(instance=instance, io_data=prod_io_data, cycles=2, step='S104.4.{}'.format(instance))
            # Assert ---------------------------------------------------------------------------------------------------
            self.assertEqual(prod_io_data.iStatus, 0, 'S104.5.{}: Producer instance {} returned {} error'.format(instance, instance, prod_io_data.iStatus))
            self.assertTrue(prod_io_data.pDone, 'S104.6.{}: Producer instance {} did not send data'.format(instance, instance))
        
        # Act ----------------------------------------------------------------------------------------------------------
        prod_io_data.usiProducerInstanceId = 17
        self.SCOM_X_PRODUCER(instance=17, io_data=prod_io_data, cycles=2, step='S104.7')
        self.assertEqual(prod_io_data.iStatus, -31647, 'S104.8: Producer instance 17 returned {} expected -31647'.format(prod_io_data.iStatus))
        
        # Clean up -----------------------------------------------------------------------------------------------------
        self.plc_stop()
        time.sleep(0.5)
        self.plc_start()
        
        # Arrange ------------------------------------------------------------------------------------------------------
        init_io_data = SCOM_X_CAN_INIT_IO_T(xInit=True, usiInterfaceId=1, udiSafetyMessageIdentifier=1, usiPDO=1)
        self.SCOM_X_CAN_INIT(pou_prefix='CAN1', fb_enable_value=True, deactivate_after_execution=False, io_data=init_io_data,
                             cycles=1, step='S104.9')
        self.assertFalse(init_io_data.xError, 'S104.10: Error occurred during initialization')
        self.assertEqual(init_io_data.iStatus, 0, 'S104.11: FB returned {} while initializing'.format(init_io_data.iStatus))
        
        prod_io_data = SCOM_X_PRODUCER_IO_T(xEnable=True, usiProducerInstanceId=1, uiInhibitTime=200,
                                            uiLinkHandler=init_io_data.uiLinkHandler, uiEventTime=2000)
        
        # Act -- Enable all producer instances at the same time. -------------------------------------------------------
        for instance in range(1, 18):
            prod_io_data.usiProducerInstanceId = instance
            self.SCOM_X_PRODUCER(instance=instance, io_data=prod_io_data, cycles=0,
                                 step='S104.12.{}'.format(instance))
        self.run_cycles_mSCOMx(cycles=2)
        # Assert ---------------------------------------------------------------------------------------------------
        for instance in range(1, 17):
            self.SCOM_X_PRODUCER(instance=instance, io_data=prod_io_data, cycles=0,
                                 update_output_only=True, step='S104.13.{}'.format(instance))
            
            self.assertEqual(prod_io_data.iStatus, 0, 'S104.14.{}: Producer instance {} returned {} error'.format(instance, instance, prod_io_data.iStatus))
        
        self.SCOM_X_PRODUCER(instance=17, io_data=prod_io_data, cycles=1,
                             update_output_only=True, step='S104.15')
        self.assertEqual(prod_io_data.iStatus, -31647, 'S104.16: Producer instance 17 returned {} expected -32647'.format(prod_io_data.iStatus))
        
        # Cleanup ------------------------------------------------------------------------------------------------------
        self.plc_stop()
        time.sleep(0.5)
        self.plc_start()
    
    @unittest.skip("WIP")
    def test_103_maximum_number_of_consumer_instance(self):
        """
        \StepDefinition
        S104: Check if maximum 16 consumer instances can be initialized.
            - Initialise the CAN interface for the Safety communication using SCOM_X_CAN_INIT
            - Initialise 17 producer instances using the initialized instance.
            - Check if the first 16 instances can be successfully initialized.
            - Check if the 17th instance gives an err_MAS_SafetyCom_NoFreeInstance (-31647) error.
        
        \PassCriteria
            - CAN interface can be successfully initialized for the safety communication.
            - 16 consumer instances can be successfully initialized.
            - 17th Instance returns -31647 error during initialization.
        
        \Requirement
            - \what{251,213679} - Anzahl SafetyCom® Consumer
        
        \Issue
            - None
        \Info
            - None
        """
        # Arrange ------------------------------------------------------------------------------------------------------
        io_data_can1 = SCOM_X_CAN_INIT_IO_T(xInit=True, usiInterfaceId=2, udiSafetyMessageIdentifier=1, usiPDO=3)
        self.SCOM_X_CAN_INIT(io_data=io_data_can1, cycles=1, pou_prefix='CAN1', step='S105.1')
        
        io_data_can2 = SCOM_X_CAN_INIT_IO_T(xInit=True, usiInterfaceId=3, udiSafetyMessageIdentifier=1, usiPDO=3)
        self.SCOM_X_CAN_INIT(io_data=io_data_can2, cycles=1, pou_prefix='CAN2', step='S105.2')
        
        # Act-----------------------------------------------------------------------------------------------------------
        io_data_producer = SCOM_X_PRODUCER_IO_T(xEnable=True, usiProducerInstanceId=2, uiEventTime=2000,
                                                uiInhibitTime=200, uiLinkHandler=io_data_can1.uiLinkHandler)
        self.SCOM_X_PRODUCER(io_data=io_data_producer, cycles=2, step='S105.3')
        self.assertEqual(io_data_producer.iStatus, 0, 'S105.4: Producer instance 1 returned {} expected 0'.format(io_data_producer.iStatus))
        
        io_data_consumer = SCOM_X_CONSUMER_IO_T(xEnable=True, pSync=False, usiConsumerInstanceId=3, uiMaxDelay=1000,
                                                uiLinkHandler=io_data_can2.uiLinkHandler, usiProducerInterfaceId=2,
                                                usiProducerInstanceId=2, uiSyncTimeout=500,  usiWatchdogTimeoutFactor=2)
        for instance in range(1, 17):
            io_data_consumer.usiConsumerInstanceId = instance
            self.SCOM_X_CONSUMER(pou_prefix='fb_consumers_1', instance=instance, io_data=io_data_consumer, cycles=2,
                                 step='S105.5.{}'.format(instance))
            # Assert ---------------------------------------------------------------------------------------------------
            self.assertEqual(io_data_consumer.iStatus, 0, 'S105.6.{}: Consumer instance {} returned {} error'.format(instance, instance, io_data_consumer.iStatus))
            self.assertFalse(io_data_consumer.xError, 'S105.7.{}: Consumer instance {} invalid error returned'.format(instance, instance))
        
        self.plc_stop()
        time.sleep(0.5)
        self.plc_start()
    
    def test_104_ClientServer(self):
        """
        \StepDefinition
        S105:   Test if SYS_MOS83x supports the SafetyCom® protocol(Producer, Consumer).
            - Initializes 'L1_CAN1' and 'L2_CAN2' for the SafetyCom communication.
            - Define and initialise a client communication instance.
            - Define and initialise a server communication instance.
            - Send request to server.
            - Receive Client request.
            - Send response to Client.
            - Receive response from server.
        
        \PassCriteria
            - 'L1_CAN1' and 'L2_CAN2' CAN interfaces are initialised.
            - Both client and server communication instances are initialised.
            - Request from Client is sent successfully to Server.
            - Request from Client is received successfully at Server.
            - Response is sent to client from server.
            - Same response is received at client.
        
        \Requirement
            - \what{251,212915} - SafetyCom® CAN
            - \what{410,83837} - SCOM_X_SERVER_REQUEST
            - \what{410,83840} - SCOM_X_GET_REQUEST
            - \what{410,83841} - SCOM_X_SEND_RESPONSE
        
        \Issue
            - None
        
        \Info
            - None
        """
        # Prepare test data --------------------------------------------------------------------------------------------
        
        # Send request to server
        test_set = namedtuple('test_set',
                              ['usiServerInstanceId',     'usiClientInterfaceMask',  'usiClientInstanceMask', 'server_uiResponseTimeout', 'usiClientInstanceId',  'usiServerInterfaceId', 'client_uiResponseTimeout', 'client_uiConnectionTimeout',
                               'request_to__server_data', 'response_to__client_data'])
        test_sets = (
                        test_set(2,                            0,                           0,                       500,                   3,                        2,                     500,                      0,
                                 list(range(1, 255)),     list(range(11, 20))),
                        
                        test_set(2,                            0,                           0,                       500,                   3,                        2,                     500,                      0,
                                 list(range(1, 10)),     list(range(1, 255))),
                        
                        test_set(0xFE,                            0,                        0,                       500,                   0xFF,                     0xFE,                  500,                      0,
                                 list(range(1, 255)),     list(range(40, 255))),
                        
                        test_set(2,                            0,                        0,                       500,                   3,                     2,                  500,                      0,
                                 list(range(1, 255)),     list(range(40, 255))),
                        
                        test_set(2,                            0,                        0,                       500,                   3,                     2,                  500,                      0,
                                 list(range(1, 255)),     list(range(40, 255))),
                    )
        for index, test_set in enumerate(test_sets):
            # Send request to server
            self.plc_stop()
            self.plc_start()
            self.test_client_server(usiServerInstanceId=test_set.usiServerInstanceId, usiClientInterfaceMask=test_set.usiClientInterfaceMask, usiClientInstanceMask=test_set.usiClientInstanceMask,
                                    server_uiResponseTimeout=test_set.server_uiResponseTimeout, usiClientInstanceId=test_set.usiClientInstanceId, usiServerInterfaceId=test_set.usiServerInterfaceId,
                                    client_uiResponseTimeout=test_set.client_uiResponseTimeout, client_uiConnectionTimeout=test_set.client_uiConnectionTimeout, request_to__server_data=test_set.request_to__server_data,
                                    response_to__client_data=test_set.response_to__client_data, test_step_id='S107.{}'.format(index))
    
    def test_301_SCOM_X_SERVER(self):
        """
        \StepDefinition
               S200: Call 'SCOM_X_SERVER' FB after Initializing 1st SCOM CAN1 interface
                     Check iStatus
                     Check xError
                     Check xConnected
                     Check usiServerHandler
        \PassCriteria
            - Pass  : iStatus = err_MAS_OK
                      xError = False
                      usiServerHandler = Expected value
        \Requirement
            - \what{251,212915} - SafetyCom® CAN
            - \what{410,83839} - SCOM_X_SERVER
            - \what{410,8951} - Selbstüberwachung
        \Issue
            - \Redmine{22305} - [IN TEST] Add a valid check for input parameter UILINKHANDLER
        \Info
            - None
        """
        # Arrange------------------------------------------------------------------------------------------------------------------------------
        test_set_format = namedtuple('test_set_format',
                                                 ['pou_prefix',     'xInit',  'usiInterfaceId', 'udiSftyMsgId', 'usiPDO',  'iStatus', 'xError'])
        test_sets = (
                                  test_set_format('CAN1',            True,       0xFD,           0xFEDCBA98,       4,        0,          False),
                    )
        
        for index, test_set in enumerate(test_sets):
            io_data = SCOM_X_CAN_INIT_IO_T(xInit=test_set.xInit, usiInterfaceId=test_set.usiInterfaceId, udiSafetyMessageIdentifier=test_set.udiSftyMsgId, usiPDO=test_set.usiPDO)
            io_data.xInit = False
            self.SCOM_X_CAN_INIT(pou_prefix=test_set.pou_prefix, fb_enable_value=True, deactivate_after_execution=False, io_data=io_data, cycles=1, step='s001.1.{}'.format(index))
            io_data.xInit = True
            self.SCOM_X_CAN_INIT(pou_prefix=test_set.pou_prefix, fb_enable_value=True, deactivate_after_execution=False, io_data=io_data, cycles=1, step='s001.2.{}'.format(index))
            self.assertEqual(io_data.iStatus, test_set.iStatus, msg="S200.3.{} iStatus wrong".format(index))
            self.assertEqual(io_data.xError, test_set.xError, msg="S200.4.{} xError wrong".format(index))
            if io_data.xError is False:
                self.assertTrue(0 < io_data.uiLinkHandler <= 0xFFFF, msg="S200.5.{} xError wrong".format(index))
        
        h_result, mas_function_name, can1_ui_link_handler = self.iec_item_read(item_name='CAN1_uiLinkHandler')
        test_set_format = namedtuple('test_set_format',
                                     ['pou_prefix', 'xEnable',  'usiServerInstanceId', 'uiLinkHandler', 'usiClientInterfaceMask',  'usiClientInstanceMask', 'uiResponseTimeout', 'xConnected', 'xError', 'iStatus', 'usiServerHandler'])
        test_sets = (
                    test_set_format('SERVER_01',    False,        0xFE,             can1_ui_link_handler,       0,                      0,                    500,                     False,      False,      0,      0),
                    test_set_format('SERVER_01',    True,         0xFE,             can1_ui_link_handler,       0,                      0,                    500,                     False,      False,       0,      0),
                    test_set_format('SERVER_01',    True,         0xFE,             0,                        0,                      0,                    500,                     False,      True,  -32752,      0),
                    )
        
        for index, test_set in enumerate(test_sets):
            io_data = SCOM_X_SERVER_IO_T(xEnable=test_set.xEnable, usiServerInstanceId=test_set.usiServerInstanceId, uiLinkHandler=test_set.uiLinkHandler, usiClientInterfaceMask=test_set.usiClientInterfaceMask,
                                         usiClientInstanceMask=test_set.usiClientInstanceMask, uiResponseTimeout=test_set.uiResponseTimeout, xConnected=test_set.xConnected,
                                         xError=test_set.xError, iStatus=test_set.iStatus, usiServerHandler=test_set.usiServerHandler)
            io_data.xEnable = False
            self.SCOM_X_SERVER(io_data=io_data, cycles=1, step='s001.1.{}'.format(index))
            io_data.xEnable = True
            self.SCOM_X_SERVER(io_data=io_data, cycles=1, step='s001.1.{}'.format(index))
            self.assertEqual(io_data.iStatus, test_set.iStatus, msg="S200.3.{} iStatus wrong".format(index))
            self.assertEqual(io_data.xError, test_set.xError, msg="S200.4.{} xError wrong".format(index))
            if io_data.xError is False:
                self.assertTrue(0 <= io_data.usiServerHandler <= 0xFF, msg="S200.5.{} usiServerHandler wrong".format(index))
    
    def test_302_SCOM_X_CLIENT(self):
        """
        \StepDefinition
               S200: Call 'SCOM_X_CLIENT' FB after Initializing 1st SCOM CAN2 interface
                     Check iStatus
                     Check xError
                     Check xConnected
                     Check usiServerHandler
        \PassCriteria
            - Pass  : iStatus = err_MAS_OK
                      xError = False
                      usiCLientHandler = Expected value
        \Requirement
            - \what{251,212915} - SafetyCom® CAN
            - \what{410,83831} - SCOM_X_CLIENT
            - \what{410,8951} - Selbstüberwachung
        \Issue
            - \Redmine{22305} - [IN TEST] Add a valid check for input parameter UILINKHANDLER
        \Info
            - None
        """
        # Arrange------------------------------------------------------------------------------------------------------------------------------
        test_set_format = namedtuple('test_set_format',
                                                 ['pou_prefix',     'xInit',  'usiInterfaceId', 'udiSftyMsgId', 'usiPDO',  'iStatus', 'xError'])
        test_sets = (
                                  test_set_format('CAN2',            True,       0xFD,           0xFEDCBA98,       4,        0,          False),
                    )
        
        for index, test_set in enumerate(test_sets):
            io_data = SCOM_X_CAN_INIT_IO_T(xInit=test_set.xInit, usiInterfaceId=test_set.usiInterfaceId, udiSafetyMessageIdentifier=test_set.udiSftyMsgId, usiPDO=test_set.usiPDO)
            io_data.xInit = False
            self.SCOM_X_CAN_INIT(pou_prefix=test_set.pou_prefix, fb_enable_value=True, deactivate_after_execution=False, io_data=io_data, cycles=1, step='s001.1.{}'.format(index))
            io_data.xInit = True
            self.SCOM_X_CAN_INIT(pou_prefix=test_set.pou_prefix, fb_enable_value=True, deactivate_after_execution=False, io_data=io_data, cycles=1, step='s001.2.{}'.format(index))
            self.assertEqual(io_data.iStatus, test_set.iStatus, msg="S200.3.{} iStatus wrong".format(index))
            self.assertEqual(io_data.xError, test_set.xError, msg="S200.4.{} xError wrong".format(index))
            if io_data.xError is False:
                self.assertTrue(0 < io_data.uiLinkHandler <= 0xFFFF, msg="S200.5.{} xError wrong".format(index))
        
        h_result, mas_function_name, can2_uiLinkHandler = self.iec_item_read(item_name='CAN2_uiLinkHandler')
        test_set = namedtuple('test_set',
                            ['pou_prefix', 'xEnable',  'xConnect', 'usiClientInstanceId', 'uiLinkHandler', 'usiServerInterfaceId',  'usiServerInstanceId', 'uiConnectionTimeout', 'uiResponseTimeout', 'xConnected', 'xError', 'iStatus', 'usiClientHandler'])
        test_sets = (
                    test_set('CLIENT_01',    False,        False,        0x7E,        can2_uiLinkHandler,       0xFF,                  0xFE,                 0,                          500,              False,      False,      0,        0),
                    test_set('CLIENT_01',    True,         False,        0x7E,        can2_uiLinkHandler,       0xFF,                  0xFE,                 0,                          500,              False,      False,      0,        0),
                    test_set('CLIENT_01',    True,         False,        0x7E,        0,                        0xFF,                  0xFE,                 0,                          500,              False,      True,   -32752,       0),
                    )
        
        for index, test_set in enumerate(test_sets):
            io_data = SCOM_X_CLIENT_IO_T(xEnable=test_set.xEnable, xConnect=test_set.xConnect, usiClientInstanceId=test_set.usiClientInstanceId,
                                         uiLinkHandler=test_set.uiLinkHandler, usiServerInterfaceId=test_set.usiClientInstanceId, usiServerInstanceId=test_set.usiServerInstanceId,
                                         uiConnectionTimeout=test_set.uiConnectionTimeout, uiResponseTimeout=test_set.uiResponseTimeout)
            io_data.xEnable = False
            self.SCOM_X_CLIENT(io_data=io_data, cycles=1, step='s001.1.{}'.format(index))
            io_data.xEnable = True
            self.SCOM_X_CLIENT(io_data=io_data, cycles=1, step='s001.1.{}'.format(index))
            self.assertEqual(io_data.iStatus, test_set.iStatus, msg="S200.3.{} iStatus wrong".format(index))
            self.assertEqual(io_data.xError, test_set.xError, msg="S200.4.{} xError wrong".format(index))
            if io_data.xError is False:
                self.assertTrue(0 <= io_data.usiClientHandler <= 0xFF, msg="S200.5.{} usiClientHandler wrong".format(index))
    
    def test_105_maximum_number_of_server_instance(self):
        """
        \StepDefinition
        S201: Check if maximum 16 server instances can be initialized.
            - Initialise the CAN interface for the Safety communication using SCOM_X_CAN_INIT
            - Initialise 16 sever instances using the initialized instance.
            - Check if the first 16 instances can be successfully initialized.
            - Check if the 17th instance gives an err_MAS_SafetyCom_NoFreeInstance (-31647) error.
        
        \PassCriteria
            - CAN interface can be successfully initialized for the safety communication.
            - 16 server instances can be successfully initialized.
            - 17th Instance returns -31647 error during initialization.
        
        \Requirement
            - \what{251,213681} - Anzahl SafetyCom® Server
        
        \Issue
            - None
        \Info
            - None
        """
        init_io_data = SCOM_X_CAN_INIT_IO_T(xInit=True, usiInterfaceId=1, udiSafetyMessageIdentifier=1, usiPDO=1)
        self.SCOM_X_CAN_INIT(pou_prefix='CAN1', fb_enable_value=True, deactivate_after_execution=False, io_data=init_io_data,
                             cycles=1, step='S201.0')
        self.assertFalse(init_io_data.xError, 'S201.1: Error occurred during initialization')
        self.assertEqual(init_io_data.iStatus, 0, 'S201.2: FB returned {} while initializing'.format(init_io_data.iStatus))
        server_io_data = SCOM_X_SERVER_IO_T(xEnable=True, usiServerInstanceId=1, uiLinkHandler=init_io_data.uiLinkHandler, 
                                            usiClientInterfaceMask=0, usiClientInstanceMask=0, uiResponseTimeout=500)
        for instance in range(1, 17):
            server_io_data.usiServerInstanceId = instance
            self.SCOM_X_SERVER(instance=instance, pou_prefix='fb_servers_1', io_data=server_io_data, cycles=2, step='S201.3.{}'.format(instance))
            # Assert ---------------------------------------------------------------------------------------------------
            self.assertEqual(server_io_data.iStatus, 0, 'S201.4.{}: Server instance {} returned {} error'.format(instance, instance, server_io_data.iStatus))
            self.assertFalse(server_io_data.xError, 'S201.5.{}: Server instance {} did not send data'.format(instance, instance))
            self.assertEqual(server_io_data.usiServerHandler, instance, 'S0201.6.{} value of SeverHandler is incorrect'.format(instance))
        
        server_io_data.usiServerInstanceId = 17
        self.SCOM_X_SERVER(pou_prefix='fb_servers_1', instance=17, io_data=server_io_data, cycles=2, step='201.7')
        self.assertEqual(server_io_data.iStatus, err['err_MAS_SafetyCom_NoFreeInstance'], '201.8: Server instance 17 returned {} expected -31647'.format(server_io_data.iStatus))
        
        self.plc_stop()
        time.sleep(0.5)
        self.plc_start()
    
    def test_106_maximum_number_of_client_instance(self):
        """
        \StepDefinition
        S202: Check if maximum 16 clients instances can be initialized.
            - Initialise the CAN interface for the Safety communication using SCOM_X_CAN_INIT
            - Initialise 16 client instances using the initialized instance.
            - Check if the first 16 instances can be successfully initialized.
            - Check if the 17th instance gives an err_MAS_SafetyCom_NoFreeInstance (-31647) error.
        
        \PassCriteria
            - CAN interface can be successfully initialized for the safety communication.
            - 16 client instances can be successfully initialized.
            - 17th Instance returns -31647 error during initialization.
        
        \Requirement
            - \what{251,213680} - Anzahl SafetyCom® Client
        
        \Issue
            - None
        \Info
            - None
        """
        init_io_data = SCOM_X_CAN_INIT_IO_T(xInit=True, usiInterfaceId=1, udiSafetyMessageIdentifier=1, usiPDO=1)
        self.SCOM_X_CAN_INIT(pou_prefix='CAN1', fb_enable_value=True, deactivate_after_execution=False, io_data=init_io_data,
                             cycles=1, step='S202.0')
        self.assertFalse(init_io_data.xError, 'S202.1: Error occurred during initialization')
        self.assertEqual(init_io_data.iStatus, 0, 'S202.2: FB returned {} while initializing'.format(init_io_data.iStatus))
        client_io_data = SCOM_X_CLIENT_IO_T(xEnable=True, xConnect=False, usiClientInstanceId=1, uiLinkHandler=init_io_data.uiLinkHandler,
                                            usiServerInterfaceId=0, usiServerInstanceId=0, uiConnectionTimeout=0, uiResponseTimeout=500)
        for instance in range(1, 17):
            client_io_data.usiClientInstanceId = instance
            self.SCOM_X_CLIENT(instance=instance, pou_prefix='fb_clients_1', io_data=client_io_data, cycles=2, step='S202.3.{}'.format(instance))
            # Assert ---------------------------------------------------------------------------------------------------
            self.assertEqual(client_io_data.iStatus, 0, 'S202.4.{}: client instance {} returned {} error'.format(instance, instance, client_io_data.iStatus))
            self.assertFalse(client_io_data.xError, 'S202.5.{}: client instance {} returned error'.format(instance, instance))
            self.assertEqual(client_io_data.usiClientHandler, instance, 'S0202.6.{} value of client handler is incorrect'.format(instance))
        
        client_io_data.usiClientInstanceId = 17
        self.SCOM_X_SERVER(pou_prefix='fb_servers_1', instance=17, io_data=client_io_data, cycles=2, step='202.7')
        self.assertEqual(client_io_data.iStatus, err['err_MAS_SafetyCom_NoFreeInstance'], '202.8: client instance 17 returned {} expected -31647'.format(client_io_data.iStatus))
        
        self.plc_stop()
        time.sleep(0.5)
        self.plc_start()
    
    def test_201_SCOM_X_PRODUCER(self):
        """
        \StepDefinition
        S201: Test function block SCOM_X_PRODUCER.
            - Initialize SafetyCom over CAN.
            - Call SCOM_X_PRODUCER() as per input test data and check outputs.
        \PassCriteria
            - Check if outputs are set as per test data.
        \Requirement
            - \what{410,83505} - SCOM_X_PRODUCER
            - \what{410,8951} - Selbstüberwachung
        \Issue
            - \Redmine{22305} - [In Test] Add a valid check for input parameter UILINKHANDLER.
        \Info
            - None
        """
        # Arrange-------------------------------------------------------------------------------------------------------
        valid_link_handler = -1
        test_sets = namedtuple(
            'test_sets',
            'xEnable usiProducerInstanceId uiLinkHandler uiEventTime uiInhibitTime pDone xError iStatus')
        
        test_data_set = (
            test_sets(xEnable=False, usiProducerInstanceId=1, uiLinkHandler=valid_link_handler, uiEventTime=2000,
                      uiInhibitTime=200, pDone=False, xError=False, iStatus=0),
            test_sets(xEnable=True, usiProducerInstanceId=1, uiLinkHandler=valid_link_handler, uiEventTime=2000,
                      uiInhibitTime=200, pDone=True, xError=False, iStatus=0),
            
            # EC for usiProducerInstanceId
            test_sets(xEnable=True, usiProducerInstanceId=USINT.MIN, uiLinkHandler=valid_link_handler, uiEventTime=2000,
                      uiInhibitTime=200, pDone=False, xError=True, iStatus=-32761),
            test_sets(xEnable=True, usiProducerInstanceId=USINT.MID, uiLinkHandler=valid_link_handler, uiEventTime=2000,
                      uiInhibitTime=200, pDone=True, xError=False, iStatus=0),
            test_sets(xEnable=True, usiProducerInstanceId=USINT.MAX, uiLinkHandler=valid_link_handler, uiEventTime=2000,
                      uiInhibitTime=200, pDone=True, xError=False, iStatus=0),
            
            # EC for uiLinkHandler
            test_sets(xEnable=True, usiProducerInstanceId=1, uiLinkHandler=UINT.MIN, uiEventTime=2000,
                      uiInhibitTime=200, pDone=False, xError=True, iStatus=-32752),
            test_sets(xEnable=True, usiProducerInstanceId=1, uiLinkHandler=UINT.MID, uiEventTime=2000,
                      uiInhibitTime=200, pDone=False, xError=True, iStatus=-32761),
            test_sets(xEnable=True, usiProducerInstanceId=1, uiLinkHandler=UINT.MAX, uiEventTime=2000,
                      uiInhibitTime=200, pDone=False, xError=True, iStatus=-32761),
            
            # EC for uiEventTime
            test_sets(xEnable=True, usiProducerInstanceId=1, uiLinkHandler=valid_link_handler, uiEventTime=UINT.MIN,
                      uiInhibitTime=UINT.MIN, pDone=False, xError=True, iStatus=-32761),
            test_sets(xEnable=True, usiProducerInstanceId=1, uiLinkHandler=valid_link_handler, uiEventTime=UINT.MID,
                      uiInhibitTime=200, pDone=True, xError=False, iStatus=0),
            test_sets(xEnable=True, usiProducerInstanceId=1, uiLinkHandler=valid_link_handler, uiEventTime=UINT.MAX,
                      uiInhibitTime=200, pDone=True, xError=False, iStatus=0),
            
            # EC for uiInhibitTime
            test_sets(xEnable=True, usiProducerInstanceId=1, uiLinkHandler=valid_link_handler, uiEventTime=2000,
                      uiInhibitTime=UINT.MIN, pDone=False, xError=True, iStatus=-32761),
            test_sets(xEnable=True, usiProducerInstanceId=1, uiLinkHandler=valid_link_handler, uiEventTime=UINT.MAX,
                      uiInhibitTime=UINT.MID, pDone=True, xError=False, iStatus=0),
            test_sets(xEnable=True, usiProducerInstanceId=1, uiLinkHandler=valid_link_handler, uiEventTime=UINT.MAX,
                      uiInhibitTime=UINT.MAX, pDone=True, xError=False, iStatus=0),
            
            # InhibitTime must not be greater than EventTime
            test_sets(xEnable=True, usiProducerInstanceId=1, uiLinkHandler=valid_link_handler, uiEventTime=200,
                      uiInhibitTime=2000, pDone=False, xError=True, iStatus=-31616),
        )
        
        # Initial Conditions -------------------------------------------------------------------------------------------
        for step_id, test_data in enumerate(test_data_set):
            
            if test_data.uiLinkHandler == -1:
                # Initialize SafetyCom SafetyCom CAN interface for producer.
                io_data_can1 = SCOM_X_CAN_INIT_IO_T(xInit=True, usiInterfaceId=2, udiSafetyMessageIdentifier=28,
                                                    usiPDO=3)
                io_data_can1.xInit = False
                self.SCOM_X_CAN_INIT(io_data=io_data_can1, cycles=1, pou_prefix='CAN1',
                                     step='S201.1.{}:'.format(step_id))
                io_data_can1.xInit = True
                self.SCOM_X_CAN_INIT(io_data=io_data_can1, cycles=1, pou_prefix='CAN1',
                                     step='S201.1.{}:'.format(step_id))
                
                valid_link_handler = io_data_can1.uiLinkHandler
                self.assertNotEqual(valid_link_handler, -1,
                                    msg='S201.0: create_uiLinkHandler() Failed to Initialize SafetyCom over CAN')
            else:
                valid_link_handler = test_data.uiLinkHandler
        
        # --------------------------------------------------------------------------------------------------------------
            io_data = SCOM_X_PRODUCER_IO_T(
                xEnable=test_data.xEnable, usiProducerInstanceId=test_data.usiProducerInstanceId,
                uiLinkHandler=valid_link_handler, uiEventTime=test_data.uiEventTime,
                uiInhibitTime=test_data.uiInhibitTime)
        # Act-----------------------------------------------------------------------------------------------------------
            self.SCOM_X_PRODUCER(io_data=io_data, cycles=2, step='S201.1.{}:'.format(step_id))
        # Assert--------------------------------------------------------------------------------------------------------
            self.assertEqual(io_data.iStatus, test_data.iStatus, msg='S201.2.{}:'.format(step_id))
            self.assertEqual(io_data.xError, test_data.xError, msg='S201.3.{}:'.format(step_id))
            self.assertEqual(io_data.pDone, test_data.pDone, msg='S201.4.{}:'.format(step_id))
        # Clean up -----------------------------------------------------------------------------------------------------
            self.close_SafetyCom_for_producer()
            self.deactivate_producer()
        # --------------------------------------------------------------------------------------------------------------
        # Note:
        # Update this test function to check Event time and Inhibit time.
        # --------------------------------------------------------------------------------------------------------------
    
    def test_202_SCOM_X_CONSUMER(self):
        """
        \StepDefinition
        S202: Test function block SCOM_X_CONSUMER.
            - Initialize SafetyCom over CAN.
            - Call SCOM_X_CONSUMER() as per input test data and check outputs.
        \PassCriteria
            - Check if outputs are set as per test data.
        \Requirement
            - \what{410,83770} - SCOM_X_CONSUMER
            - \what{410,8951} - Selbstüberwachung
        \Issue
            - \Redmine{22305} - [In Test] Add a valid check for input parameter UILINKHANDLER.
        \Info
            - None
        """
        # --------------------------------------------------------------------------------------------------------------
        valid_link_handler = -1
        dont_care = -2
        
        test_sets = namedtuple(
            'test_sets',
            'test_id p_interface_id c_interface_id '
            'p_link_handler c_link_handler '
            'p_event_time p_inhibit_time '
            
            'xEnable pSync usiConsumerInstanceId uiLinkHandler usiProducerInterfaceId usiProducerInstanceId '
            'usiWatchdogTimeoutFactor uiMaxDelay uiSyncTimeout '
            'xSynchronized pNdr uiNbrOfRxBytes xError iStatus')
        
        test_data_set = (
            test_sets(test_id=1, p_interface_id=2, c_interface_id=3,
                      p_link_handler=valid_link_handler, c_link_handler=valid_link_handler,
                      p_event_time=2000, p_inhibit_time=200,
                      xEnable=True, pSync=True,
                      usiConsumerInstanceId=3, uiLinkHandler=valid_link_handler,
                      usiProducerInterfaceId=2, usiProducerInstanceId=2,
                      usiWatchdogTimeoutFactor=2, uiMaxDelay=1000, uiSyncTimeout=500,
                      xSynchronized=True, pNdr=0, uiNbrOfRxBytes=0, xError=0, iStatus=0),
            
            # EC of usiConsumerInstanceId
            test_sets(test_id=2, p_interface_id=2, c_interface_id=3,
                      p_link_handler=valid_link_handler, c_link_handler=valid_link_handler,
                      p_event_time=2000, p_inhibit_time=200,
                      xEnable=True, pSync=True,
                      usiConsumerInstanceId=USINT.MIN, uiLinkHandler=valid_link_handler,
                      usiProducerInterfaceId=2, usiProducerInstanceId=2,
                      usiWatchdogTimeoutFactor=2, uiMaxDelay=1000, uiSyncTimeout=500,
                      xSynchronized=dont_care, pNdr=dont_care, uiNbrOfRxBytes=dont_care,
                      xError=True, iStatus=-32761),
            test_sets(test_id=3, p_interface_id=2, c_interface_id=3,
                      p_link_handler=valid_link_handler, c_link_handler=valid_link_handler,
                      p_event_time=2000, p_inhibit_time=200,
                      xEnable=True, pSync=True,
                      usiConsumerInstanceId=USINT.MID, uiLinkHandler=valid_link_handler,
                      usiProducerInterfaceId=2, usiProducerInstanceId=2,
                      usiWatchdogTimeoutFactor=2, uiMaxDelay=1000, uiSyncTimeout=500,
                      xSynchronized=dont_care, pNdr=dont_care, uiNbrOfRxBytes=dont_care,
                      xError=True, iStatus=-32761),
            test_sets(test_id=4, p_interface_id=2, c_interface_id=3,
                      p_link_handler=valid_link_handler, c_link_handler=valid_link_handler,
                      p_event_time=2000, p_inhibit_time=200,
                      xEnable=True, pSync=True,
                      usiConsumerInstanceId=USINT.MAX, uiLinkHandler=valid_link_handler,
                      usiProducerInterfaceId=2, usiProducerInstanceId=2,
                      usiWatchdogTimeoutFactor=2, uiMaxDelay=1000, uiSyncTimeout=500,
                      xSynchronized=dont_care, pNdr=dont_care, uiNbrOfRxBytes=dont_care,
                      xError=True, iStatus=-32761),
            # usiConsumerInstanceId = usiProducerInstanceId
            test_sets(test_id=5, p_interface_id=2, c_interface_id=3,
                      p_link_handler=valid_link_handler, c_link_handler=valid_link_handler,
                      p_event_time=2000, p_inhibit_time=200,
                      xEnable=True, pSync=True,
                      usiConsumerInstanceId=2, uiLinkHandler=valid_link_handler,
                      usiProducerInterfaceId=2, usiProducerInstanceId=2,
                      usiWatchdogTimeoutFactor=2, uiMaxDelay=1000, uiSyncTimeout=500,
                      xSynchronized=dont_care, pNdr=dont_care, uiNbrOfRxBytes=dont_care,
                      xError=True, iStatus=-32761),
            
            # EC for uiLinkHandler
            test_sets(test_id=6, p_interface_id=2, c_interface_id=3,
                      p_link_handler=valid_link_handler, c_link_handler=UINT.MIN,
                      p_event_time=2000, p_inhibit_time=200,
                      xEnable=True, pSync=True,
                      usiConsumerInstanceId=2, uiLinkHandler=UINT.MIN,
                      usiProducerInterfaceId=2, usiProducerInstanceId=2,
                      usiWatchdogTimeoutFactor=2, uiMaxDelay=1000, uiSyncTimeout=500,
                      xSynchronized=dont_care, pNdr=dont_care, uiNbrOfRxBytes=dont_care,
                      xError=True, iStatus=-32752),
            test_sets(test_id=7, p_interface_id=2, c_interface_id=3,
                      p_link_handler=valid_link_handler, c_link_handler=UINT.MID,
                      p_event_time=2000, p_inhibit_time=200,
                      xEnable=True, pSync=True,
                      usiConsumerInstanceId=2, uiLinkHandler=UINT.MID,
                      usiProducerInterfaceId=2, usiProducerInstanceId=2,
                      usiWatchdogTimeoutFactor=2, uiMaxDelay=1000, uiSyncTimeout=500,
                      xSynchronized=dont_care, pNdr=dont_care, uiNbrOfRxBytes=dont_care,
                      xError=True, iStatus=-32752),
            test_sets(test_id=8, p_interface_id=2, c_interface_id=3,
                      p_link_handler=valid_link_handler, c_link_handler=UINT.MAX,
                      p_event_time=2000, p_inhibit_time=200,
                      xEnable=True, pSync=True,
                      usiConsumerInstanceId=2, uiLinkHandler=UINT.MAX,
                      usiProducerInterfaceId=2, usiProducerInstanceId=2,
                      usiWatchdogTimeoutFactor=2, uiMaxDelay=1000, uiSyncTimeout=500,
                      xSynchronized=dont_care, pNdr=dont_care, uiNbrOfRxBytes=dont_care,
                      xError=True, iStatus=-32752),
            
            # EC for usiProducerInterfaceId
            test_sets(test_id=9, p_interface_id=2, c_interface_id=3,
                      p_link_handler=valid_link_handler, c_link_handler=valid_link_handler,
                      p_event_time=2000, p_inhibit_time=200,
                      xEnable=True, pSync=True,
                      usiConsumerInstanceId=3, uiLinkHandler=valid_link_handler,
                      usiProducerInterfaceId=USINT.MIN, usiProducerInstanceId=2,
                      usiWatchdogTimeoutFactor=2, uiMaxDelay=1000, uiSyncTimeout=500,
                      xSynchronized=dont_care, pNdr=dont_care, uiNbrOfRxBytes=dont_care,
                      xError=True, iStatus=-32761),
            
            test_sets(test_id=10, p_interface_id=2, c_interface_id=3,
                      p_link_handler=valid_link_handler, c_link_handler=valid_link_handler,
                      p_event_time=2000, p_inhibit_time=200,
                      xEnable=True, pSync=True,
                      usiConsumerInstanceId=3, uiLinkHandler=valid_link_handler,
                      usiProducerInterfaceId=USINT.MID, usiProducerInstanceId=2,
                      usiWatchdogTimeoutFactor=2, uiMaxDelay=1000, uiSyncTimeout=500,
                      xSynchronized=dont_care, pNdr=dont_care, uiNbrOfRxBytes=dont_care,
                      xError=False, iStatus=-32758),
            test_sets(test_id=11, p_interface_id=2, c_interface_id=3,
                      p_link_handler=valid_link_handler, c_link_handler=valid_link_handler,
                      p_event_time=2000, p_inhibit_time=200,
                      xEnable=True, pSync=True,
                      usiConsumerInstanceId=3, uiLinkHandler=valid_link_handler,
                      usiProducerInterfaceId=USINT.MAX, usiProducerInstanceId=2,
                      usiWatchdogTimeoutFactor=2, uiMaxDelay=1000, uiSyncTimeout=500,
                      xSynchronized=dont_care, pNdr=dont_care, uiNbrOfRxBytes=dont_care,
                      xError=False, iStatus=-32758),
            
            # usiProducerInterfaceId = InterfaceId(SCOM_X_CAN_INIT consumer)
            test_sets(test_id=12, p_interface_id=2, c_interface_id=3,
                      p_link_handler=valid_link_handler, c_link_handler=valid_link_handler,
                      p_event_time=2000, p_inhibit_time=200,
                      xEnable=True, pSync=True,
                      usiConsumerInstanceId=3, uiLinkHandler=valid_link_handler,
                      usiProducerInterfaceId=3, usiProducerInstanceId=2,
                      usiWatchdogTimeoutFactor=2, uiMaxDelay=1000, uiSyncTimeout=500,
                      xSynchronized=dont_care, pNdr=dont_care, uiNbrOfRxBytes=dont_care,
                      xError=False, iStatus=-32758),
            
            # EC for usiProducerInstanceId
            test_sets(test_id=13, p_interface_id=2, c_interface_id=3,
                      p_link_handler=valid_link_handler, c_link_handler=valid_link_handler,
                      p_event_time=2000, p_inhibit_time=200,
                      xEnable=True, pSync=True,
                      usiConsumerInstanceId=3, uiLinkHandler=valid_link_handler,
                      usiProducerInterfaceId=2, usiProducerInstanceId=USINT.MIN,
                      usiWatchdogTimeoutFactor=2, uiMaxDelay=1000, uiSyncTimeout=500,
                      xSynchronized=dont_care, pNdr=dont_care, uiNbrOfRxBytes=dont_care,
                      xError=True, iStatus=-32761),
            test_sets(test_id=14, p_interface_id=2, c_interface_id=3,
                      p_link_handler=valid_link_handler, c_link_handler=valid_link_handler,
                      p_event_time=2000, p_inhibit_time=200,
                      xEnable=True, pSync=True,
                      usiConsumerInstanceId=3, uiLinkHandler=valid_link_handler,
                      usiProducerInterfaceId=2, usiProducerInstanceId=USINT.MID,
                      usiWatchdogTimeoutFactor=2, uiMaxDelay=1000, uiSyncTimeout=500,
                      xSynchronized=dont_care, pNdr=dont_care, uiNbrOfRxBytes=dont_care,
                      xError=True, iStatus=-32761),
            test_sets(test_id=15, p_interface_id=2, c_interface_id=3,
                      p_link_handler=valid_link_handler, c_link_handler=valid_link_handler,
                      p_event_time=2000, p_inhibit_time=200,
                      xEnable=True, pSync=True,
                      usiConsumerInstanceId=3, uiLinkHandler=valid_link_handler,
                      usiProducerInterfaceId=2, usiProducerInstanceId=USINT.MAX,
                      usiWatchdogTimeoutFactor=2, uiMaxDelay=1000, uiSyncTimeout=500,
                      xSynchronized=dont_care, pNdr=dont_care, uiNbrOfRxBytes=dont_care,
                      xError=True, iStatus=-32761),
            
            # EC usiWatchdogTimeoutFactor(2..15)
            test_sets(test_id=16, p_interface_id=2, c_interface_id=3,
                      p_link_handler=valid_link_handler, c_link_handler=valid_link_handler,
                      p_event_time=2000, p_inhibit_time=200,
                      xEnable=True, pSync=True,
                      usiConsumerInstanceId=3, uiLinkHandler=valid_link_handler,
                      usiProducerInterfaceId=2, usiProducerInstanceId=2,
                      usiWatchdogTimeoutFactor=UINT.MIN, uiMaxDelay=1000, uiSyncTimeout=500,
                      xSynchronized=dont_care, pNdr=dont_care, uiNbrOfRxBytes=dont_care,
                      xError=True, iStatus=-32761),
            test_sets(test_id=17, p_interface_id=2, c_interface_id=3,
                      p_link_handler=valid_link_handler, c_link_handler=valid_link_handler,
                      p_event_time=2000, p_inhibit_time=200,
                      xEnable=True, pSync=True,
                      usiConsumerInstanceId=3, uiLinkHandler=valid_link_handler,
                      usiProducerInterfaceId=2, usiProducerInstanceId=2,
                      usiWatchdogTimeoutFactor=UINT.MID, uiMaxDelay=1000, uiSyncTimeout=500,
                      xSynchronized=dont_care, pNdr=dont_care, uiNbrOfRxBytes=dont_care,
                      xError=True, iStatus=-32761),
            test_sets(test_id=18, p_interface_id=2, c_interface_id=3,
                      p_link_handler=valid_link_handler, c_link_handler=valid_link_handler,
                      p_event_time=2000, p_inhibit_time=200,
                      xEnable=True, pSync=True,
                      usiConsumerInstanceId=3, uiLinkHandler=valid_link_handler,
                      usiProducerInterfaceId=2, usiProducerInstanceId=2,
                      usiWatchdogTimeoutFactor=UINT.MAX, uiMaxDelay=1000, uiSyncTimeout=500,
                      xSynchronized=dont_care, pNdr=dont_care, uiNbrOfRxBytes=dont_care,
                      xError=True, iStatus=-32761),
            
            # Invalid usiWatchdogTimeoutFactor.
            test_sets(test_id=19, p_interface_id=2, c_interface_id=3,
                      p_link_handler=valid_link_handler, c_link_handler=valid_link_handler,
                      p_event_time=2000, p_inhibit_time=200,
                      xEnable=True, pSync=True,
                      usiConsumerInstanceId=3, uiLinkHandler=valid_link_handler,
                      usiProducerInterfaceId=2, usiProducerInstanceId=2,
                      usiWatchdogTimeoutFactor=1, uiMaxDelay=1000, uiSyncTimeout=500,
                      xSynchronized=dont_care, pNdr=dont_care, uiNbrOfRxBytes=dont_care,
                      xError=True, iStatus=-32761),
            test_sets(test_id=20, p_interface_id=2, c_interface_id=3,
                      p_link_handler=valid_link_handler, c_link_handler=valid_link_handler,
                      p_event_time=2000, p_inhibit_time=200,
                      xEnable=True, pSync=True,
                      usiConsumerInstanceId=3, uiLinkHandler=valid_link_handler,
                      usiProducerInterfaceId=2, usiProducerInstanceId=2,
                      usiWatchdogTimeoutFactor=16, uiMaxDelay=1000, uiSyncTimeout=500,
                      xSynchronized=dont_care, pNdr=dont_care, uiNbrOfRxBytes=dont_care,
                      xError=True, iStatus=-32761),
            
            # Valid usiWatchdogTimeoutFactor
            test_sets(test_id=21, p_interface_id=2, c_interface_id=3,
                      p_link_handler=valid_link_handler, c_link_handler=valid_link_handler,
                      p_event_time=2000, p_inhibit_time=200,
                      xEnable=True, pSync=True,
                      usiConsumerInstanceId=3, uiLinkHandler=valid_link_handler,
                      usiProducerInterfaceId=2, usiProducerInstanceId=2,
                      usiWatchdogTimeoutFactor=3, uiMaxDelay=1000, uiSyncTimeout=500,
                      xSynchronized=True, pNdr=0, uiNbrOfRxBytes=0,
                      xError=0, iStatus=0),
            test_sets(test_id=22, p_interface_id=2, c_interface_id=3,
                      p_link_handler=valid_link_handler, c_link_handler=valid_link_handler,
                      p_event_time=2000, p_inhibit_time=200,
                      xEnable=True, pSync=True,
                      usiConsumerInstanceId=3, uiLinkHandler=valid_link_handler,
                      usiProducerInterfaceId=2, usiProducerInstanceId=2,
                      usiWatchdogTimeoutFactor=7, uiMaxDelay=1000, uiSyncTimeout=500,
                      xSynchronized=True, pNdr=0, uiNbrOfRxBytes=0,
                      xError=0, iStatus=0),
            test_sets(test_id=23, p_interface_id=2, c_interface_id=3,
                      p_link_handler=valid_link_handler, c_link_handler=valid_link_handler,
                      p_event_time=2000, p_inhibit_time=200,
                      xEnable=True, pSync=True,
                      usiConsumerInstanceId=3, uiLinkHandler=valid_link_handler,
                      usiProducerInterfaceId=2, usiProducerInstanceId=2,
                      usiWatchdogTimeoutFactor=15, uiMaxDelay=1000, uiSyncTimeout=500,
                      xSynchronized=True, pNdr=0, uiNbrOfRxBytes=0,
                      xError=0, iStatus=0),
            
            # uiSyncTimeout = 5
            test_sets(test_id=24, p_interface_id=2, c_interface_id=3,
                      p_link_handler=valid_link_handler, c_link_handler=valid_link_handler,
                      p_event_time=2000, p_inhibit_time=200,
                      xEnable=True, pSync=True,
                      usiConsumerInstanceId=3, uiLinkHandler=valid_link_handler,
                      usiProducerInterfaceId=2, usiProducerInstanceId=2,
                      usiWatchdogTimeoutFactor=2, uiMaxDelay=1000, uiSyncTimeout=5,
                      xSynchronized=True, pNdr=0, uiNbrOfRxBytes=0, xError=0, iStatus=0),
            
            # EC for uiSyncTimeout
            test_sets(test_id=25, p_interface_id=2, c_interface_id=3,
                      p_link_handler=valid_link_handler, c_link_handler=valid_link_handler,
                      p_event_time=2000, p_inhibit_time=200,
                      xEnable=True, pSync=True,
                      usiConsumerInstanceId=3, uiLinkHandler=valid_link_handler,
                      usiProducerInterfaceId=2, usiProducerInstanceId=2,
                      usiWatchdogTimeoutFactor=2, uiMaxDelay=1000, uiSyncTimeout=UINT.MIN,
                      xSynchronized=dont_care, pNdr=0, uiNbrOfRxBytes=0,
                      xError=True, iStatus=-32761),
            
            test_sets(test_id=26, p_interface_id=2, c_interface_id=3,
                      p_link_handler=valid_link_handler, c_link_handler=valid_link_handler,
                      p_event_time=2000, p_inhibit_time=200,
                      xEnable=True, pSync=True,
                      usiConsumerInstanceId=3, uiLinkHandler=valid_link_handler,
                      usiProducerInterfaceId=2, usiProducerInstanceId=2,
                      usiWatchdogTimeoutFactor=2, uiMaxDelay=1000, uiSyncTimeout=UINT.MID,
                      xSynchronized=True, pNdr=0, uiNbrOfRxBytes=0, xError=0, iStatus=0),
            
            test_sets(test_id=27, p_interface_id=2, c_interface_id=3,
                      p_link_handler=valid_link_handler, c_link_handler=valid_link_handler,
                      p_event_time=2000, p_inhibit_time=200,
                      xEnable=True, pSync=True,
                      usiConsumerInstanceId=3, uiLinkHandler=valid_link_handler,
                      usiProducerInterfaceId=2, usiProducerInstanceId=2,
                      usiWatchdogTimeoutFactor=2, uiMaxDelay=1000, uiSyncTimeout=UINT.MAX,
                      xSynchronized=True, pNdr=0, uiNbrOfRxBytes=0, xError=0, iStatus=0),
            
            # EC of uiMaxDelay
            test_sets(test_id=28, p_interface_id=2, c_interface_id=3,
                      p_link_handler=valid_link_handler, c_link_handler=valid_link_handler,
                      p_event_time=2000, p_inhibit_time=200,
                      xEnable=True, pSync=True,
                      usiConsumerInstanceId=3, uiLinkHandler=valid_link_handler,
                      usiProducerInterfaceId=2, usiProducerInstanceId=2,
                      usiWatchdogTimeoutFactor=2, uiMaxDelay=UINT.MIN, uiSyncTimeout=500,
                      xSynchronized=dont_care, pNdr=dont_care, uiNbrOfRxBytes=dont_care,
                      xError=True, iStatus=-32761),
            test_sets(test_id=29, p_interface_id=2, c_interface_id=3,
                      p_link_handler=valid_link_handler, c_link_handler=valid_link_handler,
                      p_event_time=2000, p_inhibit_time=200,
                      xEnable=True, pSync=True,
                      usiConsumerInstanceId=3, uiLinkHandler=valid_link_handler,
                      usiProducerInterfaceId=2, usiProducerInstanceId=2,
                      usiWatchdogTimeoutFactor=2, uiMaxDelay=UINT.MID, uiSyncTimeout=500,
                      xSynchronized=True, pNdr=0, uiNbrOfRxBytes=0,
                      xError=0, iStatus=0),
            test_sets(test_id=30, p_interface_id=2, c_interface_id=3,
                      p_link_handler=valid_link_handler, c_link_handler=valid_link_handler,
                      p_event_time=2000, p_inhibit_time=200,
                      xEnable=True, pSync=True,
                      usiConsumerInstanceId=3, uiLinkHandler=valid_link_handler,
                      usiProducerInterfaceId=2, usiProducerInstanceId=2,
                      usiWatchdogTimeoutFactor=2, uiMaxDelay=UINT.MAX, uiSyncTimeout=500,
                      xSynchronized=True, pNdr=0, uiNbrOfRxBytes=0,
                      xError=0, iStatus=0),
        )
        
        # Prepare test data --------------------------------------------------------------------------------------------
        test_data_sent = [10, 20, 30, 40, 50]
        
        for step_id, test_data in enumerate(test_data_set):
            
            if (test_data.p_link_handler == valid_link_handler) and (test_data.p_link_handler == valid_link_handler):
                p_link_handler, c_link_handler = self.init_SafetyCom_for_producer_and_consumer(
                    p_interface_id=test_data.p_interface_id, c_interface_id=test_data.c_interface_id)
            if test_data.c_link_handler != valid_link_handler:
                p_link_handler, c_link_handler = self.init_SafetyCom_for_producer_and_consumer(
                    p_interface_id=test_data.p_interface_id, c_interface_id=test_data.c_interface_id)
                c_link_handler = 0
            if test_data.p_link_handler != valid_link_handler:
                p_link_handler, c_link_handler = self.init_SafetyCom_for_producer_and_consumer(
                    p_interface_id=test_data.p_interface_id, c_interface_id=test_data.c_interface_id)
                p_link_handler = 0
            
            # Define a producer communication instance
            io_data_producer = SCOM_X_PRODUCER_IO_T(xEnable=True, usiProducerInstanceId=2,
                                                    uiLinkHandler=p_link_handler,
                                                    uiEventTime=test_data.p_event_time,
                                                    uiInhibitTime=test_data.p_inhibit_time)
            self.SCOM_X_PRODUCER(io_data=io_data_producer, test_data=test_data_sent, cycles=2,
                                 step='S202.0.{}'.format(test_data.test_id))
        
        # Act-----------------------------------------------------------------------------------------------------------
            
            # Define a consumer communication instance
            io_data_consumer = SCOM_X_CONSUMER_IO_T(xEnable=False, pSync=False,
                                                    usiConsumerInstanceId=test_data.usiConsumerInstanceId,
                                                    uiLinkHandler=c_link_handler,
                                                    usiProducerInterfaceId=test_data.usiProducerInterfaceId,
                                                    usiProducerInstanceId=test_data.usiProducerInstanceId,
                                                    usiWatchdogTimeoutFactor=test_data.usiWatchdogTimeoutFactor,
                                                    uiMaxDelay=test_data.uiMaxDelay,
                                                    uiSyncTimeout=test_data.uiSyncTimeout)
            
            if test_data.xEnable:
                io_data_consumer.xEnable = True
            
            self.SCOM_X_CONSUMER(io_data=io_data_consumer, cycles=1, step='S202.1.{}'.format(test_data.test_id))
            
            if test_data.pSync:
                io_data_consumer.pSync = True
            
            self.SCOM_X_CONSUMER(io_data=io_data_consumer, cycles=1, step='S202.2.{}'.format(test_data.test_id))
        # Assert--------------------------------------------------------------------------------------------------------
            if test_data.xError or test_data.iStatus < 0:
                self.assertEqual(io_data_consumer.xError, test_data.xError,
                                 msg='S202.3.{}: SCOM_X_CONSUMER() no error occurred'.format(test_data.test_id))
                self.assertEqual(io_data_consumer.iStatus, test_data.iStatus,
                                 msg='S202.4.{}: SCOM_X_CONSUMER() no error occurred'.format(test_data.test_id))
                return
        # --------------------------------------------------------------------------------------------------------------
            # Wait for consumer to synchronized with producer
            start_time = time.time()
            while io_data_consumer.xSynchronized == 0:
                self.SCOM_X_CONSUMER(io_data=io_data_consumer, cycles=1, step='S202.5'.format(test_data.test_id))
                self.assertLess(time.time()-start_time, 30,
                                msg='S202.6.{}: SCOM_X_CONSUMER() failed to Synchronize'.format(test_data.test_id))
            
            # Receive data from producer
            start_time = time.time()
            while io_data_consumer.pNdr == 0:
                received_data = self.SCOM_X_CONSUMER(io_data=io_data_consumer, cycles=1,
                                                     step='S202.7.{}'.format(test_data.test_id))
                self.assertLess(time.time()-start_time, 30,
                                msg='S202.8.{}: SCOM_X_CONSUMER() failed to Receive data'.format(test_data.test_id))
        
        # Assert--------------------------------------------------------------------------------------------------------
            
            self.assertEqual(io_data_producer.xError, False,
                             msg='S202.9.{}: SCOM_X_PRODUCER() Error has occurred'.format(test_data.test_id))
            self.assertGreaterEqual(io_data_producer.iStatus, 0,
                                    msg='S202.10.{}: SCOM_X_PRODUCER() Error has occurred'.format(test_data.test_id))
            
            self.assertEqual(io_data_consumer.xError, False,
                             msg='S202.11.{}: SCOM_X_CONSUMER() Error has occurred'.format(test_data.test_id))
            self.assertGreaterEqual(io_data_consumer.iStatus, 0,
                                    msg='S202.12.{}: SCOM_X_CONSUMER() Error has occurred'.format(test_data.test_id))
            self.assertEqual(io_data_consumer.xSynchronized, True,
                             msg='S202.13.{}: SCOM_X_CONSUMER() \
                             not synchronized with Producer'.format(test_data.test_id))
            self.assertEqual(io_data_consumer.pNdr, True,
                             msg='S202.14.{}: SCOM_X_CONSUMER() : Failed to receive new data'.format(test_data.test_id))
            if io_data_consumer.pNdr:
                # In this test Number received bytes are always 255.
                # As input to consumer block memory block used in CAP is of 255 bytes.
                self.assertNotEqual(io_data_consumer.uiNbrOfRxBytes, 0,
                                    msg='S202.15.{}: SCOM_X_CONSUMER(): \
                                    Number of received bytes did not matched'.format(test_data.test_id))
            self.assertEqual(test_data_sent, received_data[0:5:], msg='S202.16.{}: \
            Sent and Received data mismatched'.format(test_data.test_id))
        
        # Clean up -----------------------------------------------------------------------------------------------------
            self.close_SafetyCom_for_producer_and_consumer()
            self.deactivate_producer()
            self.deactivate_consumer()
        # --------------------------------------------------------------------------------------------------------------


class TestScenario_mSCOMx(object):
    """
    \page Scenarios Test-Scenarios
    - Test_mSCOMx.TestScenario_mSCOMx.all
    """
    def __init__(self):
        pass
    
    @staticmethod
    def functional(**kwargs):
        """
        <table>
                <tr><td><b> Scenario Name </b></td><td> Test_mSCOMx.TestScenario_mSCOMx.functional </td></tr>
                <tr><td><b> Description   </b></td><td> Tests the functionality of the mSCOM MLib </td></tr>
                <tr><td><b> Sequence      </b></td><td>
                                                        - Test_mSCOMx.TestCase_mSCOMx
                                             </td></tr>
                <tr><td><b> Comments      </b></td><td> Only the functional test steps of the listed TestCases are executed
                                             </td></tr>
        </table>
        """
        suite = unittest.TestSuite()
        suite.addTest(TestCase_mSCOMx('test_001_SCOM_X_LAN_CH_INIT', **kwargs))
        suite.addTest(TestCase_mSCOMx('test_002_SCOM_X_CAN_INIT', **kwargs))
        suite.addTest(TestCase_mSCOMx('test_003_SCOM_X_CPL_CO_INIT', **kwargs))
        # ToDo Reserve Test case name, test is not implemented yet, remove this comment once implemented.
        # suite.addTest(TestCase_mSCOMx('test_004_SCOM_X_CPL_CBUS_INIT', **kwargs))
        suite.addTest(TestCase_mSCOMx('test_005_local_LAN_instance_SCOM_X_LAN_CH_INIT', **kwargs))
        suite.addTest(TestCase_mSCOMx('test_006_local_CAN_instance_SCOM_X_CPL_CO_INIT', **kwargs))
        suite.addTest(TestCase_mSCOMx('test_101_ProducerConsumer', **kwargs))
        suite.addTest(TestCase_mSCOMx('test_102_maximum_number_of_producer_instance', **kwargs))
        suite.addTest(TestCase_mSCOMx('test_103_maximum_number_of_consumer_instance', **kwargs))
        suite.addTest(TestCase_mSCOMx('test_104_ClientServer', **kwargs))
        suite.addTest(TestCase_mSCOMx('test_105_maximum_number_of_server_instance', **kwargs))
        suite.addTest(TestCase_mSCOMx('test_106_maximum_number_of_client_instance', **kwargs))
        suite.addTest(TestCase_mSCOMx('test_201_SCOM_X_PRODUCER', **kwargs))
        suite.addTest(TestCase_mSCOMx('test_202_SCOM_X_CONSUMER', **kwargs))
        suite.addTest(TestCase_mSCOMx('test_301_SCOM_X_SERVER', **kwargs))
        suite.addTest(TestCase_mSCOMx('test_302_SCOM_X_CLIENT', **kwargs))
        xmlrunner.XMLTestRunner(verbosity=2).run(unittest.TestSuite(suite))
    
    @staticmethod
    def negative(**kwargs):
        
        suite = unittest.TestSuite()
        suite.addTest(TestCase_mSCOMx('test_1001_negative_SCOM_X_LAN_CH_INIT', **kwargs))
        suite.addTest(TestCase_mSCOMx('test_1002_negative_SCOM_X_CPL_CO_INIT', **kwargs))
        xmlrunner.XMLTestRunner(verbosity=2).run(unittest.TestSuite(suite))
    
    @staticmethod
    def all(**kwargs):
        """
        <table>
                <tr><td><b> Scenario Name </b></td><td> Test_mSCOMx.TestScenario_mSCOMx.all </td></tr>
                <tr><td><b> Description   </b></td><td> Tests the whole functionality of the mSCOMx  </td></tr>
                <tr><td><b> Sequence      </b></td><td>
                                                        - Test_mSCOMx.TestScenario_mSCOMx.functional
                                                        - Test_mSCOMx.TestScenario_mSCOMx.negative
                                            </td></tr>
                <tr><td><b> Comments      </b></td><td>  </td></tr>
        </table>
        """
        TestCase_mSCOMx.__name__ = 'TestCase_mSCOMx_' + kwargs.get('env_name')
        firmware_loc_file_path = kwargs.get('mos_hex_path').replace('.hex', '.loc')
        getFirmwareVersion(firmware_loc_file_path, print_versions=True)
        suite = unittest.TestSuite()
        suite.addTest(TestCase_mSCOMx('prepare_sut', **kwargs))
        xmlrunner.XMLTestRunner(verbosity=2).run(unittest.TestSuite(suite))
        
        TestScenario_mSCOMx.functional(**kwargs)
        TestScenario_mSCOMx.negative(**kwargs)
