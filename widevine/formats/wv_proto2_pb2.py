# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: wv_proto2.proto

"""Generated protocol buffer code."""

from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()

DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0fwv_proto2.proto\"\xe7\x05\n\x14\x43lientIdentification\x12-\n\x04Type\x18\x01 \x02(\x0e\x32\x1f.ClientIdentification.TokenType\x12\'\n\x05Token\x18\x02 \x01(\x0b\x32\x18.SignedDeviceCertificate\x12\x33\n\nClientInfo\x18\x03 \x03(\x0b\x32\x1f.ClientIdentification.NameValue\x12\x1b\n\x13ProviderClientToken\x18\x04 \x01(\x0c\x12\x16\n\x0eLicenseCounter\x18\x05 \x01(\r\x12\x45\n\x13_ClientCapabilities\x18\x06 \x01(\x0b\x32(.ClientIdentification.ClientCapabilities\x12 \n\x0b_FileHashes\x18\x07 \x01(\x0b\x32\x0b.FileHashes\x1a(\n\tNameValue\x12\x0c\n\x04Name\x18\x01 \x02(\t\x12\r\n\x05Value\x18\x02 \x02(\t\x1a\xa4\x02\n\x12\x43lientCapabilities\x12\x13\n\x0b\x43lientToken\x18\x01 \x01(\r\x12\x14\n\x0cSessionToken\x18\x02 \x01(\r\x12\"\n\x1aVideoResolutionConstraints\x18\x03 \x01(\r\x12L\n\x0eMaxHdcpVersion\x18\x04 \x01(\x0e\x32\x34.ClientIdentification.ClientCapabilities.HdcpVersion\x12\x1b\n\x13OemCryptoApiVersion\x18\x05 \x01(\r\"T\n\x0bHdcpVersion\x12\r\n\tHDCP_NONE\x10\x00\x12\x0b\n\x07HDCP_V1\x10\x01\x12\x0b\n\x07HDCP_V2\x10\x02\x12\r\n\tHDCP_V2_1\x10\x03\x12\r\n\tHDCP_V2_2\x10\x04\"S\n\tTokenType\x12\n\n\x06KEYBOX\x10\x00\x12\x16\n\x12\x44\x45VICE_CERTIFICATE\x10\x01\x12\"\n\x1eREMOTE_ATTESTATION_CERTIFICATE\x10\x02\"\x9b\x02\n\x11\x44\x65viceCertificate\x12\x30\n\x04Type\x18\x01 \x02(\x0e\x32\".DeviceCertificate.CertificateType\x12\x14\n\x0cSerialNumber\x18\x02 \x01(\x0c\x12\x1b\n\x13\x43reationTimeSeconds\x18\x03 \x01(\r\x12\x11\n\tPublicKey\x18\x04 \x01(\x0c\x12\x10\n\x08SystemId\x18\x05 \x01(\r\x12\x1c\n\x14TestDeviceDeprecated\x18\x06 \x01(\r\x12\x11\n\tServiceId\x18\x07 \x01(\x0c\"K\n\x0f\x43\x65rtificateType\x12\x08\n\x04ROOT\x10\x00\x12\x10\n\x0cINTERMEDIATE\x10\x01\x12\x0f\n\x0bUSER_DEVICE\x10\x02\x12\x0b\n\x07SERVICE\x10\x03\"\xc4\x01\n\x17\x44\x65viceCertificateStatus\x12\x14\n\x0cSerialNumber\x18\x01 \x01(\x0c\x12:\n\x06Status\x18\x02 \x01(\x0e\x32*.DeviceCertificateStatus.CertificateStatus\x12*\n\nDeviceInfo\x18\x04 \x01(\x0b\x32\x16.ProvisionedDeviceInfo\"+\n\x11\x43\x65rtificateStatus\x12\t\n\x05VALID\x10\x00\x12\x0b\n\x07REVOKED\x10\x01\"o\n\x1b\x44\x65viceCertificateStatusList\x12\x1b\n\x13\x43reationTimeSeconds\x18\x01 \x01(\r\x12\x33\n\x11\x43\x65rtificateStatus\x18\x02 \x03(\x0b\x32\x18.DeviceCertificateStatus\"\xaf\x01\n\x1d\x45ncryptedClientIdentification\x12\x11\n\tServiceId\x18\x01 \x02(\t\x12&\n\x1eServiceCertificateSerialNumber\x18\x02 \x01(\x0c\x12\x19\n\x11\x45ncryptedClientId\x18\x03 \x02(\x0c\x12\x1b\n\x13\x45ncryptedClientIdIv\x18\x04 \x02(\x0c\x12\x1b\n\x13\x45ncryptedPrivacyKey\x18\x05 \x02(\x0c\"\x9c\x01\n\x15LicenseIdentification\x12\x11\n\tRequestId\x18\x01 \x01(\x0c\x12\x11\n\tSessionId\x18\x02 \x01(\x0c\x12\x12\n\nPurchaseId\x18\x03 \x01(\x0c\x12\x1a\n\x04Type\x18\x04 \x01(\x0e\x32\x0c.LicenseType\x12\x0f\n\x07Version\x18\x05 \x01(\r\x12\x1c\n\x14ProviderSessionToken\x18\x06 \x01(\x0c\"\xa1\x0e\n\x07License\x12\"\n\x02Id\x18\x01 \x01(\x0b\x32\x16.LicenseIdentification\x12 \n\x07_Policy\x18\x02 \x01(\x0b\x32\x0f.License.Policy\x12\"\n\x03Key\x18\x03 \x03(\x0b\x32\x15.License.KeyContainer\x12\x18\n\x10LicenseStartTime\x18\x04 \x01(\r\x12!\n\x19RemoteAttestationVerified\x18\x05 \x01(\r\x12\x1b\n\x13ProviderClientToken\x18\x06 \x01(\x0c\x12\x18\n\x10ProtectionScheme\x18\x07 \x01(\r\x1a\xbb\x02\n\x06Policy\x12\x0f\n\x07\x43\x61nPlay\x18\x01 \x01(\x08\x12\x12\n\nCanPersist\x18\x02 \x01(\x08\x12\x10\n\x08\x43\x61nRenew\x18\x03 \x01(\x08\x12\x1d\n\x15RentalDurationSeconds\x18\x04 \x01(\r\x12\x1f\n\x17PlaybackDurationSeconds\x18\x05 \x01(\r\x12\x1e\n\x16LicenseDurationSeconds\x18\x06 \x01(\r\x12&\n\x1eRenewalRecoveryDurationSeconds\x18\x07 \x01(\r\x12\x18\n\x10RenewalServerUrl\x18\x08 \x01(\t\x12\x1b\n\x13RenewalDelaySeconds\x18\t \x01(\r\x12#\n\x1bRenewalRetryIntervalSeconds\x18\n \x01(\r\x12\x16\n\x0eRenewWithUsage\x18\x0b \x01(\x08\x1a\xf9\t\n\x0cKeyContainer\x12\n\n\x02Id\x18\x01 \x01(\x0c\x12\n\n\x02Iv\x18\x02 \x01(\x0c\x12\x0b\n\x03Key\x18\x03 \x01(\x0c\x12+\n\x04Type\x18\x04 \x01(\x0e\x32\x1d.License.KeyContainer.KeyType\x12\x32\n\x05Level\x18\x05 \x01(\x0e\x32#.License.KeyContainer.SecurityLevel\x12\x42\n\x12RequiredProtection\x18\x06 \x01(\x0b\x32&.License.KeyContainer.OutputProtection\x12\x43\n\x13RequestedProtection\x18\x07 \x01(\x0b\x32&.License.KeyContainer.OutputProtection\x12\x35\n\x0b_KeyControl\x18\x08 \x01(\x0b\x32 .License.KeyContainer.KeyControl\x12[\n\x1e_OperatorSessionKeyPermissions\x18\t \x01(\x0b\x32\x33.License.KeyContainer.OperatorSessionKeyPermissions\x12S\n\x1aVideoResolutionConstraints\x18\n \x03(\x0b\x32/.License.KeyContainer.VideoResolutionConstraint\x1a\xdb\x01\n\x10OutputProtection\x12\x42\n\x04Hdcp\x18\x01 \x01(\x0e\x32\x34.ClientIdentification.ClientCapabilities.HdcpVersion\x12>\n\tCgmsFlags\x18\x02 \x01(\x0e\x32+.License.KeyContainer.OutputProtection.CGMS\"C\n\x04\x43GMS\x12\r\n\tCOPY_FREE\x10\x00\x12\r\n\tCOPY_ONCE\x10\x02\x12\x0e\n\nCOPY_NEVER\x10\x03\x12\r\n\tCGMS_NONE\x10*\x1a\x31\n\nKeyControl\x12\x17\n\x0fKeyControlBlock\x18\x01 \x02(\x0c\x12\n\n\x02Iv\x18\x02 \x01(\x0c\x1a|\n\x1dOperatorSessionKeyPermissions\x12\x14\n\x0c\x41llowEncrypt\x18\x01 \x01(\r\x12\x14\n\x0c\x41llowDecrypt\x18\x02 \x01(\r\x12\x11\n\tAllowSign\x18\x03 \x01(\r\x12\x1c\n\x14\x41llowSignatureVerify\x18\x04 \x01(\r\x1a\x99\x01\n\x19VideoResolutionConstraint\x12\x1b\n\x13MinResolutionPixels\x18\x01 \x01(\r\x12\x1b\n\x13MaxResolutionPixels\x18\x02 \x01(\r\x12\x42\n\x12RequiredProtection\x18\x03 \x01(\x0b\x32&.License.KeyContainer.OutputProtection\"J\n\x07KeyType\x12\x0b\n\x07SIGNING\x10\x01\x12\x0b\n\x07\x43ONTENT\x10\x02\x12\x0f\n\x0bKEY_CONTROL\x10\x03\x12\x14\n\x10OPERATOR_SESSION\x10\x04\"z\n\rSecurityLevel\x12\x14\n\x10SW_SECURE_CRYPTO\x10\x01\x12\x14\n\x10SW_SECURE_DECODE\x10\x02\x12\x14\n\x10HW_SECURE_CRYPTO\x10\x03\x12\x14\n\x10HW_SECURE_DECODE\x10\x04\x12\x11\n\rHW_SECURE_ALL\x10\x05\"\x98\x01\n\x0cLicenseError\x12&\n\tErrorCode\x18\x01 \x01(\x0e\x32\x13.LicenseError.Error\"`\n\x05\x45rror\x12\x1e\n\x1aINVALID_DEVICE_CERTIFICATE\x10\x01\x12\x1e\n\x1aREVOKED_DEVICE_CERTIFICATE\x10\x02\x12\x17\n\x13SERVICE_UNAVAILABLE\x10\x03\"\xac\x07\n\x0eLicenseRequest\x12\'\n\x08\x43lientId\x18\x01 \x01(\x0b\x32\x15.ClientIdentification\x12\x38\n\tContentId\x18\x02 \x01(\x0b\x32%.LicenseRequest.ContentIdentification\x12)\n\x04Type\x18\x03 \x01(\x0e\x32\x1b.LicenseRequest.RequestType\x12\x13\n\x0bRequestTime\x18\x04 \x01(\r\x12!\n\x19KeyControlNonceDeprecated\x18\x05 \x01(\x0c\x12)\n\x0fProtocolVersion\x18\x06 \x01(\x0e\x32\x10.ProtocolVersion\x12\x17\n\x0fKeyControlNonce\x18\x07 \x01(\r\x12\x39\n\x11\x45ncryptedClientId\x18\x08 \x01(\x0b\x32\x1e.EncryptedClientIdentification\x1a\xa2\x04\n\x15\x43ontentIdentification\x12:\n\x06\x43\x65ncId\x18\x01 \x01(\x0b\x32*.LicenseRequest.ContentIdentification.CENC\x12:\n\x06WebmId\x18\x02 \x01(\x0b\x32*.LicenseRequest.ContentIdentification.WebM\x12\x46\n\x07License\x18\x03 \x01(\x0b\x32\x35.LicenseRequest.ContentIdentification.ExistingLicense\x1a_\n\x04\x43\x45NC\x12!\n\x04Pssh\x18\x01 \x01(\x0b\x32\x13.WidevineCencHeader\x12!\n\x0bLicenseType\x18\x02 \x01(\x0e\x32\x0c.LicenseType\x12\x11\n\tRequestId\x18\x03 \x01(\x0c\x1aL\n\x04WebM\x12\x0e\n\x06Header\x18\x01 \x01(\x0c\x12!\n\x0bLicenseType\x18\x02 \x01(\x0e\x32\x0c.LicenseType\x12\x11\n\tRequestId\x18\x03 \x01(\x0c\x1a\x99\x01\n\x0f\x45xistingLicense\x12)\n\tLicenseId\x18\x01 \x01(\x0b\x32\x16.LicenseIdentification\x12\x1b\n\x13SecondsSinceStarted\x18\x02 \x01(\r\x12\x1e\n\x16SecondsSinceLastPlayed\x18\x03 \x01(\r\x12\x1e\n\x16SessionUsageTableEntry\x18\x04 \x01(\x0c\"0\n\x0bRequestType\x12\x07\n\x03NEW\x10\x01\x12\x0b\n\x07RENEWAL\x10\x02\x12\x0b\n\x07RELEASE\x10\x03\"\xa9\x07\n\x11LicenseRequestRaw\x12\'\n\x08\x43lientId\x18\x01 \x01(\x0b\x32\x15.ClientIdentification\x12;\n\tContentId\x18\x02 \x01(\x0b\x32(.LicenseRequestRaw.ContentIdentification\x12,\n\x04Type\x18\x03 \x01(\x0e\x32\x1e.LicenseRequestRaw.RequestType\x12\x13\n\x0bRequestTime\x18\x04 \x01(\r\x12!\n\x19KeyControlNonceDeprecated\x18\x05 \x01(\x0c\x12)\n\x0fProtocolVersion\x18\x06 \x01(\x0e\x32\x10.ProtocolVersion\x12\x17\n\x0fKeyControlNonce\x18\x07 \x01(\r\x12\x39\n\x11\x45ncryptedClientId\x18\x08 \x01(\x0b\x32\x1e.EncryptedClientIdentification\x1a\x96\x04\n\x15\x43ontentIdentification\x12=\n\x06\x43\x65ncId\x18\x01 \x01(\x0b\x32-.LicenseRequestRaw.ContentIdentification.CENC\x12=\n\x06WebmId\x18\x02 \x01(\x0b\x32-.LicenseRequestRaw.ContentIdentification.WebM\x12I\n\x07License\x18\x03 \x01(\x0b\x32\x38.LicenseRequestRaw.ContentIdentification.ExistingLicense\x1aJ\n\x04\x43\x45NC\x12\x0c\n\x04Pssh\x18\x01 \x01(\x0c\x12!\n\x0bLicenseType\x18\x02 \x01(\x0e\x32\x0c.LicenseType\x12\x11\n\tRequestId\x18\x03 \x01(\x0c\x1aL\n\x04WebM\x12\x0e\n\x06Header\x18\x01 \x01(\x0c\x12!\n\x0bLicenseType\x18\x02 \x01(\x0e\x32\x0c.LicenseType\x12\x11\n\tRequestId\x18\x03 \x01(\x0c\x1a\x99\x01\n\x0f\x45xistingLicense\x12)\n\tLicenseId\x18\x01 \x01(\x0b\x32\x16.LicenseIdentification\x12\x1b\n\x13SecondsSinceStarted\x18\x02 \x01(\r\x12\x1e\n\x16SecondsSinceLastPlayed\x18\x03 \x01(\r\x12\x1e\n\x16SessionUsageTableEntry\x18\x04 \x01(\x0c\"0\n\x0bRequestType\x12\x07\n\x03NEW\x10\x01\x12\x0b\n\x07RENEWAL\x10\x02\x12\x0b\n\x07RELEASE\x10\x03\"\xa6\x02\n\x15ProvisionedDeviceInfo\x12\x10\n\x08SystemId\x18\x01 \x01(\r\x12\x0b\n\x03Soc\x18\x02 \x01(\t\x12\x14\n\x0cManufacturer\x18\x03 \x01(\t\x12\r\n\x05Model\x18\x04 \x01(\t\x12\x12\n\nDeviceType\x18\x05 \x01(\t\x12\x11\n\tModelYear\x18\x06 \x01(\r\x12=\n\rSecurityLevel\x18\x07 \x01(\x0e\x32&.ProvisionedDeviceInfo.WvSecurityLevel\x12\x12\n\nTestDevice\x18\x08 \x01(\r\"O\n\x0fWvSecurityLevel\x12\x15\n\x11LEVEL_UNSPECIFIED\x10\x00\x12\x0b\n\x07LEVEL_1\x10\x01\x12\x0b\n\x07LEVEL_2\x10\x02\x12\x0b\n\x07LEVEL_3\x10\x03\"\x15\n\x13ProvisioningOptions\"\x15\n\x13ProvisioningRequest\"\x16\n\x14ProvisioningResponse\"i\n\x11RemoteAttestation\x12\x33\n\x0b\x43\x65rtificate\x18\x01 \x01(\x0b\x32\x1e.EncryptedClientIdentification\x12\x0c\n\x04Salt\x18\x02 \x01(\t\x12\x11\n\tSignature\x18\x03 \x01(\t\"\r\n\x0bSessionInit\"\x0e\n\x0cSessionState\"\x1d\n\x1bSignedCertificateStatusList\"\x86\x01\n\x17SignedDeviceCertificate\x12.\n\x12_DeviceCertificate\x18\x01 \x01(\x0b\x32\x12.DeviceCertificate\x12\x11\n\tSignature\x18\x02 \x01(\x0c\x12(\n\x06Signer\x18\x03 \x01(\x0b\x32\x18.SignedDeviceCertificate\"\x1b\n\x19SignedProvisioningMessage\"\x9b\x02\n\rSignedMessage\x12(\n\x04Type\x18\x01 \x01(\x0e\x32\x1a.SignedMessage.MessageType\x12\x0b\n\x03Msg\x18\x02 \x01(\x0c\x12\x11\n\tSignature\x18\x03 \x01(\x0c\x12\x12\n\nSessionKey\x18\x04 \x01(\x0c\x12-\n\x11RemoteAttestation\x18\x05 \x01(\x0b\x32\x12.RemoteAttestation\"}\n\x0bMessageType\x12\x13\n\x0fLICENSE_REQUEST\x10\x01\x12\x0b\n\x07LICENSE\x10\x02\x12\x12\n\x0e\x45RROR_RESPONSE\x10\x03\x12\x1f\n\x1bSERVICE_CERTIFICATE_REQUEST\x10\x04\x12\x17\n\x13SERVICE_CERTIFICATE\x10\x05\"\xc5\x02\n\x12WidevineCencHeader\x12\x30\n\talgorithm\x18\x01 \x01(\x0e\x32\x1d.WidevineCencHeader.Algorithm\x12\x0e\n\x06key_id\x18\x02 \x03(\x0c\x12\x10\n\x08provider\x18\x03 \x01(\t\x12\x12\n\ncontent_id\x18\x04 \x01(\x0c\x12\x1d\n\x15track_type_deprecated\x18\x05 \x01(\t\x12\x0e\n\x06policy\x18\x06 \x01(\t\x12\x1b\n\x13\x63rypto_period_index\x18\x07 \x01(\r\x12\x17\n\x0fgrouped_license\x18\x08 \x01(\x0c\x12\x19\n\x11protection_scheme\x18\t \x01(\r\x12\x1d\n\x15\x63rypto_period_seconds\x18\n \x01(\r\"(\n\tAlgorithm\x12\x0f\n\x0bUNENCRYPTED\x10\x00\x12\n\n\x06\x41\x45SCTR\x10\x01\"\xba\x02\n\x14SignedLicenseRequest\x12/\n\x04Type\x18\x01 \x01(\x0e\x32!.SignedLicenseRequest.MessageType\x12\x1c\n\x03Msg\x18\x02 \x01(\x0b\x32\x0f.LicenseRequest\x12\x11\n\tSignature\x18\x03 \x01(\x0c\x12\x12\n\nSessionKey\x18\x04 \x01(\x0c\x12-\n\x11RemoteAttestation\x18\x05 \x01(\x0b\x32\x12.RemoteAttestation\"}\n\x0bMessageType\x12\x13\n\x0fLICENSE_REQUEST\x10\x01\x12\x0b\n\x07LICENSE\x10\x02\x12\x12\n\x0e\x45RROR_RESPONSE\x10\x03\x12\x1f\n\x1bSERVICE_CERTIFICATE_REQUEST\x10\x04\x12\x17\n\x13SERVICE_CERTIFICATE\x10\x05\"\xc3\x02\n\x17SignedLicenseRequestRaw\x12\x32\n\x04Type\x18\x01 \x01(\x0e\x32$.SignedLicenseRequestRaw.MessageType\x12\x1f\n\x03Msg\x18\x02 \x01(\x0b\x32\x12.LicenseRequestRaw\x12\x11\n\tSignature\x18\x03 \x01(\x0c\x12\x12\n\nSessionKey\x18\x04 \x01(\x0c\x12-\n\x11RemoteAttestation\x18\x05 \x01(\x0b\x32\x12.RemoteAttestation\"}\n\x0bMessageType\x12\x13\n\x0fLICENSE_REQUEST\x10\x01\x12\x0b\n\x07LICENSE\x10\x02\x12\x12\n\x0e\x45RROR_RESPONSE\x10\x03\x12\x1f\n\x1bSERVICE_CERTIFICATE_REQUEST\x10\x04\x12\x17\n\x13SERVICE_CERTIFICATE\x10\x05\"\xa5\x02\n\rSignedLicense\x12(\n\x04Type\x18\x01 \x01(\x0e\x32\x1a.SignedLicense.MessageType\x12\x15\n\x03Msg\x18\x02 \x01(\x0b\x32\x08.License\x12\x11\n\tSignature\x18\x03 \x01(\x0c\x12\x12\n\nSessionKey\x18\x04 \x01(\x0c\x12-\n\x11RemoteAttestation\x18\x05 \x01(\x0b\x32\x12.RemoteAttestation\"}\n\x0bMessageType\x12\x13\n\x0fLICENSE_REQUEST\x10\x01\x12\x0b\n\x07LICENSE\x10\x02\x12\x12\n\x0e\x45RROR_RESPONSE\x10\x03\x12\x1f\n\x1bSERVICE_CERTIFICATE_REQUEST\x10\x04\x12\x17\n\x13SERVICE_CERTIFICATE\x10\x05\"\xcb\x02\n\x18SignedServiceCertificate\x12\x33\n\x04Type\x18\x01 \x01(\x0e\x32%.SignedServiceCertificate.MessageType\x12%\n\x03Msg\x18\x02 \x01(\x0b\x32\x18.SignedDeviceCertificate\x12\x11\n\tSignature\x18\x03 \x01(\x0c\x12\x12\n\nSessionKey\x18\x04 \x01(\x0c\x12-\n\x11RemoteAttestation\x18\x05 \x01(\x0b\x32\x12.RemoteAttestation\"}\n\x0bMessageType\x12\x13\n\x0fLICENSE_REQUEST\x10\x01\x12\x0b\n\x07LICENSE\x10\x02\x12\x12\n\x0e\x45RROR_RESPONSE\x10\x03\x12\x1f\n\x1bSERVICE_CERTIFICATE_REQUEST\x10\x04\x12\x17\n\x13SERVICE_CERTIFICATE\x10\x05\"\xb5\x01\n\nFileHashes\x12\x0e\n\x06signer\x18\x01 \x01(\x0c\x12)\n\nsignatures\x18\x02 \x03(\x0b\x32\x15.FileHashes.Signature\x1al\n\tSignature\x12\x10\n\x08\x66ilename\x18\x01 \x01(\t\x12\x14\n\x0ctest_signing\x18\x02 \x01(\x08\x12\x12\n\nSHA512Hash\x18\x03 \x01(\x0c\x12\x10\n\x08main_exe\x18\x04 \x01(\x08\x12\x11\n\tsignature\x18\x05 \x01(\x0c*1\n\x0bLicenseType\x12\x08\n\x04ZERO\x10\x00\x12\x0b\n\x07\x44\x45\x46\x41ULT\x10\x01\x12\x0b\n\x07OFFLINE\x10\x02*\x1e\n\x0fProtocolVersion\x12\x0b\n\x07\x43URRENT\x10\x15')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'wv_proto2_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _LICENSETYPE._serialized_start=8339
  _LICENSETYPE._serialized_end=8388
  _PROTOCOLVERSION._serialized_start=8390
  _PROTOCOLVERSION._serialized_end=8420
  _CLIENTIDENTIFICATION._serialized_start=20
  _CLIENTIDENTIFICATION._serialized_end=763
  _CLIENTIDENTIFICATION_NAMEVALUE._serialized_start=343
  _CLIENTIDENTIFICATION_NAMEVALUE._serialized_end=383
  _CLIENTIDENTIFICATION_CLIENTCAPABILITIES._serialized_start=386
  _CLIENTIDENTIFICATION_CLIENTCAPABILITIES._serialized_end=678
  _CLIENTIDENTIFICATION_CLIENTCAPABILITIES_HDCPVERSION._serialized_start=594
  _CLIENTIDENTIFICATION_CLIENTCAPABILITIES_HDCPVERSION._serialized_end=678
  _CLIENTIDENTIFICATION_TOKENTYPE._serialized_start=680
  _CLIENTIDENTIFICATION_TOKENTYPE._serialized_end=763
  _DEVICECERTIFICATE._serialized_start=766
  _DEVICECERTIFICATE._serialized_end=1049
  _DEVICECERTIFICATE_CERTIFICATETYPE._serialized_start=974
  _DEVICECERTIFICATE_CERTIFICATETYPE._serialized_end=1049
  _DEVICECERTIFICATESTATUS._serialized_start=1052
  _DEVICECERTIFICATESTATUS._serialized_end=1248
  _DEVICECERTIFICATESTATUS_CERTIFICATESTATUS._serialized_start=1205
  _DEVICECERTIFICATESTATUS_CERTIFICATESTATUS._serialized_end=1248
  _DEVICECERTIFICATESTATUSLIST._serialized_start=1250
  _DEVICECERTIFICATESTATUSLIST._serialized_end=1361
  _ENCRYPTEDCLIENTIDENTIFICATION._serialized_start=1364
  _ENCRYPTEDCLIENTIDENTIFICATION._serialized_end=1539
  _LICENSEIDENTIFICATION._serialized_start=1542
  _LICENSEIDENTIFICATION._serialized_end=1698
  _LICENSE._serialized_start=1701
  _LICENSE._serialized_end=3526
  _LICENSE_POLICY._serialized_start=1935
  _LICENSE_POLICY._serialized_end=2250
  _LICENSE_KEYCONTAINER._serialized_start=2253
  _LICENSE_KEYCONTAINER._serialized_end=3526
  _LICENSE_KEYCONTAINER_OUTPUTPROTECTION._serialized_start=2774
  _LICENSE_KEYCONTAINER_OUTPUTPROTECTION._serialized_end=2993
  _LICENSE_KEYCONTAINER_OUTPUTPROTECTION_CGMS._serialized_start=2926
  _LICENSE_KEYCONTAINER_OUTPUTPROTECTION_CGMS._serialized_end=2993
  _LICENSE_KEYCONTAINER_KEYCONTROL._serialized_start=2995
  _LICENSE_KEYCONTAINER_KEYCONTROL._serialized_end=3044
  _LICENSE_KEYCONTAINER_OPERATORSESSIONKEYPERMISSIONS._serialized_start=3046
  _LICENSE_KEYCONTAINER_OPERATORSESSIONKEYPERMISSIONS._serialized_end=3170
  _LICENSE_KEYCONTAINER_VIDEORESOLUTIONCONSTRAINT._serialized_start=3173
  _LICENSE_KEYCONTAINER_VIDEORESOLUTIONCONSTRAINT._serialized_end=3326
  _LICENSE_KEYCONTAINER_KEYTYPE._serialized_start=3328
  _LICENSE_KEYCONTAINER_KEYTYPE._serialized_end=3402
  _LICENSE_KEYCONTAINER_SECURITYLEVEL._serialized_start=3404
  _LICENSE_KEYCONTAINER_SECURITYLEVEL._serialized_end=3526
  _LICENSEERROR._serialized_start=3529
  _LICENSEERROR._serialized_end=3681
  _LICENSEERROR_ERROR._serialized_start=3585
  _LICENSEERROR_ERROR._serialized_end=3681
  _LICENSEREQUEST._serialized_start=3684
  _LICENSEREQUEST._serialized_end=4624
  _LICENSEREQUEST_CONTENTIDENTIFICATION._serialized_start=4028
  _LICENSEREQUEST_CONTENTIDENTIFICATION._serialized_end=4574
  _LICENSEREQUEST_CONTENTIDENTIFICATION_CENC._serialized_start=4245
  _LICENSEREQUEST_CONTENTIDENTIFICATION_CENC._serialized_end=4340
  _LICENSEREQUEST_CONTENTIDENTIFICATION_WEBM._serialized_start=4342
  _LICENSEREQUEST_CONTENTIDENTIFICATION_WEBM._serialized_end=4418
  _LICENSEREQUEST_CONTENTIDENTIFICATION_EXISTINGLICENSE._serialized_start=4421
  _LICENSEREQUEST_CONTENTIDENTIFICATION_EXISTINGLICENSE._serialized_end=4574
  _LICENSEREQUEST_REQUESTTYPE._serialized_start=4576
  _LICENSEREQUEST_REQUESTTYPE._serialized_end=4624
  _LICENSEREQUESTRAW._serialized_start=4627
  _LICENSEREQUESTRAW._serialized_end=5564
  _LICENSEREQUESTRAW_CONTENTIDENTIFICATION._serialized_start=4980
  _LICENSEREQUESTRAW_CONTENTIDENTIFICATION._serialized_end=5514
  _LICENSEREQUESTRAW_CONTENTIDENTIFICATION_CENC._serialized_start=5206
  _LICENSEREQUESTRAW_CONTENTIDENTIFICATION_CENC._serialized_end=5280
  _LICENSEREQUESTRAW_CONTENTIDENTIFICATION_WEBM._serialized_start=4342
  _LICENSEREQUESTRAW_CONTENTIDENTIFICATION_WEBM._serialized_end=4418
  _LICENSEREQUESTRAW_CONTENTIDENTIFICATION_EXISTINGLICENSE._serialized_start=4421
  _LICENSEREQUESTRAW_CONTENTIDENTIFICATION_EXISTINGLICENSE._serialized_end=4574
  _LICENSEREQUESTRAW_REQUESTTYPE._serialized_start=4576
  _LICENSEREQUESTRAW_REQUESTTYPE._serialized_end=4624
  _PROVISIONEDDEVICEINFO._serialized_start=5567
  _PROVISIONEDDEVICEINFO._serialized_end=5861
  _PROVISIONEDDEVICEINFO_WVSECURITYLEVEL._serialized_start=5782
  _PROVISIONEDDEVICEINFO_WVSECURITYLEVEL._serialized_end=5861
  _PROVISIONINGOPTIONS._serialized_start=5863
  _PROVISIONINGOPTIONS._serialized_end=5884
  _PROVISIONINGREQUEST._serialized_start=5886
  _PROVISIONINGREQUEST._serialized_end=5907
  _PROVISIONINGRESPONSE._serialized_start=5909
  _PROVISIONINGRESPONSE._serialized_end=5931
  _REMOTEATTESTATION._serialized_start=5933
  _REMOTEATTESTATION._serialized_end=6038
  _SESSIONINIT._serialized_start=6040
  _SESSIONINIT._serialized_end=6053
  _SESSIONSTATE._serialized_start=6055
  _SESSIONSTATE._serialized_end=6069
  _SIGNEDCERTIFICATESTATUSLIST._serialized_start=6071
  _SIGNEDCERTIFICATESTATUSLIST._serialized_end=6100
  _SIGNEDDEVICECERTIFICATE._serialized_start=6103
  _SIGNEDDEVICECERTIFICATE._serialized_end=6237
  _SIGNEDPROVISIONINGMESSAGE._serialized_start=6239
  _SIGNEDPROVISIONINGMESSAGE._serialized_end=6266
  _SIGNEDMESSAGE._serialized_start=6269
  _SIGNEDMESSAGE._serialized_end=6552
  _SIGNEDMESSAGE_MESSAGETYPE._serialized_start=6427
  _SIGNEDMESSAGE_MESSAGETYPE._serialized_end=6552
  _WIDEVINECENCHEADER._serialized_start=6555
  _WIDEVINECENCHEADER._serialized_end=6880
  _WIDEVINECENCHEADER_ALGORITHM._serialized_start=6840
  _WIDEVINECENCHEADER_ALGORITHM._serialized_end=6880
  _SIGNEDLICENSEREQUEST._serialized_start=6883
  _SIGNEDLICENSEREQUEST._serialized_end=7197
  _SIGNEDLICENSEREQUEST_MESSAGETYPE._serialized_start=6427
  _SIGNEDLICENSEREQUEST_MESSAGETYPE._serialized_end=6552
  _SIGNEDLICENSEREQUESTRAW._serialized_start=7200
  _SIGNEDLICENSEREQUESTRAW._serialized_end=7523
  _SIGNEDLICENSEREQUESTRAW_MESSAGETYPE._serialized_start=6427
  _SIGNEDLICENSEREQUESTRAW_MESSAGETYPE._serialized_end=6552
  _SIGNEDLICENSE._serialized_start=7526
  _SIGNEDLICENSE._serialized_end=7819
  _SIGNEDLICENSE_MESSAGETYPE._serialized_start=6427
  _SIGNEDLICENSE_MESSAGETYPE._serialized_end=6552
  _SIGNEDSERVICECERTIFICATE._serialized_start=7822
  _SIGNEDSERVICECERTIFICATE._serialized_end=8153
  _SIGNEDSERVICECERTIFICATE_MESSAGETYPE._serialized_start=6427
  _SIGNEDSERVICECERTIFICATE_MESSAGETYPE._serialized_end=6552
  _FILEHASHES._serialized_start=8156
  _FILEHASHES._serialized_end=8337
  _FILEHASHES_SIGNATURE._serialized_start=8229
  _FILEHASHES_SIGNATURE._serialized_end=8337
# @@protoc_insertion_point(module_scope)
