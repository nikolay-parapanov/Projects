
import data_retrieval
import data_enrichment

if __name__ == '__main__':

    tickers_list_requested = ['AAPL', 'MSFT', 'TSLA', 'GOOG']

    step_1_retrieved_data = data_retrieval.data_retrieval_daily(tickers_list_requested)

    print(step_1_retrieved_data)

    step_2_enriched_data = data_enrichment.enrichment_sma(step_1_retrieved_data)



    print('the end :)')
