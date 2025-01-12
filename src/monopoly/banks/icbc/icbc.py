import logging
from re import compile as regex

from monopoly.config import DateOrder, StatementConfig
from monopoly.constants import (
    ISO8601,
    BankNames,
    DebitTransactionPatterns,
    EntryType,
    StatementBalancePatterns,
)
from monopoly.constants.statement import StatementCurrentBalancePatterns
from monopoly.identifiers import MetadataIdentifier, TextIdentifier

from ..base import BankBase

logger = logging.getLogger(__name__)


class Icbc(BankBase):
    name = BankNames.ICBC

    debit = StatementConfig(
        statement_type=EntryType.DEBIT,
        statement_date_pattern=regex(rf"Statement Date 结单日期：{ISO8601.YYYY_MM_DD}"),
        statement_date_order=DateOrder("YMD"),
        header_pattern=regex(
            r"(Date.*Remark.*CCY.*Deposit Amount.*Withdrawal Amount.*A/C Balance)"
        ),
        transaction_pattern=DebitTransactionPatterns.ICBC,
        transaction_date_order=DateOrder("YMD"),
        transaction_bound=170,
        multiline_transactions=True,
    )

    identifiers = [
        [
            MetadataIdentifier(
                producer="iText 2.0.8 (by lowagie.com)",
            ),
            TextIdentifier("B/F"),
            TextIdentifier("Statement Date 结单日期"),
        ],
    ]
    statement_configs = [debit]
