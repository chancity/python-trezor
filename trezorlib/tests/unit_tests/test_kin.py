# This file is part of the Trezor project.
#
# Copyright (C) 2012-2018 SatoshiLabs and contributors
#
# This library is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License version 3
# as published by the Free Software Foundation.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the License along with this library.
# If not, see <https://www.gnu.org/licenses/lgpl-3.0.html>.

#THESE WILL ALL FAIL BECAUSE THE KIN MAINNET PASSPHRASE IS DIFFERENT
import base64

from trezorlib import messages, kin


def test_kin_parse_transaction_bytes_simple():
    b64 = b"AAAAABXWSL/k028ZbPtXNf/YylTNS4Iz90PyJEnefPMBzbRpAAAAZAAAAAEAAAAAAAAAAAAAAAAAAAABAAAAAAAAAAAAAAAAXVVkJGaxhbhDFS6eIZFR28WJICfsQBAaUXvtXKAwwuAAAAAAO5/eyAAAAAA="

    tx, operations = kin.parse_transaction_bytes(base64.b64decode(b64))

    assert (
        tx.source_account == "GAK5MSF74TJW6GLM7NLTL76YZJKM2S4CGP3UH4REJHPHZ4YBZW2GSBPW"
    )
    assert tx.fee == 100
    assert tx.sequence_number == 4294967296
    assert tx.timebounds_start is None
    assert tx.timebounds_end is None
    assert tx.memo_type == kin.MEMO_TYPE_NONE
    assert tx.memo_text is None
    assert tx.memo_id is None
    assert tx.memo_hash is None
    assert tx.num_operations == len(operations)


def test_kin_parse_transaction_bytes_memo_text():
    b64 = b"AAAAABXWSL/k028ZbPtXNf/YylTNS4Iz90PyJEnefPMBzbRpAAAAZAAAAAEAAAAAAAAAAAAAAAEAAAAMZXhhbXBsZSBtZW1vAAAAAQAAAAAAAAAAAAAAAF1VZCRmsYW4QxUuniGRUdvFiSAn7EAQGlF77VygMMLgAAAAADuf3sgAAAAA"

    tx, operations = kin.parse_transaction_bytes(base64.b64decode(b64))

    assert (
        tx.source_account == "GAK5MSF74TJW6GLM7NLTL76YZJKM2S4CGP3UH4REJHPHZ4YBZW2GSBPW"
    )
    assert tx.fee == 100
    assert tx.sequence_number == 4294967296
    assert tx.timebounds_start is None
    assert tx.timebounds_end is None
    assert tx.memo_type == kin.MEMO_TYPE_TEXT
    assert tx.memo_text == b"example memo"
    assert tx.memo_id is None
    assert tx.memo_hash is None
    assert tx.num_operations == len(operations)


def test_kin_parse_transaction_bytes_memo_id():
    b64 = b"AAAAABXWSL/k028ZbPtXNf/YylTNS4Iz90PyJEnefPMBzbRpAAAAZAAAAAEAAAAAAAAAAAAAAAIAAAAAB1vNFQAAAAEAAAAAAAAAAAAAAABdVWQkZrGFuEMVLp4hkVHbxYkgJ+xAEBpRe+1coDDC4AAAAAA7n97IAAAAAA=="

    tx, operations = kin.parse_transaction_bytes(base64.b64decode(b64))

    assert (
        tx.source_account == "GAK5MSF74TJW6GLM7NLTL76YZJKM2S4CGP3UH4REJHPHZ4YBZW2GSBPW"
    )
    assert tx.fee == 100
    assert tx.sequence_number == 4294967296
    assert tx.timebounds_start is None
    assert tx.timebounds_end is None
    assert tx.memo_type == kin.MEMO_TYPE_ID
    assert tx.memo_text is None
    assert tx.memo_id == 123456789
    assert tx.memo_hash is None
    assert tx.num_operations == len(operations)


