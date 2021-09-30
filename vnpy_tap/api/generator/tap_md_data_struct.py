TapAPIQuoteLoginAuth = {
    "UserNo": "string",
    "ISModifyPassword": "char",
    "Password": "string",
    "NewPassword": "string",
    "QuoteTempPassword": "string",
    "ISDDA": "char",
    "DDASerialNo": "string",
}

TapAPIQuotLoginRspInfo = {
    "UserNo": "string",
    "UserType": "int",
    "UserName": "string",
    "QuoteTempPassword": "string",
    "ReservedInfo": "string",
    "LastLoginIP": "string",
    "LastLoginProt": "unsigned int",
    "LastLoginTime": "string",
    "LastLogoutTime": "string",
    "TradeDate": "string",
    "LastSettleTime": "string",
    "StartTime": "string",
    "InitTime": "string",
}

TapAPIQuoteCommodityInfo = {
    "Commodity": "dict",
    "CommodityName": "string",
    "CommodityEngName": "string",
    "ContractSize": "double",
    "CommodityTickSize": "double",
    "CommodityDenominator": "int",
    "CmbDirect": "char",
    "CommodityContractLen": "int",
    "IsDST": "char",
    "RelateCommodity1": "dict",
    "RelateCommodity2": "dict",
}

TapAPIQuoteContractInfo = {
    "Contract": "dict",
    "ContractType": "char",
    "QuoteUnderlyingContract": "string",
    "ContractName": "string",
    "ContractExpDate": "string",
    "LastTradeDate": "string",
    "FirstNoticeDate": "string",
}

TapAPIQuoteWhole = {
    "Contract": "dict",
    "CurrencyNo": "string",
    "TradingState": "char",
    "DateTimeStamp": "string",
    "QPreClosingPrice": "double",
    "QPreSettlePrice": "double",
    "QPrePositionQty": "unsigned long long",
    "QOpeningPrice": "double",
    "QLastPrice": "double",
    "QHighPrice": "double",
    "QLowPrice": "double",
    "QHisHighPrice": "double",
    "QHisLowPrice": "double",
    "QLimitUpPrice": "double",
    "QLimitDownPrice": "double",
    "QTotalQty": "unsigned long long",
    "QTotalTurnover": "double",
    "QPositionQty": "unsigned long long",
    "QAveragePrice": "double",
    "QClosingPrice": "double",
    "QSettlePrice": "double",
    "QLastQty": "unsigned long long",
    "QBidPrice": "double",
    "QBidQty": "unsigned long long",
    "QAskPrice": "double",
    "QAskQty": "unsigned long long",
    "QImpliedBidPrice": "double",
    "QImpliedBidQty": "unsigned long long",
    "QImpliedAskPrice": "double",
    "QImpliedAskQty": "unsigned long long",
    "QPreDelta": "double",
    "QCurrDelta": "double",
    "QInsideQty": "unsigned long long",
    "QOutsideQty": "unsigned long long",
    "QTurnoverRate": "double",
    "Q5DAvgQty": "unsigned long long",
    "QPERatio": "double",
    "QTotalValue": "double",
    "QNegotiableValue": "double",
    "QPositionTrend": "long long",
    "QChangeSpeed": "double",
    "QChangeRate": "double",
    "QChangeValue": "double",
    "QSwing": "double",
    "QTotalBidQty": "unsigned long long",
    "QTotalAskQty": "unsigned long long",
    "UnderlyContract": "dict",
}
