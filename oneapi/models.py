# -*- coding: utf-8 -*-

import object as mod_object
import utils as mod_utils

# ----------------------------------------------------------------------------------------------------
# Generic objects:
# ----------------------------------------------------------------------------------------------------

class OneApiError(mod_object.AbstractModel):

    message_id = [ mod_object.FieldConverter('requestError.serviceException.messageId'), mod_object.FieldConverter('requestError.policyException.messageId') ]
    text = [ mod_object.FieldConverter('requestError.serviceException.text'), mod_object.FieldConverter('requestError.policyException.text') ]
    variables = [ mod_object.FieldConverter('requestError.serviceException.variables'), mod_object.FieldConverter('requestError.policyException.variables') ]

    def __init__(self):
        mod_object.AbstractModel.__init__(self)

class GenericObject(mod_object.AbstractModel):
    """ May be used where only is_success() is important. """

    def __init__(self):
        mod_object.AbstractModel.__init__(self)

# ----------------------------------------------------------------------------------------------------
# SMS message models:
# ----------------------------------------------------------------------------------------------------

class SMSRequest(mod_object.AbstractModel):

    sender_address = mod_object.FieldConverter('senderAddress')
    sender_name = mod_object.FieldConverter('senderName')
    message = mod_object.FieldConverter()
    address = mod_object.FieldConverter()

    # Used later for querying about the message status.
    client_correlator = mod_object.FieldConverter('clientCorrelator')

    # If not empty -- this is the url where the delivery notification will be pushed. 
    # 
    # If empty -- the delivery notification may be queried using the 
    # clientCorrelator string.
    notify_url = mod_object.FieldConverter('notifyURL')

    # Artibtrary string that will be pushed if notifyURL is set.
    callback_data = mod_object.FieldConverter('callbackData')

    def __init__(self, sender_address=None, message=None, address=None, client_correlator=None,
                 notify_url=None, sender_name=None, callback_data=None):
        mod_object.AbstractModel.__init__(self)

        self.sender_address = sender_address
        self.message = message
        self.address = address
        self.client_correlator = client_correlator
        self.notify_url = notify_url
        self.sender_name = sender_name
        self.callback_data = callback_data

# ----------------------------------------------------------------------------------------------------

class ResourceReference(mod_object.AbstractModel):

    # The client correlator for this message. This value may be used to query 
    # for message status later.
    client_correlator = mod_object.LastPartOfUrlFieldConverter('resourceReference.resourceURL')

    def __init__(self, client_correlator=None):
        mod_object.AbstractModel.__init__(self)

        self.client_correlator = client_correlator

# ----------------------------------------------------------------------------------------------------

class DeliveryInfo(mod_object.AbstractModel):

    delivery_status = mod_object.FieldConverter('deliveryStatus')

    def __init__(self):
        mod_object.AbstractModel.__init__(self)

# ----------------------------------------------------------------------------------------------------

class DeliveryInfoList(mod_object.AbstractModel):

    delivery_info = mod_object.ObjectsListFieldConverter(DeliveryInfo, json_field_name='deliveryInfoList.deliveryInfo')

    def __init__(self):
        mod_object.AbstractModel.__init__(self)

# ----------------------------------------------------------------------------------------------------
# HLR models:
# ----------------------------------------------------------------------------------------------------


class ServingMccMnc(mod_object.AbstractModel):

    mcc = mod_object.FieldConverter('mcc')
    mnc = mod_object.FieldConverter('mnc')

    def __init__(self):
        mod_object.AbstractModel.__init__(self)

class TerminalRoamingExtendedData(mod_object.AbstractModel):

    destination_address = mod_object.FieldConverter('destinationAddress')
    status_id = mod_object.FieldConverter('statusId')
    done_time = mod_object.FieldConverter('doneTime')
    price_per_message = mod_object.FieldConverter('pricePerMessage')
    mcc_mnc = mod_object.FieldConverter('mccMnc')
    serving_msc = mod_object.FieldConverter('servingMsc')
    censored_serving_msc = mod_object.FieldConverter('censoredServingMsc')
    gsm_error_code = mod_object.FieldConverter('gsmErrorCode')
    original_network_name = mod_object.FieldConverter('originalNetworkName')
    ported_network_name = mod_object.FieldConverter('portedNetworkName')
    serving_hlr = mod_object.FieldConverter('servingHlr')
    imsi = mod_object.FieldConverter('imsi')
    original_network_prefix = mod_object.FieldConverter('originalNetworkPrefix')
    original_country_prefix = mod_object.FieldConverter('originalCountryPrefix')
    original_country_name = mod_object.FieldConverter('originalCountryName')
    is_number_ported = mod_object.FieldConverter('isNumberPorted')
    ported_network_prefix = mod_object.FieldConverter('portedNetworkPrefix')
    ported_country_prefix = mod_object.FieldConverter('portedCountryPrefix')
    ported_country_name = mod_object.FieldConverter('portedCountryName')
    number_in_roaming = mod_object.FieldConverter('numberInRoaming')

    def __init__(self):
        mod_object.AbstractModel.__init__(self)

class TerminalRoamingStatus(mod_object.AbstractModel):

    servingMccMnc = mod_object.ObjectFieldConverter(ServingMccMnc, 'servingMccMnc')
    address = mod_object.FieldConverter()
    currentRoaming = mod_object.FieldConverter('currentRoaming')
    resourceURL = mod_object.FieldConverter('resourceURL')
    retrievalStatus = mod_object.FieldConverter('retrievalStatus')
    callbackData = mod_object.FieldConverter('callbackData')
    extendedData = mod_object.ObjectFieldConverter(TerminalRoamingExtendedData, 'extendedData')

    def __init__(self):
        mod_object.AbstractModel.__init__(self)

# ----------------------------------------------------------------------------------------------------
# MO models:

class InboundSmsMessage(mod_object.AbstractModel):

    date_time = mod_object.FieldConverter('dateTime')
    destination_address = mod_object.FieldConverter('destinationAddress')
    message_id = mod_object.FieldConverter('messageId')
    message = mod_object.FieldConverter('message')
    resource_url = mod_object.FieldConverter('resourceURL')
    sender_address = mod_object.FieldConverter('senderAddress')

    def __init__(self):
        mod_object.AbstractModel.__init__(self)

class InboundSmsMessages(mod_object.AbstractModel):

    inbound_sms_message = mod_object.ObjectsListFieldConverter(InboundSmsMessage, 'inboundSMSMessageList.inboundSMSMessage')
    number_of_messages_in_this_batch = mod_object.FieldConverter('inboundSMSMessageList.numberOfMessagesInThisBatch')
    total_number_of_pending_messages = mod_object.FieldConverter('inboundSMSMessageList.totalNumberOfPendingMessages')
    callback_data = mod_object.FieldConverter('inboundSMSMessageList.callbackData')

    def __init__(self):
        mod_object.AbstractModel.__init__(self)

# ----------------------------------------------------------------------------------------------------