def test_kin_parse_transaction_bytes_memo_hash():
    b64 = b"AAAAABXWSL/k028ZbPtXNf/YylTNS4Iz90PyJEnefPMBzbRpAAAAZAAAAAEAAAAAAAAAAAAAAAMjLtb5+r8U47tVOSsYz+PQ/ryU0gzGMnw4odB11uoRjAAAAAEAAAAAAAAAAAAAAABdVWQkZrGFuEMVLp4hkVHbxYkgJ+xAEBpRe+1coDDC4AAAAAA7n97IAAAAAA=="

    tx, operations = kin.parse_transaction_bytes(base64.b64decode(b64))

    assert (
        tx.source_account == "GAK5MSF74TJW6GLM7NLTL76YZJKM2S4CGP3UH4REJHPHZ4YBZW2GSBPW"
    )
    assert tx.fee == 100
    assert tx.sequence_number == 4294967296
    assert tx.timebounds_start is None
    assert tx.timebounds_end is None
    assert tx.memo_type == kin.MEMO_TYPE_HASH
    assert tx.memo_text is None
    assert tx.memo_id is None
    # base-64 encoding of the raw bytes of sha256('kin')
    assert (
        base64.b64encode(tx.memo_hash)
        == b"Iy7W+fq/FOO7VTkrGM/j0P68lNIMxjJ8OKHQddbqEYw="
    )
    assert tx.num_operations == len(operations)


def test_kin_parse_transaction_bytes_memo_return():
    b64 = b"AAAAABXWSL/k028ZbPtXNf/YylTNS4Iz90PyJEnefPMBzbRpAAAAZAAAAAEAAAAAAAAAAAAAAAQjLtb5+r8U47tVOSsYz+PQ/ryU0gzGMnw4odB11uoRjAAAAAEAAAAAAAAAAAAAAABdVWQkZrGFuEMVLp4hkVHbxYkgJ+xAEBpRe+1coDDC4AAAAAA7n97IAAAAAA=="

    tx, operations = kin.parse_transaction_bytes(base64.b64decode(b64))

    assert (
        tx.source_account == "GAK5MSF74TJW6GLM7NLTL76YZJKM2S4CGP3UH4REJHPHZ4YBZW2GSBPW"
    )
    assert tx.fee == 100
    assert tx.sequence_number == 4294967296
    assert tx.timebounds_start is None
    assert tx.timebounds_end is None
    assert tx.memo_type == kin.MEMO_TYPE_RETURN
    assert tx.memo_text is None
    assert tx.memo_id is None
    # base-64 encoding of the raw bytes of sha256('kin')
    assert (
        base64.b64encode(tx.memo_hash)
        == b"Iy7W+fq/FOO7VTkrGM/j0P68lNIMxjJ8OKHQddbqEYw="
    )
    assert tx.num_operations == len(operations)


def test_kin_parse_operation_bytes_create_account_simple():
    b64 = b"AAAAABXWSL/k028ZbPtXNf/YylTNS4Iz90PyJEnefPMBzbRpAAAAZAAAAAEAAAAAAAAAAAAAAAAAAAABAAAAAAAAAAAAAAAAXVVkJGaxhbhDFS6eIZFR28WJICfsQBAaUXvtXKAwwuAAAAAAO5/eyAAAAAA="

    tx, operations = kin.parse_transaction_bytes(base64.b64decode(b64))
    op = operations[0]

    assert isinstance(op, messages.KinCreateAccountOp)
    assert op.source_account is None
    assert op.new_account == "GBOVKZBEM2YYLOCDCUXJ4IMRKHN4LCJAE7WEAEA2KF562XFAGDBOB64V"
    assert op.starting_balance == 1000333000


def test_kin_parse_operation_bytes_payment_native():
    b64 = b"AAAAABXWSL/k028ZbPtXNf/YylTNS4Iz90PyJEnefPMBzbRpAAAAZAAAAAEAAAAAAAAAAAAAAAAAAAABAAAAAAAAAAEAAAAAXVVkJGaxhbhDFS6eIZFR28WJICfsQBAaUXvtXKAwwuAAAAAAAAAAAB3PFpgAAAAA"

    tx, operations = kin.parse_transaction_bytes(base64.b64decode(b64))
    op = operations[0]

    assert isinstance(op, messages.KinPaymentOp)
    assert op.source_account is None
    assert (
        op.destination_account
        == "GBOVKZBEM2YYLOCDCUXJ4IMRKHN4LCJAE7WEAEA2KF562XFAGDBOB64V"
    )
    assert op.asset.type == kin.ASSET_TYPE_NATIVE
    assert op.amount == 500111000


def test_kin_parse_operation_bytes_payment_custom4():
    b64 = b"AAAAABXWSL/k028ZbPtXNf/YylTNS4Iz90PyJEnefPMBzbRpAAAAZAAAAAEAAAAAAAAAAAAAAAAAAAABAAAAAAAAAAEAAAAAXVVkJGaxhbhDFS6eIZFR28WJICfsQBAaUXvtXKAwwuAAAAABVEVTVAAAAAAphJYCwg5YNl8SPBLYehykVQ0QzSGwrg4Y1E4+Vv1qFQAAAAAdzxaYAAAAAA=="

    tx, operations = kin.parse_transaction_bytes(base64.b64decode(b64))
    op = operations[0]

    assert op.source_account is None
    assert (
        op.destination_account
        == "GBOVKZBEM2YYLOCDCUXJ4IMRKHN4LCJAE7WEAEA2KF562XFAGDBOB64V"
    )
    assert op.asset.type == kin.ASSET_TYPE_ALPHA4
    assert op.asset.code == b"TEST"
    assert op.asset.issuer == "GAUYJFQCYIHFQNS7CI6BFWD2DSSFKDIQZUQ3BLQODDKE4PSW7VVBKENC"
    assert op.amount == 500111000


