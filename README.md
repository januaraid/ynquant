# ynquant
株式分析とかそういうの

## 使ってるAPI

[J-Quants API](https://jpx.gitbook.io/j-quants-ja/)


@J-Quants:財務情報(/fins/statements) で取得出来るカラム

| 変数名                                                                          | 説明                                         | 型      | 備考                                                               |
| ---------------------------------------------------------------------------- | ------------------------------------------ | ------ | ---------------------------------------------------------------- |
| DisclosedDate                                                                | 開示日                              | String |                                                                  |
| DisclosedTime                                                                | 開示時刻                             | String |                                                                  |
| LocalCode                                                                    | 銘柄コード（5桁）                        | String |                                                                  |
| DisclosureNumber                                                             | 開示番号                             | String | APIから出力されるjsonは開示番号で昇順に並んでいます。                                   |
| TypeOfDocument                                                               | 開示書類種別                           | String | [開示書類種別一覧](/j-quants-ja/api-reference/statements/typeofdocument) |
| TypeOfCurrentPeriod                                                          | 当会計期間の種類                         | String | \[1Q, 2Q, 3Q, 4Q, 5Q, FY\]                                       |
| CurrentPeriodStartDate                                                       | 当会計期間開始日                         | String |                                                                  |
| CurrentPeriodEndDate                                                         | 当会計期間終了日                         | String |                                                                  |
| CurrentFiscalYearStartDate                                                   | 当事業年度開始日                         | String |                                                                  |
| CurrentFiscalYearEndDate                                                     | 当事業年度終了日                         | String |                                                                  |
| NextFiscalYearStartDate                                                      | 翌事業年度開始日                         | String | 開示レコードに翌事業年度の開示情報がない場合空欄になります。                                   |
| NextFiscalYearEndDate                                                        | 翌事業年度終了日                         | String | 同上                                                               |
| NetSales                                                                     | 売上高                              | String |                                                                  |
| OperatingProfit                                                              | 営業利益                             | String |                                                                  |
| OrdinaryProfit                                                               | 経常利益                             | String |                                                                  |
| Profit                                                                       | 当期純利益                            | String |                                                                  |
| EarningsPerShare                                                             | 一株あたり当期純利益                       | String |                                                                  |
| DilutedEarningsPerShare                                                      | 潜在株式調整後一株あたり当期純利益                | String |                                                                  |
| TotalAssets                                                                  | 総資産                              | String |                                                                  |
| Equity                                                                       | 純資産                              | String |                                                                  |
| EquityToAssetRatio                                                           | 自己資本比率                           | String |                                                                  |
| BookValuePerShare                                                            | 一株あたり純資産                         | String |                                                                  |
| CashFlowsFromOperatingActivities                                             | 営業活動によるキャッシュ・フロー                 | String |                                                                  |
| CashFlowsFromInvestingActivities                                             | 投資活動によるキャッシュ・フロー                 | String |                                                                  |
| CashFlowsFromFinancingActivities                                             | 財務活動によるキャッシュ・フロー                 | String |                                                                  |
| CashAndEquivalents                                                           | 現金及び現金同等物期末残高                    | String |                                                                  |
| ResultDividendPerShare1stQuarter                                             | 一株あたり配当実績\_第1四半期末                | String |                                                                  |
| ResultDividendPerShare2ndQuarter                                             | 一株あたり配当実績\_第2四半期末                | String |                                                                  |
| ResultDividendPerShare3rdQuarter                                             | 一株あたり配当実績\_第3四半期末                | String |                                                                  |
| ResultDividendPerShareFiscalYearEnd                                          | 一株あたり配当実績\_期末                    | String |                                                                  |
| ResultDividendPerShareAnnual                                                 | 一株あたり配当実績\_合計                    | String |                                                                  |
| DistributionsPerUnit(REIT)                                                   | 1口当たり分配金                         | String |                                                                  |
| ResultTotalDividendPaidAnnual                                                | 配当金総額                            | String |                                                                  |
| ResultPayoutRatioAnnual                                                      | 配当性向                             | String |                                                                  |
| ForecastDividendPerShare1stQuarter                                           | 一株あたり配当予想\_第1四半期末                | String |                                                                  |
| ForecastDividendPerShare2ndQuarter                                           | 一株あたり配当予想\_第2四半期末                | String |                                                                  |
| ForecastDividendPerShare3rdQuarter                                           | 一株あたり配当予想\_第3四半期末                | String |                                                                  |
| ForecastDividendPerShareFiscalYearEnd                                        | 一株あたり配当予想\_期末                    | String |                                                                  |
| ForecastDividendPerShareAnnual                                               | 一株あたり配当予想\_合計                    | String |                                                                  |
| ForecastDistributionsPerUnit(REIT)                                           | 1口当たり予想分配金                       | String |                                                                  |
| ForecastTotalDividendPaidAnnual                                              | 予想配当金総額                          | String |                                                                  |
| ForecastPayoutRatioAnnual                                                    | 予想配当性向                           | String |                                                                  |
| NextYearForecastDividendPerShare1stQuarter                                   | 一株あたり配当予想\_翌事業年度第1四半期末           | String |                                                                  |
| NextYearForecastDividendPerShare2ndQuarter                                   | 一株あたり配当予想\_翌事業年度第2四半期末           | String |                                                                  |
| NextYearForecastDividendPerShare3rdQuarter                                   | 一株あたり配当予想\_翌事業年度第3四半期末           | String |                                                                  |
| NextYearForecastDividendPerShareFiscalYearEnd                                | 一株あたり配当予想\_翌事業年度期末               | String |                                                                  |
| NextYearForecastDividendPerShareAnnual                                       | 一株あたり配当予想\_翌事業年度合計               | String |                                                                  |
| NextYearForecastDistributionsPerUnit(REIT)                                   | 1口当たり翌事業年度予想分配金                  | String |                                                                  |
| NextYearForecastPayoutRatioAnnual                                            | 翌事業年度予想配当性向                      | String |                                                                  |
| ForecastNetSales2ndQuarter                                                   | 売上高\_予想\_第2四半期末                  | String |                                                                  |
| ForecastOperatingProfit2ndQuarter                                            | 営業利益\_予想\_第2四半期末                 | String |                                                                  |
| ForecastOrdinaryProfit2ndQuarter                                             | 経常利益\_予想\_第2四半期末                 | String |                                                                  |
| ForecastProfit2ndQuarter                                                     | 当期純利益\_予想\_第2四半期末                | String |                                                                  |
| ForecastEarningsPerShare2ndQuarter                                           | 一株あたり当期純利益\_予想\_第2四半期末           | String |                                                                  |
| NextYearForecastNetSales2ndQuarter                                           | 売上高\_予想\_翌事業年度第2四半期末             | String |                                                                  |
| NextYearForecastOperatingProfit2ndQuarter                                    | 営業利益\_予想\_翌事業年度第2四半期末            | String |                                                                  |
| NextYearForecastOrdinaryProfit2ndQuarter                                     | 経常利益\_予想\_翌事業年度第2四半期末            | String |                                                                  |
| NextYearForecastProfit2ndQuarter                                             | 当期純利益\_予想\_翌事業年度第2四半期末           | String |                                                                  |
| NextYearForecastEarningsPerShare2ndQuarter                                   | 一株あたり当期純利益\_予想\_翌事業年度第2四半期末      | String |                                                                  |
| ForecastNetSales                                                             | 売上高\_予想\_期末                      | String |                                                                  |
 |
| ForecastOperatingProfit                                                      | 営業利益\_予想\_期末                     | String |                                                                  |
| ForecastOrdinaryProfit                                                       | 経常利益\_予想\_期末                     | String |                                                                  |
| ForecastProfit                                                               | 当期純利益\_予想\_期末                    | String |                                                                  |
| ForecastEarningsPerShare                                                     | 一株あたり当期純利益\_予想\_期末               | String |                                                                  |
| NextYearForecastNetSales                                                     | 売上高\_予想\_翌事業年度期末                 | String |                                                                  |
| NextYearForecastOperatingProfit                                              | 営業利益\_予想\_翌事業年度期末                | String |                                                                  |
| NextYearForecastOrdinaryProfit                                               | 経常利益\_予想\_翌事業年度期末                | String |                                                                  |
| NextYearForecastProfit                                                       | 当期純利益\_予想\_翌事業年度期末               | String |                                                                  |
| NextYearForecastEarningsPerShare                                             | 一株あたり当期純利益\_予想\_翌事業年度期末          | String |                                                                  |
| MaterialChangesInSubsidiaries                                                | 期中における重要な子会社の異動                  | String |                                                                  |
| SignificantChangesInTheScopeOfConsolidation                                  | 期中における連結範囲の重要な変更                 | String | \*指定されたdateが2024-07-21以前のレスポンスは、当該項目には値が収録されません。                 |
| ChangesBasedOnRevisionsOfAccountingStandard                                  | 会計基準等の改正に伴う会計方針の変更               | String |                                                                  |
| ChangesOtherThanOnesBasedOnRevisionsOfAccountingStandard                     | 会計基準等の改正に伴う変更以外の会計方針の変更          | String |                                                                  |
| ChangesInAccountingEstimates                                                 | 会計上の見積りの変更                       | String |                                                                  |
| RetrospectiveRestatement                                                     | 修正再表示                            | String |                                                                  |
| NumberOfIssuedAndOutstandingSharesAtTheEndOfFiscalYearIncludingTreasuryStock | 期末発行済株式数                         | String |                                                                  |
| NumberOfTreasuryStockAtTheEndOfFiscalYear                                    | 期末自己株式数                          | String |                                                                  |
| AverageNumberOfShares                                                        | 期中平均株式数                          | String |                                                                  |
| NonConsolidatedNetSales                                                      | 売上高\_非連結                         | String |                                                                  |
| NonConsolidatedOperatingProfit                                               | 営業利益\_非連結                        | String |                                                                  |
| NextYearForecastNonConsolidatedOrdinaryProfit2ndQuarter                      | 経常利益\_予想\_翌事業年度第2四半期末\_非連結       | String |                                                                  |
| NextYearForecastNonConsolidatedProfit2ndQuarter                              | 当期純利益\_予想\_翌事業年度第2四半期末\_非連結      | String |                                                                  |
| NextYearForecastNonConsolidatedEarningsPerShare2ndQuarter                    | 一株あたり当期純利益\_予想\_翌事業年度第2四半期末\_非連結 | String |                                                                  |
| ForecastNonConsolidatedNetSales                                              | 売上高\_予想\_期末\_非連結                 | String |                                                                  |
| ForecastNonConsolidatedOperatingProfit                                       | 営業利益\_予想\_期末\_非連結                | String |                                                                  |
| ForecastNonConsolidatedOrdinaryProfit                                        | 経常利益\_予想\_期末\_非連結                | String |                                                                  |
| ForecastNonConsolidatedProfit                                                | 当期純利益\_予想\_期末\_非連結               | String |                                                                  |
| ForecastNonConsolidatedEarningsPerShare                                      | 一株あたり当期純利益\_予想\_第四半期末\_非連結       | String |                                                                  |
| NextYearForecastNonConsolidatedNetSales                                      | 売上高\_予想\_翌事業年度期末\_非連結            | String |                                                                  |
| NextYearForecastNonConsolidatedOperatingProfit                               | 営業利益\_予想\_翌事業年度期末\_非連結           | String |                                                                  |
| NextYearForecastNonConsolidatedOrdinaryProfit                                | 経常利益\_予想\_翌事業年度期末\_非連結           | String |                                                                  |
| NextYearForecastNonConsolidatedProfit                                        | 当期純利益\_予想\_翌事業年度期末\_非連結          | String |                                                                  |
| NextYearForecastNonConsolidatedEarningsPerShare                              | 一株あたり当期純利益\_予想\_翌事業年度期末\_非連結     | String |                                                                  |

@J-Quants_API-reference 上場銘柄一覧で取得出来るカラム

| 変数名                  | 説明                     | 型      | 備考       |
| -------------------- | ---------------------- | ------ | -------- |
| Date                 | 日付                     | String | YY-MM-DD |
| Code                 | 銘柄コード                | String |          |
| CompanyName          | 会社名                   | String |          |
| CompanyNameEnglish   | 会社名（英語）             | String |          |
| Sector17Code         | 17業種コード              | String |          |
| Sector17CodeName     | 17業種コード名            | String |          |
| Sector33Code         | 33業種コード              | String |          |
| Sector33CodeName     | 33業種コード名            | String |          |
| ScaleCategory        | 規模カテゴリ               | String |          |
| MarketCode           | 市場コード                | String |          |
| MarketCodeName       | 市場コード名              | String |          |
| MarginCode           | 信用コード                | String |          |
| MarginCodeName       | 信用コード名              | String |          |

@J-Quants_API-reference /prices/daily_quotesで取得出来るカラム

| 変数名                  | 説明                     | 型      | 備考       |
| -------------------- | ---------------------- | ------ | -------- |
| Date                 | 日付                     | String | YYYY-MM-DD |
| Code                 | 銘柄コード                | String |          |
| Open                 | 始値（調整前）             | Number |          |
| High                 | 高値（調整前）             | Number |          |
| Low                  | 安値（調整前）             | Number |          |
| Close                | 終値（調整前）             | Number |          |
| UpperLimit           | 日通ストップ高を記録したか、否かを表すフラグ | String | 0：ストップ高以外 1：ストップ高 |
| LowerLimit           | 日通ストップ安を記録したか、否かを表すフラグ | String | 0：ストップ安以外 1：ストップ安 |
| Volume               | 取引高（調整前）            | Number |          |
| TurnoverValue        | 取引代金                  | Number |          |
| AdjustmentFactor     | 調整係数                  | Number | 株式分割1:2の場合、権利落ち日のレコードにおいて本項目に”0.5”が収録されます。 |
| AdjustmentOpen       | 調整済み始値               | Number |          |
| AdjustmentHigh       | 調整済み高値               | Number |          |
| AdjustmentLow        | 調整済み安値               | Number |          |
| AdjustmentClose      | 調整済み終値               | Number |          |
| AdjustmentVolume     | 調整済み取引高              | Number |          |
| MorningOpen          | 前場始値                  | Number |          |
| MorningHigh          | 前場高値                  | Number |          |
| MorningLow           | 前場安値                  | Number |          |
| MorningClose         | 前場終値                  | Number |          |
| MorningUpperLimit    | 前場ストップ高を記録したか、否かを表すフラグ | String | 0：ストップ高以外 1：ストップ高 |
| MorningLowerLimit    | 前場ストップ安を記録したか、否かを表すフラグ | String | 0：ストップ安以外 1：ストップ安 |
| MorningVolume        | 前場売買高                 | Number |          |
| MorningTurnoverValue | 前場取引代金                | Number |          |
| MorningAdjustmentOpen| 調整済み前場始値            | Number |          |
| MorningAdjustmentHigh| 調整済み前場高値            | Number |          |
| MorningAdjustmentLow | 調整済み前場安値            | Number |          |
| MorningAdjustmentClose| 調整済み前場終値           | Number |          |
| MorningAdjustmentVolume| 調整済み前場売買高         | Number |          |
| AfternoonOpen        | 後場始値                  | Number |          |
| AfternoonHigh        | 後場高値                  | Number |          |
| AfternoonLow         | 後場安値                  | Number |          |
| AfternoonClose       | 後場終値                  | Number |          |
| AfternoonUpperLimit  | 後場ストップ高を記録したか、否かを表すフラグ | String | 0：ストップ高以外 1：ストップ高 |
| AfternoonLowerLimit  | 後場ストップ安を記録したか、否かを表すフラグ | String | 0：ストップ安以外 1：ストップ安 |
| AfternoonVolume      | 後場売買高                 | Number |          |
| AfternoonTurnoverValue| 後場取引代金               | Number |          |
| AfternoonAdjustmentOpen| 調整済み後場始値           | Number |          |
| AfternoonAdjustmentHigh| 調整済み後場高値           | Number |          |
| AfternoonAdjustmentLow| 調整済み後場安値           | Number |          |
| AfternoonAdjustmentClose| 調整済み後場終値          | Number |          |
| AfternoonAdjustmentVolume| 調整済み後場売買高        | Number |          |