def test_kin_parse_operation_bytes_payment_custom7():
    b64 = b"AAAAABXWSL/k028ZbPtXNf/YylTNS4Iz90PyJEnefPMBzbRpAAAAZAAAAAEAAAAAAAAAAAAAAAAAAAABAAAAAAAAAAEAAAAAXVVkJGaxhbhDFS6eIZFR28WJICfsQBAaUXvtXKAwwuAAAAACU0VWRU5YWAAAAAAAAAAAACmElgLCDlg2XxI8Eth6HKRVDRDNIbCuDhjUTj5W/WoVAAAAAB3PFpgAAAAA"

    tx, operations = kin.parse_transaction_bytes(base64.b64decode(b64))
    op = operations[0]

    assert isinstance(op, messages.KinPaymentOp)
    assert op.source_account is None
    assert (
        op.destination_account
        == "GBOVKZBEM2YYLOCDCUXJ4IMRKHN4LCJAE7WEAEA2KF562XFAGDBOB64V"
    )
    assert op.asset.type == kin.ASSET_TYPE_ALPHA12
    # asset codes are either 4 or 12 characters, so this will be null-padded at the end
    assert op.asset.code == b"SEVENXX\x00\x00\x00\x00\x00"
    assert op.asset.issuer == "GAUYJFQCYIHFQNS7CI6BFWD2DSSFKDIQZUQ3BLQODDKE4PSW7VVBKENC"
    assert op.amount == 500111000


def test_kin_parse_operation_bytes_path_payment_none():
    b64 = b"AAAAABXWSL/k028ZbPtXNf/YylTNS4Iz90PyJEnefPMBzbRpAAAAZAAAAAEAAAAAAAAAAAAAAAAAAAABAAAAAAAAAAIAAAAAAAAAAHfOKn8AAAAAXVVkJGaxhbhDFS6eIZFR28WJICfsQBAaUXvtXKAwwuAAAAABSlBZAAAAAADE+xa3Eb3cy85WSdqgwnUtC6UDwrC41YDANuCqe8vGxgAAAAAL68IBAAAAAAAAAAA="

    tx, operations = kin.parse_transaction_bytes(base64.b64decode(b64))
    op = operations[0]

    assert isinstance(op, messages.KinPathPaymentOp)
    assert op.source_account is None
    assert (
        op.destination_account
        == "GBOVKZBEM2YYLOCDCUXJ4IMRKHN4LCJAE7WEAEA2KF562XFAGDBOB64V"
    )

    assert op.send_asset.type == kin.ASSET_TYPE_NATIVE
    assert op.send_max == 2009999999

    assert (
        op.destination_account
        == "GBOVKZBEM2YYLOCDCUXJ4IMRKHN4LCJAE7WEAEA2KF562XFAGDBOB64V"
    )
    assert op.destination_asset.type == kin.ASSET_TYPE_ALPHA4
    # asset codes are either 4 or 12 characters, so this will be null-padded at the end
    assert op.destination_asset.code == b"JPY\x00"
    assert (
        op.destination_asset.issuer
        == "GDCPWFVXCG65ZS6OKZE5VIGCOUWQXJIDYKYLRVMAYA3OBKT3ZPDMNTIJ"
    )

    assert len(op.paths) == 0


def test_kin_parse_operation_bytes_path_payment_one():
    b64 = b"AAAAABXWSL/k028ZbPtXNf/YylTNS4Iz90PyJEnefPMBzbRpAAAAZAAAAAEAAAAAAAAAAAAAAAAAAAABAAAAAAAAAAIAAAAAAAAAAHfOKn8AAAAAXVVkJGaxhbhDFS6eIZFR28WJICfsQBAaUXvtXKAwwuAAAAABSlBZAAAAAADE+xa3Eb3cy85WSdqgwnUtC6UDwrC41YDANuCqe8vGxgAAAAAL68IBAAAAAQAAAAFQVEgxAAAAAMz/d9fJ3rFifblw3jT7sRZv/Ja+fqLfob//aLZQRQibAAAAAA=="

    tx, operations = kin.parse_transaction_bytes(base64.b64decode(b64))
    op = operations[0]

    assert isinstance(op, messages.KinPathPaymentOp)
    assert op.source_account is None
    assert (
        op.destination_account
        == "GBOVKZBEM2YYLOCDCUXJ4IMRKHN4LCJAE7WEAEA2KF562XFAGDBOB64V"
    )

    assert op.send_asset.type == kin.ASSET_TYPE_NATIVE
    assert op.send_max == 2009999999

    assert (
        op.destination_account
        == "GBOVKZBEM2YYLOCDCUXJ4IMRKHN4LCJAE7WEAEA2KF562XFAGDBOB64V"
    )
    assert op.destination_asset.type == kin.ASSET_TYPE_ALPHA4
    # asset codes are either 4 or 12 characters, so this will be null-padded at the end
    assert op.destination_asset.code == b"JPY\x00"
    assert (
        op.destination_asset.issuer
        == "GDCPWFVXCG65ZS6OKZE5VIGCOUWQXJIDYKYLRVMAYA3OBKT3ZPDMNTIJ"
    )
    assert op.destination_amount == 200000001

    assert len(op.paths) == 1
    assert op.paths[0].type == kin.ASSET_TYPE_ALPHA4
    assert op.paths[0].code == b"PTH1"
    assert (
        op.paths[0].issuer == "GDGP656XZHPLCYT5XFYN4NH3WELG77EWXZ7KFX5BX77WRNSQIUEJXAJK"
    )


def test_kin_parse_operation_bytes_manage_offer_new():
    b64 = b"AAAAABXWSL/k028ZbPtXNf/YylTNS4Iz90PyJEnefPMBzbRpAAAAZAAAAAEAAAAAAAAAAAAAAAAAAAABAAAAAAAAAAMAAAAAAAAAAVVTRAAAAAAABkAD8fq0d+bofA1LCatUL0dCTJexnyYYd4Y1ghnNUXMAAAAAdzWUAAAKSzYAD0JAAAAAAAAAAAAAAAAA"

    tx, operations = kin.parse_transaction_bytes(base64.b64decode(b64))
    op = operations[0]

    assert isinstance(op, messages.KinManageOfferOp)
    assert op.source_account is None

    assert op.selling_asset.type == kin.ASSET_TYPE_NATIVE

    assert op.buying_asset.type == kin.ASSET_TYPE_ALPHA4
    # asset codes are either 4 or 12 characters, so this will be null-padded at the end
    assert op.buying_asset.code == b"USD\x00"
    assert (
        op.buying_asset.issuer
        == "GADEAA7R7K2HPZXIPQGUWCNLKQXUOQSMS6YZ6JQYO6DDLAQZZVIXG74A"
    )

    assert op.amount == 2000000000
    assert op.price_n == 674614
    assert op.price_d == 1000000
    assert op.offer_id == 0  # indicates a new offer


def test_kin_parse_operation_bytes_passive_offer_new():
    b64 = b"AAAAABXWSL/k028ZbPtXNf/YylTNS4Iz90PyJEnefPMBzbRpAAAAZAAAAAEAAAAAAAAAAAAAAAAAAAABAAAAAAAAAAQAAAAAAAAAAVVTRAAAAAAABkAD8fq0d+bofA1LCatUL0dCTJexnyYYd4Y1ghnNUXMAAAAAdzWUAAAKSzYAD0JAAAAAAA=="

    tx, operations = kin.parse_transaction_bytes(base64.b64decode(b64))
    op = operations[0]

    assert isinstance(op, messages.KinCreatePassiveOfferOp)
    assert op.source_account is None

    assert op.selling_asset.type == kin.ASSET_TYPE_NATIVE

    assert op.buying_asset.type == kin.ASSET_TYPE_ALPHA4
    # asset codes are either 4 or 12 characters, so this will be null-padded at the end
    assert op.buying_asset.code == b"USD\x00"
    assert (
        op.buying_asset.issuer
        == "GADEAA7R7K2HPZXIPQGUWCNLKQXUOQSMS6YZ6JQYO6DDLAQZZVIXG74A"
    )

    assert op.amount == 2000000000
    assert op.price_n == 674614
    assert op.price_d == 1000000


def test_kin_parse_operation_bytes_set_options_inflation():
    b64 = b"AAAAABXWSL/k028ZbPtXNf/YylTNS4Iz90PyJEnefPMBzbRpAAAAZAAAAAEAAAAAAAAAAAAAAAAAAAABAAAAAAAAAAUAAAABAAAAAAt5i66vbwH70/2M4Oj0rQW81SNLAjfOsMV2bavzocXhAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"

    tx, operations = kin.parse_transaction_bytes(base64.b64decode(b64))
    op = operations[0]

    assert isinstance(op, messages.KinSetOptionsOp)
    assert op.source_account is None

    assert (
        op.inflation_destination_account
        == "GAFXTC5OV5XQD66T7WGOB2HUVUC3ZVJDJMBDPTVQYV3G3K7TUHC6CLBR"
    )


def test_kin_parse_operation_bytes_change_trust_add():
    b64 = b"AAAAABXWSL/k028ZbPtXNf/YylTNS4Iz90PyJEnefPMBzbRpAAAAZAAAAAEAAAAAAAAAAAAAAAAAAAABAAAAAAAAAAYAAAABVVNEAAAAAACkn7CoQZEWAlyO6z6VBUAddrDDR078TtLt/nP/hZJ9KQAAAAJUC+QAAAAAAA=="

    tx, operations = kin.parse_transaction_bytes(base64.b64decode(b64))
    op = operations[0]

    assert isinstance(op, messages.KinChangeTrustOp)
    assert op.source_account is None

    assert op.asset.type == kin.ASSET_TYPE_ALPHA4
    assert op.asset.code == b"USD\x00"
    assert op.asset.issuer == "GCSJ7MFIIGIRMAS4R3VT5FIFIAOXNMGDI5HPYTWS5X7HH74FSJ6STSGF"

    assert op.limit == 10000000000


def test_kin_parse_operation_bytes_allow_trust_allow():
    b64 = b"AAAAABXWSL/k028ZbPtXNf/YylTNS4Iz90PyJEnefPMBzbRpAAAAZAAAAAEAAAAAAAAAAAAAAAAAAAABAAAAAAAAAAcAAAAAZ0Me3OnxI2tuaC8qt95THF1fuB42qARTnP2ookJapQUAAAABSlBZAAAAAAEAAAAA"

    tx, operations = kin.parse_transaction_bytes(base64.b64decode(b64))
    op = operations[0]

    assert isinstance(op, messages.KinAllowTrustOp)
    assert op.source_account is None

    assert op.asset_type == kin.ASSET_TYPE_ALPHA4
    assert op.asset_code == b"JPY\x00"

    assert (
        op.trusted_account == "GBTUGHW45HYSG23ONAXSVN66KMOF2X5YDY3KQBCTTT62RISCLKSQLYF4"
    )


def test_kin_parse_operation_bytes_account_merge_simple():
    b64 = b"AAAAABXWSL/k028ZbPtXNf/YylTNS4Iz90PyJEnefPMBzbRpAAAAZAAAAAEAAAAAAAAAAAAAAAAAAAABAAAAAAAAAAgAAAAAXVVkJGaxhbhDFS6eIZFR28WJICfsQBAaUXvtXKAwwuAAAAAA"

    tx, operations = kin.parse_transaction_bytes(base64.b64decode(b64))
    op = operations[0]

    assert isinstance(op, messages.KinAccountMergeOp)
    assert op.source_account is None

    assert (
        op.destination_account
        == "GBOVKZBEM2YYLOCDCUXJ4IMRKHN4LCJAE7WEAEA2KF562XFAGDBOB64V"
    )


def test_kin_parse_operation_bytes_manage_data_set_simple():
    b64 = b"AAAAABXWSL/k028ZbPtXNf/YylTNS4Iz90PyJEnefPMBzbRpAAAAZAAAAAEAAAAAAAAAAAAAAAAAAAABAAAAAAAAAAoAAAAJdGVzdCBkYXRhAAAAAAAAAQAAAARhc2RmAAAAAA=="

    tx, operations = kin.parse_transaction_bytes(base64.b64decode(b64))
    op = operations[0]

    assert isinstance(op, messages.KinManageDataOp)
    assert op.source_account is None

    assert op.key == b"test data"
    assert op.value == b"asdf"


def test_kin_parse_operation_bytes_bump_sequence_simple():
    b64 = b"AAAAABXWSL/k028ZbPtXNf/YylTNS4Iz90PyJEnefPMBzbRpAAAAZAAAAAEAAAAAAAAAAAAAAAAAAAABAAAAAAAAAAsAAAAASZYC0gAAAAA="

    tx, operations = kin.parse_transaction_bytes(base64.b64decode(b64))
    op = operations[0]

    assert isinstance(op, messages.KinBumpSequenceOp)
    assert op.source_account is None

    assert op.bump_to == 1234567890
